'''
Python script for porting from CarScanner profiles to WiCAN json
Run as 
$ python CarScanner_to_WiCANjson.py <profiles_all_dump.json> "<profile name substring>"
The script will output several files in the current directory:
<profile_name>.json
<profile_name>.params.json
<profile_name>.params.definitive.json
<profile_name>.params.uncertain.json
<profile_name>.params.notfound.json
<profile_name>.json is formatted to be merged with ./<make>/<model>.json
<profile_name>.params.json is formatted to be merged with ../.vehicle_profiles/params.json
The script also maps CarScanner parameters onto existing WiCAN parameter names from
../.vehicle_profiles/params.json and the existing car profiles in ../../vehicle_profiles.
Three categorized params files are produced:
  definitive: parameters that map to an existing WiCAN name by matching the PID
              and the response data byte (and, when several params share a byte,
              by an exact expression match). These are safe to merge using the
              existing WiCAN name.
  uncertain:  parameters that only match an existing WiCAN name by name, or that
              are ambiguous at the byte level; these need manual review.
  notfound:   parameters with no match in the existing WiCAN params.
Each categorized entry carries a description of the form
"Matches CarScanner <CarScannerName>." so the source parameter can be traced.

This part requires care and should be done manually and/or with help from an LLM. Blindly copy-pasting will likely produce duplicate parameters and should be avoided. There is low likelihood that the ported CarScanner short names map onto existing WiCAN shortnames. Use long names to make the mapping correctly.
We use params.csv to map params from CarScanner names to WiCAN names. The script will skip adding params entries for any CarScanner shortname that has a mapping, so the mapping should be updated to include any existing WiCAN params that match CarScanner shortnames. The mapping is case-insensitive and will ignore spaces in the header, but should otherwise be formatted as "torque,WiCAN" with no extra columns.

This script is tested on profiles in profiles_all_dump.json (a full export of the CarScanner profile database) and may need more work to import other files, but should be a good start.
'''
import re
import json
import sys
import csv
from pathlib import Path

# Load CarScanner name to WiCAN name mapping from params.csv
def load_name_mapping(mapping_path):
    mapping = {}
    try:
        with open(mapping_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Fix: strip spaces from fieldnames to handle 'torque, WiCAN' header
            if reader.fieldnames:
                reader.fieldnames = [f.strip() for f in reader.fieldnames]
            for row in reader:
                # Also strip keys in row for robustness
                carscanner = row.get('torque', row.get('torque', '')).strip().lower()
                wican = row.get('WiCAN', row.get('WiCAN', '')).strip()
                if carscanner:
                    mapping[carscanner] = wican
    except Exception as e:
        print(f"Warning: Could not load mapping file: {e}")
    return mapping

# CarScanner unit codes -> WiCAN unit strings. Codes taken from the CarScanner
# app profile format. Unmapped codes fall back to ''.
UN_TO_UNIT = {
    0: '',
    1: 'km/h',
    2: 'mph',
    3: 'km',
    4: 'mi',
    5: 'kPa',
    6: 'rpm',
    7: 'deg',
    10: 'V',
    13: 'Nm',
    14: '%',
    15: '°C',
    16: '°F',
    17: 's',
    18: 'min',
    19: 'A',
    20: 'm',
    22: 'L/100km',
    24: 'L',
    26: 'Ohm',
    27: 'Ohm',
    28: 'Ohm',
    41: 'ppm',
    42: 'g',
    43: 'g',
    44: 'ms',
    46: 'kW',
    47: 'kPa',
    48: 'kPa',
    49: 'V',
    51: 'ms',
    52: 'kPa',
    53: 'kW',
    54: 'min',
    56: 'L/100km',
    59: 'A',
    60: 'kWh',
    61: 'kWh',
    62: 'Ah',
    63: 'h',
    68: 'g/s',
    69: 'kPa',
    71: 'deg/s',
    74: 'kPa',
    75: 'mm',
    79: 'Ohm',
    84: 'km/h',
    101: 'deg',
}


def format_shortname(short_name):
    short_name = re.sub(r"\s", "_", short_name)
    short_name = re.sub(r"([a-z])([A-Z])", r"\1_\2", short_name)
    return short_name.upper()


def determine_class(long_name, unit):
    has_batt = re.search('battery', long_name, flags=re.IGNORECASE)
    has_curr = re.search('current', long_name)
    has_soc = re.search('state of charge', long_name, flags=re.IGNORECASE)
    has_V = re.search('voltage', long_name)
    has_power = re.search('power', long_name)
    has_temp = re.search('temperature', long_name, flags=re.IGNORECASE)
    has_press = re.search('pressure', long_name, flags=re.IGNORECASE)
    if unit.casefold() in ('km', 'mi'):
        return 'distance'
    elif has_power or unit.casefold() in ('kw', 'w'):
        return 'power'
    elif has_curr or unit.casefold() == 'a':
        return 'current'
    elif unit.casefold() in ('c', '°c', 'f', '°f') or has_temp:
        return 'temperature'
    elif unit.casefold() in ('psi', 'kpa') or has_press:
        return 'pressure'
    elif unit.casefold() == 'v' or has_V or has_batt or has_soc:
        return 'battery'
    else:
        return 'none'


def echo_len(cmd):
    return len(cmd) // 2


def multi_frame(cmd, max_data_len):
    # A single CAN frame can carry up to 7 data bytes (after the PCI byte).
    # If the echoed command plus data exceeds that, the response is multi-frame.
    return echo_len(cmd) + max_data_len > 7


def bindex(k, cmd, multi):
    # Byte index in the WiCAN data array for CarScanner data byte k (SBI).
    # Single frame:  data = [PCI, echoed cmd..., data...]
    # Multi frame:   first frame = [0x10, len, 6 data bytes] each subsequent
    #                frame adds a PCI byte before its 7 data bytes.
    echo = echo_len(cmd)
    if not multi:
        return k + 1 + echo
    first_frame_data = 6 - echo
    if k < first_frame_data:
        return k + 2 + echo
    return k + 3 + echo + (k - first_frame_data) // 7


def fmt_num(n):
    if float(n).is_integer():
        return str(int(n))
    return str(float(n))


def apply_scale(raw, mul, div, ofs):
    mul = mul if mul else 1.0
    div = div if div else 1.0
    expr = raw
    if mul != 1.0:
        expr = f"({expr}*{fmt_num(mul)})"
    if div != 1.0:
        expr = f"({expr}/{fmt_num(div)})"
    if ofs != 0.0:
        if ofs < 0:
            expr = f"({expr}-{fmt_num(abs(ofs))})"
        else:
            expr = f"({expr}+{fmt_num(ofs)})"
    return expr


def build_byte_expr(pid, cmd):
    sbi = pid.get('SBI', 0)
    dl = pid.get('DL', 1)
    bit = pid.get('BIT', 0)
    sig = pid.get('SIG', False)
    mul = pid.get('MUL', 1.0)
    div = pid.get('DIV', 1.0)
    ofs = pid.get('OFS', 0.0)
    # Total data length of the response, so we can decide single vs multi-frame.
    max_data = sbi + dl
    multi = multi_frame(cmd, max_data)

    start = bindex(sbi, cmd, multi)
    if dl == 1:
        if sig:
            raw = f"S{start}"
        elif bit:
            raw = f"B{start}:{bit}"
        else:
            raw = f"B{start}"
    else:
        end = start + dl - 1
        if sig:
            raw = f"[S{start}:S{end}]"
        else:
            raw = f"[B{start}:B{end}]"

    return apply_scale(raw, mul, div, ofs)


def letter_index(token):
    # A=0 ... Z=25, AA=26 ... AZ=51, BA=52 ...
    token = token.upper()
    if len(token) == 1:
        return ord(token) - ord('A')
    return (ord(token[0]) - ord('A') + 1) * 26 + (ord(token[1]) - ord('A'))


def translate_fr(fr, cmd):
    # CarScanner FR formulas reference the response data bytes as letters,
    # A=first data byte, B=second, ... AA=27th, etc. There are also helper
    # functions (Signed, ShortSigned, GetBit, FLOAT32, MAX, ...) and a stray
    # '@' character that marks a byte reference. Translate the byte references
    # into WiCAN B-indexes / S-indexes.
    expr = fr

    # B243(...) / if(...) is CarScanner's conditional IF function. WiCAN has
    # no equivalent, so these can't be ported automatically.
    if 'B243(' in expr or re.search(r'\bif\s*\(', expr, flags=re.IGNORECASE):
        raise ValueError("CarScanner conditional IF function is not supported")

    # Detect frame layout: use the highest letter used in the formula.
    letters = re.findall(r"\b([A-Z]{1,2})\b", expr)
    max_k = max((letter_index(l) for l in letters), default=0)
    multi = multi_frame(cmd, max_k + 1)

    def bfor(token):
        return bindex(letter_index(token), cmd, multi)

    # Signed(X) -> S{n} ;  ShortSigned(A,B) -> [S{a}:S{b}]
    expr = re.sub(r"ShortSigned\(\s*([A-Z]{1,2})\s*,\s*([A-Z]{1,2})\s*\)",
                  lambda m: f"[S{bfor(m.group(1))}:S{bfor(m.group(2))}]", expr,
                  flags=re.IGNORECASE)
    expr = re.sub(r"Signed\(\s*([A-Z]{1,2})\s*\)",
                  lambda m: f"S{bfor(m.group(1))}", expr, flags=re.IGNORECASE)

    # GetBit(X,n) -> B{idx}:{n}
    expr = re.sub(r"GetBit\(\s*([A-Z]{1,2})\s*,\s*(\d+)\s*\)",
                  lambda m: f"B{bfor(m.group(1))}:{m.group(2)}", expr,
                  flags=re.IGNORECASE)

    # FLOAT32(A,B,C,D) -> [B{a}:B{d}]
    expr = re.sub(r"FLOAT\d+\(\s*([A-Z]{1,2})\s*,\s*([A-Z]{1,2})\s*\)",
                  lambda m: f"[B{bfor(m.group(1))}:B{bfor(m.group(2))}]", expr,
                  flags=re.IGNORECASE)

    # Remove the '@' byte-reference marker used by CarScanner
    expr = expr.replace('@', '')

    # Translate remaining bare byte references (letters)
    def repl(m):
        token = m.group(1)
        if token.upper() in ('MAX', 'SIGNED', 'SHORTSIGNED', 'GETBIT', 'FLOAT', 'PID', 'VAL'):
            return token
        return f"B{bfor(token)}"

    expr = re.sub(r"\b([A-Za-z]{1,2})\b", repl, expr)

    return expr


def extract_bytes(expr):
    # Return the set of data byte indices referenced by a WiCAN expression
    # (B{n}, S{n}, [B{a}:B{b}], [S{a}:S{b}], B{n}:bit).
    result = set()
    for m in re.finditer(r"\[([BS])(\d+):\1(\d+)\]", expr):
        start = int(m.group(2))
        end = int(m.group(3))
        result.update(range(start, end + 1))
    # Handle single byte references, ignoring those already inside a range.
    expr2 = re.sub(r"\[[BS]\d+:[BS]\d+\]", " ", expr)
    for m in re.finditer(r"\b[BS](\d+)\b", expr2):
        result.add(int(m.group(1)))
    return result


def build_pid_byte_map(profiles_dir):
    # Scan existing WiCAN car profiles and build a map of
    # (pid, byte) -> set of WiCAN param names used at that pid and byte, plus
    # (pid, expr) -> set of WiCAN param names used at that pid and expression.
    import glob
    pid_byte = {}
    pid_expr = {}
    for f in glob.glob(str(profiles_dir / "**" / "*.json"), recursive=True):
        try:
            with open(f) as fh:
                profile = json.load(fh)
        except (OSError, ValueError):
            continue
        for group in profile.get("pids", []):
            pid = group.get("pid", "")
            # Strip the optional trailing frame-count digit
            base_pid = pid[:-1] if len(pid) % 2 == 1 else pid
            for param, expr in group.get("parameters", {}).items():
                for byte in extract_bytes(expr):
                    pid_byte.setdefault((base_pid, byte), set()).add(param)
                pid_expr.setdefault((base_pid, normalize_expr(expr)), set()).add(param)
    return pid_byte, pid_expr


def normalize_expr(expr):
    # Normalize an expression for comparison: drop whitespace and parens.
    return re.sub(r"\s+", "", expr).replace("(", "").replace(")", "")


def classify_param(cmd, expr, snm, name_mapping, wican_param_names, wican_pid_byte, wican_pid_expr):
    # Classify a CarScanner param against the existing WiCAN params.
    #   definitive: the (pid, byte) pair matches exactly one existing WiCAN
    #               param, so it can be mapped by PID and byte (not just name).
    #               If several existing params share a byte, fall back to an
    #               exact (pid, expression) match.
    #   uncertain:  a name-level match exists but PID/byte is ambiguous or
    #               unmapped; these need manual review.
    #   notfound:   no match found in the existing WiCAN params.
    bytes_ = extract_bytes(expr)
    candidates = set()
    for b in bytes_:
        candidates.update(wican_pid_byte.get((cmd, b), set()))
    if candidates:
        # definitive only when every referenced byte maps to the same single
        # WiCAN param.
        common = set(candidates)
        for b in bytes_:
            common &= wican_pid_byte.get((cmd, b), set())
        if len(common) == 1 and all(len(wican_pid_byte.get((cmd, b), set())) == 1
                                   for b in bytes_):
            return 'definitive', next(iter(common))
        # Several params share a byte; check if the expression matches exactly.
        expr_matches = wican_pid_expr.get((cmd, normalize_expr(expr)), set())
        if len(expr_matches) == 1:
            return 'definitive', next(iter(expr_matches))
        return 'uncertain', None
    # Fall back to name matching (case-insensitive) using the shortname and any
    # name mapping from params.csv.
    snm_lc = snm.lower()
    formatted = format_shortname(snm).lower()
    if snm_lc in wican_param_names or formatted in wican_param_names:
        return 'uncertain', None
    if snm_lc in name_mapping:
        return 'uncertain', None
    return 'notfound', None


class PID_group(object):

    def __init__(self, cmd, init):
        self.cmd = cmd
        self.init = init
        self.parameters = {}
        self.frame_count = None

    def add_parameter(self, pid, params, name_mapping, params_definitive,
                      params_uncertain, params_notfound, wican_pid_byte,
                      wican_pid_expr, wican_param_names):
        long_name = pid.get('NM', '')
        snm = pid.get('SNM', '')
        snm_lc = snm.lower()
        try:
            expr = process_pid(pid, self.cmd)
        except (ValueError, TypeError) as e:
            print(f"  Skipping {pid.get('CMD')} {long_name}: {e}")
            return
        category, wican_name = classify_param(self.cmd, expr, snm, name_mapping,
                                              wican_param_names, wican_pid_byte,
                                              wican_pid_expr)
        # Use mapping if available (case-insensitive), else fallback to formatted shortname
        if snm_lc in name_mapping:
            short_name = name_mapping[snm_lc]
        elif category == 'definitive' and wican_name:
            short_name = wican_name
        else:
            short_name = format_shortname(snm)
        unit = UN_TO_UNIT.get(pid.get('UN'), '')
        class_ = determine_class(long_name, unit)
        settings = {"unit": unit, "class": class_}
        min_val = pid.get('MIN')
        max_val = pid.get('MAX')
        if min_val:
            settings["min"] = str(min_val)
        if max_val:
            settings["max"] = str(max_val)
        entry = {"description": f"Matches CarScanner {long_name}.", "settings": settings}

        if category == 'definitive':
            # Matches an existing WiCAN param by PID and data byte, so the car
            # profile should reference the existing WiCAN name.
            params_definitive[short_name] = entry
        elif category == 'uncertain':
            params_uncertain[short_name] = entry
        else:
            params_notfound[short_name] = entry
        # Only add to the merge-able params file if it is a new param (not an
        # existing WiCAN param reached through name_mapping or a definitive match)
        if snm_lc not in name_mapping and category != 'definitive':
            params[short_name] = entry
        self.parameters[short_name] = expr

    def make_json_dict(self):
        json_dict = {"pid": self.pid_string()}
        if self.init:
            json_dict["pid_init"] = self.init
        json_dict["parameters"] = self.parameters
        return json_dict

    def pid_string(self):
        pid = self.cmd
        if self.frame_count and len(self.cmd) % 2 == 0:
            # Odd length command, last digit is the expected response frame count
            pid = self.cmd + str(self.frame_count)
        return pid


def process_pid(pid, cmd):
    tp = pid.get('TP')
    fr = pid.get('FR')
    if tp == 0 and fr:
        if 'PID(' in fr:
            # References to other parameters by internal CarScanner ID can't be
            # ported to WiCAN expressions.
            raise ValueError(f"Unsupported PID() reference in {pid.get('CMD')} {pid.get('NM')}")
        return translate_fr(fr, cmd)
    elif tp in (1, 2, 5):
        return build_byte_expr(pid, cmd)
    else:
        raise ValueError(f"Unhandled TP {tp} for {pid.get('CMD')} {pid.get('NM')}")


def pid_init_for(pid):
    hdr = pid.get('HDR', '')
    bcm = pid.get('BCM', '')
    commands = []
    # Only keep actual AT commands from the before-command sequence. CarScanner
    # sometimes stores a bare number in BCM (e.g. "1003") which is not an AT
    # command and is not useful for WiCAN.
    for c in bcm.split(';'):
        c = c.strip()
        if c and c.upper().startswith('AT'):
            commands.append(c)
    if hdr:
        # ATSH sets the header; add it if not already present
        if not any(c.upper() == f'ATSH{hdr}' for c in commands):
            commands.append(f'ATSH{hdr}')
    if not commands:
        return ''
    return ';'.join(commands) + ';'


# Main script logic
if len(sys.argv) < 3:
    print("Usage: python CarScanner_to_WiCANjson.py <profiles_all_dump.json> \"<profile name substring>\" [--frame-count]")
    sys.exit(1)

add_frame_count = False
if '--frame-count' in sys.argv:
    add_frame_count = True
    sys.argv.remove('--frame-count')

dump_path = sys.argv[1]
profile_match = sys.argv[2]

with open(dump_path) as f:
    profiles = json.load(f)

matches = [p for p in profiles if profile_match.lower() in p.get('Name', '').lower()]
if not matches:
    print(f"No profile matched '{profile_match}'")
    sys.exit(1)
if len(matches) > 1:
    print("Multiple profiles matched:")
    for m in matches:
        print(f"  {m['Name']} | {m.get('Description')}")
    print(f"Using: {matches[0]['Name']}")

profile = matches[0]
pids = json.loads(profile['ProfilePIDs'])

# Try to load mapping from params.csv in the same directory as this script
mapping_path = str(Path(__file__).parent / 'params.csv')
name_mapping = load_name_mapping(mapping_path)

# Load existing WiCAN params and build a (pid, byte) -> param name map from the
# existing WiCAN car profiles so CarScanner params can be mapped to existing
# WiCAN names where possible.
wican_params_path = Path(__file__).parent.parent / 'params.json'
wican_param_names = set()
try:
    with open(wican_params_path) as f:
        wican_param_names = set(json.load(f).keys())
except (OSError, ValueError) as e:
    print(f"Warning: Could not load {wican_params_path}: {e}")

wican_profiles_dir = Path(__file__).parent.parent.parent / 'vehicle_profiles'
wican_pid_byte, wican_pid_expr = build_pid_byte_map(wican_profiles_dir)

groups = {}
params = {}
params_definitive = {}
params_uncertain = {}
params_notfound = {}
for pid in pids:
    cmd = pid.get('CMD')
    if not cmd or pid.get('VIS') is False:
        continue
    if pid.get('ACT'):
        # These are commands (write requests), not measurements
        continue
    if not re.fullmatch(r'[0-9A-Fa-f]+', cmd):
        # CarScanner also has special protocol commands (e.g. VWTP:02:2106)
        # that aren't valid WiCAN hex PIDs.
        continue
    init = pid_init_for(pid)
    key = (cmd, init)
    if key not in groups:
        groups[key] = PID_group(cmd, init)
    groups[key].add_parameter(pid, params, name_mapping,
                              params_definitive, params_uncertain,
                              params_notfound, wican_pid_byte,
                              wican_pid_expr, wican_param_names)

json_dict = {"pids": []}
for group in groups.values():
    # Optional: append the expected response frame count as a trailing digit to
    # multi-frame pids. This is an ELM327 optimization and is not required.
    if add_frame_count:
        max_data = max(pid.get('SBI', 0) + pid.get('DL', 0)
                       for pid in pids if pid.get('CMD') == group.cmd)
        if multi_frame(group.cmd, max_data):
            total = echo_len(group.cmd) + max_data
            group.frame_count = 1 + (total - 1) // 7 if total > 6 else 1
    json_dict["pids"].append(group.make_json_dict())

new_fname = Path(profile_match.replace(' ', '_').replace('/', '_') + '.json')
new_params_fname = new_fname.with_suffix('.params.json')
with open(new_fname, 'w') as f:
    json.dump(json_dict, f, indent=2)
with open(new_params_fname, 'w') as f:
    json.dump(params, f, indent=2)

# Also write categorized params files:
#   definitive: params that map to an existing WiCAN name by matching PID + byte
#   uncertain:  params that only match by name and need manual review
#   notfound:   params with no match in the existing WiCAN params
for suffix, data in (('definitive', params_definitive),
                     ('uncertain', params_uncertain),
                     ('notfound', params_notfound)):
    out_fname = new_fname.with_suffix(f'.params.{suffix}.json')
    with open(out_fname, 'w') as f:
        json.dump(data, f, indent=2)

print(f"Wrote {new_fname} ({len(json_dict['pids'])} pid groups) and {new_params_fname} ({len(params)} params)")
print(f"  definitive: {len(params_definitive)} | uncertain: {len(params_uncertain)} | notfound: {len(params_notfound)}")

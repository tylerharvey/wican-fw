# CarScanner Profile Names

This file lists all vehicle profile names found in `profiles_all_dump.json`.
Any of these substrings can be passed to `CarScanner_to_WiCANjson.py` as the
`"<profile name substring>"` argument to generate WiCAN json profiles, e.g.:

```bash
python CarScanner_to_WiCANjson.py profiles_all_dump.json "IONIQ 5 (2022-2025)"
```

Leave out the make. A partial name works, e.g. IONIQ. It's case-insensitive. 
You'll be able to choose between any matches. 

There are 1229 unique profile names. The list is alphabetical by make, then by 
name. Only the make name is needed to run the script. 

Profiles named `OBD-II / EOBD` are universal and apply to many makes, so they 
are grouped under "Universal".

| # | Make | Name |
|---|------|------|
| 1 | Acura, Honda | Honda/Acura Hybrids |
| 2 | Aiways | U5 |
| 3 | Alfa Romeo | 156 (BOSCH M1.5.5) |
| 4 | Alfa Romeo | Giulia |
| 5 | Alfa Romeo | Stelvio |
| 6 | Alfa Romeo, Fiat | Giulietta 1.4 MultiAir 16V (CAN) |
| 7 | Alfa Romeo, Fiat | MiTo 1.2 Fire 8V (CAN) |
| 8 | Alfa Romeo, Fiat | MiTo 1.3 MultiJet 16V (CAN) |
| 9 | Alfa Romeo, Fiat | MiTo 1.4 MultiAir 16V (CAN) |
| 10 | Audi | EV: eTron 55 |
| 11 | Audi | MLB-EVO: Diesel DPF var.13 [EA288 Evo 2.0TDI] (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A8 4N, A7 4K8, A6 4K, Q8 4MN, VW Touareg CR) |
| 12 | Audi | MLB-EVO: TSI/TFSI EA211 1.4/1.5L (Audi: A4 8W, A5 8W) |
| 13 | Audi | MLB: 2.0 TSI/TFSI: CAEB, CDNC |
| 14 | Audi | MLB: 2.0 TSI/TFSI: CPMA |
| 15 | Audi | MLB: A5/S5 B8/8T (2007-2013) + AT |
| 16 | Audi | MLB: Diesel DPF var.16 [EA896] |
| 17 | Audi | MLB: Diesel var.14 EA189 2.0 TDI (UDS ECM ONLY) |
| 18 | Audi | MLB: EA824 4.0 TFSI (CWUB, CWUC) |
| 19 | Audi | MQB: TSI/TFSI EA855 EVO 2.5 (DAZA, DNWA, DNWC, DNWD) |
| 20 | Audi | WWH-OBD (CAN 11 bit) |
| 21 | Audi, Bentley, Porsche, Volkswagen | MLB-EVO: Diesel EA898 4.0L |
| 22 | Audi, Cupra | MQB-EVO: TSI/TFSI EA855 2.5L |
| 23 | Audi, Cupra, Ford, Jetta, Porsche, Seat, Skoda, Volkswagen | EV MEB: ID.3, ID.4, ID.5, ID.6, ID.7, ID.Buzz, Enyaq, Elroq, Q4 E-tron, Q6 e-tron, Cupra Born, Cupra Tavascan, Porsche Macan EV, etc.; Ford Explorer EV, Capri EV |
| 24 | Audi, Cupra, Jetta, Seat, Skoda, Volkswagen | MQB-EVO: 1.6 MPI |
| 25 | Audi, Cupra, Jetta, Seat, Skoda, Volkswagen | MQB-EVO: Diesel DPF var.7 [EA288Evo] |
| 26 | Audi, Cupra, Jetta, Seat, Skoda, Volkswagen | MQB-EVO: TSI/TFSI EA211 1.4L; 1.5L; EA888 2.0L <200hp |
| 27 | Audi, Cupra, Jetta, Seat, Skoda, Volkswagen | MQB-EVO: TSI/TFSI EA888 2.0L >200hp |
| 28 | Audi, Jetta, Porsche, Seat, Skoda, Volkswagen | MLB: EA837 3.0L TFSI |
| 29 | Audi, Jetta, Porsche, Seat, Skoda, Volkswagen | MQB, PQ26: TSI/TFSI 1.0L-2.0L CAN-UDS + AT/DSG |
| 30 | Audi, Jetta, Porsche, Seat, Skoda, Volkswagen | MQB: TSI/TFSI EA888 Gen.3 (1.8L; 2.0L >200 hp) |
| 31 | Audi, Jetta, Porsche, Seat, Skoda, Volkswagen | MQB: TSI/TFSI EA888 Gen.3B, EA888 Evo4 (Gen.4) 2.0L (with Miller cycle) |
| 32 | Audi, Jetta, Porsche, Seat, Skoda, Volkswagen | VW TP2.0 Readings |
| 33 | Audi, Jetta, Seat, Skoda, Volkswagen | MQB, PQ26: Diesel DPF var.1 [EA288] |
| 34 | Audi, Jetta, Seat, Skoda, Volkswagen | MQB, PQ26: Diesel DPF var.2 [EA288] |
| 35 | Audi, Jetta, Seat, Skoda, Volkswagen | MQB, PQ26: Diesel DPF var.3 [EA288] |
| 36 | Audi, Jetta, Seat, Skoda, Volkswagen | MQB, PQ26: MPI 1.0 / 1.6 CAN-UDS + AT |
| 37 | Audi, Jetta, Seat, Skoda, Volkswagen | MQB, PQ26: TSI/TFSI EA211 1.0L/1.2L/1.4L/1.5L |
| 38 | Audi, Jetta, Seat, Skoda, Volkswagen | MQB: Diesel DPF var.11 [EA288 Evo] |
| 39 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ25, PQ26, PQ35, PQ46, MQB: Diesel 1.6 TDI CAYC, CAYA engine |
| 40 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ25, PQ35, PQ46 |
| 41 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ25, PQ35, PQ46 + UDS AT/DSG DQ500 |
| 42 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ25, PQ35: EA211 1.4 TSI (UDS) |
| 43 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ35, PQ46 ONLY UDS Dashboard |
| 44 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ35, PQ46: Diesel DPF var.10: EA189 1.6, 2.0L (UDS + VWTP2.0 AT/DSG) |
| 45 | Audi, Jetta, Seat, Skoda, Volkswagen | PQ35: TSI/TFSI 1.2 EA111 (UDS) |
| 46 | Audi, Porsche | EV: eTron, eTron GT, Taycan |
| 47 | Audi, Porsche, Volkswagen | MLB-EVO: TSI/TFSI EA839 3.0L |
| 48 | Audi, Porsche, Volkswagen | MLB: VW Touareg II (NF), Audi Q7 4L, Porsche Cayenne II (3.0D / 3.6 FSI / 4.2D) |
| 49 | Audi, Volkswagen | MLB-EVO: Diesel DPF var.12 [EA897 Evo 3.0TDI] (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A8 4N, A7 4K8, A6 4K, Q8 4MN, VW Touareg CR) |
| 50 | Audi, Volkswagen | MLB-EVO: Diesel DPF var.15 [EA897 Evo3 3.0TDI] |
| 51 | Audi, Volkswagen | MLB-EVO: Diesel DPF var.4 [EA288 2.0 TDI] (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A8 4N, A7 4K8, A6 4K, Q8 4MN) |
| 52 | Audi, Volkswagen | MLB-EVO: Diesel DPF var.5 [EA897 3.0TDI] (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A8 4N, A7 4K8, A6 4K, Q8 4MN, VW Touareg CR) |
| 53 | Audi, Volkswagen | MLB-EVO: Diesel DPF var.8 [EA897 Evo2 3.0TDI] (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A8 4N, A7 4K8, A6 4K, Q8 4MN, VW Touareg CR) |
| 54 | Audi, Volkswagen | MLB-EVO: Diesel DPF var.9 [EA897 gen.2 3.0TDI] (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A8 4N, A7 4K8, A6 4K, Q8 4MN, VW Touareg CR) |
| 55 | Audi, Volkswagen | MLB-EVO: TSI/TFSI EA888 Gen.3(3B) (2.0L >200 hp) (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A7 4K8, A6 4K, Q8 4MN, VW Touareg CR) |
| 56 | Audi, Volkswagen | MLB-EVO: TSI/TFSI EA888 Gen.3B, EA888 Evo4 (Gen.4) 2.0L (with Miller cycle) (Audi: A4 8W, A5 8W, Q5 80A, Q7 4M, A7 4K8, A6 4K) |
| 57 | Audi, Volkswagen | MLB: Diesel DPF var.6 [EA897] |
| 58 | Audi, Volkswagen | MQB: Passat B8 GTE Hybrid, Golf 7 GTE Hybrid, A3 e-Tron Hybrid |
| 59 | Avatr | Avatr 11 |
| 60 | BAIC | Beijing U5 Plus |
| 61 | BAIC | Senova X55 / Beijing X5 |
| 62 | Baojun, MG, SAIC-GM-Wuling, Wuling | Baojun Yunduo 宝骏云朵 / Wuling Cloud EV / MG Windsor EV (India) |
| 63 | Belgee, Geely, Proton | Geely Galaxy Starship 7 / EX5 EM-i / E5 EM-i / Galaxy EX5 EM-i / Starray EM-i / BelGee X80 PHEV / Proton eMas 7 PHEV |
| 64 | Belgee, Geely, Proton | SX11 / Coolray / Binyue / Atlas PRO / Binyue PRO / X50 1.5T (3 cylinders) +DCT |
| 65 | BMW | i3 (pure EV) |
| 66 | BMW | i3 + ICE range extender |
| 67 | BMW | i4, i5, i7, iX, iX1, IX2 and PHEV [+ OBDII] |
| 68 | BMW | i4, i5, i7, iX, iX1, IX2 and PHEV [EV BATTERY ONLY] |
| 69 | BMW | iX3 (G08) |
| 70 | BMW | N47, N57(*) |
| 71 | Briggs & Stratton, Delphi | Delphi MT05 / MT05.2 / Briggs & Stratton MT05 |
| 72 | BYD | BYD Electric Vehicle (EV) |
| 73 | BYD | E6Y |
| 74 | BYD | Qin Plus DM-i |
| 75 | BYD | Seagull EV / Dolphin Mini |
| 76 | BYD | Tang DM-p |
| 77 | BYD, Chery, Great Wall | Delphi MT20U (Tiggo, Hover, etc.) |
| 78 | BYD, Chery, Great Wall | Delphi MT20U2 (Tiggo, Hover, etc.) |
| 79 | BYD, Denza | Atto 2 / Atto 3 / Yuan Plus EV / Dolphin / Seal / Seal U / Sealion / M6 / eMax 7 / 海豚 / Denza D9 / Denza N7 / Sealion 7 EV (EU version, only before 2024.10 update) |
| 80 | Changan | CS35 |
| 81 | Changan | CS35 Plus |
| 82 | Changan | CS35 Plus New (1.4T) |
| 83 | Changan | CS55 Plus (2017-) 1.5 + AT |
| 84 | Changan | CS55 Plus (2017-) 1.5 + DCT |
| 85 | Changan | CS55 Plus II (2021-) |
| 86 | Changan | CS75 |
| 87 | Changan | CS75 FL (1.8+AT) |
| 88 | Changan | CS75 FL (1.8+DCT) |
| 89 | Changan | CS75 Plus 1.5 |
| 90 | Changan | CS75 Plus 2.0 |
| 91 | Changan | CS95 (2.0+AT) |
| 92 | Changan | EADO Plus 2022- (1.4T) |
| 93 | Changan | UNI-K (1.5/2.0+AT) |
| 94 | Changan | UNI-K (1.5/2.0+DCT) |
| 95 | Changan | UNI-T (1.5+DCT) |
| 96 | Changan | UNI-T (2.0+AT) |
| 97 | Changan | UNI-V (1.5+DCT) |
| 98 | Changan | UNI-V (2.0+AT) |
| 99 | Changan, Deepal | G318 |
| 100 | Changan, Deepal | S07 |
| 101 | Changan, Deepal, Mazda | EZ-6 / 6e |
| 102 | Chery | Acteco BOSCH ME 7.8.8 |
| 103 | Chery | Acteco BOSCH ME 7.9.7 |
| 104 | Chery | Arrizo 5 (Country VI) |
| 105 | Chery | Arrizo 8 / M1E 1.6/2.0 |
| 106 | Chery | QQ Marelli |
| 107 | Chery | Tiggo + CVT19 |
| 108 | Chery | Tiggo + CVT25/CVT18 |
| 109 | Chery | Tiggo 8 Pro Max |
| 110 | Chery | Tiggo 9 (AT) |
| 111 | Chery | Tiggo 9 (DCT) |
| 112 | Chery, Exeed | Exeed New TX/TXL 1.6T (2021-) |
| 113 | Chery, Exeed | Exeed New TX/TXL 2.0T (2022-) |
| 114 | Chery, Exeed | Exeed RX (T22) + 7DCT300/400 |
| 115 | Chery, Exeed | Exeed RX (T22) + 8AT |
| 116 | Chery, Exeed | Exeed TX/TXL 1.6T (-2021) |
| 117 | Chery, Exeed | Exeed VX + 8AT |
| 118 | Chery, Exeed | Exeed VX + DCT |
| 119 | Chery, Exeed, Omoda, Soueast | Tiggo 7/7 Pro, T15/T18/T1A, Tiggo 8/8 Pro, T18, T1D, Tiggo 4, Exeed LX, Omoda C5 1.5T/1.6T/2.0T + DCT |
| 120 | Chery, Exeed, Omoda, Xcite | Tiggo 7/7 Pro, T15/T18/T1A, Tiggo 8/8 Pro, T18, T1D, Exeed LX, Omoda C5 1.5T/2.0T, Tiggo 4 Pro 1.5T, XCross 7 + CVT25/18 |
| 121 | Chery, Exeed, Omoda, Xcite | Tiggo 7/7 Pro, T15/T18/T1A, Tiggo 8/8 Pro, T18, T1D, Tiggo 4 Pro, Exeed LX, Omoda C5 1.5T/2.0T, Tiggo 4 2.0, XCross 7 + CVT19 |
| 122 | Chery, Kaiyi, Omoda | Arrizo 7 / Kaiyi E5 / Omoda S5 1.5T |
| 123 | Chery, Omoda | Omoda C5 / 5 1.6 DCT |
| 124 | Chery, Omoda | Omoda E5 / C5 EV |
| 125 | Chery, Omoda | Omoda S5 GT 1.6T + 7DCT |
| 126 | Chevrolet | Camaro Gen.6 (2016-2024) 3.6 |
| 127 | Chevrolet, Daewoo, Opel, Vauxhall | ECU Sirius D42 (EN) |
| 128 | Chevrolet, Daewoo, Opel, Vauxhall | ECU Sirius D42 (RU) |
| 129 | Chevrolet, Daewoo, Opel, Vauxhall | Lacetti + AT |
| 130 | Chevrolet, General Motors, GMC | Silverado / Sierra 6.6L Duramax Diesel (2024-n.d.) |
| 131 | Chevrolet, General Motors, GMC | Silverado/Sierra 3.0 LZ0 (2023-n.d.) |
| 132 | Chevrolet, General Motors, Opel | Bolt / Ampera-E |
| 133 | Chevrolet, General Motors, Opel | Bolt / Ampera-E 2017-2020 |
| 134 | Chevrolet, General Motors, Opel | Volt / Ampera |
| 135 | Chevrolet, Holden, Opel, Vauxhall | Combo C 1.3 CDTi |
| 136 | Chevrolet, Opel, Vauxhall | A14NET |
| 137 | Chevrolet, Opel, Vauxhall | A20DTH |
| 138 | Chevrolet, Opel, Vauxhall | B16DTH |
| 139 | Chevrolet, Opel, Vauxhall | B20DTH |
| 140 | Chrysler | Grand Voyager 2009 |
| 141 | Chrysler | Pacifica Minivan 2015+ |
| 142 | Chrysler, Dodge, Jeep | 5.7L / 6.4L Hemi Engine |
| 143 | Cirelli, Dongfeng, Fengxing, FMC, Forthing | Yacht /  Forthing 4 U-Tour / Youting / Cirelli 7 / Suba M4 (ECM var.1) |
| 144 | Cirelli, Dongfeng, Fengxing, FMC, Forthing | Yacht /  Forthing 4 U-Tour / Youting / Cirelli 7 / Suba M4 (ECM var.2) |
| 145 | Citroen | C4 B7 (2010-) |
| 146 | Citroen | C4 with 1.6 BOSCH MED 17.4.2 |
| 147 | Citroen, DS, Fiat, Jeep, Opel, Peugeot, Vauxhall | EV Electric (Stellantis/PSA based) |
| 148 | Citroen, DS, Fiat, Jeep, Opel, Peugeot, Vauxhall | EV Electric STLA Medium |
| 149 | Citroen, DS, Opel, Peugeot, Vauxhall | HEV/PHEV Hybrids (Stellantis/PSA based) 2021-n.d. |
| 150 | Citroen, DS, Peugeot | 1.5 BlueHDI ECU MD1CS003 |
| 151 | Citroen, DS, Peugeot | AISIN8 |
| 152 | Citroen, Fiat, Opel | Citroen e-C3 CC21 (2024-) / Fiat Grande Panda EV (2025-) / Opel Frontera EV (2024-) |
| 153 | Citroen, Fiat, Opel, Peugeot, RAM, Vauxhall | Fiat: Ducato; Peugeot: Boxer/Manager; Citroen: Relay/Jumper; RAM: ProMaster; Opel/Vauxhall: Movano 2.0 HDI / 2.2 HDI (2021-) |
| 154 | Citroen, Fiat, Opel, Peugeot, RAM, Vauxhall | Fiat: Ducato; Peugeot: Boxer/Manager; Citroen: Relay/Jumper; RAM: ProMaster; Opel/Vauxhall: Movano 2.2 Blue HDI (2021-) |
| 155 | Citroen, Fiat, Opel, Peugeot, RAM, Vauxhall | Fiat: Ducato; Peugeot: Boxer/Manager; Citroen: Relay/Jumper; RAM: ProMaster; Opel/Vauxhall: Movano 2.2 HDI |
| 156 | Citroen, Fiat, Opel, Peugeot, RAM, Vauxhall | Fiat: Ducato; Peugeot: Boxer/Manager; Citroen: Relay/Jumper; RAM: ProMaster; Opel/Vauxhall: Movano 3.0 HDI |
| 157 | Citroen, Fiat, Opel, Peugeot, Toyota, Vauxhall | Citroen: Spacetourer/Dispatch/Jumpy; Peugeot: Expert/Traveller; Toyota: ProAce; Fiat: Scudo/Ulysse; Opel Zafira Life; Vauxhall: Vivaro [2.0 HDI ECU: DCM6.2] |
| 158 | Citroen, Fiat, Peugeot, Toyota | Citroen Jumpy II/Dispatch; Fiat Scudo; Peugeot Expert; Toyota Proace [2.0 Diesel ECU SID803A] |
| 159 | Citroen, Mitsubishi, Peugeot | Outlander II, XL, III, ASX, RVR (2.0, 2.4), Lancer X (1.8, 2.0), ASX (1.8, 2.0), Citroen C-Crosser, Peugeot 3008 (2008-2016), 4007 (2007-2012) + CVT |
| 160 | Citroen, Peugeot | AL4 K-Line/KWP |
| 161 | Citroen, Peugeot | Bosch MEDV 17.4.4 ECU (EP6FDTX) |
| 162 | Citroen, Peugeot | ECU EDC16C3 KWP |
| 163 | Citroen, Peugeot | ECU EDC17C10_BR2 |
| 164 | Citroen, Peugeot | ECU EDC17C60 |
| 165 | Citroen, Peugeot | ECU MD1CS003 |
| 166 | Citroen, Peugeot | ECU MEV 17.4.2 |
| 167 | Citroen, Peugeot | ECU MEV_17_4_EURO_4 |
| 168 | Dacia | Spring FL 2024- |
| 169 | Dacia, Nissan, Renault | Duster / Terrano III 1.5 dCi |
| 170 | Dacia, Nissan, Renault | Duster / Terrano III 1.6 |
| 171 | Dacia, Nissan, Renault | Duster / Terrano III AT RU |
| 172 | Dacia, Nissan, Renault | Duster I / Terrano III 2.0 4WD [EN] |
| 173 | Dacia, Nissan, Renault | Duster I / Terrano III 2.0 4WD [RU] |
| 174 | Dacia, Nissan, Renault | Duster II 1.5 dCi [EN] |
| 175 | Dacia, Nissan, Renault | Duster II 1.5 dCi [RU] |
| 176 | Dacia, Nissan, Renault | Duster II 2.0 F4R [EN] |
| 177 | Dacia, Nissan, Renault | Duster II 2.0 F4R [RU] |
| 178 | Dacia, Nissan, Renault | Duster ph.1 / Terrano III 2.0 4WD [RU] |
| 179 | Dacia, Nissan, Renault | Duster ph.2 / Duster II / Terrano III / Kaptur 1.6 H4M [EN] |
| 180 | Dacia, Nissan, Renault | Duster ph.2 / Duster II / Terrano III / Kaptur 1.6 H4M [RU] |
| 181 | Dacia, Nissan, Renault | Duster ph.2 / Terrano III 1.5 dCi 4WD [EN] |
| 182 | Dacia, Nissan, Renault | Duster ph.2 / Terrano III 1.5 dCi 4WD [RU] |
| 183 | Dacia, Nissan, Renault | Duster ph.2 / Terrano III 2.0 F4R [EN] |
| 184 | Dacia, Nissan, Renault | Duster ph.2 / Terrano III 2.0 F4R [RU] |
| 185 | Dacia, Renault | Duster ph.1 / ph.2 1.2 TCE H5Ft |
| 186 | Dacia, Renault | Jogger Hybrid 140, Clio V Hybrid, Captur Hybrid, Arkana Hybrid |
| 187 | Dacia, Renault | Kaptur 2.0 F4R [EN] |
| 188 | Dacia, Renault | Kaptur 2.0 F4R [RU] |
| 189 | Dacia, Renault | Logan 1.4/1.6 (CAN) |
| 190 | Dacia, Renault | Logan 1.5 dCi (CAN) |
| 191 | Dacia, Renault | Logan 1.5 dCi K9K 796 K-Line/KWP [EN] |
| 192 | Dacia, Renault | Logan 1.5 dCi K9K 796 K-Line/KWP [RU] |
| 193 | Dacia, Renault | Logan I, Sandero I K7J 1.4 |
| 194 | Dacia, Renault | Logan I, Sandero I, Thalia, Symbol II 1.4/1.6 8v (KWP) [EN] |
| 195 | Dacia, Renault | Logan I, Sandero I, Thalia, Symbol II 1.4/1.6 8v (KWP) [RU] |
| 196 | Dacia, Renault | Logan II / Sandero II 0.9L H4B [EN] |
| 197 | Dacia, Renault | Logan II / Sandero II 0.9L H4B [RU] |
| 198 | Dacia, Renault | Logan II, Sandero II 1.0 B4D |
| 199 | Dacia, Renault | Logan II, Sandero II K7M (CAN) [EN] |
| 200 | Dacia, Renault | Logan II, Sandero II K7M (CAN) [RU] |
| 201 | Dacia, Renault | Logan II, Sandero II, Sandero Stepway II (X52) K4M/H4M + CAN [EN] |
| 202 | Dacia, Renault | Logan II, Sandero II, Sandero Stepway II (X52) K4M/H4M + CAN [RU] |
| 203 | Dacia, Renault | Logan II, Sandero II, Sandero Stepway II (X52) K4M/H4M + K-Line [EN] |
| 204 | Dacia, Renault | Logan II, Sandero II, Sandero Stepway II (X52) K4M/H4M + K-Line [RU] |
| 205 | Dacia, Renault | Logan III / Sandero III / Clio V / Captur II (2019-) H4Dt 1.0L, H5Ht 1.3L |
| 206 | Dacia, Renault | Megane III / Megane IV / Scenic III / Scenic IV / SM3 / Fluence / Kangoo ZE / Lodgy / Clio IV / Captur / Duster ph.2 / Kadjar / Talisman 1.5 dCi K9K 656 |
| 207 | Dacia, Renault | Megane IV / Scenic IV / Talisman / SM6 / Kadjar / Captur / Duster III K9K 646 |
| 208 | Dacia, Renault | Sandero 1.5 dCi (CAN) |
| 209 | Dacia, Renault | Sandero 1.6 (CAN) |
| 210 | Dacia, Renault | Spring / CITY K-ZE var.1 |
| 211 | Dacia, Renault | Spring / CITY K-ZE var.2 |
| 212 | Dacia, Renault | Talisman 1.5dci 2016-2019 K9K 649 [EN] |
| 213 | Dacia, Renault | Talisman 1.5dci 2016-2019 K9K 649 [RU] |
| 214 | Dacia, Renault, Samsung | Arkana, Kaptur, Duster II 1.3 TCe [EN] |
| 215 | Dacia, Renault, Samsung | Arkana, Kaptur, Duster II 1.3 TCe [RU] |
| 216 | Dacia, Renault, Samsung | Arkana/XM3 1.6 [EN] |
| 217 | Dacia, Renault, Samsung | Arkana/XM3 1.6 [RU] |
| 218 | Daihatsu | JDM K-Line var.1 |
| 219 | Daihatsu | JDM K-Line var.2 |
| 220 | Datsun, Lada, ВАЗ, Лада | Granta / Mi-Do / On-Do + АКПП Jatco |
| 221 | Delphi | MT05.3 (CAN) |
| 222 | Delphi, Rongmao | Delphi MT05 / MT05.2 / Rongmao MT05 |
| 223 | Dodge, Fiat | Dart / Viaggio |
| 224 | Dodge, Jeep | Patriot, Compass, Grand Cherokee, Caliber |
| 225 | Dodge, Jeep, RAM | 3.0 V6 Eco-Diesel |
| 226 | Dodge, Mitsubishi | Mirage (2012-), Space Star, Dodge Attitude 1.2 |
| 227 | Dodge, RAM | RAM 1500 2006 3.7 Magnum V6 |
| 228 | Dodge, RAM | RAM 5.7 2008+ |
| 229 | Dodge, RAM | RAM 5.9 2006-2007 |
| 230 | Dodge, RAM | RAM 6.7 2007-2010 |
| 231 | Dodge, RAM | RAM 6.7 2010-2012 |
| 232 | Dodge, RAM | RAM 6.7 2013-2019 |
| 233 | Dongfeng | 580 |
| 234 | Dongfeng | S30/H30/H30 Cross (CAN) |
| 235 | Elaris, Imperium, Skywell, Skyworth | ET5/EV6/Beo/Imperium SEV/BE11 |
| 236 | Euler, Great Wall, Ora | Good Cat / Funky Cat / ES11 / Haomao / Ora 03 / Lightning Cat / ORA 07 / 好猫 |
| 237 | FAW | Bestune T77 |
| 238 | FAW, Hongqi | Hongqi H5 (2020-2022) |
| 239 | FAW, Hongqi | Hongqi HS5 (3023-) |
| 240 | Fiat | 500 |
| 241 | Fiat | 500 1.2 Fire 8V (CAN) |
| 242 | Fiat | 500 1.3 MultiJet 16V (CAN) |
| 243 | Fiat | 500 1.4 MultiAir 16V (CAN) |
| 244 | Fiat | 500 1.4 T-Jet 16V (CAN) |
| 245 | Fiat | 500e (2013 - 2019) |
| 246 | Fiat | 500e (2020-) BEV Electric |
| 247 | Fiat | 500X |
| 248 | Fiat | Bravo 1.4 T-Jet 16V (CAN) |
| 249 | Fiat | Bravo 1.4 T-Jet 16V (KWP) |
| 250 | Fiat | Doblo 1.3 MultiJet 16V (CAN) |
| 251 | Fiat | Doblo 1.4 8v KWP |
| 252 | Fiat | Freemont Diesel |
| 253 | Fiat | Punto 1.2 8V (CAN) |
| 254 | Fiat | Punto 1.3 MultiJet 16V (CAN) |
| 255 | Fiat | Punto 1.4 Fire 8V (CAN) |
| 256 | Fiat | Punto 1.4 MultiAir 16V (CAN) |
| 257 | Fiat | Punto 1.4 T-Jet 16V (CAN) |
| 258 | Fiat | Punto 1.4 T-Jet 16V (KWP) |
| 259 | Fiat | Qubo 1.2 Fire 8V (CAN) |
| 260 | Fiat | Qubo 1.3 MultiJet 16V (CAN) |
| 261 | Fiat | Tipo / Egea 1.6 Multijet |
| 262 | Fiat | Tipo 1.3 Mjet Diesel |
| 263 | Fiat | Ypsilon 1.2 Fire 8V (CAN) |
| 264 | Fiat | Ypsilon 1.3 MultiJet
16V (CAN) |
| 265 | Ford | 3.0L & 3.2L Diesel |
| 266 | Ford | Bronco 2021- |
| 267 | Ford | EcoSport 1.6 Ztec 2009- |
| 268 | Ford | Everest Gen.3 U704/UB (2022-n.d.) 3.0 Diesel + 10AT |
| 269 | Ford | Explorer 3.5 TiVCT |
| 270 | Ford | Explorer Gen.6 3.0L (2020-n.d.) |
| 271 | Ford | F150 VCT |
| 272 | Ford | Falcon 4.0 |
| 273 | Ford | Focus II ST 2.5 |
| 274 | Ford | Ford PHEV plug-in hybrid |
| 275 | Ford | Fusion 2.0 ecoboost |
| 276 | Ford | Maverick 2022-n.d. 2.5 Hybrid |
| 277 | Ford | Mondeo Hybrid / Fusion Hybrid |
| 278 | Ford | Mustang 2.3 EcoBoost (2015-2018) |
| 279 | Ford | Mustang 2011 5.0 V8 |
| 280 | Ford | Mustang 2011-2017 3.7 V6 |
| 281 | Ford | Mustang GT 2016 5.0 |
| 282 | Ford | Mustang Mach-E (2023-) |
| 283 | Ford | Mustang Mach-E / F-150 Lightning / E-Transit |
| 284 | Ford | Powerstroke 6.0L CAN |
| 285 | Ford | Powerstroke 6.4L CAN |
| 286 | Ford | Powerstroke 6.7L CAN |
| 287 | Ford | Powerstroke 7.3L |
| 288 | Ford | PUMA Gen-E, E-Transit Custom |
| 289 | Ford | Ranger Gen.2 P703/RA (2022-n.d.) 3.0 Diesel + 10AT |
| 290 | Ford | Ranger Gen.2 P703/RA (2022-n.d.) 3.0 Gasoline + 10AT |
| 291 | Ford, Lincoln | WWH-OBD + CAN and extra PIDs (2025-) |
| 292 | Ford, Mazda | Everest / Ranger / BT-50 Gen.2 |
| 293 | GAC, Toyota | BZ3X |
| 294 | GAC, Trumpchi | Aion Y Plus; Aion V Gen.2 (2024-) (BMS: G-Pulse) |
| 295 | GAC, Trumpchi | GN8 (-2020.07) |
| 296 | GAC, Trumpchi | GN8 (2019/07-2020/06) |
| 297 | GAC, Trumpchi | GS3 Shadow Speed / GS3 Yingsu (2023-n.d.) |
| 298 | GAC, Trumpchi | GS5 (2019-) |
| 299 | GAC, Trumpchi | GS8 (-2019/07) |
| 300 | GAC, Trumpchi | GS8 Gen.2 (2021-n.d.) |
| 301 | GAC, Trumpchi | GS8/GS8S (2019/08-) |
| 302 | Geely | Emgrand Gen.4 (2021-) |
| 303 | Geely | MK M7.9.7 |
| 304 | Geely | Monjaro |
| 305 | Geely | NL-3 / Boyue / Atlas 1.8T |
| 306 | Geely | NL-3 / Boyue / Atlas 2.0, 2.4 |
| 307 | Geely | NL3-B / Atlas PRO / Boyue PRO 1.5T+ AT |
| 308 | Geely | OKAVANGO / Haoyue / 吉利豪越 1.5T |
| 309 | Geely | OKAVANGO / Haoyue / 吉利豪越 2.0T |
| 310 | Geely | Preface |
| 311 | Geely | X7 (NL-4) |
| 312 | Geely, Geometry | Geometry C |
| 313 | Geely, Knewstar | 吉利星越 / Xingyue / Tugella / Knewstar 001 |
| 314 | Geely, Livan | Coolray / Binyue / Vision X6 Pro 1.5T (4 cylinders) 2023- |
| 315 | Geely, Livan, Maple | Yuanjing V3/GX3/GX3 Pro/X3Pro (2017-2020) |
| 316 | Geely, Livan, Maple | Yuanjing V3/GX3/GX3 Pro/X3Pro (2020-) |
| 317 | Geely, Lynk & Co, Proton, Smart, Volvo, Zeekr | EX30 electric / Smart #1 (EV) / Smart #3 (EV) / Zeekr 001 / Zeekr X / Zeekr Mix / Geely EX5 / Galaxy E5 / Geely EX5 / Lynk & Co 02 |
| 318 | General Motors, Opel, Vauxhall | Simtec 56.5 |
| 319 | Genesis | G80 2.0 |
| 320 | Genesis | G80 2.5T |
| 321 | Genesis | GV70 2.2D CRDI |
| 322 | Genesis | GV80 2.5T |
| 323 | Genesis | GV80 3.0D |
| 324 | Genesis, Hyundai, Kia | IONIQ 5 (2022-2025) / IONIQ 6 / Inster / EV3 / EV5 / EV6 / Niro EV 2023- / Kona EV 2023- / Ray EV 2023- / Genesis GV60 / GV70 EV / G80 Electrified |
| 325 | GMC | Yukon/Chevrolet Tahoe/Cadillac escalade Hybrid |
| 326 | Great Wall | Cannon/Poer/Sahar (2023-) 2.0 Diesel |
| 327 | Great Wall | Cannon/Poer/Sahar (2023-) 2.4 Diesel |
| 328 | Great Wall, Haval | Cool Dog / H3 (2022-n.d.) |
| 329 | Great Wall, Haval | Dagou / Dargo / Big Dog / 大狗 |
| 330 | Great Wall, Haval | H5 4D20 (Bosch) |
| 331 | Great Wall, Haval | H5 4D20 (Delphi) |
| 332 | Great Wall, Haval | H5 4G63T |
| 333 | Great Wall, Haval | H5 Gen.2 (2023-) 4C20B |
| 334 | Great Wall, Haval | H7 (2025-) / F7 (2025-) / Shenshou (2025-) |
| 335 | Great Wall, Haval | M6 2021- |
| 336 | Great Wall, Haval, Tank, WEY | Tank 300 |
| 337 | Great Wall, Haval, Tank, WEY | Tank 300 2.0T 4C20B/E20CB + 8AT (2025-n.d.) |
| 338 | Great Wall, Haval, Tank, WEY | Tank 300 2.4 Diesel + 9AT (2025-n.d.) |
| 339 | Great Wall, Haval, Tank, WEY | Tank 300 Hi4T 2.0+9AT+Hybrid |
| 340 | Great Wall, Haval, Tank, WEY | Tank 400 |
| 341 | Great Wall, Haval, Tank, WEY | Tank 500 2.0T+HEV |
| 342 | Great Wall, Haval, Tank, WEY | Tank 500 3.0+9AT |
| 343 | Great Wall, WEY | Mocha / Coffee 01 / 05 |
| 344 | Harvard, Haval | First Love / Jolion 1.5T (4B15D) |
| 345 | Harvard, Haval | First Love / Jolion 1.5T (4G15H, 4G15K, 4B15C) |
| 346 | Haval | F7 (2020-), F7x (4B15A, 4C20B, 4G15K) |
| 347 | Haval | F7 (2020-), F7x (4C20NT) |
| 348 | Haval | H6 gen.2 / H6 Coupe / H6 Sport 1.5T + 6AT |
| 349 | Haval | H6 gen.3 (2020-) |
| 350 | Haval | H6 Gen.3 HEV/PHEV (2021-) |
| 351 | Haval | H9 2.0 2014-2019 |
| 352 | Haval | H9 2020-2024 (4B15A, 4C20B) |
| 353 | Haval | H9 2020-2024 (4D20M) |
| 354 | Haval | H9 New 2024- (2.0 Gasoline 4C20B) |
| 355 | Haval | H9 New 2024- (2.4 Diesel 4D24) |
| 356 | Honda | Accord, Civic, CRV, CX-7 etc. 2008-2012 (var.1) |
| 357 | Honda | Accord, Civic, CRV, CX-7 etc. 2008-2012 (var.2) |
| 358 | Honda | Clarity PHEV, e:NY1 |
| 359 | Honda | CR-V RE6 Diesel |
| 360 | Honda | E |
| 361 | Honda | Fit GK3 |
| 362 | Honda | Insight II (2010-2014) |
| 363 | Hyundai | Accent III / Verna MC 1.5 CRDI |
| 364 | Hyundai | Accent III MC / Verna 1.4/1.6 MPI |
| 365 | Hyundai | Accent IV (RB/RC) / Verna / i25 / Excel III / Grand Pony 2010-2017 1.4/1.6 MPI |
| 366 | Hyundai | Accent IV RB 1.4/1.6 GDI |
| 367 | Hyundai | Accent IV RB 1.6 CRDI |
| 368 | Hyundai | Accent V / Verna HC 1.5 CRDI |
| 369 | Hyundai | Accent V / Verna HC 1.6 CRDI (2018-2022) |
| 370 | Hyundai | Creta / ix25 1.6 MPI AT 2WD |
| 371 | Hyundai | Creta / ix25 1.6 MPI AT 2WD (Alternative) |
| 372 | Hyundai | Creta / ix25 1.6 MPI AT 4WD |
| 373 | Hyundai | Creta / ix25 1.6 MPI AT 4WD (Alternative) |
| 374 | Hyundai | Creta / ix25 1.6 MPI MT 2WD |
| 375 | Hyundai | Creta / ix25 1.6 MPI MT 2WD (alternative) |
| 376 | Hyundai | Creta / ix25 1.6 MPI MT 4WD |
| 377 | Hyundai | Creta / ix25 1.6 MPI MT 4WD (alternative) |
| 378 | Hyundai | Creta / ix25 2.0 MPI AT 2WD |
| 379 | Hyundai | Creta / ix25 2.0 MPI AT 2WD (alternative) |
| 380 | Hyundai | Creta / ix25 2.0 MPI AT 4WD |
| 381 | Hyundai | Creta / ix25 2.0 MPI AT 4WD (alternative) |
| 382 | Hyundai | Creta / ix25 GS 1.6 CRDI 2015-2020 |
| 383 | Hyundai | Creta 2 SU2r 2.0 MPI (2021-2022) |
| 384 | Hyundai | Custo / Custin (KU) 1.5 T-GDI (2021-n.d.) |
| 385 | Hyundai | Custo / Custin (KU) 2.0 T-GDI (2021-n.d.) |
| 386 | Hyundai | Elantra AD (J6) 1.6 (2015-2019) |
| 387 | Hyundai | Elantra AD 1.6 T-GDI + DCT (2017-2020) |
| 388 | Hyundai | Elantra CN7 2.0 SmartStream+CVT (2023-) |
| 389 | Hyundai | Elantra CN7 HEV (2020-) |
| 390 | Hyundai | Elantra N |
| 391 | Hyundai | Elantra, Avante AD (J6) 2.0L (2015-2020) |
| 392 | Hyundai | Elantra, Avante CN7 (2020-) |
| 393 | Hyundai | Elantra, Avante HD (J4) (2006-2010) |
| 394 | Hyundai | Elantra, Avante, i35 MD/UD (J5) 1.6/1.8 (2010-2016) |
| 395 | Hyundai | Elantra/Avante AD 1.6 LPI (2015-2020) |
| 396 | Hyundai | Elantra/i30 FD 2.0 MPI (2006-2010) |
| 397 | Hyundai | Equus |
| 398 | Hyundai | Genesis Coupe BK-A 2.0 MPI |
| 399 | Hyundai | Genesis Coupe BK-A 3.8 V6 |
| 400 | Hyundai | Genesis Coupe BK-B 2.0 MPI |
| 401 | Hyundai | Genesis Coupe BK-B 3.8 V6 MPI |
| 402 | Hyundai | Genesis Coupe BK-C 2.0 MPI |
| 403 | Hyundai | Genesis DH 5.0 V8 |
| 404 | Hyundai | Getz TB 1.5 CRDI |
| 405 | Hyundai | Getz TB-A 1.6/1.4/1.3 |
| 406 | Hyundai | Getz TB-B 1.6/1.4/1.3 |
| 407 | Hyundai | Grand Santa Fe NC 3.3 MPI (2013-2019) |
| 408 | Hyundai | Grand Santa Fe NC CRDI (2016-2019) |
| 409 | Hyundai | Grand Starex / H-1 (TQ FL) 2.5L 4D56 Euro5 (2018-2021) |
| 410 | Hyundai | Grand Starex / H-1 (TQ FL) 2.5L D4CB Euro6 (2016-2021) |
| 411 | Hyundai | Grand Starex / H-1 (TQ FL) 2.5L D4CB Euro6 (2020 - n.d.) |
| 412 | Hyundai | Grand Starex / H-1 (TQ) 2007-2017 |
| 413 | Hyundai | Grandeur 4 (TG) (2005-2010) |
| 414 | Hyundai | Grandeur V (HG) / Azera Diesel (2011-2017) |
| 415 | Hyundai | Grandeur V (HG) / Azera Gasoline (2011-2017) |
| 416 | Hyundai | Grandeur VI (IG) 2.2 CRDI (2016-) |
| 417 | Hyundai | Grandeur VI (IG) 3.0 V6 GDI (2016-2022) |
| 418 | Hyundai | Grandeur VI (IG) 3.0 V6 LPI (2016-2022) |
| 419 | Hyundai | HB20 BR (2012-2018) 1.0 MPI |
| 420 | Hyundai | HB20 BR (2012-2018) 1.6 MPI |
| 421 | Hyundai | i10 / Grand i10 NIOS (AI3) (2019-) 1.2 MPI |
| 422 | Hyundai | i10 IA 1.0 Bi-fuel GPI (2014-2018) |
| 423 | Hyundai | i10 IA 1.2 MPI (2013-2018) |
| 424 | Hyundai | i10 PA 1.2 MPI (2008-2017) |
| 425 | Hyundai | i20 (BC3/BI3) / Bayon (BC3 CUV) 1.4 MPI (2020-) |
| 426 | Hyundai | i20 (BI3) 1.5 U2 CRDI (2020-) |
| 427 | Hyundai | i20 (PB) 1.4 CRDI |
| 428 | Hyundai | i20 CRDI (2020-) |
| 429 | Hyundai | i20 GB 1.2 MPI (2014-2021) |
| 430 | Hyundai | i20 PB 1.2 MPI (2008-2013) |
| 431 | Hyundai | i20 PB 1.4 MPI (2013-2016) |
| 432 | Hyundai | i20/Bayon (BC3) 1.0 T-GDI (2021-n.d.) |
| 433 | Hyundai | i20/Bayon (BC3) 1.2 (2021-n.d.) |
| 434 | Hyundai | i20N (BC3/BI3) / Bayon (BC3 CUV) 1.6 T-GDI |
| 435 | Hyundai | i30 GD 1.4 CRDI (2011-2017) |
| 436 | Hyundai | i30 GD 1.4 MPI (2011-2017) |
| 437 | Hyundai | i30 GD 1.6 CRDI (2011-2013) |
| 438 | Hyundai | i30 GD 1.6 CRDI (2013-2015) |
| 439 | Hyundai | i30 GD 1.6 CRDI (2016-2018) |
| 440 | Hyundai | i30 GD 1.6 MPI/GDI  (2011-2017) |
| 441 | Hyundai | i30 N |
| 442 | Hyundai | i30 PD (2016-) |
| 443 | Hyundai | i30 PD (2016-2022) CRDI TCI-U2 |
| 444 | Hyundai | i30 PD (2019-n.d.) CRDI TCI-NEW U |
| 445 | Hyundai | i30 PD 1.0 T-GDI |
| 446 | Hyundai | i30 PD 1.4T (2018-) |
| 447 | Hyundai | i30 PD 1.5 DPi |
| 448 | Hyundai | i30 PD 1.5 T-GDI |
| 449 | Hyundai | i30/Elantra FD 1.4 MPI (2006-2011) |
| 450 | Hyundai | i30/Elantra FD 1.6 CRDI (2006-2011) |
| 451 | Hyundai | i30/Elantra FD 1.6 MPI (2006-2011) |
| 452 | Hyundai | i40 1.7 CRDI TCI-U2 (2012-2015) |
| 453 | Hyundai | i40 1.7 CRDI TCI-U2 (2016-2019) |
| 454 | Hyundai | i40 2.0/2.4 MPI/GDI |
| 455 | Hyundai | Ioniq EV (2016-2020) |
| 456 | Hyundai | Ioniq EV (OBDII + EV)  (2016-2020) |
| 457 | Hyundai | Ioniq EV (only EV)  (2016-2020) |
| 458 | Hyundai | Ioniq EV 38 kWh (2019-2021) |
| 459 | Hyundai | Ioniq HEV (2016-2019) |
| 460 | Hyundai | Ioniq HEV (2020-2022) |
| 461 | Hyundai | Ioniq PHEV (2017-2022) |
| 462 | Hyundai | ix20 1.4 |
| 463 | Hyundai | ix35 NU 2.0 Gasoline AT (2017-2023) |
| 464 | Hyundai | Kona N OS 2.0 T-GDI (2022-) |
| 465 | Hyundai | Kona OS 1.0 T-GDI (2017-2022) |
| 466 | Hyundai | Kona OS 1.6 GDI + Hybrid (2020-2022) |
| 467 | Hyundai | Kona OS 1.6 T-GDI (2017-2022) |
| 468 | Hyundai | Mufasa 2.0 MPI (2023-n.d.) |
| 469 | Hyundai | Palisade LX2 2.2 CRDI |
| 470 | Hyundai | Palisade LX2 3.5 V6 |
| 471 | Hyundai | Palisade LX2 3.8 V6 |
| 472 | Hyundai | Palisade LX3 (2024-n.d.) 2.5 T-GDI |
| 473 | Hyundai | Santa Fe 3 (DM FL, 2016-2018) CRDI |
| 474 | Hyundai | Santa Fe 3 (DM, 2012-2018) 2.0 T-GDI |
| 475 | Hyundai | Santa Fe 3 (DM, 2012-2018) CRDI |
| 476 | Hyundai | Santa Fe 3 (DM, 2012-2018) MPI/GDI |
| 477 | Hyundai | Santa Fe CM 2.0/2.2 CRDI (2005-2011) |
| 478 | Hyundai | Santa Fe CM MPI 2.0/2.4 (2005-2012) |
| 479 | Hyundai | Santa Fe CM-A 2.7 V6 MPI (2005-2012) |
| 480 | Hyundai | Santa Fe CM-A 2.7 V6 MPI var.2 (2005-2012) |
| 481 | Hyundai | Santa Fe CM-A 3.3 V6 MPI (2005-2012) |
| 482 | Hyundai | Santa Fe CM-A 3.5 V6 MPI (2010-2012) |
| 483 | Hyundai | Santa Fe CM-B 2.0/2.2 CRDI (2005-2012) |
| 484 | Hyundai | Santa Fe CM-B 2.7 V6 MPI (2005-2012) |
| 485 | Hyundai | Santa Fe CM-B 3.3 V6 MPI (2005-2012) |
| 486 | Hyundai | Santa Fe MX5 2.5 GDI (2024-n.d.) |
| 487 | Hyundai | Santa Fe MX5 HEV (2024-n.d.) |
| 488 | Hyundai | Santa Fe SM (2000-2006) / Santa Fe Classic Tagaz (2007-2012) |
| 489 | Hyundai | Santa Fe TM 2.0 T-GDI (2018-2020) |
| 490 | Hyundai | Santa Fe TM 2.4 MPI/GDI (2018-2020) |
| 491 | Hyundai | Santa Fe TM CRDI + AT (2018-2020) |
| 492 | Hyundai | Santa Fe TM PE 2.2 CRDI+DCT (2020-2023) |
| 493 | Hyundai | Santa Fe TM PE 2.5 + AT (2020-2023) |
| 494 | Hyundai | Santa Fe TM PE 2.5 T-GDI + DCT (2020-2023) |
| 495 | Hyundai | Santa Fe TM PE 3.5 + AT (2020-2023) |
| 496 | Hyundai | Santa Fe TM PE HEV (2021-2023) |
| 497 | Hyundai | Santa Fe TM PE PHEV (2021-2023) |
| 498 | Hyundai | Sata Fe CM K-Line/KWP (2005-2012) |
| 499 | Hyundai | Solaris I 2011-2017 1.4/1.6 |
| 500 | Hyundai | Solaris I G4FC |
| 501 | Hyundai | Solaris II (HCr) 2017- |
| 502 | Hyundai | Solaris II (HCr) 2017- ONLY ABS TPMS ODOMETER READINGS! |
| 503 | Hyundai | Sonata (DN8) 1.6 T-GDI 2019- |
| 504 | Hyundai | Sonata (DN8) 2.0 LPI 2019- |
| 505 | Hyundai | Sonata (DN8) 2.0 MPI 2019- |
| 506 | Hyundai | Sonata (DN8) 2.5 GDI 2019- |
| 507 | Hyundai | Sonata (DN8) 2.5 MPI 2019- |
| 508 | Hyundai | Sonata Hybrid (DN8) HEV 2020- |
| 509 | Hyundai | Sonata IV (EF) 2.7 V6 |
| 510 | Hyundai | Sonata IV (EF), Elantra J3 2.0 G4GC |
| 511 | Hyundai | Sonata LF 2.0 LPI (2014-2020) |
| 512 | Hyundai | Sonata LF 2.0 MPI (2014-2020) |
| 513 | Hyundai | Sonata LF GDI (2014-2019) |
| 514 | Hyundai | Sonata LF Hybrid (2014-2020) |
| 515 | Hyundai | Sonata NF-A 2.0/2.4 MPI (2004-2010) |
| 516 | Hyundai | Sonata NF-B 2.0/2.4 MPI (2004-2010) |
| 517 | Hyundai | Sonata YF 2.0 LPI (2009-2014) |
| 518 | Hyundai | Sonata YF/i45 2.0 T-GDI (2009-2014) |
| 519 | Hyundai | Sonata YF/i45 2.0/2.4 MPI/GDI (2009-2014) |
| 520 | Hyundai | Starex/H1 2.5 D4CB (K-Line/KWP) |
| 521 | Hyundai | Staria US4 2.2 CRDI (2021-) |
| 522 | Hyundai | Staria US4 3.5 MPI (2021-) |
| 523 | Hyundai | Terracan HP 2.9 CRDI |
| 524 | Hyundai | Tiburon GK 2.7 V6 MPI |
| 525 | Hyundai | Tucson JM 2.0 (KWP/K-Line) (2004-2008) |
| 526 | Hyundai | Tucson JM 2.0 MPI (CAN) (2008-2009) |
| 527 | Hyundai | Tucson JM 2.7 V6 (2004-2009) |
| 528 | Hyundai | Tucson JM-A 2.0 CRDI (K-Line/KWP) (2004-2008) |
| 529 | Hyundai | Tucson JM-B 2.0 CRDI (CAN) (2008-2009) |
| 530 | Hyundai | Tucson LM, ix35 EL 1.6 (2009-2015) |
| 531 | Hyundai | Tucson LM, ix35 EL 1.7 CRDI (2009-2015) |
| 532 | Hyundai | Tucson LM, ix35 EL 1.7 CRDI 2WD (2009-2016) |
| 533 | Hyundai | Tucson LM, ix35 EL 2.0 CRDI 2WD (2009-2015) |
| 534 | Hyundai | Tucson LM, ix35 EL 2.0 CRDI 4WD (2009-2015) |
| 535 | Hyundai | Tucson LM, ix35 EL 2.0 Flex fuel |
| 536 | Hyundai | Tucson LM, ix35 EL 2.0/2.4 MPI 2WD (2009-2015) |
| 537 | Hyundai | Tucson LM, ix35 EL 2.0/2.4 MPI 4WD (2009-2015) |
| 538 | Hyundai | Tucson NX4 (2021-) 1.6 CRDI |
| 539 | Hyundai | Tucson NX4 (2021-) 1.6 T-GDI |
| 540 | Hyundai | Tucson NX4 (2021-) 2.0 MPI |
| 541 | Hyundai | Tucson NX4 (2021-) 2.0D CRDI + 8AT |
| 542 | Hyundai | Tucson NX4 (2021-) 2.5 GDI + AT |
| 543 | Hyundai | Tucson NX4 (2021-) GDI/MPI |
| 544 | Hyundai | Tucson NX4 HEV (2020-) |
| 545 | Hyundai | Tucson NX4 PHEV (2020-) |
| 546 | Hyundai | Tucson TL 1.6 CRDI (2015-2021) |
| 547 | Hyundai | Tucson TL 1.6 T-GDI (2015-2021) |
| 548 | Hyundai | Tucson TL 1.7 CRDI (2015-2021) |
| 549 | Hyundai | Tucson TL 2.0 MPI 2WD (2015-2018) |
| 550 | Hyundai | Tucson TL 2.0 MPI 4WD (2015-2018) |
| 551 | Hyundai | Tucson TL CRDI 2.0 AT 4WD (2015-2018) |
| 552 | Hyundai | Tucson TL FL CRDI 2.0 8AT 4WD (2018-2020) |
| 553 | Hyundai | Tucson TL FL MPI/GDI 2.0/2.4 (2018-2020) |
| 554 | Hyundai | Veloster (JS) 2.0 MPI 2018- |
| 555 | Hyundai | Veloster FS 1.6 MPFI/GDI (2011-2018) |
| 556 | Hyundai | Veloster FS 1.6 T-GDI (2011-2018) |
| 557 | Hyundai | Venue |
| 558 | Hyundai | Veracruz / ix55 (A) 3.0 CRDI |
| 559 | Hyundai | Veracruz / ix55 (B) 3.0 CRDI |
| 560 | Hyundai | Veracruz / ix55 3.8 V6 |
| 561 | Hyundai, Kia | IONIQ 5 (2026-) / IONIQ 9 / EV9 |
| 562 | Hyundai, Kia | Kona EV/Niro EV/Soul EV gen.1 (2018-2022) |
| 563 | ICH-X, Jetour, Jietu | Traveller / T2 / T1 / Shanhai T2 / ICH-X K3 2.0L |
| 564 | Infiniti | G37, M37, M56, FX35, FX45, Q50, Q60, Q70, QX56, QX70, QX80 |
| 565 | Infiniti | J50: EX25, EX35, EX37; S50: FX35; V36: G25, G35, G37; Y50: M35; Y51: M25, M35 |
| 566 | Infiniti | Q50 (2.0 + 7AT Mercedes-Benz) |
| 567 | Infiniti, Nissan | Nissan Consult II |
| 568 | Infiniti, Nissan | Nissan Consult II ABS ONLY |
| 569 | Infiniti, Nissan | Nissan Consult III |
| 570 | ISUZU | D-Max gen. II (2012-2019) |
| 571 | ISUZU, Mazda | D-Max gen.3 (2019-), BT-50 gen.3 (2020-) |
| 572 | JAC | S2 II + CVT |
| 573 | JAC | T8 2.0 CTI |
| 574 | JAC | T8 2.4T |
| 575 | JAC, Sehol | JS6 |
| 576 | JAC, Sehol | S7 |
| 577 | JAC, Sehol, Москвич | Jiayue X4 / X4 / T60 Plus / JS4 J7 / JS7 / Sehol A5 / A5 Plus / SX6 / Москвич 3 |
| 578 | Jaecoo | J7 / T1EJ 1.6/2.0 + 7DCT300/400 |
| 579 | Jaecoo | J8 / T26 2.0 + 7DCT300/400 |
| 580 | Jaguar | F-Pace 2017 3.0 V6 Diesel |
| 581 | Jaguar | F-Pace 3.0 Gasoline (Supercharged) (2016-2017) |
| 582 | Jaguar | I-Pace |
| 583 | Jaguar | XF 2008-2009 (Diesel V6) |
| 584 | Jaguar | XF 2008-2009 (Gasoline V8, V6) |
| 585 | Jaguar | XJ 2010-2012 |
| 586 | Jaguar, Land Rover, Range Rover | Ingenium 2.0 Diesel (AJ200D, 204DTA, 204DTD) |
| 587 | Jaguar, Land Rover, Range Rover | Ingenium 2.0 Gasoline (AJ200P, PT204) |
| 588 | Jeep | Cherokee / Liberty KK 2012 2.8 Diesel |
| 589 | Jeep | Cherokee KL (2014-) |
| 590 | Jeep | Grand Cherokee (WK) 2005-2006 |
| 591 | Jeep | Grand Cherokee (WK) 2007-2010 |
| 592 | Jeep | Grand Cherokee (WK2) 2011-2013 |
| 593 | Jeep | Grand Cherokee (WK2) 2014 |
| 594 | Jeep | Grand Cherokee (WK2) 2015- 3.0 Diesel |
| 595 | Jeep | Grand Cherokee (WK2) 2015-2016 |
| 596 | Jeep | Grand Cherokee CRD 2007-2008 |
| 597 | Jeep | Renegade (B1) |
| 598 | Jeep | Renegade (BU) 2.0 Multijet |
| 599 | Jeep | Renegade e-Hybrid |
| 600 | Jeep | Wrangler JK 2007-2011 |
| 601 | Jeep | Wrangler JK 2012-2018 |
| 602 | Jeep | Wrangler JL 2.0 |
| 603 | Jetour, Jietu, Soueast | X70(S/M/Coupe) / X90 / X95 / Dashing / Grand Saint 1.5T/1.6T + DCT |
| 604 | Jetta, Seat, Skoda, Volkswagen | PQ25, PQ26, PQ35: Diesel 1.2 TDI CFWA |
| 605 | Jetta, Skoda, Volkswagen | EV: e-Up!, CitiGo E, Mii EV gen.1 |
| 606 | KG Mobility, KGM, Mahindra, SsangYong | Rexton G4 Y400 / Alturas 2.2 |
| 607 | KG Mobility, KGM, Mahindra, SsangYong | Rexton G4 Y450 / Alturas 2.2 |
| 608 | KG Mobility, KGM, SsangYong | Korando C300 (IV) 2019- 1.5 G15DTF |
| 609 | KG Mobility, KGM, SsangYong | Korando C300 (IV) 2019- 1.6 D16DTF / Tivoli 1.6 D16DTF |
| 610 | KG Mobility, KGM, SsangYong | Korando C300 (IV) 2019- 1.6 D16DTF-LPEGR |
| 611 | KG Mobility, KGM, SsangYong | Torres EVX/Musso EV |
| 612 | Kia | Cadenza VG / K7 (2011-2016) 2.7 |
| 613 | Kia | Cadenza VG / K7 (2011-2018) 3.0 |
| 614 | Kia | Cadenza VG / K7 (2011-2018) 3.0 LPI |
| 615 | Kia | Carens KY 1.5 Diesel CRDI (2021-n.d.) |
| 616 | Kia | Carens/Rondo 2 UN (2006-2012) 2.0/2.4 MPI CAN |
| 617 | Kia | Carens/Rondo 3 RP (2012-2021) |
| 618 | Kia | Carens/Rondo 3 RP (2012-2021) 1.6 GDI |
| 619 | Kia | Carens/Rondo 3 RP (2013-2014) 1.7 CRDI TCI |
| 620 | Kia | Carens/Rondo 3 RP (2015-2021) 1.7 CRDI TCI-U2 |
| 621 | Kia | Carnival KA4 1.6 T-GDI HEV (2020-) |
| 622 | Kia | Carnival KA4 2.2 CRDI (2020-) |
| 623 | Kia | Carnival KA4 PE 2.0 T-GDI (2020-) |
| 624 | Kia | Carnival KA4 PE 3.5 (2020-) |
| 625 | Kia | Carnival/Sedona VQ-2 2.7 V6 (2006-2014) |
| 626 | Kia | Carnival/Sedona VQ-2 2.9 VGT Diesel (2006-2015) |
| 627 | Kia | Carnival/Sedona VQ-A 2.7 V6 (2006-2014) |
| 628 | Kia | Carnival/Sedona VQ-A 3.8 V6 (2006-2014) |
| 629 | Kia | Carnival/Sedona VQ-B 3.8 V6 (2006-2014) |
| 630 | Kia | Carnival/Sedona VQ-С 3.8 V6 (2006-2014) |
| 631 | Kia | Carnival/Sedona XM 2.2 CRDI (2006-2014) |
| 632 | Kia | Carnival/Sedona YP (2015-2017) 2.2 CRDI |
| 633 | Kia | Carnival/Sedona YP (2015-2018) 3.3 GDI |
| 634 | Kia | Carnival/Sedona YP (2018-2020) 2.2 CRDI |
| 635 | Kia | Carnival/Sedona YP (2018-2020) 3.3 GDI |
| 636 | Kia | Carrens UN 2.0 LPI (2006-2009) |
| 637 | Kia | Cee'd ED 1.6 CRDI (2006-2012) |
| 638 | Kia | Cee'd ED 2.0 CRDI (2006-2012) |
| 639 | Kia | Cee'd ED 2.0 MPI (2009-2012) |
| 640 | Kia | Cee'd ED-A (2006-2009) 1.4/1.6 |
| 641 | Kia | Cee'd ED-B (2009-2012) 1.4/1.6 |
| 642 | Kia | Cee'd JD (2012-2017) 1.4/1.6, Rio III UB (2011+) 1.4/1.6, Cerato/Forte YD 1.6 MPI, Soul AM 1.6 MPI/GDI |
| 643 | Kia | Cee'd JD 1.6 GDI + DCT (2012-2018) |
| 644 | Kia | Cee'd JD 1.6 T-GDI (2012-2018) |
| 645 | Kia | Ceed CD (2018-), Pro Ceed, XCeed CD PHEV |
| 646 | Kia | Ceed CD, Pro Ceed, XCeed 1.6 CRDI (2018-) |
| 647 | Kia | Ceed CD, Pro Ceed, XCeed 1.6 GDI (2018-) |
| 648 | Kia | Ceed CD, Pro Ceed, XCeed 1.6 T-GDI (2018-) |
| 649 | Kia | Ceed CD, ProCeed, XCeed 1.0T KAPPA II (2018-2023) |
| 650 | Kia | Ceed CD, ProCeed, XCeed 1.4T (2018-) |
| 651 | Kia | Ceed CD, ProCeed, XCeed 1.5T (2021-) |
| 652 | Kia | Ceed CD, ProCeed, XCeed 1.6 MPI (2018-) |
| 653 | Kia | Ceed JD 1.6 CRDI (2013-2015) |
| 654 | Kia | Ceed JD 1.6 CRDI (2016-2018) |
| 655 | Kia | Cerato / K3 / Forte BD (2018-2022) |
| 656 | Kia | Cerato / K3 / Forte BD 1.6 T-GDI + DCT (2018-2022) |
| 657 | Kia | Cerato Classic YD FL 1.6 MPI (2017-2019) |
| 658 | Kia | Cerato/Forte TD 2.0/2.4 (2008-2012) |
| 659 | Kia | Cerato/Forte TD-2 (2008-2012) |
| 660 | Kia | Cerato/Forte TD-A (2008-2012) |
| 661 | Kia | Cerato/Forte YD 2.0 MPI NU (2013-2017) |
| 662 | Kia | Cerato/Forte YD 2.0 MPI NU PE (2016-2019) |
| 663 | Kia | K5 (DL3) 1.6 T-GDI (2019-) |
| 664 | Kia | K5 (DL3) 2.0 (2019-) |
| 665 | Kia | K5 (DL3) 2.5 (2019-) |
| 666 | Kia | K5 (DL3) HEV (2020-) |
| 667 | Kia | K5 / Optima JF LPI 2.0 (2015-2020) |
| 668 | Kia | K5 TF LPI 2.0 (2010-2014) |
| 669 | Kia | Mohave/Borrego HM 3.8 V6 |
| 670 | Kia | Mohave/Borrego HM-A 3.0 CRDI (2008-2017) |
| 671 | Kia | Mohave/Borrego HM-B 3.0 CRDI (2008-2017) |
| 672 | Kia | Mohave/Borrego HM-C/HM2 3.0 CRDI (2017-2021.01) |
| 673 | Kia | Mohave/Borrego HM-C/HM2 3.0 CRDI (2021.02-n.d.) |
| 674 | Kia | Niro EV gen.1 (2018-2022) |
| 675 | Kia | Niro HEV gen.1 (2016-2022) |
| 676 | Kia | Niro PHEV gen.1 (2016-2022) |
| 677 | Kia | Optima / K5 4 (JF) 1.7 CRDI (2016-2019) |
| 678 | Kia | Optima / K5 4 (JF) 2.0 MPI / 2.4 MPI (2016-2019) |
| 679 | Kia | Optima / K5 4 (JF) 2.0 T-GDI (2016-2020) |
| 680 | Kia | Optima / K5 4 (JF) 2.4 GDI (2016-2019) |
| 681 | Kia | Optima / K5 4 (JF) 2016-2019 [deprecated] |
| 682 | Kia | Optima JF PHEV (2016-2019) |
| 683 | Kia | Optima TF Hybrid (2010-2015) |
| 684 | Kia | Optima/K5 TF 2.0 GDI (2010-2015) |
| 685 | Kia | Optima/K5 TF 2.0 T-GDI (2010-2015) |
| 686 | Kia | Optima/K5 TF 2.0/2.4 MPI/GDI (2010-2015) |
| 687 | Kia | Optima/K5 TF CRDI (2010-2015) |
| 688 | Kia | Picanto JA (2017+) |
| 689 | Kia | Picanto TA 1.0/1.2, Rio UB 1.2 (2011-2017) |
| 690 | Kia | Quoris / K900 (KH) 3.8 GDI (2012-2018) |
| 691 | Kia | Ray EV (OBDII + EV) (2011-2018) |
| 692 | Kia | Ray EV (pure EV) (2011-2018) |
| 693 | Kia | Rio (UB) 1.1 CRDI (2011-2017) |
| 694 | Kia | Rio (YB) 1.0 T-GDI (2016-) |
| 695 | Kia | Rio (YB) 1.4 CRDI |
| 696 | Kia | Rio I (1999-2005) |
| 697 | Kia | Rio II (JB) 1.4/1.6 MPI (2005-2011) |
| 698 | Kia | Rio III (QB) 1.4/1.6 MPI (2011-2017) |
| 699 | Kia | Rio IV (FB), Rio X-Line, Rio-X 1.4, 1.6 (2017-) |
| 700 | Kia | Rio IV (FB), Rio X-Line, Rio-X 1.4, 1.6 (2017-) ONLY ABS-TPMS ODOMETER READINGS |
| 701 | Kia | Seltos / KX3 1.5 MPI (+AT) |
| 702 | Kia | Seltos / KX3 1.5 MPI (+CVT) |
| 703 | Kia | Seltos / KX3 1.6 Diesel + DCT (2019-) |
| 704 | Kia | Seltos / KX3 1.6 T-GDI (2019-) |
| 705 | Kia | Seltos / KX3 1.6, 2.0 MPI/GDI (2019-) |
| 706 | Kia | Sonet 1.5 U2 CRDI (2020-n.d.) |
| 707 | Kia | Sorento 4 MQ4 2.2 CRDI+DCT (2020-) |
| 708 | Kia | Sorento 4 MQ4 2.5 MPI/GDI (2020-) |
| 709 | Kia | Sorento 4 MQ4 HEV (2020-) |
| 710 | Kia | Sorento 4 MQ4 PHEV (2020-) |
| 711 | Kia | Sorento BL 3.3 V6 (2002-2008) |
| 712 | Kia | Sorento BL CRDI CAN (2007-2008) |
| 713 | Kia | Sorento BL CRDI K-LINE (2002-2008) |
| 714 | Kia | Sorento UM FL, Sorento Prime (2018-2020) |
| 715 | Kia | Sorento UM, Sorento Prime (2015-2017) |
| 716 | Kia | Sorento UM, Sorento Prime (2015-2018) 2.0/2.2 CRDI |
| 717 | Kia | Sorento UM, Sorento Prime FL (2018-2020) 2.0/2.2 CRDI |
| 718 | Kia | Sorento XM 2.0/2.2 CRDI (2009-2012) |
| 719 | Kia | Sorento XM 2.0/2.2 CRDI (2013-) |
| 720 | Kia | Sorento XM 2.4 GDI/MPI (2009-2012) |
| 721 | Kia | Sorento XM 2.4 GDI/MPI (2013-) |
| 722 | Kia | Sorento XM 3.5 V6 (2009-2012) |
| 723 | Kia | Sorento XM 3.5 V6 (2013-) |
| 724 | Kia | Soul (2013-2018), Forte EX/Cerato/K5 (2012-2018), Optima/K5 |
| 725 | Kia | Soul AM 1.6 CRDI (2008-2012) |
| 726 | Kia | Soul AM 1.6 MPI |
| 727 | Kia | Soul EV 27 kWh (OBDII + EV) |
| 728 | Kia | Soul EV 27 kWh (pure EV) |
| 729 | Kia | Soul EV 30 kWh (OBDII + EV) |
| 730 | Kia | Soul EV 30 kWh (Pure EV) |
| 731 | Kia | Soul EV 64 kWh (Pure EV) |
| 732 | Kia | Soul PS (2012-), Cerato/Forte 2.0 (2012-2018) |
| 733 | Kia | Soul PS 1.6 CRDI (2013-2015) |
| 734 | Kia | Soul PS 1.6 GDI (2014-2019) |
| 735 | Kia | Soul PS 1.6 MPI (2013-2018) |
| 736 | Kia | Soul PS Facelift (2017-2019) |
| 737 | Kia | Soul SK3 (2019-) 1.6 MPI |
| 738 | Kia | Soul SK3 (2019-) 2.0 MPI |
| 739 | Kia | Spectra/Cerato I (LD-A) 1.6 MPI |
| 740 | Kia | Spectra/Cerato I (LD-B) 1.6 MPI |
| 741 | Kia | Spectra/Cerato I 2.0 MPI (2004-2006) |
| 742 | Kia | Spectra/Cerato I LD (2006-2008) |
| 743 | Kia | Sportage 4 (QL) 2.4 GDI 4WD (2016-2022) |
| 744 | Kia | Sportage 4 (QL) CRDI 1.7 (2015-2021) |
| 745 | Kia | Sportage 4 (QL) CRDI 2.0 (2015-2021) |
| 746 | Kia | Sportage 4 (QL-A) MPI, GDI 2WD (2015-2021) |
| 747 | Kia | Sportage 4 (QL-A) MPI, GDI 2WD (alternative) (2015-2021) |
| 748 | Kia | Sportage 4 (QL-A) MPI, GDI 4WD (2015-2021) |
| 749 | Kia | Sportage 4 (QL-A) MPI, GDI 4WD (alternative) (2015-2021) |
| 750 | Kia | Sportage 4 (QL-B) 2.0/2.4 MPI 2WD (2015-2021) |
| 751 | Kia | Sportage 4 (QL-B) 2.0/2.4 MPI 4WD (2015-2021) |
| 752 | Kia | Sportage 4 (QL-B) 2.0/2.4 T-GDI 4WD (2016-2022) |
| 753 | Kia | Sportage 4 QL 1.6 CRDI (2015-2021) |
| 754 | Kia | Sportage 4 QL 1.6 T-GDI (2015-2021) |
| 755 | Kia | Sportage 5 NQ5 (2021-) 1.6 T-GDI |
| 756 | Kia | Sportage 5 NQ5 (2021-) 2.0 MPI + AT |
| 757 | Kia | Sportage 5 NQ5 (2021-) 2.0D CRDI + 8AT |
| 758 | Kia | Sportage 5 NQ5 (2021-) 2.5 MPI/GDI + AT |
| 759 | Kia | Sportage 5 NQ5 (2021-) HEV |
| 760 | Kia | Sportage 5 NQ5 (2021-) PHEV |
| 761 | Kia | Sportage 5 NQ5 1.6 CRDI (2021-) |
| 762 | Kia | Sportage 5 NQ5C (2021-) 2.0 T-GDI + AT |
| 763 | Kia | Sportage ACE (China) 2.0 MPi (2021-n.d.) |
| 764 | Kia | Sportage II KM 2.0 MPI CAN (2008-2010) |
| 765 | Kia | Sportage II KM 2.0 MPI K-Line/KWP (2004-2008) |
| 766 | Kia | Sportage II KM 2.7 V6 (2004-2009) |
| 767 | Kia | Sportage II KM-A 2.0 CRDI (K-Line/KWP) (2004-2008) |
| 768 | Kia | Sportage II KM-B 2.0 CRDI CAN (2008-2009) |
| 769 | Kia | Sportage III SL 1.6 GDI (2010-2016) |
| 770 | Kia | Sportage III SL 1.7 CRDI (2010-2016) |
| 771 | Kia | Sportage III SL 2.0 CRDI 2WD (2010-2016) |
| 772 | Kia | Sportage III SL 2.0 CRDI 4WD (2010-2016) |
| 773 | Kia | Sportage III SL 2.0 T-GDI (2010-2016) |
| 774 | Kia | Sportage III SL 2.0/2.4 MPI 2WD (2010-2016) |
| 775 | Kia | Sportage III SL 2.0/2.4 MPI 4WD (2010-2016) |
| 776 | Kia | Stinger 2.0 |
| 777 | Kia | Stinger 2.2 CRDI |
| 778 | Kia | Stinger 2.5 |
| 779 | Kia | Stinger GT 3.3 V6 |
| 780 | Kia | Stonic (YB CUV) 1.0 T-GDI |
| 781 | Kia | Stonic (YB CUV) 1.4 MPI |
| 782 | Kia | Stonic (YB CUV) 1.6 CRDI |
| 783 | Kia | Telluride 3.8 V6 |
| 784 | Kia | Venga YN 1.4/1.6 CRDI |
| 785 | Kia | Venga YN 1.4/1.6 MPI |
| 786 | Lada, ВАЗ, Лада | Bosch MP7.0 |
| 787 | Lada, ВАЗ, Лада | Largus (M86) |
| 788 | Lada, ВАЗ, Лада | Largus 1.6 K4M (CAN) |
| 789 | Lada, ВАЗ, Лада | Largus 1.6 K4M (К-Линия) 1.6 K4M (EMS 3132) |
| 790 | Lada, ВАЗ, Лада | M74 CAN, ME17.9.7 CAN |
| 791 | Lada, ВАЗ, Лада | M74/M75/Bosch 17.9.7 |
| 792 | Lada, ВАЗ, Лада | M75 CAN |
| 793 | Lada, ВАЗ, Лада | Vesta (H4M+CVT, все блоки) 2019-2022 |
| 794 | Lada, ВАЗ, Лада | Vesta (M86, все блоки) 2015-2022 |
| 795 | Lada, ВАЗ, Лада | Vesta NG / Iskra + OBDII 2024- (M74.9 CAN) |
| 796 | Lada, ВАЗ, Лада | Vesta NG 2023- (M74.9 CAN), Niva Travel 2022-, Granta 2023- (M74.8, M74.9 CAN) |
| 797 | Lada, ВАЗ, Лада | Vesta, X-Ray (M86) без поддержки OBDII (2015-2022) |
| 798 | Lada, ВАЗ, Лада | X-Ray (M86) OBDII (двигатели ВАЗ, кроме Renault/Nissan) |
| 799 | Lada, ВАЗ, Лада | X-RAY (OBDII+доп блоки) |
| 800 | Lada, ВАЗ, Лада | X-Ray 1.6 H4M + CVT |
| 801 | Lada, ВАЗ, Лада | Итэлма М73 |
| 802 | Lada, ВАЗ, Лада | Итэлма М73 (вариант 2) |
| 803 | Lada, ВАЗ, Лада | Итэлма М73, Bosch 7.9.7 |
| 804 | Lada, ВАЗ, Лада | Январь 5.1.1 |
| 805 | Lada, ВАЗ, Лада | Январь 5.1.1 (вар. 2) |
| 806 | Lada, ВАЗ, Лада | Январь 7.2 |
| 807 | Lada, ВАЗ, Лада | Январь 7.2 (вар. 2) |
| 808 | Lada, ВАЗ, Лада, УАЗ | ABS BOSCH |
| 809 | Land Rover | Defender 2007-2010 2.4L |
| 810 | Land Rover | Defender Puma 2.2L Diesel |
| 811 | Land Rover | Discovery 4 2.7L [EN] |
| 812 | Land Rover | Discovery 4 2.7L [RU] |
| 813 | Land Rover | Discovery 5 3.0 Diesel (2021-n.d.) |
| 814 | Land Rover | Discovery III 2.7L TD6 [EN] |
| 815 | Land Rover | Discovery III 2.7L TD6 [RU] |
| 816 | Land Rover | Discovery III 4.4 V8 |
| 817 | Land Rover | Discovery Sport 2015-2016 2.2D |
| 818 | Land Rover | Discovery Sport 2017-2020 |
| 819 | Land Rover | Freelander II 2.2L TD4 [EN] |
| 820 | Land Rover | Freelander II 2.2L TD4 [RU] |
| 821 | Land Rover | Freelander II 3.2L |
| 822 | Land Rover, Range Rover | Discovery 4 3.0L OBD-II + Extra / RangeRover 2009-2012 5.0L |
| 823 | Land Rover, Range Rover | Evoque Gen.1 2012-2017 Diesel 2.0/2.2 |
| 824 | Land Rover, Range Rover | Evoque Gen.1 2012-2017 Gasoline 2.0 |
| 825 | Land Rover, Range Rover | Range Rover 2010-2012 V8 4.4 Diesel |
| 826 | Land Rover, Range Rover | Range Rover 2013-2016 V8 4.4 Diesel |
| 827 | Land Rover, Range Rover | Range Rover 2014-2015 L405 3.0 Diesel V6 |
| 828 | Land Rover, Range Rover | Range Rover 2014-2015 L405 3.0 SC Gasoline |
| 829 | Land Rover, Range Rover | Range Rover 2016 5.0 SC |
| 830 | Land Rover, Range Rover | Range Rover 2017-2021 |
| 831 | Land Rover, Range Rover | Range Rover Sport 2012-2013 3.0 D |
| 832 | Land Rover, Range Rover | Range Rover Sport 2012-2013 V8 |
| 833 | Land Rover, Range Rover | Range Rover Sport 2017-2022 L494 3.0 Diesel |
| 834 | Land Rover, Range Rover | Range Rover Sport V8 4.2/4.4 [EN] |
| 835 | Land Rover, Range Rover | Range Rover Sport V8 4.2/4.4 [RU] |
| 836 | Land Rover, Range Rover | Range Rover TD V8 3.6 [EN] |
| 837 | Land Rover, Range Rover | Range Rover TD V8 3.6 [RU] |
| 838 | Land Rover, Range Rover | Range Rover V8 3.6 [EN] |
| 839 | Land Rover, Range Rover | Range Rover V8 3.6 [RU] |
| 840 | LDV, Maxus | D60 |
| 841 | LDV, Maxus | EUNIC 5, EUNIC 6, EUNIC 9, EV30, EG10, eDeliver3, eDeliver9 |
| 842 | LDV, Maxus | Mifa7/DaJia 7 EV |
| 843 | LDV, Maxus | T60 |
| 844 | Leapmotor | C11 (2023-present) |
| 845 | Lexus | RX330 |
| 846 | Lexus | RX400h (Hybrid) |
| 847 | Lexus, Subaru, Toyota | bZ4X RAV4 Prime PHEV / Solterra / Lexus RZ / NX450h+ PHEV |
| 848 | Lexus, Toyota | JOBD JDM CAN |
| 849 | Lexus, Toyota | RAV4 Prime PHEV (2019-n.d.), Prius Prime (2023-n.d.) / Lexus NX450h+ PHEV |
| 850 | Li Auto / Li Xiang / 理想汽车 | Li One +experimental L6 / L7 / L8 |
| 851 | Lifan | Maiwai / MyWay (ECU ME17.8.8) |
| 852 | Lotus | Eletre (EV) |
| 853 | Lynk & Co | 09 |
| 854 | MAN, Volkswagen | Crafter NF 2016-2019, TGE 1 2.0 TDI |
| 855 | Mando | ABS |
| 856 | Maserati | Levante Diesel |
| 857 | Mazda | 3 / 6 (GH1, GH2) / Miata (NC 2006-2015) / CX-7 |
| 858 | Mazda | BT50 UP, UR 2011-2020 (CAN) |
| 859 | Mazda | MX-30 |
| 860 | Mazda | MX-30 (not for use!) |
| 861 | Mazda | SKYACTIV |
| 862 | Mercedes-Benz | E250 BlueTEC Diesel 2014- |
| 863 | Mercedes-Benz | E350 Diesel |
| 864 | Mercedes-Benz | EQA / EQB / G-Class G580 EQ |
| 865 | Mercedes-Benz | EQC / EQV |
| 866 | Mercedes-Benz | GLK 220 CDI |
| 867 | Mercedes-Benz | GLK 350 3.5L, ML 350 Gasoline |
| 868 | Mercedes-Benz | Sprinter 2011- 3.0 Diesel |
| 869 | Mercedes-Benz | Sprinter II (2006-), NCV3 |
| 870 | Mercedes-Benz | W164 ML300 CDI 3L |
| 871 | Mercedes-Benz | W168 |
| 872 | Mercedes-Benz | W203 CDI |
| 873 | Mercedes-Benz | W204 Diesel |
| 874 | MG | MG4 EV (2021-2024) / MGS 5 / IM5 / IM6 |
| 875 | MG | MG4 EV (2024-) / Cyberster EV |
| 876 | MG | MG5 2021-2022 |
| 877 | MG | MG5 EV / Marvel EV / MG ZS EV Facelift 2022 |
| 878 | MG | ZS EV |
| 879 | Mini | Cooper SE |
| 880 | Mini | Cooper SE Electric |
| 881 | Mini | Countryman R60 |
| 882 | Mini | Generation 2 MINI |
| 883 | Mitsubishi | ASX 2.2 AT |
| 884 | Mitsubishi | Colt 1.3/1.5 |
| 885 | Mitsubishi | Eclipse Cross 1.5T/2.0/2.4 + CVT |
| 886 | Mitsubishi | Eclipse Cross 2.2 Diesel / Delica D5 (2019-) + 8AT |
| 887 | Mitsubishi | Eclipse Cross PHEV |
| 888 | Mitsubishi | Galant 9 AT CAN |
| 889 | Mitsubishi | i-MiEV |
| 890 | Mitsubishi | L200 / Triton Gen.6 (LC/MV) (2023-n.d.) 4N16 |
| 891 | Mitsubishi | L200 2.5 DI-D |
| 892 | Mitsubishi | Lancer VIII 1.5/1.6 AT |
| 893 | Mitsubishi | Lancer VIII 2.0/2.4 CVT |
| 894 | Mitsubishi | Lancer VIII 2.0/2.4 SST |
| 895 | Mitsubishi | Outlander II 2.2 DI-D |
| 896 | Mitsubishi | Outlander II, III 2.3 DI-D |
| 897 | Mitsubishi | Outlander II, XL, III (3.0+AT) |
| 898 | Mitsubishi | Outlander IV (2021-) |
| 899 | Mitsubishi | Outlander PHEV |
| 900 | Mitsubishi | Pajero IV 3.0, 3.8 V6 + AT V4A51 [EN] |
| 901 | Mitsubishi | Pajero IV 3.0, 3.8 V6 + AT V4A51 [RU] |
| 902 | Mitsubishi | Pajero IV 3.0, 3.8 V6 [EN] |
| 903 | Mitsubishi | Pajero IV 3.0, 3.8 V6 [RU] |
| 904 | Mitsubishi | Pajero IV 3.2 DI-D |
| 905 | Mitsubishi | Pajero Sport II / L200 / Triton / Challenger 2.5D [EN] |
| 906 | Mitsubishi | Pajero Sport II / L200 / Triton / Challenger 2.5D [RU] |
| 907 | Mitsubishi | Pajero Sport II / L200 / Triton / Challenger 3.0 V6 [EN] |
| 908 | Mitsubishi | Pajero Sport II / L200 / Triton / Challenger 3.0 V6 [RU] |
| 909 | Mitsubishi | Pajero Sport III / L200 V / Triton 4N15 |
| 910 | NETA | V / Aya |
| 911 | Nissan | 370Z Z34 3.7 V6 |
| 912 | Nissan | Almera G15 + AT |
| 913 | Nissan | Altima 2013- |
| 914 | Nissan | Altima L32 2.5 |
| 915 | Nissan | Altima L32 3.5 V6 |
| 916 | Nissan | Armada TA60 5.6 V8 |
| 917 | Nissan | Frontier D40 2.5 |
| 918 | Nissan | Frontier D40 4.0 V6 |
| 919 | Nissan | Frontier D41 Gen.3 (2022-n.d.) |
| 920 | Nissan | GT-R (R35) |
| 921 | Nissan | Juke 1.5dci K9K 636 [EN] |
| 922 | Nissan | Juke 1.5dci K9K 636 [RU] |
| 923 | Nissan | Juke 2014- |
| 924 | Nissan | Juke F15 (2010-2018) 1.6 TURBO + CVT |
| 925 | Nissan | Kicks HP15 e-Power (Gen.1) |
| 926 | Nissan | Leaf ZE0/AZE0 (2010-2017) |
| 927 | Nissan | Leaf ZE1 (2017-) |
| 928 | Nissan | March/Micra K13 1.5 |
| 929 | Nissan | March/Micra K13 1.6 |
| 930 | Nissan | Maxima A35 3.5 V6 |
| 931 | Nissan | Murano Z51 3.5 V6 + CVT |
| 932 | Nissan | Murano Z52 2015- |
| 933 | Nissan | Note e-Power HE12 |
| 934 | Nissan | Note e-Power/Aura HE13 (2022/09-) |
| 935 | Nissan | Pathfinder 2013+ |
| 936 | Nissan | Pathfinder R51 4.0 V6 (FL 2008-2012) |
| 937 | Nissan | Pathfinder R51 AT CAN |
| 938 | Nissan | Pathfinder R51 AT K-Line (2004-2008) |
| 939 | Nissan | Patrol / Armada Y62 |
| 940 | Nissan | Qashqai HJ12 e-power (2022-) |
| 941 | Nissan | Qashqai J10 1.5 dCi (K9K 732) [EN] |
| 942 | Nissan | Qashqai J10 1.5 dCi (K9K 732) [RU] |
| 943 | Nissan | Qashqai J10 1.5 dCi K9K 836, K9K 430 [EN] |
| 944 | Nissan | Qashqai J10 1.5 dCi K9K 836, K9K 430 [RU] |
| 945 | Nissan | Qashqai J10 1.6 |
| 946 | Nissan | Qashqai J10 2.0 |
| 947 | Nissan | Qashqai J11 |
| 948 | Nissan | Qashqai J11 1.5dci K9K 636 [EN] |
| 949 | Nissan | Qashqai J11 1.5dci K9K 636 [RU] |
| 950 | Nissan | Qashqai J12 1.3 DIG-T |
| 951 | Nissan | Rogue / X-Trail T33 (2021-) |
| 952 | Nissan | Rogue S35 2.5 |
| 953 | Nissan | Rogue T32 2014-2020 |
| 954 | Nissan | Sentra B16 2.0 |
| 955 | Nissan | Tiida/Versa C11 1.8 |
| 956 | Nissan | Titan A60 5.6 V8 |
| 957 | Nissan | Titan A61 |
| 958 | Nissan | X-Trail T31 2.0 |
| 959 | Nissan | X-Trail T31 2.0, Qashqai J10 CVT |
| 960 | Nissan | X-Trail T31 2.5 |
| 961 | Nissan | X-Trail T31 2.5 CVT, Teana J32 2.5 CVT |
| 962 | Nissan | X-Trail T31, Qashqai 2.0 dCi (Diesel) M9R [EN] |
| 963 | Nissan | X-Trail T31, Qashqai 2.0 dCi (Diesel) M9R [RU] |
| 964 | Nissan | X-Trail T32 |
| 965 | Nissan | X-Trail T32 (NT32) 2.0 MR20DD [EN] |
| 966 | Nissan | X-Trail T32 (NT32) 2.0 MR20DD [RU] |
| 967 | Nissan | X-Trail T32, Qashqai 1.6 dCi R9M [EN] |
| 968 | Nissan | X-Trail T32, Qashqai 1.6 dCi R9M [RU] |
| 969 | Nissan | Xterra N50 4.0 V6 |
| 970 | Nissan, Opel, Renault, Vauxhall | Master 3 (2010-), NV400 (2010-2021), Interstar (2022-), Movano (2010-2021)  M9T gen.1 (2010-2014) |
| 971 | Nissan, Opel, Renault, Vauxhall | Master 3 (2010-), NV400 (2010-2021), Interstar (2022-), Movano (2010-2021) M9T 8xx, ECU Bosch EDC17C42 |
| 972 | Nissan, Opel, Renault, Vauxhall | Master 3 (2010-), NV400 (2010-2021), Interstar (2022-), Movano (2010-2021) M9T ECU: Continental SID309 |
| 973 | Nissan, Opel, Renault, Vauxhall | Master 3 (2010-), NV400 (2010-2021), Interstar (2022-), Movano (2010-2021) M9T+AdBlue, ECU: Siemens SID321 |
| 974 | Nissan, Opel, Renault, Vauxhall | Trafic II / Vivaro A / Primastar 2.0 dCi R9M CAN [EN] |
| 975 | Nissan, Opel, Renault, Vauxhall | Trafic II / Vivaro A / Primastar 2.0 dCi R9M CAN [RU] |
| 976 | Nissan, Opel, Renault, Vauxhall | Trafic II / Vivaro A / Primastar dCi K-Line/KWP [EN] |
| 977 | Nissan, Opel, Renault, Vauxhall | Trafic II / Vivaro A / Primastar dCi K-Line/KWP [RU] |
| 978 | Nissan, Opel, Renault, Vauxhall | Trafic II ph.2/3 / Vivaro A / Primastar 2.0 dCi R9M CAN var.2 [EN] |
| 979 | Nissan, Opel, Renault, Vauxhall | Trafic II ph.2/3 / Vivaro A / Primastar 2.0 dCi R9M CAN var.2 [RU] |
| 980 | Nissan, Renault | Ariya / Scenic EV E-TECH / Renault 5 E-TECH / Renault 4 E-TECH / Megane E-TECH GSR2 2024- / Master EV E-TECH |
| 981 | Nissan, Renault | Zoe II / Renault Kangoo Van E-Tech / Nissan Townstar EV |
| 982 | Opel, Vauxhall | Astra G Y17DT (1998-2004) |
| 983 | Opel, Vauxhall | Multec-S |
| 984 | Opel, Vauxhall | Vectra B, Astra G, etc. with X16XEL, X18XE (1998-2002) |
| 985 | Peugeot | 307 (2001-2005) |
| 986 | Peugeot | 308 (T9) + 6AT (CAN) |
| 987 | Peugeot | 308 (T9) + 8AT (CAN) |
| 988 | Peugeot | 308 + 4AT (CAN) |
| 989 | Peugeot | 308, 508, etc. with 1.6 BOSCH MED 17.4.2 |
| 990 | Polestar | Polestar 4 |
| 991 | Polestar, Volvo | XC40 EV/C40 EV E400V2/E400V5/E400V6 2020- / Polestar 2 |
| 992 | Porsche | Cayenne Turbo (gen. II 2011-2017) |
| 993 | Proton | EMS400 ECU |
| 994 | Proton | EMS700 ECU |
| 995 | Renault | Austral Hybrid |
| 996 | Renault | Captur 1.2 |
| 997 | Renault | Captur 1.5 dCi |
| 998 | Renault | Captur II (HR16DEg3+PHEV) |
| 999 | Renault | Clio 1.2 D4F 740 [EN] |
| 1000 | Renault | Clio 1.2 D4F 740 [RU] |
| 1001 | Renault | Clio III GT K4M 862 |
| 1002 | Renault | Clio III RS 2.0 |
| 1003 | Renault | Clio IV 0.9L H4B |
| 1004 | Renault | Clio IV RS 200 EDC |
| 1005 | Renault | Clio V H5H 1.3L |
| 1006 | Renault | Clio-III 1.5 dCi |
| 1007 | Renault | Clio-III 1.6 |
| 1008 | Renault | Clio-III 1.6 K4M 801 ECU S3000 + AT DP0 [EN] |
| 1009 | Renault | Clio-III 1.6 K4M 801 ECU S3000 + AT DP0 [RU] |
| 1010 | Renault | Dokker K7M |
| 1011 | Renault | Dokker K9K 608, 612 [EN] |
| 1012 | Renault | Dokker K9K 608, 612 [RU] |
| 1013 | Renault | Espace 4 M9R 760 [EN] |
| 1014 | Renault | Espace 4 M9R 760 [RU] |
| 1015 | Renault | Espace IV 1.9 diesel [EN] |
| 1016 | Renault | Espace IV 1.9 diesel [RU] |
| 1017 | Renault | Espace IV 2.2 dCi K-Line/KWP [EN] |
| 1018 | Renault | Espace IV 2.2 dCi K-Line/KWP [RU] |
| 1019 | Renault | Espace V R9M |
| 1020 | Renault | Fluence / New SM3 K4M 1.6 [EN] |
| 1021 | Renault | Fluence / New SM3 K4M 1.6 [RU] |
| 1022 | Renault | Fluence 1.5 dCi |
| 1023 | Renault | Fluence 1.6 |
| 1024 | Renault | Fluence, Grand Scenic III, Scenic III, Gran Tour III, Megane CC, Megane III 1.5 dCi K9K 832, K9K 836 [EN] |
| 1025 | Renault | Fluence, Grand Scenic III, Scenic III, Gran Tour III, Megane CC, Megane III 1.5 dCi K9K 832, K9K 836 [RU] |
| 1026 | Renault | Kadjar 1.2 + DCT [EN] |
| 1027 | Renault | Kadjar 1.2 + DCT [RU] |
| 1028 | Renault | Kadjar 1.3T H5H |
| 1029 | Renault | Kadjar 1.5 dCi (K9K 674, 675, 676, 677) |
| 1030 | Renault | Kadjar 1.6 R9M dCi |
| 1031 | Renault | Kangoo I (X76) 1.4 K7J [EN] |
| 1032 | Renault | Kangoo I (X76) 1.4 K7J [RU] |
| 1033 | Renault | Kangoo II 1.5 dCi K9K 816 [EN] |
| 1034 | Renault | Kangoo II 1.5 dCi K9K 816 [RU] |
| 1035 | Renault | Kaptur 1.6 [EN] |
| 1036 | Renault | Kaptur 1.6 [RU] |
| 1037 | Renault | Kwid |
| 1038 | Renault | Laguna II F4P 770 [EN] |
| 1039 | Renault | Laguna II F4P 770 [RU] |
| 1040 | Renault | Laguna II F4R 714 [EN] |
| 1041 | Renault | Laguna II F4R 714 [RU] |
| 1042 | Renault | Laguna II F9Q diesel [EN] |
| 1043 | Renault | Laguna II F9Q diesel [RU] |
| 1044 | Renault | Laguna II ph.2 1.6 K4M 716 [EN] |
| 1045 | Renault | Laguna II ph.2 1.6 K4M 716 [RU] |
| 1046 | Renault | Laguna III 2.0 dCi M9R var.1 [EN] |
| 1047 | Renault | Laguna III 2.0 dCi M9R var.1 [RU] |
| 1048 | Renault | Laguna III 2.0 dCi M9R var.2 [EN] |
| 1049 | Renault | Laguna III 2.0 dCi M9R var.3 [EN] |
| 1050 | Renault | Laguna III 2.0 F4R 813 |
| 1051 | Renault | Laguna III K9K 1.5 dCi [EN] |
| 1052 | Renault | Laguna III K9K 1.5 dCi [RU] |
| 1053 | Renault | Laguna-III 1.5 dCi |
| 1054 | Renault | Laguna-III 2.0 |
| 1055 | Renault | Megane E-TECH electric (2022 - mid 2024) |
| 1056 | Renault | Megane II 1.4 K4J 730 [EN] |
| 1057 | Renault | Megane II 1.4 K4J 730 [RU] |
| 1058 | Renault | Megane II 1.5 dCi K9K 734 [EN] |
| 1059 | Renault | Megane II 1.5 dCi K9K 734 [RU] |
| 1060 | Renault | Megane II 1.9 dCi F9Q |
| 1061 | Renault | Megane II 2.0 F4R 744 [EN] |
| 1062 | Renault | Megane II 2.0 F4R 744 [RU] |
| 1063 | Renault | Megane II 2.0 M9R |
| 1064 | Renault | Megane II ph.2 1.6 [EN] |
| 1065 | Renault | Megane II ph.2 1.6 [RU] |
| 1066 | Renault | Megane II ph1 K9K 722 [EN] |
| 1067 | Renault | Megane II ph1 K9K 722 [RU] |
| 1068 | Renault | Megane II X84 K9K 722, 728, 729 [EN] |
| 1069 | Renault | Megane II X84 K9K 722, 728, 729 [RU] |
| 1070 | Renault | Megane II, Scenic II F9Q 816 [EN] |
| 1071 | Renault | Megane II, Scenic II F9Q 816 [RU] |
| 1072 | Renault | Megane II, Scenic II K4M 812 [EN] |
| 1073 | Renault | Megane II, Scenic II K4M 812 [RU] |
| 1074 | Renault | Megane II, Scenic II, Modus, Clio III - K9K 732 [EN] |
| 1075 | Renault | Megane II, Scenic II, Modus, Clio III - K9K 732 [RU] |
| 1076 | Renault | Megane III 1.5 dCi K9K 836 [EN] |
| 1077 | Renault | Megane III 1.5 dCi K9K 836 [RU] |
| 1078 | Renault | Megane IV H5F |
| 1079 | Renault | Megane IV H5H |
| 1080 | Renault | Megane IV R9M 409 [EN] |
| 1081 | Renault | Megane IV R9M 409 [RU] |
| 1082 | Renault | Megane-III 1.4 TCE [EN] |
| 1083 | Renault | Megane-III 1.4 TCE [RU] |
| 1084 | Renault | Megane-III 1.5 dCi |
| 1085 | Renault | Megane-III 1.5 K9K 846 [EN] |
| 1086 | Renault | Megane-III 1.5 K9K 846 [RU] |
| 1087 | Renault | Megane-III 1.6 H4M |
| 1088 | Renault | Megane-III 1.6 K4M 858 [EN] |
| 1089 | Renault | Megane-III 1.6 K4M 858 [RU] |
| 1090 | Renault | Megane-III, Scenic-III 2.0 + CVT [EN] |
| 1091 | Renault | Megane-III, Scenic-III 2.0 + CVT [RU] |
| 1092 | Renault | Modus 1.2 D4F 740 [EN] |
| 1093 | Renault | Modus 1.2 D4F 740 [RU] |
| 1094 | Renault | Renault Megane III RS [EN] |
| 1095 | Renault | Renault Megane III RS [RU] |
| 1096 | Renault | Scenic III / Megane III 1.5 dCi K9K 830, 834 [EN] |
| 1097 | Renault | Scenic III / Megane III 1.5 dCi K9K 830, 834 [RU] |
| 1098 | Renault | Scenic III / Megane III 1.6 dCi R9M [EN] |
| 1099 | Renault | Scenic III / Megane III 1.6 dCi R9M [RU] |
| 1100 | Renault | Scenic III F9Q 1.9 [EN] |
| 1101 | Renault | Scenic III F9Q 1.9 [RU] |
| 1102 | Renault | Scenic III, Megane III, Grand Scenic III, Gran Tour III 1.5 dCi K9K 636 [EN] |
| 1103 | Renault | Scenic III, Megane III, Grand Scenic III, Gran Tour III 1.5 dCi K9K 636 [RU] |
| 1104 | Renault | Scenic-III 1.5 dCi |
| 1105 | Renault | Scenic-III 1.6 |
| 1106 | Renault | Symbol 1.6 |
| 1107 | Renault | Talisman 1.5dci K9K 647 [EN] |
| 1108 | Renault | Trafic III R9M 1.6 dCi |
| 1109 | Renault | Twingo EV |
| 1110 | Renault | Twingo III H4B 0.9 |
| 1111 | Renault | Twizy (EV) |
| 1112 | Renault | Zoe Phase 2 |
| 1113 | Renault | Zoe R240 |
| 1114 | Renault, Samsung | Koleos I / QM5 2.0/2.5 + CVT [EN] |
| 1115 | Renault, Samsung | Koleos I / QM5 2.0/2.5 + CVT [RU] |
| 1116 | Renault, Samsung | Koleos I / QM5 dCi (Diesel) [EN] Var.1 |
| 1117 | Renault, Samsung | Koleos I / QM5 dCi (Diesel) [EN] Var.2 |
| 1118 | Renault, Samsung | Koleos I / QM5 dCi (Diesel) [RU] Вар.1 |
| 1119 | Renault, Samsung | Koleos I / QM5 dCi (Diesel) [RU] Вар.2 |
| 1120 | Renault, Samsung | Koleos II / QM6 1.6 dCi R9M [EN] |
| 1121 | Renault, Samsung | Koleos II / QM6 1.6 dCi R9M [RU] |
| 1122 | Renault, Samsung | Koleos II / QM6 2.0 dCi M9R [EN] |
| 1123 | Renault, Samsung | Koleos II / QM6 2.0 dCi M9R [RU] |
| 1124 | Renault, Samsung | Koleos II / QM6 2.0 MR20DD [EN] |
| 1125 | Renault, Samsung | Koleos II / QM6 2.0 MR20DD [RU] |
| 1126 | Renault, Samsung | Talisman / SM6 1.6 Energy dCi (160 hv) EDC [EN] |
| 1127 | Renault, Samsung | Talisman / SM6 1.6 Energy dCi (160 hv) EDC [RU] |
| 1128 | Renault, Samsung | XM3 1.3 H5Ht |
| 1129 | Roewe, SAIC Roewe | eRX5 |
| 1130 | Scion | FRS |
| 1131 | Seat, Skoda, Volkswagen | EV: e-UP! gen.2, Citigo E, Mii EV (32kWh) |
| 1132 | Seat, Skoda, Volkswagen | Up! / Citigo / Mii 1.0 MPI |
| 1133 | Skywell, Skyworth | ET5/ET6 |
| 1134 | Smart | Smart FourTwo EV / FourFour EV (W453 2017-2020) |
| 1135 | Solaris | HC 2.0 |
| 1136 | SsangYong | Action NEW 2.0 Gasoline (CAN bus) |
| 1137 | SsangYong | Action NEW D20DTF (CAN bus) |
| 1138 | SsangYong | Kyron, Action, Rexton Diesel (D20DT, D27DT) |
| 1139 | SsangYong | Kyron, Rexton, Action, Musso, Korando Gasoline 2.3 MSE |
| 1140 | Subaru | 2010 - n.d. (CVT/AT + CAN) |
| 1141 | Subaru | 2022 - n.d. (CVT/AT + CAN) |
| 1142 | Subaru | BRZ (gen.1 2012-2021) |
| 1143 | Subaru | SSM2 over CAN (2008-2010) |
| 1144 | Subaru, Toyota | GR86/BRZ gen.2 (2021-) |
| 1145 | Suzuki | Grand Vitara, XL7, Swift var.1 |
| 1146 | Suzuki | Grand Vitara, XL7, Swift var.2 |
| 1147 | Suzuki | S-Cross ABU310 |
| 1148 | Suzuki | Vitara 2016-, SX4 S-Cross 2016- (K14C, 6AT) |
| 1149 | Tata | Hexa |
| 1150 | Tata | Nexon EV |
| 1151 | Toyota | BZ (2026-) |
| 1152 | Toyota | Camry Hybrid XV50, RAV4 Hybrid 2016-2018, Auris TS Hybrid |
| 1153 | Toyota | Corolla E110, E120 1CD-FTV |
| 1154 | Toyota | Corolla Hybrid 2020-, RAV4 Hybrid 2019-, Camry Hybrid 2018-, Avalon Hybrid 2019- |
| 1155 | Toyota | Corolla Verso gen.2 (2004-2007) Diesel |
| 1156 | Toyota | GT-86 (2012-2021) |
| 1157 | Toyota | Highlander Hybrid Gen.3 |
| 1158 | Toyota | Prius Gen. 2 (2004-2009) |
| 1159 | Toyota | Prius Gen. IV (2015-) |
| 1160 | Toyota | Prius Gen.3 2010- |
| 1161 | Toyota | Prius Prime |
| 1162 | Toyota | Tacoma gen.3 (2016-n.d.) |
| 1163 | Toyota | Vitz 2009 CVT |
| 1164 | Universal | OBD-II (alternative) |
| 1165 | Universal | OBD-II (AT) |
| 1166 | Universal | OBD-II + SAE J1850 |
| 1167 | Universal | OBD-II / EOBD |
| 1168 | Universal | OBD-II / EOBD + AT (CAN) |
| 1169 | Universal | OBD-II / EOBD + AT/CVT (CAN) |
| 1170 | Universal | OBD-II / EOBD + CAN |
| 1171 | Universal | OBD-II / EOBD + CAN 11 bit (2004 - n.d.) |
| 1172 | Universal | OBD-II / EOBD + CAN and AT |
| 1173 | Universal | OBD-II / EOBD + CAN and extra PIDs |
| 1174 | Universal | OBD-II / EOBD + extra (CAN) |
| 1175 | Universal | OBD-II / EOBD + MUT-2 (K-LINE) (-2005) |
| 1176 | Universal | OBD-II / EOBD Diesel + CAN 11 bit (2004 - n.d.) |
| 1177 | Universal | OBD-II / EOBD E-body(CAN/UDS) |
| 1178 | Universal | OBD-II / EOBD Exx N57 3.0D |
| 1179 | Universal | OBD-II / EOBD F-body |
| 1180 | Universal | OBD-II / EOBD G-body |
| 1181 | Universal | OBD-II / EOBD ~1999-2008 K-Line/KWP + extra sensors |
| 1182 | Universal | OBD-II / EOBD ~2006-2009 CAN + extra sensors |
| 1183 | Universal | OBD-II / EOBD ~2010-2022 CAN + extra sensors |
| 1184 | Universal | OBD-II / EOBD ~2016 - n.d. CAN + extra sensors |
| 1185 | Universal | OBDII / EOBD |
| 1186 | Universal | OBDII / EOBD + AT var.3 |
| 1187 | Universal | OBDII / EOBD + AT/CVT var.1 |
| 1188 | Universal | OBDII / EOBD + CVT var.2 |
| 1189 | Universal | OBDII / EOBD GM based Ultium EV vehicles (2021-2025) |
| 1190 | Universal | OBDII / EOBD GM based Ultium EV vehicles (2026-n.d.) |
| 1191 | Universal | OBDII/EOBD |
| 1192 | Universal | OBDII/EOBD + SAE J1850 (Old Ford vehicles and trucks) |
| 1193 | Volkswagen | Amarok (2010-2021) 2.0 TDI |
| 1194 | Volkswagen | Amarok (2010-2021) 3.0 TDI |
| 1195 | Volkswagen | Caravelle 2.5 TDI |
| 1196 | Volkswagen | EV: e-Golf (24 kWh) 2014-2016 |
| 1197 | Volkswagen | EV: e-Golf (36 kWh) 2017-2021 |
| 1198 | Volkswagen | MQB: Atlas / Teramont 3.6 FSI EA390 |
| 1199 | Volkswagen | MQB: Passat B8 (2015-) 2.0 TDI |
| 1200 | Volkswagen | PQ35: Caddy mk3 (2K) 1.6 TDI CAYD |
| 1201 | Volkswagen | T5 (Transporter, Caravelle, Multivan) 2.0 TSI (2010-2015) |
| 1202 | Volkswagen | T6 (Transporter, Caravelle, Multivan, California) 2.0 TDI (2015-2022) |
| 1203 | Volvo | 2014-2018 VEA engine (not SPA) |
| 1204 | Volvo | D2 (1.6) |
| 1205 | Volvo | EX90 (2024 - n.d.) |
| 1206 | Volvo | Platform 2 + CAN 29-bit protocol |
| 1207 | Volvo | Platform 2 + ISO 9141-2 protocol |
| 1208 | Volvo | Platform 3 MY2008- |
| 1209 | Volvo | S80-V70 with 2.0D Ford engine |
| 1210 | Volvo | SPA (4 cylinders: B4204T*, D4204T*) |
| 1211 | Volvo | SPA/CMA (3 cylinders: B3154T*) |
| 1212 | Volvo | V60 D6 PHEV AWD Diesel Plug-in Hybrid (2012-2017) |
| 1213 | Volvo | Volvo P1 platform 2.0D diesel 2004-2010 |
| 1214 | Voyah | Free |
| 1215 | Wuling | Starlight 730 EV / Xingguang 730 / Darion EV / Starlight EV |
| 1216 | XPeng | P5 / P7 / G6 / G9 / X9 |
| 1217 | Yamaha | AEROX 155, Breeze DX (XC125KR), Breeze BS (XC125LR), BW'S 125, BW'S R 125, BW'S X 125, C3(XF50), CUXi, Cygnus 125, Cygnus-X 125, CIAO, Exciter 150, Fancy 50, FINN 115, FORCE(XC155), Giggle (XF50), GTR Aero 125, JUPITER RC 2017, Jog Ciao, Jog Sweet 115, Janus 2017, Limi 115, MAJESTY 125, M-Slaz, MT-03, MT-07, MT-09, MT-10, N-MAX 155, Neo's 50, NVX 155, R1, R3, R25, R15, Raptor 700 FL, Ray 125, RS-Z 100, SMAX 155, SR400, TMAX530, Tricity 125, TENERE 660, VINO 50, Vity 125, WR125R, WR125X, X-City 125, X-Max 125, X-City 250, X-Max 250, X-Max 300, YBR125, YBR250, YZF-R125, YZF-RA3 |
| 1218 | ZAZ | Sens (ЭБУ Микас) |
| 1219 | ZAZ | Sens Mikas 10.3 |
| 1220 | ZAZ | Sens Mikas 7.6 |
| 1221 | ZAZ, ЗАЗ | Chance (ECU MR140) |
| 1222 | ZAZ, ЗАЗ | Sens (Микас 10.3) |
| 1223 | ZAZ, ЗАЗ | Sens (Микас 7.6) |
| 1224 | Zeekr | 7x |
| 1225 | Тайга | Барс |
| 1226 | УАЗ | ЗМЗ 51432 евро4 |
| 1227 | УАЗ | Патриот Bosch ME17.9.71 E5 VS35/VS36/VS38 |
| 1228 | УАЗ | Патриот АКПП |
| 1229 | УАЗ | Патриот/Хантер Bosch ME 17.9.7 Euro-3 |

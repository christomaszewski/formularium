---
id: castex2023
citation: Castex, Victorine, García de Cortázar-Atauri, Iñaki, Beniston, Martin, Moreau, Jérôme, Semenov, Mikhail, Stoffel, Markus & Calanca, Pierluigi. 2023. Exploring future changes in synchrony between grapevine (Vitis vinifera) and its major insect pest, Lobesia botrana. OENO One 57(1):161-174
doi: 10.20870/oeno-one.2023.57.1.7250
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Sanlúcar, Yecla, Avignon, Stäfa]
processes: [phenology, grape berry moth, synchrony, climate projection]
records: []
datasets: []
files: [2023-castex-10-20870-oeno-one-2023-57-1-7250.pdf]
---

# Castex et al. 2023: vine and berry-moth synchrony to 2100 at four European sites

The Lobesia Generic Model of Castex et al. 2020 and a BRIN plus Wang-Engel vine model
for Chardonnay, both on the same Wang-Engel temperature response, run on LARS-WG weather
carrying five CMIP5 models' change signals under RCP4.5 and 8.5, to score how close the
third moth generation's flight peak comes to maturity. Parameters in the supplements.

## What it holds

- **Sites:** Sanlúcar (36.7 °N), Yecla, Avignon, Stäfa (47.2 °N); observed series from
  Castex et al. 2020 train the weather generator (1981-2017 at Stäfa to 2004-2017 at
  Sanlúcar) (l. 139-192).
- **Models:** LGM, multivoltine, stages from eggs to adults, one parameter set and one
  Wang-Engel response for every site, diapause ending only with days over 12 h (day 78),
  a 32 °C slowdown of the last generation (l. 225-269); the vine by BRIN
  (`cortazar2009.brin`) and Wang & Engel 1998 for flowering, veraison and maturity, run
  in PMP5 (l. 204-211). Parameters in ESM 3-5, not printed.
- **Risk rule:** high when the third generation's 50 % flight is within 15 d of maturity,
  moderate to low beyond 16 d, the threshold from unspecified observations (l. 263-290).
- **Results** (Tables 1-2): by 2080-2100 under RCP8.5 the third peak is delayed 19-43 d
  in the south (the text rounds differently) while Stäfa's maturity advances 20-31 d;
  the gap at Stäfa falls to 12 d under RCP8.5 against 33-47 d under RCP4.5, so the risk
  rises in the north (l. 332-448). The accepted date prints before the received one.

## Dependence

- **Computes** BRIN, Wang & Engel and the LGM as calibrated elsewhere (Castex et al.
  2020); shares one temperature response between pest and host. García de
  Cortázar-Atauri again.

## Bearing (2026-10-13)

- For Cooptera's grape berry moth model: the LGM is a competitor form (Wang-Engel
  response, photoperiod gate, 32 °C cap) and its 2020 source is the one to fetch; here
  only the synchrony rule and the projections.

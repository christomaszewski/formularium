---
id: magarey2005b
citation: Magarey, R. D., Russo, J. M., Seem, R. C. & Gadoury, D. M. 2005. Surface wetness duration under controlled environmental conditions. Agricultural and Forest Meteorology 128:111-122
doi: 10.1016/j.agrformet.2004.07.017
read: 2026-10-19, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-7 and Table 1 read in the page images by the reading agent
status: read
diseases: []
crops: []
regions: [New York, Geneva]
processes: [leaf wetness duration, drop and film drying, energy balance, transfer coefficient, wind tunnel]
records: []
datasets: []
files: [1-s2.0-S0168192304002175-main.pdf (the 2026-10-19 drop, supplied by Chris 2026-10-19)]
---

# Magarey et al. 2005: how long drops and films stay wet in a wind tunnel

"Magarey et al. 2005a" in `magarey2006` and `magarey2006b` (this note is `magarey2005b` because
`magarey2005` is the generic infection paper by Magarey, Sutton & Thayer). It derives the
transfer-coefficient constants SWEB uses. No record: it is a laboratory model of drying, not
something a tool runs.

## What it holds

- **Setup** (l. 159-231): drops (1 to 50 ul, depth 50 to 200 x 10^-3 cm) and films (depth 1 to
  29 x 10^-3 cm) on artificial leaves (Parafilm, polystyrene, UV-treated polystyrene) in a wind
  tunnel (45 cm of 9.5 cm PVC pipe) and a humidity carboy; observations every 5 min. On
  artificial leaves drop drying times repeat to +/-6 min at 95 % CI, on real leaves only
  +/-30 min (l. 218, 226), hence the artificial leaves.
- **Model** (Eqs 1-6): SWD = Dd/Ed + Df/Ef; drops dry at Ep/Aw, films at Ep; Ep is the Tanner &
  Fuchs 1968 combination equation (Eq 3); h = c (U/l)^0.5 (Eq 4), hd = cd U^0.5 for drops and hf =
  cf U^0.5 for films; wet while water depth D > 0 (l. 143-146). Length scale l = 1 cm for leaves 4
  cm or longer.
- **Constants:** cd = 8.7 and cf = 2.0 cm^0.5 min^-0.5, solved from the drying of 5 ul drops and
  from film data (l. 181-201). Eq 7, a fit to 5 ul drops: SWD = 19.6 + 37.0 x 0.34^U (min, U in
  m/s; the text layer drops the exponent, read on the image).
- **Standard test** (Table 1): depth 89 x 10^-3 cm, wettability index Hw 1.14, leaf width 4.5 cm,
  Rn 0, 20 °C, RH 70 %, 0.5 m/s. Ranges: Hw 1.14 to 0.15; leaf width 1 to 11 cm; Rn 0 to 840 W
  m-2; 10 to 35 °C; RH 14 to 90 %; 0 to 5 m/s.
- **Errors:** drops MAE 24 min and bias 16 min in depth (Table 1); films MAE and bias 15 min;
  variable leaf width MAE 25 min for drops and films against 19 and 12 min with a fixed width;
  against LeClerc et al. 1985's data MAE 18 min, three times worse than LeClerc's own model (6 min).
- **Findings:** films dry 4 to 5 times slower than drops (l. 346); water distribution makes a
  four-fold difference; RH and wind matter most for drops, temperature least; leaf width is
  unimportant for drops and for films wider than 3 cm; wettability barely matters for films.
  5 ul drops dry in about 90 min on Parafilm and about 30 min on UV-treated polystyrene.
- **Cited:** Huber 1988, RH 75 to 95 % doubles simulated wetness (l. 390); LeClerc et al. 1986,
  drop transfer rate four times lower than film's.
- **Not tested:** condensation (dew); wettability of real leaves (not measured); species; sensors.
  The model "best simulates" a 5 cm leaf and 0.9 mm drops (l. 451-452). The field version of the
  model (Magarey 1999; Seem et al. 2000) is cited, not read.
- **Garbles:** drop volumes printed as ml where ul is meant (l. 325-326); Eq 3 and Eq 7 units are
  not reconciled with cm/min in Eqs 4-5; powers of ten are lost in the text layer.

## Dependence

- **Borrowed:** Tanner & Fuchs 1968 and Bird et al. 1960 (not in the catalogue).
- **Fitted to** its own wind-tunnel data (cd, cf, Eq 7); LeClerc et al. 1985 is a comparison,
  not a fit. This is the origin of SWEB's cd and cf (`magarey2006`).
- Same authors as `magarey2006` and `magarey2006b`: a flag.

## Bearing (2026-10-19)

- **Constants a truth could take:** cd 8.7 and cf 2.0 are lab values for a hydrophobic artificial
  leaf, not vine leaves; the paper measured no real leaf's Hw. They are not in Agrarium's micro.*
  set, which has an evaporation rate per hPa (micro.evap_mm_h_per_hpa 0.015, range 0.005-0.05).
- **Film depths tested** are 0.01 to 0.29 mm (1 to 29 x 10^-3 cm), drops 0.5 to 2 mm deep. The
  engine's micro.wet_threshold_mm (0.02 mm) is within the film range; micro.storage_mm_per_lai
  (0.25 mm) sits at its upper end. The paper sets no wetness threshold: any depth above zero is
  wet.
- **Dew:** untested, and the paper asks for condensation tests (l. 437).
- **RH:** the strongest atmospheric controls on drying are RH and wind, but only for water
  already on the leaf; no RH rule for the start of wetness is tested.

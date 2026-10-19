---
id: magarey2006b
citation: Magarey, R. D., Seem, R. C. & Russo, J. M. 2006. Grape canopy surface wetness: simulation versus visualization and measurement. Agricultural and Forest Meteorology 139:361-372
doi: 10.1016/j.agrformet.2006.08.015
read: 2026-10-19, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Tables 1-5 checked in the page images by the reading agent
status: read
diseases: []
crops: [grapevine]
regions: [New York, Geneva, Adelaide Hills]
processes: [leaf wetness duration, SWEB, wetness sensor, visual wetness, dew, rain]
records: [magarey2006.sweb]
datasets: [magarey2006.geneva_adelaide]
files: [1-s2.0-S016819230600236X-main.pdf (the 2026-10-19 drop, supplied by Chris 2026-10-19)]
---

# Magarey, Seem & Russo 2006: SWEB against the eye and against sensors in grape canopies

The companion of `magarey2006`: the same model scored against visual wetness and painted
Campbell 237 sensors in three vineyards.

## What it holds

- **Sites** (Table 1, l. 189-218): GV97, Chardonnay, Geneva NY 1997, LAI 1.0, 15 unpainted and 3
  painted sensors; LO98, Concord, Geneva 1998, LAI 2.0, 15 painted; AA98, Cabernet Franc,
  Adelaide Hills 1998, LAI 1.0, 15 painted. Canopy about 1.8 m. LAI by Li-Cor 2000. Rows
  east-west at GV97, north-south at the others. Training system not stated.
- **Truth:** water seen on 15 tagged leaves of each of 3 vines at 5 canopy positions (45 leaves
  a site). Canopy surface wetness (CSW) is water visible for 12 min or more on 10 % of leaves
  (l. 151); the 12 min was chosen to overestimate wetness for decision support (l. 161). Hourly
  analyses average the sub-hourly observations.
- **Model settings:** Wth 0.1, Wmax 0.5, Cl 0.02 (credited here to Hoppmann & Wittich 1997; lab
  values 0.022 Concord and 0.016 Chancellor, three samples each, l. 262-266). Inputs from on-site
  canopy sensors (four HMP35C, the bottom three averaged), rain, wind and net radiation
  (l. 236-254), logged at 60 s.
- **Sensors:** Model 237 plates at 45°, parallel to rows; painted ones with thresholds of
  <150, <900 and <6999 kOhm (Geneva; the text layer prints kV) and <50 at Adelaide; an hour
  counts wet when the sensor proportion exceeds 0.2 (l. 284).
- **Results:** abstract: SWEB r2 0.73 against 0.6 for sensors overall; MAE 0.7-1.5 h (sensors
  1.1-1.9 h); both worse in dew than in rain. Table 3, GV97: visual mean 6.9 h, SWEB 6.3 h, MAE
  1.5 h, dew r2 0.66, rain 0.99. Table 4, LO98: visual 5.1, SWEB 5.5, MAE 0.8 h; best painted
  sensor (<150) MAE 1.9 h. Table 5, AA98: visual 2.0, SWEB 1.2, MAE 0.7 h, dew r2 0.78; sensors
  r2 below 24 % in dew; <150 overestimated wetness (r 0.22, not significant), <50 best (r 0.38).
  Table 2 hourly r: SWEB 0.73 all, 0.76 rain, 0.61 dew. SWEB under-predicted observed wetness
  except when the canopy was only partly wet (l. 318), and put Wsim between 0 and 0.2 where
  nothing was seen (l. 305).
- **Conflicts:** event counts differ among the text (LO98 8 dew, 4 rain), Table 1 (7, 5) and Table 4
  (7 dew, 6 rain rows); AA98 text 8 and 4, Table 1 9 dew. LO98 10-min r 0.62 in the text, 0.66 in
  Table 2. The Table 2 footnote says r2 and the text says Pearson r (l. 231). Table 3-5 mean-error
  signs are dropped by the text layer; on the images 1998 is -0.5 for SWEB and the Adelaide
  sensors -0.4, -0.8 and -1.1. The sign is not defined (visual minus estimate, from the means).
- **Others cited:** Madeira et al. 2002, mean error 1.5-1.6 h; Cicogna et al. 2005 ran SWEB on
  interpolated ground-station and radar inputs in Italy (operational use).
- **Code** on request; no licence. Digital imaging data are unpublished.
- **Not printed:** drying times, a dense against open canopy comparison, SWEB's error by canopy
  position, a comparison with a station or an RH rule.

## Dependence

- **Model:** SWEB (`magarey2006`); its borrowings are listed there. Sensor painting and the
  Geneva thresholds are Portraz et al. 1994's (cited).
- **Not independent for the sensors:** the sensor thresholds were chosen on these data. No model
  produced the visual truth.
- **Cl** is credited to Hoppmann & Wittich 1997 here and to Noilhan & Planton 1989 in the
  companion. The lab Cl values come from Concord leaves, the LO98 cultivar.

## Bearing (2026-10-19)

- **A record to compare with.** Visual wetness by canopy position in vineyards, against a model
  with water-budget parameters of the micro.* kind. SWEB's mean error against the eye is 0.5 h
  or less in size at Geneva in both years and 0.6 h at the dry Adelaide site, all with
  canopy-height inputs, and it beat painted sensors (MAE 1.1-1.9 h), which a truth can treat
  as a noisy observation.
- **LAI.** The sites span LAI 1.0 to 2.0 but differ in cultivar, year and place, so there is no
  clean density effect. The denser canopy (LO98, LAI 2.0) had the shorter visual wetness (5.1 h)
  against GV97 (LAI 1.0, 6.9 h), so nothing here supports micro.density_drying_slowdown as a
  slowing effect (own reading, confounded by year and site).
- **Wetness against RH:** no RH threshold is tested here. Agrarium's micro.wet_threshold_mm,
  micro.storage_mm_per_lai and micro.interception are not compared to measurements in this paper
  beyond the values in `magarey2006`.
- **Sensors:** a wet-hour threshold changes a sensor's hours by 1 h or more (Adelaide: <150 kOhm
  overestimated, <50 best), which bears on the engine's sensor model.

---
id: herrero2012
citation: Herrero, J. & Polo, M.J. 2012. Parameterization of atmospheric longwave emissivity in a mountainous site for all sky conditions. Hydrology and Earth System Sciences 16:3139-3147
doi: 10.5194/hess-16-3139-2012
read: 2026-10-27, sections 2-4 in the text; Eqs 7-10 in the text; Table 1 garbled, only the 3sParam row used; Eqs 4-6 not read; by a reading agent (model not recorded in its JSON) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Spain, Sierra Nevada]
processes: [longwave radiation, atmospheric emissivity, cloud index]
records: []
datasets: []
files: [dr1027_herrero2012.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Herrero and Polo 2012: all-sky atmospheric emissivity from station RH and clearness index, fitted at 2500 m in the Sierra Nevada

A Brutsaert clear-sky emissivity with a locally fitted coefficient and a cloud index built from screen RH and clearness index.

**Read this first.** A snow-melt site at 2500 m, daytime calibration, not a vineyard. Table 1's other columns are garbled.

## What it holds

- **Data:** CGR3 pyrgeometer, accuracy 5 W m-2, 5-min logging, Refugio Poqueira, 2500 m, Sierra Nevada, sky view factor 0.97 (l. 232).
- **Clear sky (Eq. 7):** eps_acs = lc (10 ea / Ta)^(1/7), ea in kPa. **Cloudy (Eq. 8):** eps_a = eps_acs (1 + C N^2). **Cloud index (Eq. 10):** N = 1 - 0.45 CI - 3.5 Wa CI + 4 Wa^2 CI, with CI the clearness index and Wa the RH fraction; N limited to 0..1 (l. 599). Equations are printed complete.
- **Seasonal lc (Eq. 9):** Crawford and Duchon's 1.22 + 0.06 sin[(month + 2) pi / 6], 1.28 in January to 1.22 in July (l. 580; cited from Crawford and Duchon, Oklahoma).
- **Local fit:** lc constant at 1.17 (l. 589); C = 0.42 for fully covered skies (same passage).
- **Error:** 3sParam daytime calibration MBE 0.000, MAE 0.045, RMSE 0.065 in emissivity units (Table 1, as read); about 20 W m-2 by arithmetic, not printed.
- **Use:** local calibration lets emissivity series be built at stations without a longwave sensor (l. 845).

## Dependence

- Brutsaert 1982 and Crawford and Duchon 1999, with local coefficients. Same cloud factor as duarte2026. Independent of the engine's wetness pieces.

## Bearing (2026-10-27)

- **What it supports:** a longwave and cloud fill from T, RH and global radiation (all common station variables), but at the price of a local fit of lc and C that no vineyard data support here.
- **Not shown:** night values (daytime fit), vineyards, other climates. Kind of result: a local re-fit of a published form.

---
id: duarte2026
citation: Duarte, T.F., Dong, X., Leskovar, D., Ahmad, U., Silva, T.J.A.D., Silva, E.M.B. & Tortorici, N. 2026. Net radiation estimation using the Brunt equation for clear sky emissivity and air and canopy temperatures for longwave radiation in well watered crops. International Agrophysics 40:423-435
doi: 10.31545/intagr/224655
read: 2026-10-27, text in reading order; Eqs 15-16 and Table 1 in the page image (p. 427); Eqs 4-13 not read; by a reading agent (model not recorded in its JSON) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [cotton, sesame]
regions: [USA, Texas, Uvalde]
processes: [net radiation, longwave radiation, clear-sky emissivity, cloud factor]
records: []
datasets: []
files: [dr1027_duarte2026.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Duarte et al. 2026: net radiation from the Brunt clear-sky emissivity with a shortwave-based cloud factor, on cotton and sesame

Regionally calibrated Brunt emissivity beats the FAO method for hourly and daily Rn on two field crops in Texas. Not a vineyard.

**Read this first.** A crop paper, not vines (it cites Pieri 2010 for grapevines; l. 130; not held, not read). Eqs 4-13 (the FAO forms) were not read; Table 1 coefficients were read in the page image only.

## What it holds

- **Site and sensor:** Uvalde, Texas; cotton and sesame in 2015, cotton in 2025 (l. 11). NR-Lite2 net radiometer at 3.0 m; weather station within 500 m (l. 207).
- **Model (Eqs 15-16, page image, l. 336):** L_down = [clf + (1 - clf) eps_c] sigma Tair^4, with clf = 1 - Rs/Rso (Crawford and Duchon 1999). Inputs are air temperature, vapour pressure ea, global radiation Rs and the clear-sky Rso.
- **Table 1 (page image):** eps_c = 0.62 + 0.16 sqrt(ea in kPa) (Formetta 2016, Texas); 0.598 + 0.057 sqrt(ea in hPa) by day and 0.633 + 0.057 sqrt(ea in hPa) by night (Li 2017, seven US stations). Cited from those sources.
- **Error, hourly Rn:** 2015 RMSE 37.74, MAE 26.60, bias -7.92 W m-2, KGE 0.94 (l. 569); 2025 RMSE 55.94, MAE 40.10, bias -14 W m-2, KGE 0.81 (l. 574); 2025 daily RMSE 13.45 (l. 574, units as printed there).
- **Claim:** both regionally calibrated Brunt models beat the Allen/FAO method (l. 29). Air temperature can stand in for canopy temperature in the outgoing longwave under well-watered conditions (l. 22).

## Dependence

- Brunt (via Formetta 2016 and Li 2017) with the Crawford and Duchon cloud factor; the same cloud factor is used in herrero2012. Independent of the engine's wetness pieces.

## Bearing (2026-10-27)

- **What it supports:** Rn and downward longwave from station Rs, T and RH with an RMSE of about 38-56 W m-2 hourly over well-watered row crops; good as a second, differently built Rn fill beside carrasco2008.
- **Not shown:** vines, night-only skill, dew or wetness, or Mediterranean sites. Coefficients are regional to Texas. Kind of result: a re-fit and validation (measurement) on other crops.

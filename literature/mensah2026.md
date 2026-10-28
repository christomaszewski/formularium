---
id: mensah2026
citation: Mensah, T.A., White, N., Rincón-Flórez, V. & Akinsanmi, O.A. 2026. Weather data sources influence predictive performance of disease forecasting models. International Journal of Biometeorology 70:238
doi: 10.1007/s00484-026-03285-3
read: 2026-10-27, lightly: abstract, methods, results and discussion by search and section reads (not every paragraph), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [macadamia flower blight (Botrytis, Cladosporium, Neopestalotiopsis/Pestalotiopsis)]
crops: [macadamia]
regions: [Australia, Central Queensland, Northern Rivers (New South Wales)]
processes: [weather data source, gridded interpolated weather, in-canopy sensors, vapour pressure deficit, spore trap, leave-one-out validation, forecasting]
records: []
datasets: []
files: [syn1027_mensah2026.pdf (the 2026-10-27 drop)]
---

# Mensah et al. 2026: the weather source changes the skill of a conidia-versus-VPD model (macadamia orchards, analogue crop)

Compares in-canopy and on-farm stations, the SILO gridded product and Bureau of Meteorology station data as inputs to one simple model of airborne flower-blight conidia in macadamia orchards. No record: a method with a measured comparison.

**Read this first.** Macadamia, not a vine, and the target is airborne conidia from spore traps, not disease on the plant. The model has one predictor (mean vapour pressure deficit) and the weather sources, not the model, are what is compared. The numbers are scores of a regression on four orchards over two seasons.

## What it holds

- **Real data** (l. 23): 10 commercial macadamia orchards, five in Central Queensland and five in Northern Rivers, with fine-scale records for up to three seasons (2022 to 2024); July to December each season (l. 25-26). Weather inputs are ten variables common to the four sources.
- **Weather sources** (l. 23): two fine-scale (in-canopy and on-farm Davis stations) and two coarse (SILO gridded or point data, and the nearest Bureau of Meteorology station). All are measured or interpolated from measurements; no reanalysis and no simulation.
- **Labels are observed**: airborne conidia counts from spore traps, one predictor per source (mean VPD), one model per source (l. 59). Leaf wetness, where used, is a daily RH >= 90% stand-in after Sentelhas et al. 2008 (l. 27).
- **Validation** (l. 59, 198): leave-one-out cross-validation over trap observations from four orchards in 2023 and 2024; neither seasons nor orchards are held out as blocks. Polynomial and linear models were tried per source (l. 59).
- **Scores** (l. 197): a prediction robustness index (PRI; a composite of R2, concordance, bias and normalised RMSE, as the reading agent records it): Bureau of Meteorology 0.55, SILO 0.55, on-farm 0.52, in-canopy 0.29. In-canopy was significantly lower than Bureau (p < 0.05); the other three did not differ (p > 0.05) (l. 8, 197).
- **Direction flips** (l. 197): in 2024 the VPD-conidia relation was positive with on-farm data and negative with in-canopy, SILO and Bureau data, at the same orchards.
- **Authors' reading** (l. 205): "a trade-off between local microclimatic specificity and model generalisability".
- **Rare events** (l. 197): no Botrytis conidia were trapped in one season, so that pathogen-season dropped out.

## Dependence

- Uses the RH >= 90% wetness stand-in (Sentelhas et al. 2008) and VPD from daily extremes. Labels are observed spore counts. No model's output is used as a label.

## Bearing (2026-10-27)

- **D58 and D60:** measured evidence that a different weather source changes a forecast's score and can flip the sign of a variable's effect at the same sites; for the project's hourly records this means a variable's apparent value depends on the sensor or product it came from. Coarse station and gridded data scored at least as well as in-canopy sensors.
- **Skill ceiling:** not an hourly T, RH and rain ceiling; PRI is a composite, the target is spore counts, and validation is leave-one-out on observations.
- **Not shown:** a held-out season or orchard, a vine, or a disease outcome on the plant.

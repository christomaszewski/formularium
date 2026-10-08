---
id: cameron2021
citation: Cameron, Wendy, Petrie, Paul R., Barlow, E.W.R., Howell, Kate, Jarvis, Chelsea & Fuentes, Sigfredo. 2021. A comparison of the effect of temperature on grapevine phenology between vineyards. OENO One 55(2):301-320
doi: 10.20870/oeno-one.2021.55.2.4599
read: 2026-10-08, in full (Table S2, the paper-to-vineyard map, is not in the text), by a reading agent (claude-sonnet-5-5); 28 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [global]
processes: [phenology]
records: []
datasets: []
files: [10-20870-oeno-one-2021-55-2-4599.pdf]
---

# Cameron et al. 2021: temperature and phenology compared across vineyards

From the University of Melbourne and partners. A re-analysis of 14 published papers.

## What it holds

- Method: regress stage day of year on a window temperature index; only slopes are reported (days per degC) (l. 576).
- Index: daily Tmax or Tmean floored at 0 degC, summed over a 3-month window and divided by its days (l. 200); windows screened by R2 (l. 550).
- Chosen: January-March mean for budburst; March-May maximum for flowering, veraison, harvest (l. 554).
- Slopes per degC: budburst 0.02 to 14.44 days (l. 564); flowering 1.81 to 6.67 days (l. 519).
- Data: 17 vineyards in 8 countries from 14 published papers, digitised, from 1979 (l. 400); at least 6 years each (l. 130).
- Sources include Ramos et al. 2015 (Tempranillo, Ribera del Duero) (l. 401); Garcia de Cortazar-Atauri 2017 data come through van Leeuwen 2019 (l. 387).
- Dependence: Bordeaux budburst dates came from a temperature model (l. 515).
- Temperatures are gridded (0.5 deg CPC, SILO); Cembra grid is biased cold (l. 472).
- Not a process model: no thresholds fitted, no stage prediction.

## Dependence

- Digitised data from 14 papers (17 vineyards, 8 countries) with gridded temperature; slopes only, no thresholds fitted. Ramos et al. 2015 is a source, but its Tempranillo data from Ribera del Duero, not the Penedès series behind the engine's `ramos2017.budburst`. Cembra is a vineyard here and in Molitor 2014's data; whether the observations overlap is not stated (a flag). Bordeaux's budburst dates in one source were derived with a temperature model.
- No author of an engine model.

## Bearing (2026-10-08)

- Clear: regression slopes of stage dates on window temperatures, not a phenology model the engine shares. A cross-vineyard check on how a truth's phenology responds to temperature.

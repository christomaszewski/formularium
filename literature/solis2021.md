---
id: solis2021
citation: Solís, M. & Rojas-Herrera, V. 2021. Approaches for the prediction of leaf wetness duration with machine learning. Biomimetics 6:29
doi: 10.3390/biomimetics6020029
read: 2026-10-27, in full; Tables 2 and 4 read in the page images (pages 6 and 8), Table 3 scrambled and not used; by a reading agent and note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [coffee]
regions: [Costa Rica]
processes: [leaf wetness, leaf wetness duration, machine learning, gradient boosting, time step]
records: []
datasets: []
files: [dr1027_solis2021.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Solís and Rojas-Herrera 2021: XGBoost models of daily leaf wetness in six Costa Rican coffee regions

Five set-ups of one boosted-tree model (daily or hourly regression, 15 or 30 min classification) are fitted to station data and scored on daily wetness minutes against a dielectric-grid sensor.

**Read this first.** No RH threshold, CART or physical model is run, so the paper gives no error for an RH >= 90 % rule. The validation days are a random 25 % of 1300 days (l. 442), so they sit between training days of the same stations; the MAE of about 60 min is not a held-out-site or held-out-year figure. When a whole region is left out the error doubles (l. 557). Coffee, not vines.

## What it holds

- **Data:** meteorological stations and LWD sensors in six coffee regions of Costa Rica (l. 16); regions 1-3 report every 15 min, regions 4-6 every 30 min (l. 332); last 1300 days with data, 2016-2020 (l. 441); 4-18 % of days with missing data were dropped (l. 438).
- **Reference sensor:** a conductivity grid sensor with a 0-15 scale, on a vertical pipe at 1.5 m, facing west at 45 degrees (l. 316-323, overprinted). Coffee agronomists count a leaf as wet at a reading of 1 or higher (l. 329). The leaf was wet in 38-62 % of intervals by region (Table 1, l. 368; l. 346-347).
- **Inputs:** 13 station variables (in- and outdoor temperature and RH, solar radiation, wind, barometer, rain, soil moisture) plus month and day of year (l. 331, Table 1). Day of year was the most influential variable; month, rain and wind speed the least (l. 611, l. 617).
- **Model and split:** XGBoost (l. 381); random 75 / 25 split, 10-fold cross validation on the 75 % (l. 442).
- **Set-ups:** daily records (DMR, DOR) were worst; hourly regression (HOR) and per-interval classification (NMC, NOC) were best and not different from each other (l. 410; Table 2, page image).
- **Error (Table 2, page image):** NOC daily MAE (min) 62, 57, 65 for the 15-min regions 1-3 and 99, 88, 84 for the 30-min regions 4-6; RMSE 90, 79, 93 and 146, 129, 111 (Table 2, page image). The abstract gives about 60 min per day for the best models (l. 18); 15-min data beat 30-min data (l. 20).
- **Longer sums:** the daily MAE falls to 28, 26, 30, 61, 43 and 40 min over seven-day periods (l. 515).
- **Transfer:** leaving a region out of training raised the MAE from about 60 min to over 120 min for the 15-min regions (l. 557).
- **Comparisons cited:** Kim et al. 150 min, Park et al. (2019) 90-174 min; the authors warn these are not like for like (l. 776). Park's own per-site MAE in park2019 is 1.5-3.2 h (l. 975) and all-site 2.3 h, so the 90-174 min cited is not the same quantity.
- **Release:** data on request only (l. 820); CC BY article; no code.

## Dependence

- Builds on Kim et al. 2002/2005 and the ML papers it cites (Park 2019, Francl and Panigrahi); no equation is borrowed. Kin of the engine's wetness models only in purpose; no shared threshold. Not kin to sentelhas2008.wetness, cooptera.rh90_wetness or cooptera.logistic_wetness.

## Bearing (2026-10-27)

- **Time step:** a coffee-plantation result that 15-min inputs give lower daily error (MAE about 55-65 min) than 30-min inputs (84-99 min), and that daily aggregates are worst. A measurement of model behaviour, in sample (random days), for one sensor type.
- **Not supported:** an RH threshold error, a vine value, or a portable model (the transfer error is over 120 min). Soil moisture and barometer inputs are not standard wetness drivers.

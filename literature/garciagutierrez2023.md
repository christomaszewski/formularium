---
id: garciagutierrez2023
citation: García-Gutiérrez, Víctor & Meza, Francisco. 2023. Modeling Phenology Combining Data Assimilation Techniques and Bioclimatic Indices in a Cabernet Sauvignon Vineyard (Vitis vinifera L.) in Central Chile. Remote Sensing 15:3537 (25 pp.)
doi: 10.3390/rs15143537
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Chile]
processes: [phenology]
records: []
datasets: []
files: [10-3390-rs15143537.pdf]
---

# García-Gutiérrez & Meza 2023: phenology models with data assimilation in central Chile

From the Pontificia Universidad Católica de Chile.

## What it holds

- Compares GFV (Parker 2011), CaEc (Caffarra and Eccel 2010) and BRIN, then adds an extended Kalman filter fed by Sentinel-2 NDVI (l. 90).
- GFV: degree days above Tb 0 degC from DOY 60 (l. 661).
- CaEc: budburst from a chilling state, Fcrit = co1 exp(co2 ChState) (l. 739); flowering and veraison from a sigmoid forcing sum (l. 747).
- Parameters fitted with the Phenology Modelling Platform, simulated annealing (l. 752). Table A1 lists CaEc only, e.g. Fcrit 24.76 flowering, 64.47 veraison (l. 1649, 1655).
- Fit data: TEMPO Cabernet Sauvignon, Domaine de Vassal near Montpellier, 1995-2012 (l. 766); count not given.
- Test data: one Chilean vineyard, three seasons, weekly observations (l. 538).
- Result on Chile: GFV RMSE 10.7 d flowering and 20.8 d veraison (l. 1216).
- Text and Table 6 disagree on NDVI RMSE (22.3 d against 18.6 d) (l. 1177).
- Dependence: Parker GFV and Caffarra-Eccel equations are computed, refitted on a different set.

## Dependence

- It refits GFV and Caffarra & Eccel's model on TEMPO data from the Domaine de Vassal (Montpellier, 1995-2012), then tests them on one Chilean vineyard over three seasons. The Vassal data also contributed to Parker 2011's database (a flag).
- Chilling then forcing, and forcing sums: the engine's forms (`chilling-dormancy`, `degree-day-phenology`).

## Bearing (2026-10-08)

- **Held out by structure**, as recorded. Its Kalman-filter coupling to Sentinel-2 NDVI is a method an observation operator could use.

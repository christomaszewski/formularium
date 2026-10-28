---
id: coulibaly2024
citation: Coulibaly, K.R.L., Amani, K., Kouadio, A.Z., Ette, N.K., Kouassi, G.K., Coulibaly, W.B. & Kouame, C. 2024. Estimation de la duree d'humectation des feuilles par seuillage de l'humidite relative dans la zone nord de la Cote d'Ivoire. Climatologie 22:5
doi: 10.1051/climat/202422005
read: 2026-10-27, methods and abstract; results tables not read; by a reading agent (model not recorded in its JSON) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [cashew]
regions: [Cote d'Ivoire, Korhogo]
processes: [leaf wetness, RH threshold, dew point depression, validation skill scores]
records: []
datasets: []
files: [dr1027_couliba2024.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Coulibaly et al. 2024: leaf wetness from RH and dew point depression thresholds, tested on cashew in northern Cote d'Ivoire

Ten days of hourly visual wetness on cashew trees tested against an RH >= 90 % rule and a dew point depression (DPD) rule.

**Read this first.** A cashew park and ten days only. The results tables were not read; the skill scores below are the abstract's.

## What it holds

- **Inputs:** hourly air temperature and RH from a HOBO station, sensors at 1.5 m, 100 m from the plot (l. 158); dew point follows from them.
- **Validated on:** a 1 ha park of 100 plants, ten trees watched, 13-22 August 2022, Korhogo (9 34 N) (l. 179). Wetness was seen by eye each hour: a tree was wet if the finest drop showed on at least one leaf; the plot was wet if any of eight trees was wet, a strict criterion (l. 201).
- **RH >= 90 % rule:** fraction correct 77 %, CSI 60 %, kappa 0.54 (l. 26). Bias 0.91 and FAR 0.22 are from the LEADS summary of the abstract, not in the facts.
- **DPD rule:** onset at DPD <= 1.5 degC, cessation at 4 degC: fraction correct 79 %, kappa 0.58, FAR 17 % (l. 29).
- **Threshold sets:** initial 1.8 / 2.2 degC (credited to Rao et al. 1998), site mean 1.5 / 4 degC, median 1.1 / 3.6 degC (l. 266).
- **Equations:** thresholds are a rule, not an equation; skill-score definitions are standard.

## Dependence

- Same form as the engine's sentelhas2008.wetness and cooptera.rh90_wetness (structure tag rh-threshold-wetness): RH threshold plus DPD onset and cessation thresholds. Kin by shared threshold form.
- Its 1.8 / 2.2 degC pair is Rao et al. 1998's; the fitted pair is calibrated on these ten days. Not kin to cooptera.logistic_wetness.

## Bearing (2026-10-27)

- **What it supports:** that an RH >= 90 % threshold gets about 77 % of hours right against a strict visual wetness on a tropical tree crop, and that a DPD rule is a little better (79 %). One site, ten days, not vines, sensor at 1.5 m.
- **Weighting:** because it shares the engine's threshold form, it is not an independent fill for D60; as a check of the engine's own piece it is a weak one (ten days).
- **Not shown:** any vine canopy, error in hours per day, dependence on leaf height. Kind of result: a small validation (measurement) of kin models.

---
id: schrader2020
citation: Schrader, James A., Domoto, Paul A., Nonnecke, Gail R. & Cochran, Diana R. 2020. Multifactor models for improved prediction of phenological timing in cold-climate wine grapes. HortScience 55(12):1912-1925
doi: 10.21273/HORTSCI15367-20
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; Table 6 (p. 1923) read in the page image and the text layer by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Iowa, USA]
processes: [phenology, budburst, flowering, veraison, harvest, soil temperature, photoperiod]
records: [schrader2020.days_remaining]
datasets: [schrader2020.iowa]
files: [schrader2020_hortsci.pdf]
---

# Schrader et al. 2020: days remaining to each stage from the day's predictors

A different question: not "on which day" but "how many days remain", refitted every day
from the date, soil thaw, photoperiod, air and soil degree-days and the solar sum, for
five cold-climate hybrids in Iowa. The printed equations put photoperiod and soil
temperature, two of Chris's non-thermal drivers, in one model.

## What it holds

- **Data** (`schrader2020.iowa`): Frontenac, La Crescent, Marquette, Petit Ami and St.
  Croix, 18 vines each, at Iowa State's station near Gilbert, planted 2008 (l. 125-133);
  stages at 50 % and harvest by assay (l. 162-175); seasons 2011, 2013, 2014 (l. 204);
  validation on 144 Marquette vines 400 m away in 2019 (l. 213-216). Predictors:
  cultivar, day of year, soil thaw day, previous-stage day, photoperiod, GDD10 (daily
  mean with a 30 °C cap, or hourly with none, l. 198-211), soil degree days above 5 °C
  at 10.2 cm, solar accumulation (MJ/m²), the sums restarting at soil thaw or the
  previous stage (l. 212-218, 508-511).
- **Form** (`schrader2020.days_remaining`): days until the stage = cultivar adjustment +
  Σ coefficient × factor + constant, by least squares for one or two factors and elastic
  net for more (l. 229), in JMP (l. 206). The response is days remaining, not the day
  (l. 747-752); the heat sum is a term, not a trigger (l. 757-761).
- **Fit** (Tables 1-4, 6): top budbreak model R² 0.996, mean error 0.70 d (n 4,403
  vine-days) against 5.27 d (R² 0.787) for cultivar plus hourly GDD10 alone (l. 235-241);
  bloom 0.84 against 2.24 d, veraison 1.77 against 2.79, harvest 3.80 against 4.29
  (l. 47-49). Validation 2019: 1.92, 1.31, 0.94 and 1.67 d against 10.05, 2.54, 4.23
  and 4.96 d (l. 50-51). Hourly GDD10 beat the daily form (l. 375).
- **Table 6** (p. 1923): the top budbreak equation, −2.41 × DOY + 0.152 × soil-thaw DOY
  + 24.37 × photoperiod − 0.135 × GDD10 + 0.080 × SDD5 + 0.024 × solar − 66.43, with
  cultivar adjustments (Marquette −1.98, St. Croix 0); bloom, veraison and harvest
  equations likewise. Units are not printed; n in the footnote does not match the tables
  (l. 515).

## Dependence

- **Fitted to** the authors' own vineyard; the response is computed from observed stage
  dates. GDD methods are Iowa State's and Gu 2016's (cited). Zapata et al. 2017's errors
  (5.4, 3.0, 6.6 d) are the comparison the authors cite (l. 767, 832).
- **No kin** in the catalogue by form; the heat sum inside is the engine's degree-day
  idea used as a regressor.

## Bearing (2026-10-13)

- The only paper found that prints a working model with photoperiod and soil
  temperature; its gain over GDD alone (0.7 against 5.3 d in training, 1.9 against 10.1
  d in validation) is the strongest number in the search. Hybrids, one site, three
  seasons: a form to copy, not coefficients to use.

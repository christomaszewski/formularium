---
id: kaundal2006
citation: Kaundal, R., Kapoor, A.S. & Raghava, G.P.S. 2006. Machine learning techniques in disease forecasting: a case study on rice blast prediction. BMC Bioinformatics 7:485
doi: 10.1186/1471-2105-7-485
read: 2026-10-27, in full (Europe PMC full-text XML, converted to text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [rice leaf blast (Magnaporthe oryzae)]
crops: [rice]
regions: [India, Himachal Pradesh]
processes: [forecasting, support vector regression, neural network, multiple regression, leave-one-year-out, leave-one-location-out, variable importance]
records: []
datasets: []
files: [syn1027_kaundal2006.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Kaundal et al. 2006: weather-based rice leaf blast severity, four regression methods scored on held-out years and held-out places (analogue crop)

Compares multiple regression, a back-propagation network, a generalised regression network and a support vector machine on weekly weather for rice blast severity, with whole years and whole locations left out. No record: a method. The data are not published in the paper.

**Read this first.** Rice, not a vine. Few site-years, six weekly weather variables, and fold scores swing from r near 0.98 to below zero. In the "cross-location" folds the other locations of the same year stay in training, so only the cross-year folds hold a season out. The variable ranking was made on the single best fold only. The abstract calls the design five-fold cross validation.

## What it holds

- **Real data** (l. 134): rice leaf blast severity at five locations in Himachal Pradesh (three sowing dates at one university farm, a research station, and farmers' fields), for 2000 (historical) and 2001 to 2004 (a national project); sites and sowing dates were chosen "to generate epidemics of different severity". At most 25 location-years (arithmetic, not printed).
- **Labels are observed**: field-scored leaf blast severity on 25 marked points per plot (l. 134); not computed by a model.
- **Inputs** (l. 135): six weekly averages of daily readings, maximum and minimum temperature, maximum and minimum relative humidity, rainfall and rainy days per week, from an automatic weather station at one site and thermo-hygrographs at the others. No wetness, radiation or wind.
- **Synthetic or augmented data:** none.
- **Validation** (l. 155): "cross-year" models drop each year in turn and train on the other four; "cross-location" models drop each location in turn within a year and train on the rest of that year. The cases are weekly observations, not independent within a season.
- **Cross-year scores**, average over five locations (l. 105; r, then %MAE): regression 0.50, 65.42; back-propagation network 0.60, 52.24; generalised regression network 0.70, 46.30; support vector machine 0.77, 36.66.
- **Cross-location scores** (l. 7): regression r 0.48 (%MAE 77.54), back-propagation 0.56 (66.11), generalised regression 0.66 (58.26), support vector machine 0.74 (44.12). Skill falls from held-out years to held-out places for every method.
- **Fold spread** (l. 39, 108): the best support vector fold has r 0.98 (2001, farmers' fields held out); the 2002 fold with the first sowing-date plot held out gives r from -0.34 to 0.12 for all four methods.
- **Variables** (l. 108, 111-112): leaving one variable out of the best cross-year support vector model, rainfall matters most (r 0.979 to 0.789), then minimum relative humidity (0.866); the others change r by less than 0.03. One fold only, not across folds.
- **Baseline:** the multiple regression is the baseline; no persistence or climatology baseline.

## Dependence

- No process model; labels and inputs are measured. Cites earlier regression work that did not generalise across sites and years (l. 13).

## Bearing (2026-10-27)

- **D58 (variable search):** an early design with held-out years and held-out places on six weekly weather variables. The ceiling is r 0.77 on held-out years and 0.74 on held-out places for the best method (r 0.50 and 0.48 for regression); rainfall and minimum RH carried the best fold. Weekly means of daily T, RH and rain, not hourly series; five locations; one crop.
- **Spread:** folds from r 0.98 to below zero show how much a handful of seasons decides a score; a variable ranking from one fold is not a variable shown to hold.
- **Not shown:** anything synthetic (D60); a result beyond Himachal Pradesh.

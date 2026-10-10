---
id: valleggi2023
citation: Valleggi, Lorenzo, Carella, Giuseppe, Perria, Rita, Mugnai, Laura & Stefanini, Federico Mattia. 2023. A Bayesian model for control strategy selection against Plasmopara viticola infections. Frontiers in Plant Science 14:1117498
doi: 10.3389/fpls.2023.1117498
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 30 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Tuscany]
processes: [spray strategy, season severity]
records: []
datasets: [valleggi2023.chianti]
files: [p07.pdf]
---

# Valleggi et al. 2023: choosing a control strategy from three Chianti seasons

## What it holds

- **Data:** the LIFE Green Grapes trial (Perria et al. 2022), one Sangiovese vineyard in
  Chianti Classico, 2018-2020; five strategies, 400 leaves per strategy and year scored
  infected or not at BBCH 85-89.
- **Control (biostimulants only):** 386 of 400 leaves infected in 2018, 34 in 2019 and 318
  in 2020.
- **Model:** Bayesian logistic GLMM with strategy, year and year-by-strategy effects; no
  weather (the year effect stands in for it). An expert utility picks the strategy.
- **Printed slips:** utility values for S2 and S4 in the text do not match Table 3;
  Brischetto 2020 in the text, 2021 in the references; Chen et al. 2020 credited with
  March-April rain, where Chen names May and June.

## Dependence

- None.

## Bearing (2026-10-09)

- Three seasons of end-of-season incidence in Chianti, severe, slight and severe: a
  year-to-year severity pattern.

---
id: volpi2021
citation: Volpi, Iride, Guidotti, Diego, Mammini, Michele & Marchi, Susanna. 2021. Predicting symptoms of downy mildew, powdery mildew, and gray mold diseases of grapevine through machine learning. Italian Journal of Agrometeorology 2:57-69
doi: 10.36253/ijam-1131
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 41 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew, grey mould]
crops: [grapevine]
regions: [Tuscany]
processes: [forecasting, season onset]
records: []
datasets: [volpi2021.tuscany]
files: [volpi2021_ijam.pdf]
---

# Volpi et al. 2021: tree classifiers on Tuscany's IPM monitoring network

## What it holds

- **Data:** Tuscany's area-wide IPM network (Agroambiente.info), weekly presence or absence
  of symptoms on Sangiovese in 112-179 vineyards a year, 2006-2019 except 2011: 18,857
  downy mildew, 14,848 powdery and 4,960 grey mould records.
- **Weather:** ERA5-Land reanalysis (9 km), not stations.
- **Models:** random forest and C5.0; predictors include degree-days, rain sums, treatment
  counts, elevation, distance to the sea, day of year and the previous year's symptom
  frequency.
- **Results:** balanced accuracy about 0.78-0.79 for downy mildew on the test split, about
  0.71 on 2018-2019. The previous year's frequency and cumulative rain matter most.
- **Printed slip:** the text swaps the sensitivity and PPV labels.

## Dependence

- None. Rossi et al. 2008 and Caffi et al. 2011 are cited as mechanistic models.

## Bearing (2026-10-09)

- The network's records are a large observed set of symptom presence by week and vineyard
  in a Mediterranean region: a pattern source if they can be had. They are not in the paper.

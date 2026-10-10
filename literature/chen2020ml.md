---
id: chen2020ml
citation: Chen, Mathilde, Brun, François, Raynal, Marc & Makowski, David. 2020. Forecasting severe grape downy mildew attacks using machine learning. PLoS ONE 15(3):e0230254
doi: 10.1371/journal.pone.0230254
read: 2026-10-09, in full, compared with chapter 7 of chen2019, by a reading agent (claude-haiku-5-5); 30 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [season severity, season onset, forecasting]
records: []
datasets: [chen2019.ifv]
files: [chen2020_plosone.pdf]
---

# Chen et al. 2020 (PLoS ONE): chapter 7 of the thesis, published

The published form of [chen2019](chen2019.md)'s chapter 7. Same design and models.

## Differences from the thesis

- 153 site-years, 2010-2018 (thesis 156; plots analysed 153 against 151).
- Censored onsets 95 (thesis 97), imputed by a survival model with March-June rain.
- Random forest of 500 trees (thesis 100); best AUC 0.86, gradient boosting on leaf
  incidence (thesis 0.87). Without onset, 0.77.
- Sprays: 5.1 by the first-symptom rule; 3.7 at a threshold of 0.5 and 1.5 at 0.75.

## Dependence

- None of the engine's models. The imputed onsets carry a rain model, so onset's lead among
  the predictors is partly built in, as the thesis note says.

## Bearing (2026-10-09)

- Nothing beyond chen2019.

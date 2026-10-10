---
id: kim2007nzpp
citation: Kim, K. S., Beresford, R. M. & Henshall, W. R. 2007. Prediction of disease risk using site-specific estimates of weather variables. New Zealand Plant Protection 60:128-132
doi: 
read: 2026-10-10, in full, the Bacchus equation in the page image, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py; the equation checked in the page image (p. 129), and against Hill et al. 2019's eq. 1 in its page image, by the main session
status: read
diseases: [grey mould]
crops: [grapevine]
regions: [Marlborough, Hawke's Bay]
processes: [weather interpolation, leaf wetness, infection risk]
records: [kim2007.bacchus]
datasets: []
files: [kim-beresford-henshall-2007-nzpp.pdf]
---

# Kim et al. 2007: Bacchus on interpolated weather, as first printed

The source of `kim2007.bacchus`, recorded so far from [hill2019](hill2019.md).

## What it holds

- **Bacchus as printed** (p. 129): a risk index for each wet hour, I = 84.37 - 7.238T +
  0.1856T², summed over each wet period, credited to Rengasamy & Edwards (unpublished
  data). No reciprocal and no 50 % wetness threshold.
- **Hill et al. 2019's "correction"** (eq. 1, checked in its page image): x = 1/(84.37 -
  7.238T + 0.156T²). Both the form and c changed.
- **At one point** (computed 2026-10-10): Kim's I is lowest, 13.8, at 19.5 °C and highest
  at 0 °C, so read as a risk it peaks in the cold; read as wet hours needed, it gives 13.8 h
  at the optimum, near Broome's 10.5 h at 20 °C (logit 0). Hill's form needs only 0.41 h at
  23.2 °C (x = 2.42 per wet hour).
- **Interpolated weather** (Renwick and Tomoana, 2003-05): air temperature RMSE 0.5-1.1 °C;
  fuzzy-logic wetness mean error 0.7-2.3 h/day, MAE 2.5-3.6 h/day; Bacchus risk from
  interpolated weather differed at Tomoana.

## Dependence

- The paper behind `kim2007.bacchus`. Beresford is an author of the later papers: a flag.

## Bearing (2026-10-10)

- Which Bacchus is meant matters: as recorded (Hill's) it infects in under an hour at
  23 °C. Flagged on the record.

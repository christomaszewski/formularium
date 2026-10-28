---
id: kim2007nzpp
citation: Kim, K. S., Beresford, R. M. & Henshall, W. R. 2007. Prediction of disease risk using site-specific estimates of weather variables. New Zealand Plant Protection 60:128-132
doi: 
read: 2026-10-10, in full, the Bacchus equation in the page image, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py; the equation checked in the page image (p. 129), and against Hill et al. 2019's eq. 1 in its page image, by the main session; 2026-10-27, read again for Agrarium D60 by a reading agent and a note writer (claude-sonnet-5-5), quotes found at their lines by scripts/verify_quotes.py
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
- **2026-10-13:** Hill et al. 2019's corrected form, x = 1/(84.37 − 7.238T + 0.156T²), is what Pîrcălabu et al. 2020 run in Romania as "a correction to the model published by Kim et al. 2007" (`pircalabu2020`, l. 50-56): the correction has reached users abroad.

## Read again (2026-10-27), for Agrarium D60

- **Model:** an empirical fuzzy-logic wetness model (Kim et al. 2004, not held) with a cloud parameterisation added to estimate incoming longwave radiation (Collins et al. 2004), fed with interpolated air temperature, vapour pressure and wind (l. 122). The model's equations are not printed here.
- **Validation sites:** Renwick (vineyards, Marlborough) and Tomoana (orchards, Hawke's Bay), November-March 2003-04 and 2004-05; sensor not stated (l. 68).
- **Error:** wetness duration from interpolated inputs was overestimated, ME +0.7 h/day at Renwick and +1.7 h/day at Tomoana (l. 162). MAE is in Table 1 but its columns are garbled; the LEADS summary gives 2.7 and 3.5 h/day, not checked here.
- **Not compared:** the FL model on measured inputs against a sensor is not printed here (l. 21).

## Bearing (2026-10-27)

- **What it supports:** a physical-statistical wetness fill driven by station weather with a longwave cloud term, with an error of about +0.7 to +1.7 h/day bias on interpolated inputs for NZ vineyards. Interpolation error is mixed in with the model error.
- **Not shown:** the model on its own inputs, the model itself. Kind of result: a validation on interpolated data.

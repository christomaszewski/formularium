---
id: dimitrovski2026
citation: Dimitrovski, Ivica, Kitanovski, Ivan, Davcev, Danco, Kalajdziski, Slobodan & Mitreski, Kosta. 2026. Event-based early warning of vineyard disease risk from environmental time series. arXiv:2605.04548v2 (22 September 2026); also International Journal of Data Science and Analytics, doi 10.1007/s41060-026-01282-8 (not read)
doi:
read: 2026-10-13, in full (the arXiv text), by a reading agent (claude-haiku-5-5); 52 of 52 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [not stated; the data of arvanitis2025, Emilia-Romagna]
processes: [forecasting, machine learning, spray records, early warning]
records: []
datasets: []
files: [2026-arxiv-arxiv-2605-04548.pdf]
---

# Dimitrovski et al. 2026: early warning of mildew "events" learnt from spray records

The Skopje group's reworking of `arvanitis2025`'s single-vineyard data: logistic
regression, XGBoost, LSTM and TCN models that predict whether a new mildew "event"
begins within 3 to 7 days, from daily weather and the calendar. The labels are fungicide
treatments, so this is a model of the grower's decisions, as `arvanitis2025` was.

## What it holds

- **Data:** one unnamed vineyard, daily humidity, temperature and rainfall, 2020-2023
  (training 2020-2021, validation 2022, test 2023; l. 164-167, 405-414); downy and powdery
  mildew labels "derived from historical fungicide-treatment records", agreeing on 98.9 %
  of days and combined by OR (l. 25-28, 417-423, 577); 2023 has 363 observed days, 60
  positive days and 8 events for each label (Table 1, l. 477-480). An event is the first
  positive day after at least g = 5 disease-free days (l. 591-612).
- **Features:** 22 environmental (rolling sums and means, a humid-day count above 85 % RH,
  rainy days) and 4 cyclic calendar features (l. 647-747); 75 positive against 377
  negative training windows, class weight 5.03 (l. 839-843); thresholds chosen on 2022
  by F1 (l. 896-900); transformers excluded for lack of cycles (l. 902-906).
- **Results on 2023:** a monthly climatological baseline already detects 6 of 8 events
  (F1 0.507, AUROC 0.830; l. 1081-1085); calendar-only LSTM and TCN detect 7 of 8 in every
  run, TCN with AUROC 0.913 (l. 1102, 1151); environmental-only models reach AUROC only
  0.64-0.65 (l. 1121); the combined XGBoost F1 0.555, AUROC 0.755, 6 of 8 events, about
  41 alerts (l. 1157). SHAP attribution: humidity 34 %, temperature 29 %, calendar 21 %,
  rain 16 %, with 69 % of it at lags of 14-29 days (l. 1409-1421, 1469-1473). The text's
  claim that combined XGBoost had the fewest false-alert episodes is contradicted by
  Table 3 (calendar logistic regression, 2; l. 1148, 1183). Gap and horizon
  sensitivities in Tables 5-8 (l. 1289-1433).

## Dependence

- **Fitted to** treatment records, not disease observations; no process model (3-10,
  Goidanich, VitiMeteo) is used for labels or features (search of the text). The data
  are `arvanitis2025`'s (l. 458).
- **Authors:** none shared with engine models.

## Bearing (2026-10-13)

- Not usable as a truth or as an observation of disease: the "events" are spray decisions,
  and the calendar alone predicts them about as well as the weather does. It stands as
  the measured ceiling of this approach on one vineyard, the same verdict as
  `arvanitis2025` and `steffenel2023`.

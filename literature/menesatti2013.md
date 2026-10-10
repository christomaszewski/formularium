---
id: menesatti2013
citation: Menesatti, P., Antonucci, F., Costa, C., Mandalà, C., Battaglia, V. & La Torre, A. 2013. Multivariate forecasting model to optimize management of grape downy mildew control. Vitis 52(3):141-148
doi: 
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 40 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Lazio]
processes: [forecasting, spray timing, incubation]
records: [goidanich.incubation, rule_3_10]
datasets: []
files: [p45.pdf]
---

# Menesatti et al. 2013: a PLS-DA spray model for organic Malvasia near Rome

## What it holds

- **Trial:** an organic 'Malvasia di Candia' vineyard near Rome, 2009 and 2010; standard
  organic schedule, model-guided, and untreated control.
- **Model:** partial least squares discriminant analysis on 18 daily predictors (weather,
  BBCH, and a "GOIDANICH T" variable). The response is a daily yes/no from the first
  derivative of observed incidence (0.4 %) or severity (0.02 %); the thresholds were set on
  the same observations. Calibrated on 2006-2008, which the paper does not describe.
- **Results (Table 2):** calibration 91.80 % (onset) and 91.23 % (progress); field 81.30 %
  (2009) and 81.60 % (2010). Sprays 9 against 5 (2009) and 13 against 7 (2010).

## Dependence

- Computes Goidanich et al. 1957's incubation, and uses it as a predictor; reads the 2009
  infective rain with the 3-10 rule. Both are engine models.

## Bearing (2026-10-09)

- Not usable: no equation, and its targets were cut from its own data. Recorded so that it
  is not read again.

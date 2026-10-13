---
id: pircalabu2020
citation: Pîrcălabu, Liliana, Brînduşe, Elena & Ion, Marian. 2020. Prediction of Botrytis cinerea risk in vineyards based on weather indicators. Bulletin UASVM Horticulture 77(2):59-63
doi: 10.15835/buasvmcn-hort:2020.0038
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [grey mould, botrytis bunch rot]
crops: [grapevine]
regions: [Valea Călugărească, Romania]
processes: [infection risk, season severity, leaf wetness, validation]
records: [kim2007.bacchus, broome1995.botrytis]
datasets: []
files: [pircalabu2020_usamv.pdf]
---

# Pîrcălabu, Brînduşe & Ion 2020: Bacchus and Broome over ten Romanian seasons

Open access (the Cluj bulletin), fetched 2026-10-12. The two engine Botrytis models, with
their coefficients printed, run on ten seasons of a Romanian station's weather and set
against the attack recorded there; short and inconsistent in places, but a third copy of
both equations.

## What it holds

- **The equations as printed** (l. 50-63): Bacchus per wet hour, f(x) = 1/[84.37 −
  7.238 T + 0.156 T²] with T the mean temperature, "a correction to the model published
  by Kim et al. 2007" (l. 56): this is the Hill et al. 2019 form `kim2007nzpp` and
  `hill2019` record, with c = 0.156, not Kim's original 0.1856 and reciprocal-free sum.
  Broome per wet period, f(x) = −2.647866 − 0.374927 W + 0.061601 Tw − 0.001511 Tw²
  (the Tw coefficient split across l. 58-59; W in hours of surface wetness), without the
  logit the source prints; and a "modified Broome" per wet hour, 0.00616 T − 0.00015 T²,
  of unstated origin (l. 62-63). Two infection windows: BBCH 53 to 30 % of berries full
  size, and from most berries full size to BBCH 89 (l. 54-70).
- **Data:** the Valea Călugărească institute's agri-environmental database, 2010-2019 (l.
  42-43), instruments not named; season mean temperature 19.6 °C, RH 65.3 % (Table 1,
  which labels the temperature column "%"); Table 2's leaf-wetness hours by year (2010:
  281.6 h at 22.9 °C) and an undefined "Botrytis occurrence (hours)"; Table 3's attack
  degree by year (2010: 62.9 %; 2012: 42.4 %), which the abstract assigns to 2012 and the
  text to no symptoms in 2012-2013 (l. 21, 173, 194-196); 80 % of years "high risk" by a
  rule not printed (l. 19).
- **Results:** the accumulated Broome index differs by attack class (P = 0.021), the
  accumulated Bacchus index does not (P = 0.051), by rank tests (Table 4, l. 211-215);
  both indices track sunshine hours (r 0.935 and 0.944) and leaf-wetness hours (0.833,
  0.848) (Tables 5-6, l. 232-251), and multiple regressions of each on sunshine, RH and an
  "Ih" are printed (l. 309-312); a 62.9 % attack is said to cost 37 % of the crop (1.114
  against 2.909 kg a vine), method not printed (l. 281-296). The 2.8 h and 6 h "minimum
  leaf wetness" of the text do not match Table 2 (l. 271).

## Dependence

- **Computes** `kim2007.bacchus` in Hill et al. 2019's corrected form and
  `broome1995.botrytis`'s logit coefficients, unchanged; fits nothing to disease. The
  weather and the attack scores are the station's own, observed.
- **Authors:** none shared with engine models.

## Bearing (2026-10-13)

- Closes two trails: it prints Broome's b2 as 0.061601, the coefficient the text layer of
  `broome1995` garbled (and `monteiro2015bol` read the same), and it carries Hill's
  corrected Bacchus with c = 0.156, so the correction has reached users outside New
  Zealand. As a validation it is weak: ten seasons, attack classes by an unprinted rule,
  and the text contradicting its tables.

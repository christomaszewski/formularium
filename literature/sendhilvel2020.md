---
id: sendhilvel2020
citation: Sendhilvel, V., Marimuthu, T. & Geethalakshmi, V. 2020. Epidemiological model based decision support system for the management of grapes downy mildew. Madras Agricultural Journal 107(10-12):422-428
doi: 10.29321/MAJ.10.000465
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py; dependence judged by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Tamil Nadu]
processes: [forecasting, spray timing, validation]
records: []
datasets: []
files: [in_dss_2020_madras.pdf]
---

# Sendhilvel et al. 2020: a logistic-curve spray schedule for Muscat at Coimbatore

## What it holds

- **Site and weather:** Muscat at Mathampatti, Coimbatore; an automatic station logged RH,
  temperatures, rain, leaf wetness, dew and radiation every 10 min, 2014-17.
- **Model:** Gompertz, logistic, monomolecular and Richards curves were fitted (Curve Expert
  1.3) to an unsprayed plot's disease against each weather variable; the logistic was kept
  (R 0.997). Its coefficients, units and time step are not printed, nor the "weather index".
- **Schedule:** sprays placed in the curve's lag phase. Five sprays (Pf1, azoxystrobin or
  both) against 15 by farmers.
- **Results:** PDI 12.53 (azoxystrobin), 12.56 (combined), 17.6 (Pf1 with FYM), farmers 28.50
  in Table 2 (21.23 in the text), control 78.83.
- **Printed slips:** two sprays in the lag phase in the abstract, three in the text; four
  replicates against three; P > 0.05 called significant; figure axes 0-1000 for a PDI of
  0-100.

## Dependence

- No engine model is computed. Lalancette 1988, Blaeser & Weltzien 1979 and Rossi et al. 2008
  are cited for statements only; "Goidanich 1959" is cited for McKinney's PDI formula.
- The schedule and the trial were built on the same unsprayed-plot curve, so the trial does
  not test a forecast.

## Bearing (2026-10-09)

- Context only: a tropical, two-cropping-season setting. No coefficients to reuse.

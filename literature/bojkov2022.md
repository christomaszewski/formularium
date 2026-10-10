---
id: bojkov2022
citation: Bojkov, Gligor, Arsov, Emilija & Mitrev, Saša. 2022. Forecasting model based on cumulative degree days for incubation period of Plasmopara viticola (Berk. & M.A. Curtis) Berl. & De Toni. Journal of Agriculture and Plant Sciences (JAPS) 20(1):25-31
doi: 10.46763/JAPS22201025b
read: 2026-10-09, in full (7 pages), by a reading agent (claude-haiku-5-5); 47 quotes checked by scripts/verify_quotes.py; the model's equation and the 3/10 passage checked by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [North Macedonia]
processes: [incubation, primary infection, forecasting]
records: []
datasets: []
files: [cdd-incubation-forecast-2022.pdf]
---

# Bojkov et al. 2022: a degree-day incubation model from one season at Smilica

Not the same paper as [bojkov2023](bojkov2023.md).

## What it holds

- **Site:** one 9 ha vineyard (double Guyot, four varieties) at Smilica near Kavadarci.
- **Start of incubation:** the 3/10 rule (Baldacci 1947): at least 10 °C, 10 cm shoots,
  10 mm of rain in 24-48 h. The date it was met is not printed.
- **Observation:** daily monitoring from 2 to 12 May 2022; first oil spots on 12 May
  (incubation 10 days).
- **Model:** effective temperature Ef = ADT - 11 °C; coefficient Coeff. In = Ef / ADT. The
  base is 11 °C; Müller & Sleumer's 12-13 °C is cited but not used.
- **Fit:**
  - **Regression:** Coeff. In on ADT gives intercept -0.35047, slope 0.040825, R² 0.970186,
    n = 10.
  - **End of incubation:** the first day with y > 0 (0.057 on 12 May), matching the observed
    date.
  - **Weaknesses:** the coefficient is a fixed function of temperature, so the regression is
    largely tautological, and there is no out-of-sample test. Table 4's values do not
    reproduce from the printed line.
- **Cited:** Müller & Sleumer 1934 (incubation calendar), Gessler et al. 2011, Caffi et al.
  2009 (spray counts only), Gobbin et al. 2005.

## Dependence

- Borrows the 3-10 rule, an engine model, to start its clock. Goidanich and Rossi 2008 are
  not cited.

## Bearing (2026-10-09)

- Not usable as an incubation model: one season, ten points, and tautological. Recorded so
  that it is not read again.

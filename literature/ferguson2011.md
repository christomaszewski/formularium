---
id: ferguson2011
citation: Ferguson, J. C., Tarara, J. M., Mills, L. J., Grove, G. G. & Keller, M. 2011. Dynamic thermal time model of cold hardiness for dormant grapevine buds. Annals of Botany 107(3):389-396
doi: 10.1093/aob/mcq263
read: 2026-11-03, in full (8 pages) with page images of p. 391 and p. 392, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 26 of 26 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [USA (Prosser, Washington)]
processes: [cold hardiness, LTE50, acclimation, deacclimation, thermal time, dormancy, endodormancy, ecodormancy]
records: [ferguson2011.hardiness]
datasets: [ferguson2011.prosser]
files: [dr1103_ferguson2011.pdf (the 2026-11-03 drop)]
---

# Ferguson et al. 2011: a daily thermal-time model of bud cold hardiness for Cabernet Sauvignon, Chardonnay and Concord

The source of the engine's cold-hardiness model: a daily step from leaf fall to budswell, with acclimation and deacclimation rates that differ in endodormancy and ecodormancy, fitted to measured LTE50 at Prosser.

**Read this first.** Until now the record was cited from PubMed Central and the paper was not held. The record's authors, equations and Table 2 parameters are now checked against the printed paper (see Bearing). The catalogue's ferguson2014 is a later paper with its own note.

## What it holds

- **Authors (l. 8):** five, as printed: Ferguson, Tarara, Mills, Grove and Keller.
- **Equations:** Eq. 1 (p. 390, l. 126): Hc,i = Hc,i-1 + DHc, a daily step. Eq. 2 (p. 391, l. 177): DHc = (DDc x ka x c_log,a) + (DDh x kd x c_log,d). Eq. 3 (p. 391, l. 179): DD = Tmean - Tth, negative below the threshold (chilling), positive above (heating). Eq. 5 (p. 391, l. 148): c_log,a = 1 - (Hc,min - Hc,i-1)/(Hc,min - Hc,max). Eq. 6 (p. 391): c_log,d = 1 - (Hc,i-1 - Hc,max)/(Hc,min - Hc,max). Eq. 4 and Eq. 6 were read in the page image, not in the text layer.
- **Bounds (l. 159):** Hc,max is the mean lowest measured LTE50 per cultivar; Hc,min is set to -3 °C (green tissue); Hc,initial is the mean of the earliest LTE50 near leaf fall.
- **Table 2 (p. 392), Concord / Chardonnay / Cabernet Sauvignon:**
  - Hc,initial -11.94 / -10.55 / -9.99 °C (l. 245); Hc,max -29.73 / -25.24 / -24.63 °C (l. 246); Hc,min -3.00 °C for all (l. 247).
  - Tth,endo 12.50 / 11.75 / 11.75 °C (l. 248); ka,endo 0.13 / 0.14 / 0.14 (l. 250); kd,endo 0.01 for all (l. 251).
  - Eco-dormancy boundary EDB -700 / -750 / -850 accumulated chilling degree-days (l. 252).
  - Tth,eco 4.25 / 3.75 / 5.75 °C (l. 253); ka,eco 0.01 / 0.07 / 0.01 (l. 254); kd,eco 0.16 / 0.13 / 0.12 (l. 255).
  - RMSE on the optimization set 2.05 / 1.40 / 1.47 °C (l. 256).
- **Site and data (l. 104, 111 to 113):** WSU research centre at Prosser, Washington (46.30 N), an on-site weather station for temperatures. Empirical data sets of 22 years for Cabernet Sauvignon, 14 for Chardonnay and 15 for Concord, 1988 to 2010 (l. 89, 111-112). About half the seasons were chosen at random for optimization, the rest for evaluation (l. 113, 116).
- **Fitting (l. 175):** parameters optimized by stepwise iteration to minimise RMSE (after Cesaraccio et al. 2004); sensitivity runs of at least 60 000 simulations.
- **Validation (l. 250):** Concord evaluation RMSE 2.27 °C, bias 0.18 °C.
- **Stated limits (l. 505, 529):** LTE50 data from one location only; thermal time from the daily mean; fixed Hc,max; an abrupt switch between endo- and ecodormancy. 6 to 10 years used for optimization and 8 to 12 for evaluation (l. 529).
- **Garbled:** the text layer prints °C as "8C" and "=" as a lozenge character; the PMC HTML copy prints Table 2 with the same values.

## Dependence

- **Data:** observed LTE50 by differential thermal analysis (Mills et al. 2006 method) and measured air temperature. No model computed or dated the observations; calibrated_with is empty.
- **Borrowed concepts:** degree-days, the eco- and endodormancy boundary (after Lang et al. 1987), logistic bounds (Mooney & Swift 1999), stepwise optimization (Cesaraccio et al. 2004).

## Bearing (2026-11-03)

- **Record ferguson2011.hardiness (Cooptera engine model):** checked against the paper. The authors (five, l. 8) match. Eqs 1, 2, 3 and 5 were found in the text; Eq. 4 and Eq. 6 are in the page image. Table 2's values are recorded on it as published parameters (read in the page image by the main session, 2026-11-03), with the data as `ferguson2011.prosser`; the record's "not held" is Cooptera's to change.
- **Fit:** the fit is to measured LTE50 at one site, with no model shaping the data. Cultivars differ in parameters, so a cultivar outside these three needs ferguson2014 (a refit of 23 cultivars, held).
- **Kind:** peer-reviewed fit and held-out evaluation at one site, Washington.

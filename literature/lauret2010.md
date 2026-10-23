---
id: lauret2010
citation: Lauret, P., Boland, J. & Ridley, B. 2010. Derivation of a solar diffuse fraction model in a Bayesian framework. Case Studies in Business, Industry and Government Statistics (CS-BIGS) 3:108-122
doi:
read: 2026-10-22, lightly: pages 1 to 9 and the equation pages (15 pages in all), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 26 of 26 quotes found at their lines by scripts/verify_quotes.py; the Figure 1 legend values read in the page image (PDF p. 7) by the main session
status: read
diseases: []
crops: []
regions: [Australia, Réunion, United Kingdom, Portugal, Mozambique, Macau, Belgium]
processes: [diffuse fraction, solar radiation separation, logistic model, Bayesian estimation, apparent solar time, persistence index]
records: []
datasets: []
files: [gd1021_lauret2010.pdf (the 2026-10-22 drop)]
---

# Lauret, Boland and Ridley 2010: the BRL diffuse-fraction model re-fitted in a Bayesian frame

The same logistic as `ridley2010`, with five hourly predictors, re-estimated by MCMC on five training sites and tested on seven.

**Read this first.** The text never states the unit of apparent solar time (AST). The three AST values of Figure 1's legend are only in the figure image (PDF p. 7): 8.5, 12.5 and 16.5, read by the main session in the page image at 300 dpi (the reading JSON had 18.5, which is corrected here). They read as decimal hours of the day, an inference. Table 3's beta2 row has its label on the line above its numbers (l. 436-437), and the row prints -0.005 where Eq. 10 prints -0.0047. No DOI is printed.

## What it holds

- **Form** (Eq. 2, PDF p. 4, l. 209): kd = 1 / (1 + exp(a0 + a1 kt + b1 AST + b2 alpha + b3 KT + b4 phi)), the Boland-Ridley-Lauret (BRL) model; kt = IG / I0 hourly (l. 209). The added predictors are AST, solar elevation alpha "in degrees", the daily clearness index KT and the persistence index phi (l. 194-196). AST's unit is not given in the text. AST is asymmetric about solar noon, unlike elevation, and may explain morning and afternoon differences (l. 218).
- **Persistence** (Eq. 3, PDF p. 4, l. 236-238): phi = (k(t-1) + k(t+1)) / 2 between sunrise and sunset; k(t+1) at sunrise; k(t-1) at sunset (the lag at hour h-1 and the lead at h+1).
- **Posterior** (Table 3, PDF p. 7, l. 431-441), mean (SD) with 95 % interval: a0 -5.323 (0.040), -5.403 to -5.244; a1 (kt) 7.279 (0.074), 7.135 to 7.423; b1 (AST) -0.030 (0.002), -0.033 to -0.026; b2 (elevation) -0.005 (SD 3.29E-4), -0.005 to -0.004; b3 (KT) 1.719 (0.049), 1.621 to 1.812; b4 (phi) 1.082 (0.067), 0.950 to 1.214.
- **Eq. 10** (PDF p. 7, l. 449): kd = 1 / (1 + exp(-5.32 + 7.28 kt - 0.03 AST - 0.0047 alpha + 1.72 KT + 1.08 phi)). Against Ridley et al.'s Eq. 10 (-5.38, 6.63, +0.006, -0.007, 1.75, 1.31) the AST coefficient changes sign and is five times larger in magnitude. **Eq. 11** (PDF p. 11, l. 729): the least-squares fit to the same training data: -4.60 + 6.54 kt - 0.04 AST - 0.0054 alpha + 1.71 KT + 0.85 phi. Classical least squares gave a worse bias than the Bayesian fit, especially for the southern sites (l. 760).
- **Old single-predictor logistic** (Boland et al. 2008, least squares, seven sites; cited): a0 -5.00, a1 8.60 (l. 175).
- **Method:** Bayesian variable selection (George and McCulloch 1993) over 16 candidate models chose the full model with all four extra predictors (l. 374); MCMC in WinBUGS, 30,000 iterations a chain, Student-t likelihood, robust to outliers (l. 396). Sensitivity of the output to AST and elevation is very small, but the model without them fitted worse (results not shown; l. 426).
- **Data:** training set of 11,074 hourly points: Adelaide 2003 (2,434), Darwin 2001 to 2002 (1,418), Réunion 2002 (2,125), Camborne 2001 (1,460), Lisbon 1980 (3,637), three southern and two northern sites (l. 183, 142). Test set of 19,844 points: Adelaide 2004 (2,307), Darwin 2003 and 2005 (1,179), Maputo 1970 (3,548), Réunion 2000 (2,045), Bracknell 1972 (3,613), Macau 1985 (3,513), Uccle 1990 (3,639) (Table 2, l. 153). Adelaide, Darwin and Réunion therefore appear in both sets, in other years.
- **Error on the test set** (Table 4, PDF p. 8, all sites, 19,844 h; l. 505): hourly diffuse-fraction RMSE for BRL 0.104, Skartveit 0.105, Reindl 0.111, Erbs 0.114, old logistic 0.114, least-squares BRL 0.104; MBE 0.008, 0.014, 0.015, 0.005, 0.005, 0.008. Hourly diffuse irradiance (Table 5, l. 538): RMSE of BRL 50 W m-2 (Skartveit 51, Reindl 56, Erbs 57, old 56, least squares 52); MBE 1, 6, 9, -2, 0, 6.

## Dependence

- **Same model form** as `ridley2010`, re-estimated by Bayesian MCMC on a different calibration set rather than seven-site least squares. The old logistic is from Boland et al. (2001, 2008); persistence from Boland (2008) and Erbs et al. (1982). Compared with Skartveit et al. (1998), Reindl et al. (1990) and Erbs et al. (1982).
- **Data:** none published; sites listed in Tables 1 and 2, details in Boland et al. (2008). Shared authors with `ridley2010`: the same model line, not a second opinion.

## Bearing (2026-10-22)

- **Units for `laiti2018.brl_bolzano`:** the elevation is in degrees (l. 196). AST has no stated unit; its legend values 8.5, 12.5 and 16.5 are consistent with hours of the day (inference from an image). That supports reading t as apparent solar time in hours, but nothing printed says so, and the answer is still not a stated fact.
- **The coefficient set in Laiti's Table 5 "original"** (-5.32, 7.28, -0.03, -0.0047, 1.72, 1.08; see `laiti2018`) equals this paper's Eq. 10 to the printed digits, not the set of `ridley2010`. So the "original" BRL in the catalogue's record traces to this Bayesian fit. Whether Lauret et al. 2013, the paper Laiti cites, repeats it is not known here.
- **Not shown:** the unit of AST in words; any check at a valley site. Kind of result: a Bayesian re-estimate with a test set that shares three sites with the training set in other years; the errors above are not a valley error, so Laiti's finding for Bolzano (shadowed hours inflating diffuse bias) stands apart from them.

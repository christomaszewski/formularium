---
id: ridley2010
citation: Ridley, B., Boland, J. & Lauret, P. 2010. Modelling of diffuse solar fraction with multiple predictors. Renewable Energy 35:478-483 (read from the in-press proof, whose header is dated 2009)
doi: 10.1016/j.renene.2009.07.018
read: 2026-10-22, in full, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py; the minus signs of Eq. 10 and Table 1 read in the page images (PDF pp. 3 and 4) by the reading agent
status: read
diseases: []
crops: []
regions: [Australia, United Kingdom, Portugal, Macau, Mozambique, Belgium, Réunion]
processes: [diffuse fraction, solar radiation separation, logistic model, clearness index, apparent solar time, persistence index]
records: []
datasets: []
files: [gd1021_ridley2010.pdf (the 2026-10-22 drop)]
---

# Ridley, Boland and Lauret 2010: the multiple-predictor logistic diffuse-fraction model (BRL)

The first paper of the Boland-Ridley-Lauret (BRL) hourly diffuse-fraction model: a logistic function of five predictors, fitted by least squares to seven sites.

**Read this first.** The unit of apparent solar time (AST) is printed nowhere in this paper. Only the solar angle is given a unit, degrees (l. 243). The text layer lost every minus sign in Eq. 10 and Table 1; the signs below were read from the page images (PDF pp. 3 and 4) by the reading agent. Greek letters alpha and psi print as "a" and "j", and the subscripts of Eq. 6 are lost (l. 263-270). The generic Eq. 10 here (AST coefficient +0.006) is not the set that `laiti2018` prints as "original" (see Bearing).

## What it holds

- **Predictors** (abstract, l. 44): hourly clearness index kt, daily clearness index Kt, solar altitude alpha, apparent solar time AST, and a persistence measure psi. kt = Iglobal / H0 over the hour (Eq. 2, l. 142). Kt is the sum over the 24 h of global radiation divided by the sum of extraterrestrial radiation (Eq. 7, PDF p. 3, l. 215-223): dimensionless.
- **Persistence psi** (Eq. 6, PDF p. 3, l. 263-270): the average of the lag and the lead of the hourly clearness index, (k(t-1) + k(t+1)) / 2 between sunrise and sunset, k(t+1) at sunrise and k(t-1) at sunset (subscripts read from the page image).
- **Units:** alpha "in degrees" (l. 243). AST is introduced because, unlike altitude, it is asymmetric about solar noon (l. 246-247); no unit is given, and the AST coefficients (0.006 in Eq. 10; 0.0007 to 0.0375 in Table 1) are per unit of AST.
- **Form** (Eq. 9, PDF p. 3, l. 254): d = 1 / (1 + exp(b0 + b1 kt + b2 AST + b3 alpha + b4 Kt + b5 psi)). Putting every predictor inside the logistic keeps d in (0, 1); adding them outside it (Eq. 8) gave infeasible values (l. 244-254).
- **Generic fit** (Eq. 10, PDF p. 4, l. 363): d = 1 / (1 + exp(-5.38 + 6.63 kt + 0.006 AST - 0.007 alpha + 1.75 Kt + 1.31 psi)). The minus signs of 5.38 and 0.007 are restored from the page image. Fitted on the data of all seven sites amalgamated, by least squares in Excel Solver, not Bayesian (l. 353, 341); n = 25,299 hourly points in the partial F test (l. 379).
- **Table 1** (PDF p. 3, l. 284-289; signs from the page image), columns Adelaide, Darwin, Maputo (southern), Bracknell, Lisbon, Macau, Uccle (northern): constant -6.0007, -4.6976, -6.4431, -5.0108, -5.0812, -5.1661, -4.8720; kt 8.0671, 5.4582, 7.1617, 6.1307, 6.1169, 6.3027, 7.0306; AST 0.0024*, 0.0007, 0.0375, -0.0135*, 0.0027*, -0.0037, 0.0035; alpha -0.0135, -0.0013, -0.0088, -0.0068, -0.0093, -0.0088, -0.0215; Kt 1.2590, 1.8179, 1.9497, 1.3986*, 1.3972, 2.1174, 1.8415; psi 1.5984, 1.3377, 1.7943, 1.3606, 1.5143, 1.4891, 1.1425. An asterisk marks a term not significant at 0.05; all terms were kept (l. 272). The AST sign differs between sites.
- **Error** (Table 3, PDF p. 5): median absolute percentage error of BRL 17.15, 21.13, 20.37, 5.52, 13.87, 7.11 and 6.37 % for the seven sites in the order above (l. 432; the reading JSON printed Uccle as 6.3, the text has 6.37). Median bias error 0.023, 0.144, 0.084, 0.023, 0.071, 0.007, 0.008 (l. 437); in the text layer a lost symbol stands before the first three, probably minus signs (not checked in the page image).
- **Out of sample:** Gillot (Réunion) and Camborne (UK): MeAPE 23.97 % and 7.90 %, MeBE 0.08 and 0.03 (l. 564). Gillot against a southern average of 19.55 %, Camborne against a northern average of 8.22 % (l. 585).
- **Data:** Adelaide and Darwin hourly integrated data from the Australian Bureau of Meteorology; Bracknell, Lisbon, Macau, Maputo and Uccle from various institutions as files with no metadata (l. 260); none published. Direct normal irradiance follows as (Iglobal - Idiffuse) / sin alpha (l. 547).

## Dependence

- **Extends** the single-predictor logistic of Boland et al. (2001, Environmetrics 12:103-116) and Boland et al. (2008, Renewable Energy 33:575-584; alpha0 -5.00, alpha1 8.60, as given in `lauret2010`). Persistence idea from Erbs et al. (1982). Compared with Reindl et al. (1990), Skartveit et al. (1998) and Perez et al. (1992).
- **Own fits** to seven sites. The same equation is re-fitted in a Bayesian frame by Lauret et al. (2010, CS-BIGS), note `lauret2010`. Shared authors (Boland, Ridley, Lauret) wrote the whole BRL line: the later fits are not independent checks of this one.

## Bearing (2026-10-22)

- **Units for `laiti2018.brl_bolzano`:** half answered. The solar angle is in degrees (here and in `lauret2010`). AST has no unit in this paper; the companion paper's Figure 1 legend, in the image only, uses AST = 8.5, 12.5 and 16.5, which reads as decimal hours of the day (inference; see `lauret2010`). So t in hours and h in degrees is the likely reading, not a stated one.
- **Which coefficients are "BRL":** this paper's Eq. 10 (-5.38, 6.63, +0.006, -0.007, 1.75, 1.31) is not the set in Laiti's Table 5 "original" (-5.32, 7.28, -0.03, -0.0047, 1.72, 1.08). Those match the Bayesian fit in `lauret2010` (Eq. 10) to the printed digits. The AST term changes sign and grows fivefold between the two papers. Lauret et al. 2013, which Laiti cites, is not read here.
- **Not shown:** why the AST sign flips; no check of AST in a unit other than the one used. Kind of result: an in-sample least-squares fit on seven sites with a two-site out-of-sample check; not for a valley site such as Bolzano.

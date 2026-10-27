---
id: kovaleski2018
citation: Kovaleski, A. P., Reisch, B. I. & Londo, J. P. 2018. Deacclimation kinetics as a quantitative phenotype for delineating the dormancy transition and thermal efficiency for budbreak in Vitis species. AoB PLANTS 10:ply066
doi: 10.1093/aobpla/ply066
read: 2026-10-26, in full from Europe PMC's JATS XML (no PDF held), by a reading agent (claude-haiku-5-5); 57 of 57 quotes found at their lines by scripts/verify_quotes.py; the equations are the XML's MathML, not a page image; Tables S1-S3 not held
status: read
diseases: []
crops: [grapevine]
regions: [Geneva NY]
processes: [dormancy, deacclimation, cold hardiness, chilling, budbreak]
records: [kovaleski2018.deacclimation]
datasets: [kovaleski2018.geneva]
files: [kovaleski2018.xml (the 2026-10-25 other-sources drop)]
---

# Kovaleski et al. 2018: buds lose hardiness at a rate set by temperature and by chill already had

Dormant cuttings of eleven Vitis genotypes, sampled through three winters at Geneva NY and
held at 2-30 °C, lose cold hardiness at a rate kdeacc that rises with temperature and is
scaled by a logistic of the chill accumulated, Ψdeacc; budbreak then follows the sum of
kdeacc over time as a line. The authors read the chill axis off a chill model.

## What it holds

- **Material** (l. 11, 21): V. vinifera Cabernet Franc, Cabernet Sauvignon, Riesling and
  Sauvignon blanc; V. aestivalis (2 clones), V. amurensis (3), V. riparia (4); dormant
  seasons 2014/15 to 2016/17 at two vineyards (42.705° N, 76.973° W; 42.845° N, 77.004° W)
  and the USDA unit at Geneva.
- **Chill** (l. 22): the North Carolina model (Shaltout & Unrath 1983) on hourly NEWA data,
  seasons starting 11 Sep 2014, 19 Sep 2015, 24 Sep 2016.
- **Assay** (l. 23-24): chambers at 2, 4, 7, 8, 10, 11, 22 and 30 °C; low-temperature
  exotherm (LTE) by differential thermal analysis at -4 °C an hour, 4-8 buds a point;
  budbreak on fully chilled buds (1440 units, Londo & Johnson 2014) at 2, 4, 7, 11 and 22 °C.
- **Deacclimation potential** (l. 28, 36, 41): Ψdeacc (%) = 100 / (1 + exp[b (ln Chill -
  c)]); Riesling b -7.23, c 6.88, pseudo-R² 0.87; c 6.77 for Sauvignon blanc; pseudo-R² above
  0.87 for most genotypes, 0.65 for Cabernet Sauvignon, 0.79 for V. amurensis.
- **Rate** (l. 30-32, 43): kdeacc = m exp(n T) below 12 °C and q ln(T - r) from 12 °C; the
  text puts the join at 10-11 °C; m, n, q, r in Table S2 (not held).
- **Hardiness loss** (l. 32): ΔLTE = β kdeacc Ψdeacc t, β expected to be 1, no estimate
  printed.
- **Budbreak** (l. 34, 47): GDD = kdeacc × t; stage = a + b GDD with a species interaction,
  P < 0.001, adjusted R² 0.66; a and b not printed. Outliers at a studentized residual of
  2.5 (l. 28); 19.5 % of V. amurensis observations removed (l. 36).
- **Cited** (l. 59): Cragin et al. 2017 report 0.6-1.9 °C a day for Cabernet Sauvignon.

## Dependence

- **Fitted to** its own chamber series (`kovaleski2018.geneva`), whose chill axis and season
  start dates are the North Carolina chill model's output on NEWA weather, not observations:
  a model shaped the data (`calibration_note`; no record of that model exists to name in
  `calibrated_with`).
- **Shares the form** of the engine's cold-hardiness records (`ferguson2014.cold_hardiness`,
  `ferguson2011.hardiness`): hardiness that deacclimates with temperature and chill.

## Bearing (2026-10-26)

- For Agrarium's phenology truth (the 10-14 search): a budbreak rule driven by deacclimation
  kinetics rather than a heat sum to a threshold, with printed forms but most coefficients in
  a supplement. Kin to the engine's Ferguson hardiness models by form. Campos-Arguedas et
  al. 2026 (held as XML, light read) apply the successor model NYUS.1 to budbreak.

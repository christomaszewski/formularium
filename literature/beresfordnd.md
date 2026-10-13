---
id: beresfordnd
citation: Beresford, R. M. & Hill, G. N. n.d. (about 2008, by its text). Predicting in-season risk of botrytis bunch rot in Australian and New Zealand vineyards. ASVO proceedings, pp. 24-28 (HortResearch, Auckland)
doi: 
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: [grey mould, botrytis bunch rot]
crops: [grapevine]
regions: [Tasmania, Victoria, Marlborough, Hawke's Bay, Auckland]
processes: [infection risk, season severity, latent infection, validation]
records: [kim2007.bacchus]
datasets: []
files: [nd-beresford-url-beresford-hill-bacchus.pdf]
---

# Beresford & Hill (about 2008): the Bacchus index against 44 trans-Tasman site-years

A conference paper from the trans-Tasman Botrytis project (University of Tasmania, the
Victorian DPI, HortResearch; l. 32-36), undated in the copy but written in the project's
second year with data to 2007-08 (l. 50). The field test of the engine's Botrytis model
(`kim2007.bacchus`), as run in HortPlus MetWatch.

## What it holds

- **Bacchus as described:** an hourly index for each hour that surfaces stay wet, from a
  quadratic temperature response with its optimum near 20 °C, summed over the wet
  period; a sum of 1 or more is an infection period (l. 36-43). No constant is printed
  (the c of `kim2007nzpp` is not here). Per growth interval (5 % capfall to pre-bunch
  closure, PBC to veraison, veraison to harvest; l. 25-27) the paper sums or averages
  the index, with and without the threshold, beside rainfall, rain days and daily
  temperatures, twelve variables (l. 41-50).
- **Data:** harvest severity (mean % of berries affected) in unsprayed plots of 44
  site-years, 2000-01 to 2002-03 and 2006-07 to 2007-08, in southern Tasmania, southern
  Victoria, Marlborough, Hawke's Bay and Auckland, Sauvignon Blanc in 28 (Table 1, l.
  57-71); 21 major (3 % or more) and 23 minor epidemics (l. 126); latent infection at PBC
  by the ONFIT assay (frozen, surface-sterilised berries incubated 6-12 d) and colonised
  bunch trash (l. 91-97).
- **Results:** the accumulated index correlated with severity at r 0.46 (early), 0.26
  (mid) and 0.54 (late); the mean index per wet period 0.33, 0.22, 0.44; the threshold-1
  sum not at all (Table 2, l. 105-111, 130-132); rainfall "a poor predictor" (l. 303).
  Major epidemics had a longer late interval (50.5 against 39.3 d, P < 0.001) and lower
  maximum temperatures in every interval (l. 157-189). Linear fits of severity on the
  index over five regional means: early y = 38.3x − 19.0 (R² 0.74), mid R² 0.42, late R²
  0.58, giving an index of 0.57, 0.53 and 0.60 at 3 % severity (Table 4, l. 243-273);
  major epidemics' mean index 0.5-0.7 lies below the model's threshold of 1 (l. 295).
  Latent incidence at PBC averaged 10 % in major and 4 % in minor epidemics, above 10 %
  only in major ones (l. 284-287; a logit fit on log10 incidence, R² 19 %, l. 324-327);
  colonised trash predicted severity in nine New Zealand site-years (R² 0.65, l. 292-294).
- **Inconsistencies:** the text says the index is uncorrelated with the other variables
  (l. 289) after saying rain variables correlate with it (l. 180); Figure 5's axis and
  fit disagree (l. 324); the regressions use five regional means, not the 44 site-years.

## Dependence

- **Computes** the Bacchus model through HortPlus MetWatch (a shared implementation of
  `kim2007.bacchus`) and regresses observed severity on its output: a validation, not a
  fit of the model's constants, though the paper calls it a calibration (l. 296-297).
- **Data** observed in the project's unsprayed plots; the ONFIT and trash assays are
  observations too.
- **Authors:** Beresford and Hill wrote `hill2019` and `henshall2015`: flags.

## Bearing (2026-10-13)

- For the engine's Botrytis piece: its own developers found the infection-period
  threshold of 1 useless for season severity and the mean index at 0.5-0.7 in bad years,
  which `hill2019` later recast. For a truth: 44 site-years of unsprayed severity by
  region and the latent-infection fractions, usable as patterns, with the caveat that
  the regressions are on five means.

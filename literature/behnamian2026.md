---
id: behnamian2026
citation: Behnamian, Sara & Fogh, Fatemeh. 2026. Fixed pre-season weather windows eliminate endogeneity bias in interval-censored survival models of grapevine phenology. Discover Data 4:18
doi: 10.1007/s44248-026-00118-x
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [USA]
processes: [phenology, flowering, ripening, survival analysis]
records: []
datasets: []
files: [2026-behnamian-10-1007-s44248-026-00118-x.pdf]
---

# Behnamian & Fogh 2026: survival models of grapevine flowering and ripening

A time-to-event form: accelerated failure time models (Weibull, log-logistic) of the day a
USA National Phenology Network observer first saw open flowers or ripe fruit, on heat
accumulated in a fixed pre-season window. The paper's point is statistical (windows that
close before the event avoid endogeneity); the data are seven unnamed vines.

## What it holds

- **Data:** 41,274 status records on 7 plants at 5 sites, 2012-2025 (l. 36, 226-228),
  collapsing to 50 plant-site-year units with 30 flowering and 37 ripening events
  (l. 37-38); only one plant has a cultivar name (the ornamental 'Purpurea'), two are
  flagged wild, 36 of the 50 units come from three vines at one site (l. 231-238).
  Weather from NASA POWER, no gap filling (l. 360-367); GDD base 10 °C (l. 369).
- **Model:** log T = μ + xᵀβ + σW, W extreme-value or logistic (l. 554-559), x the
  pre-season GDD over days 1-120 (flowering) or 1-180 (ripening) (l. 33). Printed as
  time ratios per unit of pre-season GDD: flowering 0.94 (Weibull) and 0.92
  (log-logistic), both with intervals crossing 1; ripening 0.864 (0.813-0.917, Weibull)
  and 0.962 (0.919-1.007, log-logistic), the latter the chosen primary model (l. 842,
  1054-1057). The log-scale coefficients are not printed (l. 572).
- **Simulation:** 1,000 runs with a true ratio of 0.85: an exogenous window recovers
  0.851, an endogenous one 1.237 (l. 664, 990-993).
- **Inconsistencies:** the ripening Weibull median (212.0) does not match Turnbull's
  (204.1) within a day as claimed (l. 874-895, 1274); the UniChill citation points to
  Chuine et al. 2004 (l. 106). Data restricted; code on GitHub and Zenodo (l. 1424-1428).

## Dependence

- **Cites** BRIN (`cortazar2009.brin`) and Camargo-Alvarez et al. for thermal ranges;
  computes none. Its own 2025 preprint (behnamian2025) is the earlier version.

## Bearing (2026-10-13)

- The form is the one Chris listed (time-to-event), but the predictor is still a heat
  sum, and the data are too thin and unnamed to carry a parameter: a method reference
  only. The endogeneity argument matters for any regression on windows that end after
  the stage, Fraga's and Didevarasl's included.

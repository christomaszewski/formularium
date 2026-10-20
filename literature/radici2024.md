---
id: radici2024
citation: Radici, A., Martinetti, D., Vanalli, C., Cunniffe, N. J. & Bevacqua, D. 2024. A metapopulation framework integrating landscape heterogeneity to model an airborne plant pathogen: the case of brown rot of peach in France. Agriculture, Ecosystems & Environment (the copy read is a manuscript without journal details)
doi: 10.1016/j.agee.2024.108994
read: 2026-10-20, LIGHT, a manuscript copy, by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [brown rot]
crops: [peach]
regions: [France]
processes: [metapopulation, airborne transport, landscape spread, regional loss]
records: []
datasets: []
files: [radici_2024.pdf (the 2026-10-20 drop)]
---

# Radici et al. 2024: brown rot spread among French peach orchards by modelled wind trajectories

755 units of about 8 × 8 km, each an epidemic model, linked by daily airborne transport
along HYSPLIT trajectories (2008-2019), fitted by approximate Bayesian computation to
regional reports of strong and weak losses, 2001-2020.

## What it holds

- Model: 755 units (about 8 x 8 km2); in-unit SEI adapted from Bevacqua et al. 2023 with a
  mummy class M (file l. 229, Eq 1-2 at l. 246-265).
- Harvest timing (t0, tf) from Vanalli et al. 2021 (file l. 227). Losses are read at
  harvest, so a model dates the comparison.
- Inoculum: P~o = 0.2 fixed (l. 336); E(t0) = 0.27 per m2 (l. 326); S(t0)+E(t0) = 15 per m2
  (l. 204).
- Airborne transport: HYSPLIT trajectories from each unit centroid, 1 m above ground, 4 a
  day in daylight, 6-hour travel, 2008 to 2019 (l. 389-395). Daily inoculation P_e = 1 -
  exp(-R dt), dt = 1 day (Eq 6-7, l. 360-374).
- Loss L = 1 - S_tf/S*_tf (l. 430); 'strong' if L > theta_L (Eq 9, l. 440).
- ABC: kappa above 0.475 accepted, epsilon = 0.525 (l. 466). 7 to 67 accepted sets (average
  29) of 200,000 (l. 538).
- Estimates: theta_E 1.8e-6 (l. 562); theta_O 1.0e-2 (l. 564); theta_L 30.3% (l. 558).
- Fit: kappa 0.41 and correct classification 71.8% overall (l. 574-575); 79.7% weak, 61.1%
  strong; (l. 594).
- Null test: wind-driven transport beats the isotropic kernel, p < 5e-6 (l. 600).
- Data: 2001 to 2020, 50,000 km2 (l. 55); sources listed at l. 416-420; public at
  data.gouv.fr (l. 1161); code on Dryad (l. 927).
- Kernel: no kernel form or parameter for orchard-to-orchard spread is printed; the null is
  isotropic (l. 480).

## Dependence

- The in-unit model adapts Bevacqua et al. 2023 and harvest timing comes from Vanalli et al.
  2021 (a model dates the loss); transport from HYSPLIT.

## Bearing (2026-10-20)

- For spread at regional or cooperative scale (t6): a published way to link field-level
  epidemics by modelled wind trajectories instead of a fixed kernel, and wind-driven
  transport beat an isotropic kernel (p < 5e-6); classification 72 % correct. Peach, 8 km
  units: a method, not parameters for vineyards.

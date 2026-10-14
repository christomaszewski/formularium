---
id: vrignonbrenas2022
citation: Vrignon-Brenas, S., Fontez, B., Bisson, A., Rolland, G., Chopard, J., Fumey, D., Metay, A. & Pellegrino, A. 2022. Quantification of the pluriannual dynamics of grapevine growth responses to nitrogen supply using a Bayesian approach. Journal of Experimental Botany 73(5):1385-1401
doi: 10.1093/jxb/erab469
read: 2026-10-14, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Table 4 (p. 10, l. 825-836) read in the text by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [leaf area, growth, nitrogen, radiation use]
records: [vrignonbrenas2022.leaf_area_ramp]
datasets: [vrignonbrenas2022.montpellier_pots]
files: [sylvain_2021.pdf]
---

# Vrignon-Brenas et al. 2022: leaf area of potted vines as a ramp of thermal time

Potted Sauvignon blanc vines given 0 to 8.61 g of nitrogen a plant, followed for up to
three years. Leaf area per plant is fitted as a piecewise-linear function of thermal time
after budburst, with the slope and the time to the plateau shifted by leaf SPAD and by
stored carbohydrate. Dry matter per MJ of radiation is a plane on SPAD and leaf area.

## What it holds

- **Design** (l. 129-148): Sauvignon blanc on SO4 in pots, outdoors at Montpellier-SupAgro;
  five experiments on three batches, 2017-2019; 110 to 150 plants; nitrogen supply from
  budburst to veraison 0 to 8.61 g a plant; SPAD 11.8-41.6. Stages are BBCH 09, 61 and 81
  on 50 % of plants (l. 176). Data on request only (l. 1074).
- **Leaf area model** (Eqs 2-3, p. 6; l. 591-634): flat to 150 °Cd after budburst (about
  10 unfolded leaves, l. 596-597, fixed), then a straight rise at slope b to a plateau
  reached at TTLAmax. Prior for the plateau time 1400 °Cd (l. 595).
- **Table 4 (p. 10, l. 829-834), posterior mean ± SD:** slope intercept 53.44 ± 3.21
  cm²/°Cd; SPAD effect on slope 1.86 ± 0.27 cm²/°Cd per unit; storage effect on slope
  -7.49 ± 1.45 cm²/°Cd per g; plateau time intercept 1335.35 ± 20.49 °Cd; SPAD effect
  12.47 ± 4.65 °Cd per unit (the text says 12.45, l. 781); storage effect -34.88 ± 3.72
  °Cd per g.
- **Ranges** (l. 787-798): slope 1.2 to 16.4 × 10⁻⁴ m²/°Cd across treatments; duration of
  leaf growth 936 to 1160 °Cd; plateau leaf area 0.17 to 1.68 m² a plant.
- **Dry matter per MJ** (Eq. 4, l. 871-872): -6.35e-3 + 6.21e-4 SPAD + 5.29e-2 leaf area
  (m²), R² 0.88; about 0.05 g/MJ per m² of leaf (l. 795).
- **Table 2 thermal times** (l. 345-353): budburst to flowering 326, 336 and 272 °Cd and
  flowering to veraison 728, 779 and 811 °Cd in 2017, 2018 and 2019; veraison to harvest
  589, 715 and 550 °Cd. 2019 had a cold spring (l. 958).
- **Not settled:** the thermal-time base and formula are not printed. Eq. 1, the leaf
  allometry from leaf length (cm², mm; fitted in Exp. 1.1, l. 217, 224), has an unprinted
  sign between its terms.
- **Not printed:** calendar dates of stages, leaf area of a vine in a vineyard, canopy
  height, width and porosity, per-date leaf area errors.

## Dependence

- **None on another model.** The model is the authors' own, with priors from earlier
  studies: the 1400 °Cd plateau from Valdés-Gómez et al. 2009 and Zufferey et al. 2012
  (l. 874-875), the 150 °Cd onset from Munitz et al. 2016 (l. 877-878). Bindi et al. 1997 is
  cited only as a crop model with similar carbon dynamics (l. 113, 997). No model shaped
  the data.

## Bearing (2026-10-14)

- **Growth on thermal time, kin to the engine by form:** leaf area is a ramp in thermal
  time after budburst with a plateau near 1,335 °Cd, the engine's form of a degree-day
  piece. A kin report lists it with them. Said so, not hidden.
- **What the truth lacks:** its leaf curve is a logistic in days. This paper gives an
  onset, slope and plateau in thermal time, usable if the base were known. Potted vines,
  outdoors, one cultivar, so the plateau areas (0.17-1.68 m²) are not a field vine's.

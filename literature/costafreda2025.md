---
id: costafreda2025
citation: Costafreda-Aumedes, Sergi, Leolini, Luisa, Menz, Christoph, Yang, Chenyao, Argenti, Giovanni, Dibari, Camilla, Bindi, Marco, Fraga, Helder, Santos, João A., Molitor, Daniel & Moriondo, Marco. 2025. Uncertainties in predicting the medium-term future occurrence of grapevine budburst in Europe: the role of phenological models and climate scenarios. OENO One 59(2)
doi: 10.20870/oeno-one.2025.59.2.8056
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Europe]
processes: [phenology, budburst, climate projection, uncertainty]
records: []
datasets: []
files: [2025-costafreda-aumedes-10-20870-oeno-one-2025-59-2-8056.pdf]
---

# Costafreda-Aumedes et al. 2025: where budburst projections' uncertainty comes from

Leolini et al. 2020's six models and eight varieties run over about 57,000 EURO-CORDEX
grid points for 1976-2005 and 2026-2055, with an analysis of variance splitting the
spread between phenological model, climate model and scenario.

## What it holds

- **Setup:** the calibrations from Leolini et al. 2020 (l. 302-303; Table 1 lists the
  French, Luxembourg and Portuguese observations, 1951-2018), bounds ±30 % on literature
  parameters, GDD base 0-10 °C, WANG 0 and 45 °C, starts 1 January (forcing) and 1
  September (chilling-forcing) (l. 314-322); outliers 4.8 % (l. 336); 60/40 splits in
  PMP (l. 337-341). Climate: 60 CORDEX-EUR11 runs at 12.5 km, 25 historical and 35
  future (RCP2.6 and RCP4.5), bias-adjusted to E-OBS by ISIMIP3BASD (l. 141-169).
- **Result:** in the baseline the phenological model explains 94.7 % of the total sum
  of squares (97.3 % for Cabernet Sauvignon, Grenache and the Tourigas), the GCM 2.6 %
  (l. 421-428); in the near future the GCM term passes 40 % for Chardonnay,
  Gewürztraminer, Pinot Gris and Riesling, about 40 % in Central Europe (l. 65,
  749-751). 13.8 % of grid points excluded in the baseline, mostly where
  chilling-forcing models failed to complete (l. 391-393).
- Fixed start dates stand in for endodormancy observations that are not available
  (l. 726-728).

## Dependence

- **Computes** Leolini et al. 2020's calibrations (`leolini2020`); fits nothing new.

## Bearing (2026-10-13)

- The point for Agrarium is the ratio: the choice of phenology model dominates the
  climate model's spread by far in the present and still matches it mid-century.

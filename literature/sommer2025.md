---
id: sommer2025
citation: Sommer, S., Ebersole, S. C. & Van Zyl, S. 2025. The Grape Health Index: Validation of a Chemometric Model for Quantifying the Wine Grape Infection Status. Beverages 11:156
doi: 10.3390/beverages11060156
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [sour rot, grey mould]
crops: [wine grape]
regions: [California]
processes: [FT-MIR spectroscopy, chemometric model, microbial spoilage index, grape health index]
records: []
datasets: []
files: [sommer_2025.pdf (the 2026-10-20 drop)]
---

# Sommer et al. 2025: an infrared index for microbial spoilage of wine grapes

Grapes with 0 to 20 % infected berries were blended and scored by mid-infrared spectra, and the
spoilage level was predicted from a calibration model. The chosen model has an RMSE of 4.6
percentage points, but the authors' own RPD of 1.04 is too low for screening (l. 298-302). The
index is a post-harvest measure, not a vineyard one.

## What it holds

- **Samples** (l. 133-141): grapes of five cultivars from California, harvested in 2019 and 2020.
  Healthy and infected clusters were blended at 0, 5, 10, 15 and 20 % infection.
- **Calibration** (Table 2, l. 264-274): 11 models on n = 48. Model 4, chosen for its pH term, has
  R2 0.620, SD 4.800 and RMSE 4.596 (l. 267). Model 1 has R2 0.512 and RMSE 5.436 (l. 264).
- **Check** (l. 298, 393-396): RPD 1.04 for model 4 (l. 298). The authors say that new samples
  are needed before the RMSE can be trusted (l. 395-396). All figures are on the same 48 samples,
  so the title's "validation" is internal.
- **Index** (l. 337-347, 363-376): the score maps percent spoilage onto thresholds, and the
  formula can be added to the FOSS WineScan interface (l. 346-347).

## Dependence

- Uses the pre-validated FOSS WineScan calibrations as supplied (l. 160, 385).
- The explanatory variables come from previous literature, in the order of Table 1 (l. 256-259).

## Bearing (2026-10-20)

- Strand t4 (other grape diseases). A decision engine could read a spoilage score at harvest,
  but the index has no external check yet (l. 395-396) and an RPD of 1.04 is too low to act on.
- Post-harvest, lab-style measure on blended grapes. Not read in full.

---
id: knauer2017
citation: Knauer, U., Matros, A., Petrovic, T., Zanker, T., Scott, E. S. & Seiffert, U. 2017. Improved classification accuracy of powdery mildew infection levels of wine grapes by spatial-spectral analysis of hyperspectral images. Journal, volume and pages not printed in the text layer; accepted 2017-06-07 (l. 15). Author order from the contributor list (l. 154-159)
doi:
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [South Australia]
processes: [hyperspectral imaging, spatial-spectral classification, random forest, linear discriminant analysis, infection levels, image segmentation]
records: []
datasets: []
files: [knauer_2017.pdf (the 2026-10-20 drop)]
---

# Knauer et al. 2017: hyperspectral classes of powdery mildew on Chardonnay bunches

A hyperspectral method that adds spatial texture to spectral features. It classes bunches as
healthy, infected or severely diseased, with accuracy 0.87 on 30 intact bunches (l. 11). The
accuracy near 1.0 is on detached berries, used for training.

## What it holds

- **Data** (l. 37, 86-88): Chardonnay bunches from a non-commercial vineyard at the University of
  Adelaide's Waite Campus. 60 hyperspectral images of 30 bunches (two sides each). Detached
  berries: 128 healthy and 136 severely diseased (l. 88). Visual classes agreed with qPCR of
  E. necator biomass for 75 % of bunches (l. 86).
- **Berry accuracy, cross-validated** (l. 83, 99-106): LDA reduction with spatial features gives
  0.998 ± 0.003 in the VNIR and 0.998 ± 0.005 in the SWIR. Pixel-wise normalised spectra give
  0.980 (VNIR) and 0.853 (SWIR).
- **Block size** (l. 114): VNIR accuracy rises from 0.782 at block size 1 to 0.998 at block size 100.
- **Intact bunches** (l. 11, 134): a random forest of 50 trees. The spatial method improves most at
  light infection (l. 13).
- **Scope** (l. 136-137): one vineyard, one cultivar, one stage (E-L 30-33), and no machine-harvested
  fruit.

## Dependence

- Uses integral-image texture features (refs 13 and 38; l. 75-79) and random-forest classifiers
  (ref 25; l. 26). LDA is the reduction method (l. 34). The authors say a fast segmentation approach
  was adapted (l. 140) without naming its source in that sentence.

## Bearing (2026-10-20)

- Strand t2 (observation). A bunch-level sensing step could report infection class. The accuracy is
  one vineyard and one stage, so it is not a field figure for growers (l. 136).
- Not read in full.

---
id: perezroncal2020
citation: Pérez-Roncal, C., López-Maestresalas, A., Lopez-Molina, C., Jarén, C., Urrestarazu, J., Santesteban, L. G. & Arazuri, S. 2020. Hyperspectral imaging to assess the presence of powdery mildew (Erysiphe necator) in cv. Carignan Noir grapevine bunches. Agronomy 10:88
doi: 10.3390/agronomy10010088
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Navarre, Spain]
processes: [hyperspectral imaging, bunch-level detection, PLS-DA classification, pixel mapping]
records: []
datasets: []
files: [perezroncal_2020.pdf (the 2026-10-20 drop)]
---

# Pérez-Roncal et al. 2020: hyperspectral imaging of powdery mildew on bunches

Thirty Carignan Noir bunches, half of them visibly infected, were imaged in the near-infrared. A PLS-DA model separated healthy from infected pixels at 85.33% cross-validated accuracy.

## What it holds

- Thirty bunches from one vineyard in the Ebro valley (Navarre). Fifteen were healthy and fifteen infected, chosen by eye in the field (l. 102-115).
- Pushbroom near-infrared camera, 900 to 1700 nm, 256 bands (l. 28, l. 130).
- Best model (smoothing, SNV and mean-centring pre-processing) gave 85.33% accuracy in cross-validation (l. 33; Table 1, l. 405). Healthy pixels were 82.67% correct and infected pixels 88% (l. 405).
- External validation: 85.70% of healthy pixels and 68.34% of infected pixels correct, over five bunches per class (l. 432-434).
- The paper suggests a bunch is "sick" when more than 20% of its pixels are called infected (l. 442-443).

## Dependence

- None recorded.

## Bearing (2026-10-20)

- Strand t2 (observation). This is a detection tool for the bunch, not a severity scale. The reference classes come from a visual call in the field (l. 113-115), and the paper does not test rater error.
- The 20% pixel share (l. 442-443) is a candidate scouting or winery-intake rule. It rests on 30 bunches, one vineyard and one sampling date. Not read in full.

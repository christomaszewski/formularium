---
id: hernandez2024b
citation: Hernández, I., Gutiérrez, S. & Tardaguila, J. 2024. Image analysis with deep learning for early detection of downy mildew in grapevine. Scientia Horticulturae 331:113155
doi: 10.1016/j.scienta.2024.113155
read: 2026-10-20, LIGHT, by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [La Rioja]
processes: [image detection, early detection, deep learning]
records: []
datasets: []
files: [hernandez_2024.pdf (the 2026-10-20 drop)]
---

# Hernández et al. 2024b: how early a camera finds downy mildew on leaf discs

Convolutional networks on RGB and HLS images of Tempranillo leaf discs inoculated with
Plasmopara viticola and imaged 3 to 9 days after inoculation.

## What it holds

- Deep learning (CNN) on RGB, HLS and mask images of Tempranillo leaf discs inoculated with
  Plasmopara viticola, imaged 3 to 9 days after inoculation (l. 36).
- 50 plants; 131 Petri dishes; 1125 discs, 529 positive (Table 1, l. 129, 130).
- Early detection, 10-fold CV at DPI 4: RGB 97%, HLS 98% (Table 2, l. 279, 280).
- Model trained on DPI 4, tested on other days (Table 3): DPI 3 47% to 53% (l. 303–306); DPI
  4 93% to 100% (l. 309–311); DPI 7 to 9 about 97% to 100% (l. 314–326).
- First day with reliable detection: DPI 4, the first visible symptoms (l. 196); DPI 3 gave
  no detection (l. 280).
- Infection stage (DPI 4, 7, 8, 9): RGB 81% accuracy, F1 0.77; HLS 77% (Table 4, l. 362,
  368). Per-day recall for RGB: DPI 4 99%, DPI 7 85%, DPI 8 62%, DPI 9 63% (l. 361, 363,
  364).
- Abstract's 99% after DPI 3 is not supported by Table 3 (l. 40).
- Fixed thresholds in pre-processing: Canny 100 (l. 146) and saturation 92 to 104 (l. 157);
  no degree-day or weather input.
- No data availability statement found; the dataset is partly from Hernández et al. (2022).

## Dependence

- Its own inoculations and images; part of the data set is Hernández et al. 2022's. No
  engine author.

## Bearing (2026-10-20)

- For Agrarium's camera operator (PLAN 7, 'no detection-by-stage figure was found'): in the
  laboratory a network detected nothing at 3 days after inoculation (47-53 %, chance) and
  93-100 % from day 4, when symptoms first show; it cannot see a latent infection. Leaf
  discs under controlled light, not a vine row.
- The abstract's '99 % after 3 days' is not what Table 3 shows.

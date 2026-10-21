---
id: delmoralmartinez2016
citation: Del-Moral-Martínez, I., Rosell-Polo, J. R., Company, J., Sanz, R., Escolà, A., Masip, J., Martínez-Casasnovas, J. A. & Arnó, J. 2016. Mapping Vineyard Leaf Area Using Mobile Terrestrial Laser Scanners: Should Rows be Scanned On-the-Go or Discontinuously Sampled? Sensors 16(1):119
doi: 10.3390/s16010119
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); 2026-10-20 (vine-leaf-area search), in full by a reading agent (claude-haiku-5-5) with Figures 1, 5, 6 and 8 and Eq. 1 in the page images, 41 of 41 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Catalonia, Raimat]
processes: [leaf area index, mobile terrestrial laser scanning, LiDAR, sampling design, kriging, management zones]
records: []
datasets: []
files: [delmoralmartinez_2016.pdf (the 2026-10-20 drop)]
---

# Del-Moral-Martínez et al. 2016: leaf area from a tractor-mounted laser scanner

A tractor-mounted laser scanner maps leaf area index (LAI) in a Syrah vineyard at Raimat,
Catalonia, on the go or at sampled sections. No disease is studied.

## What it holds

- **Field** (l. 150-175): Syrah planted 2002, six N-S rows of 360 m, about 0.70 ha; VSP;
  partial root-zone drying (volume not printed); scanned at BBCH 79. The trial year, row
  spacing and shoots are not printed; vines are 2 m apart by the validation block, "the
  distance between two consecutive trunks" (l. 701-716).
- **LAI** (Eq. 1, l. 609-613, read in the page image): both leaf walls plus the top area
  from the scan, times C = 1.70 (from an unpublished report), over row spacing times 1 m.
- **Ground truth** (l. 749-776; Figure 6 read off the page image, approximate): three 2 m
  blocks defoliated by hand: measured LAI about 0.6, 1.3 and 2.05 against scanned about
  1.35, 1.5 and 1.98. Errors 4 to 16 % for intermediate and high vigour, high for low vigour
  (l. 789-791).
- **The plot** (l. 969, 997; Figure 8 legend, approximate): LAI about 0.7 to 2.1, CV 24 %.
- **Sampling** (Table 1, l. 1262-1273): on the go gives 2,146 one-metre points (about 2 h
  and 1 GB a hectare, l. 1081-1094). Two-class kappa 0.95 at 1 m, 0.90 at 15 m; three-class
  0.91 and 0.75. Sections 1 m long no more than 15 m apart suffice (l. 1290).

## Dependence

- The scanner and LAI method are the group's 2015 paper (ref 8): a substantive borrowing.
  C = 1.70 is from an unpublished report, not checkable. Kriging in VESPER, zones by fuzzy
  c-means. Shared authors alone are a flag.

## Bearing (2026-10-20)

- Strand t1 (fungicide protection), indirectly: LAI maps can set variable-rate doses (l. 47).
- **Leaf area (vine-leaf-area search):** a VSP Syrah at Raimat (inland Lleida, PRD) ran LAI
  about 0.6 to 2.1 at BBCH 79 by hand, CV 24 % across 0.7 ha: a measured spread for the
  vigour field. Row spacing is not printed, so no leaf area per vine.

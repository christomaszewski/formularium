---
id: debei2016
citation: De Bei, R., Fuentes, S., Gilliham, M., Tyerman, S., Edwards, E., Bianchini, N., Smith, J. & Collins, C. 2016. VitiCanopy: A Free Computer App to Estimate Canopy Vigor and Porosity for Grapevine. Sensors 16(4):585
doi: 10.3390/s16040585
read: 2026-10-14, a LIGHT reading by a reading agent (claude-haiku-5-5), Sections 2.1-4.5 from the text layer with Eqs 1-6 and Tables 1-4 read in the page images (Table 4 at 80 dpi); 58 of 58 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [South Australia]
processes: [canopy porosity, leaf area index, cover photography]
records: []
datasets: []
files: [roberta_2016.pdf]
---

# De Bei et al. 2016: VitiCanopy, LAI and porosity from one photograph

A phone and tablet app that turns one upward photograph of a canopy into gap fraction,
porosity and leaf area index. It is a measurement method with no time variable.

## What it holds

- **Method** (l. 105-106, 274-301; Eqs 1-6 read from the page images): large-gap pixels lg,
  gap pixels tg and total pixels tp give the gap fractions (Eqs 1-3); the image is split
  into 25 sub-images (5 × 5) for large gaps (l. 300-301). LAI-vc = −fc ln(phi)/k, Beer's
  law (Eq 4, l. 279), with k the light extinction coefficient, set to 0.7 by default
  (l. 284, 371). The clumping index Ω(0) (Eq 5, l. 285; no source printed) corrects it:
  LAI-vce = LAI-vc × Ω(0) (Eq 6, l. 291). Ω = 1 is random and 0 < Ω < 1 clumped (l. 296).
  Real k is inverted from ground truth, kr = −ln(phi)/(fc × LAIr) (Eq 7).
- **Against the Matlab method** (l. 408, 507, 509, 1270): 113 images, R² 0.97, slope
  0.98; Ω mean 0.78, range 0.61 to 1; Matlab 3 % lower on six images.
- **Against LAI-2000** (l. 429, 782): 86 pairs in three Shiraz vineyards, 2013-14, R² 0.95,
  slope 1.08, SEE 0.51. Table 2 season averages of LAI-vc: Hilltops 0.99 (0.72 to 1.44,
  l. 754), Langhorne Creek 2.37 (1.93 to 2.71, l. 763), Sunraysia 1.30 (1.16 to 1.39,
  l. 771). Ω from 0.76 to 0.98 across the three (l. 591). LAI-vc against LAI-vce R² 0.96,
  slope 0.25 (l. 625).
- **Against planimetric and gravimetric LAI** (l. 433-469, 914-918, 968-1004): 12 Shiraz
  vines at McLaren Vale, stripped in three steps of about 30 % at five camera distances
  from the cordon (50 to 90 cm); specific leaf area 216 cm²/g. R² by distance (Table 3):
  0.76 (50 cm), 0.89 (70 and 80 cm; slope 1.06 at 80 cm), 0.70 (90 cm). The best distance
  is 70 to 80 cm (l. 1306). Before correction R² 0.84, slope 1.06, Ω 0.65 to 1; the bare
  cordons add 0.56 of LAI (l. 971, 1328); after the correction R² 0.86, slope 1.05, SEE 1.89,
  RMSE 0.24 (l. 1004). Validation images were taken at flowering (l. 1335).
- **Table 4, k methods against the ground truth** (l. 1087-1129): real k R² 0.94, slope
  0.98, SEE 0.71, RMSE 0.15; Lowess proxy R² 0.87; big-gap proxy R² 0.83, slope 0.99; luminance ratio
  (Io = 12, no unit printed) R² 0.86, slope 0.99, SEE 2.04, RMSE 0.24.
- **Unsettled:** the big-gap method's SEE and RMSE are 2.13 and 0.25 in the text (l. 1100)
  and read 2.04 and 0.24 in the table image, which are the luminance figures; the Table 4
  cells hold two unlabelled entries, read as k comparison then LAI comparison from the
  caption; Table 3 at 70 cm prints SEE 0.65 above RMSE 0.30; the distance optimum is cited
  to Table 2 but sits in Table 3 (l. 1307); "R22" at l. 625.
- **Not printed:** any seasonal series of LAI or porosity (one season in Table 2), sampling
  dates, the coefficients of the big-gap regression, the luminance formula.

## Dependence

- **Shared algorithm:** VitiCanopy "is based on" cover photography and the Matlab method of
  Fuentes et al. 2014 (l. 105-107); the tests against Matlab use the same algorithm
  (l. 1259-1267); k = 0.7 and the 5 × 5 split come from the same line of papers (l. 301,
  371-372). Fuentes is an author of both. The shared algorithm is substantive.
- **Other sources:** Beer's law and definitions (refs 14, 15, 28); the luminance idea is
  Poblete-Echeverría et al.'s, for apple, and Io = 12 is this paper's own choice. No
  calibration of k is stated.

## Bearing (2026-10-14)

- **A measurement method, not a model in time:** one photograph gives one LAI and one
  porosity. No seasonal series, nothing to run in the truth. No record.
- **Use:** it defines porosity and effective LAI the way a canopy piece of the truth could
  be checked, with a stated bias for the cordon and for non-leaf material (a 3 % overestimate
  early, none after veraison, l. 1322).

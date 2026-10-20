---
id: delmoralmartinez2016
citation: Del-Moral-Martínez, I., Rosell-Polo, J. R., Company, J., Sanz, R., Escolà, A., Masip, J., Martínez-Casasnovas, J. A. & Arnó, J. 2016. Mapping Vineyard Leaf Area Using Mobile Terrestrial Laser Scanners: Should Rows be Scanned On-the-Go or Discontinuously Sampled? Journal, volume and pages not printed in the text layer. Byline not printed; authors from the contributions statement (l. 78); year from the batch key only
doi:
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: [grapevine]
regions: [Catalonia]
processes: [leaf area index, mobile terrestrial laser scanning, LiDAR, sampling design, kriging, management zones]
records: []
datasets: []
files: [delmoralmartinez_2016.pdf (the 2026-10-20 drop)]
---

# Del-Moral-Martínez et al. 2016: leaf area from a tractor-mounted laser scanner

A tractor-mounted laser scanner maps leaf area index (LAI) in a Syrah vineyard at Raimat,
Catalonia. Scanning every row on the go gives 2,146 points. Scanning only every few metres
keeps two-class agreement between 0.73 and 0.95 up to 25 m (l. 62-70). No disease is studied.

## What it holds

- **Field** (l. 16-18): six rows of cv. Syrah planted in 2002, 360 m long, with contrasting vigour.
- **Accuracy** (l. 38-39): LAI estimates within 4 % to 16 % for intermediate and high vigour. Error
  was high for low vigour, which the authors put down to a scan every 7 cm.
- **Cost of on-the-go scanning** (l. 50-51): 2,146 points, about 2 h and about 1 GB per hectare.
  Separating sections by the scanned length halves the data (l. 54).
- **Sparser sampling** (Table 1, l. 62-70): three-class vigour maps agree with the full scan at
  kappa 0.91 for 1 m spacing, 0.80 for 10 m and 0.56 for 20 m (l. 62, 66, 69).
- **Variability** (l. 44): LAI coefficient of variation 24 % in a 0.70 ha area, with compact zones.

## Dependence

- The scanner is described in an earlier paper by the same group (ref 8, Sensors 2015; l. 20, 89).
  That is a substantive borrowing. Shared authors alone are a flag, not a dependency.
- Interpolation uses ordinary kriging in VESPER (ref 34) and fuzzy c-means in Management Zone
  Analyst (ref 35; l. 41-42).

## Bearing (2026-10-20)

- Strand t1 (fungicide protection), indirectly: the paper says LAI maps can set variable-rate
  pesticide doses (l. 47). A spray-dose term could use sparse scans rather than every row.
- Off the disease point: this is vigour, not disease. Not read in full.

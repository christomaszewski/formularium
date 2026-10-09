---
id: madden2018
citation: Madden, L. V., Hughes, G., Moraes, W. Bucker, Xu, X.-M. & Turechek, W. W. 2018. Twenty-Five Years of the Binary Power Law for Characterizing Heterogeneity of Disease Incidence. Phytopathology 108(6):656-680
doi: 10.1094/PHYTO-07-17-0234-RVW
read: 2026-10-08, in full (equations garbled; the supplement is a separate file), by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [global]
processes: [sampling, spatial heterogeneity, observation]
records: []
datasets: []
files: [10-1094-phyto-07-17-0234-rvw.pdf]
---

# Madden et al. 2018: twenty-five years of the binary power law

From Ohio State and partners. A review.

## What it holds

- Review of the binary power law (BPL), proposed in 1992 (l. 22). It collects 230 usable fits from at least 74 publications (l. 620, 406). No new field data.
- Slope b ranged 0.87 to 2.00, mean 1.24, median 1.19 (l. 637, 638). 80% of field values lay between 1.06 and 1.51 (l. 30). CV of b was 16% (l. 595).
- Median fit R2 was 0.97 (l. 646). Sampling-unit size n ranged 2 to 458, median 10 (l. 649, 584).
- Hop rows (Table 1): Turechek and Mahaffee 2004, n = 10, a 0.15-0.21, b 1.06-1.11 (l. 494); Gent 2007a, n = 10, a 0.20-0.25, b 1.10-1.14 (l. 491); Gent 2006, n = 25, a 0.11-0.35, b 1.16-1.37 (l. 492). The 2007b cone paper has no row.
- Forms: V = Ax[np(1-p)]^b (l. 244); a = Ap n^-b = Ax n^(b-2) (l. 345); N = a p^(b-2) (1-p)^b / C^2 (l. 983).
- A larger sampling unit gives a larger b; b is bounded by geometry, for example 1.49 at n = 15 with crossover p* = 0.001 (l. 820).
- Sampling methods treat a and b as known but work with approximate values (l. 1074). Almost all fits are OLS on logs (l. 1213).
- Several equations are garbled in the text file; do not read coefficients from them.

## Dependence

- No field data of its own: 230 fits from at least 74 publications. Its grape downy mildew rows are Madden et al. 1995's, the data the engine's sampling bound was fitted to (Formularium `madden1995`); the supplementary table (in the drop, `phyto-07-17-0234-rvw.sm1.xlsx`) lists them.
- Madden and Hughes are authors of the engine's sampling bound: flags; the BPL is its form.

## Bearing (2026-10-08)

- Field heterogeneity across about 40 pathosystems (slopes 0.87-2.00, 80% between 1.06 and 1.51): a range for a truth's spatial aggregation. A truth fitted to its Ohio grape rows would share the sampling bound's calibration data (D29).

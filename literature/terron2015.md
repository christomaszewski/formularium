---
id: terron2015
citation: Terrón, J. M., Blanco, J., Moral, F. J., Mancha, L. A., Uriarte, D. & Marques da Silva, J. R. 2015. Evaluation of vineyard growth under four irrigation regimes using vegetation and soil on-the-go sensors. SOIL 1:459-473
doi: 10.5194/soil-1-459-2015
read: 2026-11-05, site description and the variogram table (Table 2), by a reading agent and a note writer; 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain (Extremadura)]
processes: [vigour, spatial variability, variogram, NDVI, soil electrical conductivity, irrigation]
records: []
datasets: []
files: [dr1104_terron2015.pdf (the 2026-11-04 drop)]
---

# Terrón et al. 2015: variograms of vine NDVI and soil conductivity in an irrigated vineyard

A Spanish irrigation trial in a 1.8 ha Tempranillo vineyard that maps vine NDVI and soil apparent electrical conductivity with on-the-go sensors and fits semivariograms.

**Read this first.**
- The tables come from two-column PDF text. The range of 72.0 m repeats on all five 2013 dates (l. 283), which looks fixed by the authors rather than fitted. Use the 2013 ranges with care.
- A variogram range is not a correlation length. The lag size is 6 m for NDVI and 7 m for soil conductivity (Table 2).

## What it holds

- **Site (l. 110):** vineyard of 1.8 ha at Guadajira (Badajoz, Extremadura), Tempranillo on Richter 110, planted 2001, vertical trellis, bilateral cordon; four irrigation regimes.
- **NDVI, 29 May 2012 (Table 2, l. 274):** spherical model, lag 6 m, nugget 0.009, range 36.5 m, partial sill 0.003.
- **NDVI, 24 July 2012 (l. 276):** nugget 0.005, range 31.0 m, partial sill 0.007; nugget share about 42 % (arithmetic: 0.005 / 0.012, not printed).
- **NDVI, 2012 other dates:** ranges 32.7, 28.7 and 33.2 m (lines after l. 274 in Table 2).
- **NDVI, 2 September 2013 (l. 283):** nugget 0.002, range 72.0 m, partial sill 0.002; range 72.0 m on all 2013 dates (possibly fixed, see above).
- **Soil conductivity, 18 February 2011 (l. 285):** deep reading (ECd) spherical, lag 7 m, nugget 0.594, range 67.3 m, partial sill 2.264; the shallow reading (ECs) has range 70.6 m.

## Dependence

- Own field data from the trial; no model computed. None recorded otherwise.

## Bearing (2026-11-05)

- **fields.vigour_length_m (Agrarium):** vine NDVI variogram ranges of 29 to 36.5 m in 2012 and a stated 72 m in 2013 (l. 274, 276, 283), against 67 to 71 m for soil conductivity (l. 285). Field measurement in one irrigated vineyard; a shorter scale than Navarra's pruning weight range of 53 m is not claimed to differ.
- **Soil link:** the soil conductivity range is of similar size to the 2013 NDVI range, a hint that vigour follows soil at that scale; the paper's text on this was not read here.

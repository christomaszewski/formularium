---
id: reycarames2015
citation: Rey-Caramés, C., Diago, M. P., Martín, M. P., Lobo, A. & Tardaguila, J. 2015. Using RPAS Multi-Spectral Imagery to Characterise Vigour, Leaf Development, Yield Components and Berry Composition Variability within a Vineyard. Remote Sensing 7(11):14458-14481
doi: 10.3390/rs71114458
read: 2026-11-05, methods and results (study area, sampling, variability and variogram sections, Table 2), by a reading agent and a note writer; 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain (Navarra)]
processes: [vigour, spatial variability, variogram, NDVI, multispectral imagery, pruning weight, leaf area]
records: []
datasets: []
files: [dr1104_reycarames2015.pdf (the 2026-11-04 drop)]
---

# Rey-Caramés et al. 2015: spatial variability of vine vigour, leaf area and yield in one 3 ha vineyard

A Spanish field study that maps a 3 ha Tempranillo vineyard from drone multispectral imagery and ground measures, and prints each variable's coefficient of variation, nugget share and variogram range.

**Read this first.**
- Table 2's columns are, in order: mean, min., max., SD, CV (%), spread (%), % of nugget, range (m). Ranges are in metres. A variogram range is the distance at which the sill is reached, not a correlation length (l. 404).
- The unit column is garbled for some rows. The "Cluster number/vine" row has a mean of 1.60 with min. 0.39 and max. 3.65 (l. 453); these are values per m2 of canopy, not a count per vine. Do not use them as bunches per vine.
- One vineyard, one season, 72 points on a 20 m grid (l. 130), so the shortest lag is 20 m and ranges below about 40 m are poorly resolved.

## What it holds

- **Site (l. 115):** 3.0 ha Tempranillo vineyard in Navarra, Spain; 72 sampling points at 20 m intervals (l. 130). Planting year 2004 and VSP spur-pruned cordon are printed in the lines after l. 115.
- **Pruning weight (Table 2, l. 437):** mean 0.20 kg/m2, SD 0.05, CV 25.21 %, spread 116.96 %, nugget 70 % of total, range 52.65 m.
- **Main shoot length (Table 2, l. 439):** mean 31.99 cm/m2, SD 4.15, CV 12.98 %, nugget 46 %, range 126.33 m.
- **Main leaf area (Table 2, l. 443):** mean 0.07 m2/m2, SD 0.01, CV 12.87 %, nugget 46 %, range 122.55 m.
- **NDVI (Table 2, l. 431):** mean 0.65, SD 0.06, CV 10.01 %, nugget 29 %, range 111.41 m.
- **Cluster number (Table 2, l. 453):** CV 51.45 %, nugget 62 %, range 80.79 m. Units garbled (see above).
- **Range summary in the text (l. 405):** main leaf area, main shoot length, pH and titratable acidity about 125 m; the G index the highest at 202 m; the lowest, 38 to 65 m, for leaf chlorophyll fluorescence, pruning weight, NVI1, NVI2, berry weight and total phenols.
- **Agreement with earlier work (l. 409):** the pruning weight range agrees with Taylor and Bates for 3-vine aggregation (cited, not read here).

## Dependence

- Own field data and imagery; no model computed. Cites Taylor & Bates (Concord pruning mass) for a comparison range. None recorded otherwise.

## Bearing (2026-11-05)

- **fields.vigour_sd (Agrarium):** measured coefficients of variation in one vineyard: pruning weight 25 %, main leaf area 13 %, shoot length 13 %, NDVI 10 % (l. 437, 443, 439, 431). Field measurement, one site and season.
- **fields.vigour_length_m (Agrarium):** variogram ranges of 53 m (pruning weight) to 126 m (shoot length), with 29 to 70 % nugget (l. 437, 439). Ranges are not correlation lengths, and a 20 m grid cannot resolve shorter structure. Field measurement.

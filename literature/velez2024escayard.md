---
id: velez2024escayard
citation: Vélez, S., Ariza-Sentís, M. & Valente, J. 2024. EscaYard: Precision viticulture multimodal dataset of vineyards affected by Esca disease consisting of geotagged smartphone images, phytosanitary status, UAV 3D point clouds and Orthomosaics. Data in Brief 54:110497
doi: 10.1016/j.dib.2024.110497
read: 2026-10-27, lightly: abstract, specification table and section 3 (data description, Table 1, subsections 3.1-3.4) (Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [esca]
crops: [grapevine]
regions: [Spain, Galicia, Pontevedra, Tomiño]
processes: [dataset, UAV multispectral imaging, structure from motion, point cloud, orthomosaic, RTK GNSS, esca detection, smartphone imaging]
records: []
datasets: [velez2024escayard.tomino]
files: [syn1027_velez2024escayard.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Vélez et al. 2024: EscaYard, 253 geotagged plant photos with an esca yes/no flag, plus UAV orthomosaics and point clouds, one date

A data article for two Galician vineyards on one summer day: smartphone photos of plants, a per-plant datasheet, five-band UAV orthomosaics, structure-from-motion point clouds and RTK trunk positions. No record: a dataset. It is a different paper from Formularium's literature/velez2024 (a separate item).

**Read this first.** One date (2022-07-14, l. 73), so no disease progression, and the esca label is one agronomist's call from leaf "tiger stripes" (l. 98), binary. Cluster counts exist for only 42 plants (l. 96). The point clouds are structure-from-motion products of the multispectral images, one band per file, not LiDAR (l. 115).

## What it holds

- **Where to get it** (l. 21): Zenodo 10.5281/zenodo.10362567. Licence of the article: CC BY (l. 5). The Zenodo record's licence was not read here (the earlier catalogue lists CC BY 4.0). About 8 GB in all, from the file table (l. 45-80, Table 1: the orthomosaics 3.37 GB and 1.52 GB, the photographs 1.49 GB and 453 MB, ten clouds of 125 to 236 MB; arithmetic, not printed).
- **Contents** (l. 44): 253 geotagged smartphone plant images, one datasheet, ten 3D point clouds, two UAV orthomosaics, and RTK GNSS trunk locations (vineyard B7 only, l. 77, 121).
- **Sites** (l. 19): two vineyards, B7 and B9, at Tomiño, Pontevedra, Galicia, Spain.
- **Date and sensor** (l. 17, 73): one UAV flight at 30 m above ground on 2022-07-14 with a multispectral camera; the specification says six spectral bands (l. 17) and the orthomosaics have five (blue, green, red, red edge, NIR; l. 109).
- **Datasheet variables** (l. 90-106): plant position, the matching photo file, number of grape clusters (counted for 42 plants, hidden bunches included, l. 96), an Esca YES or NO flag (l. 98), time of day (midday or evening), vineyard, phone model and coordinates.
- **How labels were made** (l. 98, 96): esca status by one expert agronomist reading leaf symptoms; cluster counts by hand. Observed by a person; no laboratory test.
- **Disease focus** (l. 90): the datasheet records esca because it was the most widespread affliction in the vineyard at the time, so other diseases may be present and unrecorded.

## Dependence

- Point clouds and orthomosaics by Pix4D photogrammetry. Same group and same vineyards as VineLiDAR (velez2023lidar) and a precision-viticulture mapping set (Zenodo 10.5281/zenodo.10362568, from the reading agent's lead, not read), so the three are not independent. None recorded otherwise.

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); not a downy mildew set.** An esca label for a few hundred plants on a single day, with plant positions at centimetre level and multispectral orthomosaics. It could test whether a simulated vineyard's spatial pattern of diseased vines resembles a real one and whether a rendered canopy matches a real multispectral index map; it cannot judge a weather-driven variable.
- **For D58:** no weather, no onset date, no severity; an esca yes/no on one day is a prevalence snapshot, not a time course.
- **Limits:** one date, two vineyards, a binary flag by one expert, 42 cluster counts, no yield beyond that.

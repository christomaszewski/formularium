---
id: velez2023lidar
citation: Vélez, S., Ariza-Sentís, M. & Valente, J. 2023. VineLiDAR: High-resolution UAV-LiDAR vineyard dataset acquired over two years in northern Spain. Data in Brief 51:109686
doi: 10.1016/j.dib.2023.109686
read: 2026-10-27, lightly: abstract, specification table, data description, flight table and file table (Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Galicia, Pontevedra, Tomiño]
processes: [dataset, UAV LiDAR, point cloud, canopy structure, precision viticulture, digital twin]
records: []
datasets: [velez2023lidar.tomino]
files: [syn1027_velez2023vinelidar.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Vélez et al. 2023: VineLiDAR, ten UAV-LiDAR point clouds of two Galician vineyards on three dates

A data article for drone-borne LiDAR point clouds with RGB per point, at three flight heights and three dates in 2021 and 2022. No record: a dataset. It is a different paper from Formularium's literature/velez2023 (a separate item).

**Read this first.** There are no per-vine biological labels, no disease, no weather and no yield: it records shape and size of canopies only (l. 8, 42). The authors propose it as "ground truth" for satellite-derived models or digital-twin development (l. 54), which says what the sensor is, not that the clouds were checked against measurements.

## What it holds

- **Where to get it** (l. 46): Zenodo 10.5281/zenodo.8113105. Licence of the article: CC BY (l. 7). The Zenodo record's licence (CC BY 4.0) is the reading agent's look at the record, not in the paper. Total size is about 2.8 GB (the ten file sizes in Table 2, l. 149-185, add to 2,842 MB; arithmetic, not printed).
- **Content** (l. 8, 69): ten high-density point clouds in .laz format with RGB per point, from two vineyards (B7 and B9) at Tomiño, Pontevedra, Galicia, Spain.
- **Dates and heights** (l. 42, Table 1 l. 69-135): flights on 2021-09-16 (B9 only, 30 and 50 m above ground), 2022-07-14 and 2022-09-08 (both vineyards at 20 and 30 m); the months were chosen to catch vegetative growth (July) and harvest (September) (l. 189). One site, three dates, two years.
- **Sensor** (l. 19): DJI M300 multirotor with a DJI Zenmuse L1 LiDAR, point rate up to 240,000 points per second (single return), RMS ranging accuracy 3 cm at 100 m, RTK positioning, flight speed 4 m/s, side overlap 50 % and frontal overlap 80 %.
- **Size per cloud** (Table 2, l. 149-185): 75.7 MB to 557 MB; for example 71,389,912 points for the 2022-07-14 flight at 20 m over B7 (l. 157-158).
- **Canopy** (l. 193): vertical-shoot-position training with spontaneous cover crops between rows.
- **How labels were made:** none; the clouds are sensor output, georeferenced with RTK. No human or model label is attached.

## Dependence

- None recorded: sensor-derived data. The same group and vineyards as EscaYard (velez2024escayard) and a precision-viticulture mapping set (Zenodo 10.5281/zenodo.10362568, from the reading agent's lead, not read), so the three are not independent.

## Bearing (2026-10-27)

- **D60 tier 4 (research only: a drone LiDAR); a check of rendered vines.** Real 3D canopy geometry at three dates in one vineyard, usable to compare the viewer's vine models (height, width, row spacing, leaf area proxies from point density) with real vines, and to see how a canopy grows between July and September.
- **No role in D58 or D60 for weather or disease:** no outcome and no meteorology. If paired with the EscaYard labels for the same vineyards (esca yes/no, one date), it adds structure but not disease dynamics.
- **Limits:** two vineyards, three dates, no ground measurements in this paper, no season-long time series, and a large download.

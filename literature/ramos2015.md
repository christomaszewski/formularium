---
id: ramos2015
citation: Ramos, M.C. & Martínez-Casasnovas, J.A. 2015. Climate change influence on runoff and soil losses in a rainfed basin with Mediterranean climate. Natural Hazards 78:1065-1089 (accepted manuscript)
doi: 10.1007/s11069-015-1759-x
read: 2026-11-04, keyword-targeted passages (slope, rows, terraces, parcels), by a reading agent and a note writer; 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Catalonia, Penedès, Anoia]
processes: [terrain, slope, rain regime, runoff, erosion, SWAT, climate change]
records: []
datasets: []
files: [dr1104_ramos2015.pdf (the 2026-11-04 drop)]
---

# Ramos & Martínez-Casasnovas 2015: runoff and soil loss in an Anoia vineyard basin under climate change

A SWAT model of a small rainfed vineyard basin in the Penedès DO, run on 2000-2012 weather and on climate-change scenarios.

**Read this first.**
- It is the accepted manuscript. Only the basin description, slope classes and rain statistics were read, not the climate-scenario results.

## What it holds

- **Basin:** area 0.46 km2, slopes from 1 to more than 15 %; vine cultivation is about 62.9 % of the land surface, with vines in the Penedès DO (l. 254, 258).
- **Landscape:** the Penedès-Anoia viticultural region is "quite fragmented and dissected by gullies" (l. 266; cites Martínez-Casasnovas 2003).
- **Model slope classes:** 0-2, 2-5, 5-10, 10-15 and over 15 % (l. 398). The model gives 34 subbasins and HRUs, of 0.1 to 5.5 ha (l. 400 and the next line). An HRU is a soil, slope and land-use unit, not a parcel.
- **Rain regime, 2000-2012:** average annual precipitation about 550 mm, ranging from 329.8 to 751.5 mm, mainly in spring and autumn (l. 611). Rainy days (P over 1 mm) 35 to 68 a year; maximum 24 h rainfall 31.5 to 97.7 mm (l. 617).
- **Runoff:** simulated runoff 16.1 to 126.8 mm a year, 4.4 to 18.8 % of annual rain, about 12 % on average (l. 663).

## Dependence

- Model-based: SWAT driven by the basin's own 2000-2012 records. The climate-scenario outputs are model results, not observations. No engine model is computed here.

## Bearing (2026-11-04)

- **terrain.slope_pct (Agrarium):** one small Anoia vineyard basin spans 1 to over 15 %. It supports a wide slope spread within a short distance, not a regional mean.
- **Rain regime:** annual rain of about 550 mm, with spring and autumn peaks, for the basin the model uses (observed 2000-2012 inputs, as the manuscript states). A check on the Penedès rain regime for weather generators, not a source of daily values.

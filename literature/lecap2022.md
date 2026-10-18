---
id: lecap2022
citation: Le Cap, C., Carlier, J., Quénol, H., Heitz, D. & Buisson, E. 2022. Temperature spatial variability analysis in the aim of enhancing the use or implementation of wind machines park. Research Square preprint rs-1932104/v1 (version of record in Theoretical and Applied Climatology, 2023, not read)
doi: 10.21203/rs.3.rs-1932104/v1
read: 2026-10-18, in full (the preprint, posted 2022-08-10), by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by the main session; Tables 1-6 from the text layer; Fig. 5 maps not rendered
status: read
diseases: []
crops: [grapevine]
regions: [Quincy, Cher, France]
processes: [frost, minimum temperature, sensor network, spatial variability, wind machines]
records: []
datasets: [lecap2022.quincy]
files: [clara_2023.pdf (the 2026-10-18 drop)]
---

# Le Cap et al. 2022: minimum temperature across the Quincy vineyard (preprint)

This is a preprint. The published version (Theoretical and Applied Climatology, 21 September
2023, doi 10.1007/s00704-023-04642-7) was not read, so a number here may differ from it.
The file key says 2023; the paper in hand is the 2022 preprint. No record.

## What it holds

- **Site and network** (l. 178-200): the Quincy vineyard, about 700 ha, flat (slope 0-6°,
  mostly 0-3°; 5 m DEM), mean altitude 122 m at the sensors, about 60 wind machines that
  protect 85 % of the crop; vines 1-1.15 m apart in rows 1.5 m. 37 Weenat anti-frost
  temperature sensors, installed December 2019, hourly; the daily minimum is taken from 18:00
  the day before to 18:00. Sensor spacing, shield, height and accuracy are not printed.
- **Weather inputs:** synoptic data from Bourges, about 22 km away; night cloud change from
  the AROME forecast (2.5 km grid), coded -1, 0, 1.
- **Frost nights:** 34 in 2020-2022 (11, 21 and 2 by year). Hierarchical clustering (R
  `agnes`; linkage and distance not printed) gives three synoptic clusters (Table 1):
  11 blended nights (mean minimum -1.75 °C, SD across sensors 0.98 °C), 13 cloudy radiative
  (-0.99 °C, 0.88) and 10 radiative (-1.82 °C, 0.86). The range of minima across the
  vineyard is not printed.
- **Topography (Table 2):** a cluster of plots with higher slope (2.83° against 1.82°) and
  lower altitude (118.3 against 122.4 m) differs at p 0.00016 and 0.0024; a second clustering
  has a low group at 112.6 m (p 3.8e-6). Over 80 % of the hot and cold plots on blended nights
  were on plateaus; on cloudy radiative nights 5 of 17 cold plots (29 %) were in the
  low-altitude cluster against 2 of 16 hot plots (13 %); on radiative nights 3 of 6 cold plots
  (50 %). 8 plots stayed above average on every frost type, 2 below.
- **Wind machines, 2021 (Table 6):** without operation the mean minimum was -1.18 °C
  (protected plots) and -0.96 °C (unprotected); with operation -1.47 and -1.69 °C. 8 of 37
  sensors are more than 300 m from a machine.
- **Stated thresholds, no source for two:** advective frost wind above 3 m/s, radiative frost
  below 2 m/s, wind above 1.8 m/s prevents stratification; a 1.5-2 °C inversion between 1.5 and
  15 m for machines to work (cited).
- **Data:** on request from the corresponding author; code too; no repository, no licence.

## Dependence

- None computed. The AROME cloud forecast and Bourges data are inputs.

## Bearing (2026-10-18)

For strand 4 (sensor placement in a vineyard):

- **What it shows:** across 37 sensors in a flat, 700 ha vineyard, the night minimum differs
  by a standard deviation of about 0.9-1.0 °C between plots, and that spread is largest on
  mixed advective and radiative nights and smallest on radiative ones. A few metres of
  altitude (112 to 124 m) and slope are enough to place plots in the cold or warm class.
- **Take for sensor placement:** low-lying plots and plateaus are where the extremes sit,
  so a sensor set that skips the lowest 5-10 m of the relief will miss the cold end; a single
  station 22 km away does not describe plot minima. It is a minimum-temperature study:
  nothing on humidity or wetness.
- **Limits:** preprint; three frost seasons (2020-2022); one vineyard.

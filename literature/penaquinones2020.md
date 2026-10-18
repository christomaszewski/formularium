---
id: penaquinones2020
citation: Peña Quiñones, A. J., Hoogenboom, G., Salazar Gutiérrez, M. R., Stöckle, C. & Keller, M. 2020. Comparison of air temperature measured in a vineyard canopy and at a standard weather station. PLOS ONE 15(6):e0234436
doi: 10.1371/journal.pone.0234436
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 54 of 54 quotes found at their lines by the main session; Tables 1-2 and Figs 5, 6 and 8 read in the page images by the reading agent; Fig. 5 equations checked in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Prosser, Washington]
processes: [canopy temperature, station temperature, microclimate, sensor placement, berry temperature]
records: [penaquinones2020.canopy_station]
datasets: [penaquinones2020.prosser]
files: [andr_s_2020.pdf (the 2026-10-18 drop)]
---

# Peña Quiñones et al. 2020: canopy against station air temperature

Thermistors inside a Chardonnay canopy against a standard weather station, and
thermocouples in berry clusters on the east and west sides, in a rain-shadow vineyard.

## What it holds

- **Site** (l. 136-143): Roza Farm, IAREC, Prosser, 46.29 °N, 119.73 °W, 359 m; Chardonnay,
  own-rooted, planted 2010, rows 2.7 m apart (north-south), vines 1.8 m, 2,035 vines/ha.
  The station is 410 m away in the abstract and 415 m in the text (l. 143).
- **Sensors:** station, class A sensors at 1.7 m in naturally aspirated multiplate shields
  (CS-107 thermistor; HC2-S3 for RH); canopy, Apogee ST-100 thermistors in the same shield
  design, four at 0.5 m and three at 1.2 m, 0.2 m from the trunk row, installed 10 December
  2015 and ended 30 June 2017; berry clusters, T-type thermocouples (three east, three west)
  for 106 days from 1 June 2016 and 81 days from 6 July 2017, calibrated against thermistors
  (TM15 = 0.9982 TC15 + 0.4527, R² 0.9781, n 384; the equation is garbled in the text layer).
  Loggers sampled at 5 s and averaged to 15 min. Daily comparison n = 478 days.
- **Daily regressions, canopy on station (Fig. 5, page 11):** maximum at 0.5 m
  -0.155 + 1.071 WSAT (R² 0.994, n 437); at 1.2 m -0.384 + 1.082 WSAT (R² 0.991); minimum at
  0.5 m -0.728 + 0.965 WSAT (R² 0.987, n 436); at 1.2 m -0.414 + 0.942 WSAT (R² 0.987).
  WSAT is station air temperature in °C. Standard errors are not printed.
- **Differences (Tables 1-2):** over all seasons the canopy minimum is 0.92 °C (0.5 m) and
  0.74 °C (1.2 m) below the station (not significant) and the daily range is wider by 2.02
  and 1.82 °C. In summer the canopy minimum is 1.14 and 1.28 °C lower and the maximum 1.67 and
  2.16 °C higher; in spring the maximum is 1.03 and 0.82 °C higher (not significant). In
  summer the maximum at 1.2 m is 0.5 °C above that at 0.5 m.
- **Lag:** canopy extremes follow the station's by 30-45 min in spring and autumn, none in
  summer and winter (l. 407-410); the 15-min correlation peaks at R² about 0.98 (Fig. 6).
- **Berry clusters (Table 2b, Fig. 8):** the whole-series mean maximum is 1.67 °C (east) and
  6.14 °C (west) above the station; the minimum is 1.43 and 1.66 °C below. East maximum
  3.068 + 0.950 WSAT (R² 0.953, n 107); west -2.269 + 1.297 WSAT (R² 0.789, n 105). Cluster
  air is above the station's for about 12 h a day on the east side and 9 h on the west.
- **Disagreement:** the abstract gives 1.5 °C (east) and 4.0 °C (west) for the clusters'
  maximum, where Table 2b gives 1.67 and 6.14 °C. The abstract's summer canopy maximum of
  2.0 °C is not a printed value (Table 2a: 1.67 and 2.16 °C).
- **Not printed:** RMSE or bias of the regressions; sensor accuracy; canopy humidity, wind
  or leaf wetness (none measured); the S1 data file was not checked (CC BY article).

## Dependence

- None. The paper computes no other model; the cited works (Matese et al. on 0.6-1.5 °C
  canopy against outside air, Spayd et al. on berry skin up to 12 °C above air) are context.

## Bearing (2026-10-18)

For strand 4 (sensors at the canopy against the standard station):

- **What it shows:** in one dry-climate vineyard the canopy air at 0.5-1.2 m runs about
  1.2 °C colder at night and 1.7-2.2 °C hotter by day than a station 410 m off in summer, with
  almost no difference in winter, and the daily maximum and minimum follow the station
  almost linearly (R² 0.99). So a station reading can stand in for canopy air on a daily
  scale, with a season-dependent offset.
- **Take for sensor placement and the sweep:** a canopy-versus-station offset of order 1-2 °C
  at night and by day, larger at the berry on the west side; a leaf-wetness or RH sensor
  model cannot assume station minimum is the canopy minimum. The slope and intercept are one
  vineyard in a semi-arid climate, no humidity, so no offset for RH or wetness hours.
- **Limits:** one vineyard, 18 months, rows north-south, a dry site with no wetness data.

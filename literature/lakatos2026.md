---
id: lakatos2026
citation: Lakatos, L. 2026. Evaluating the representativeness of interpolated climate data at vineyard scale in complex terrain: evidence from two Hungarian wine regions. Atmosphere 17:759
doi: 10.3390/atmos17080759
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 33 of 33 quotes found at their lines by scripts/verify_quotes.py; Figure 4 values read from the rendered page 14 at 300 dpi (not in the text layer)
status: read
diseases: []
crops: [grapevine]
regions: [Hungary, Eger, Tokaj]
processes: [gridded climate data, minimum temperature, interpolation error, microclimate, vapour pressure deficit, terrain]
records: []
datasets: [lakatos2026.boreas_six_vineyards]
files: [l__2026.pdf (the 2026-10-18 drop)]
---

# Lakatos 2026: gridded climate products against six Hungarian vineyard stations

Six vineyard stations (Eger and Tokaj) against four gridded products, for daily temperature, precipitation, radiation and vapour pressure deficit, and how the error relates to terrain. No record: an evaluation, not a formulation.

## What it holds

- **Stations** (l. 214, 252-257): six Boreas stations, 148.9 to 347.1 m a.s.l., September 2019 to June 2021, 10-min loggers with about 30 sensors each. Nominal air temperature accuracy +/-0.1 C and relative humidity +/-1 % RH (manufacturer; l. 331-332); tipping-bucket gauges, 0.1 mm (l. 334). Missing data were not filled; days with a gap at the daily minimum or maximum were dropped (l. 362). Data were aggregated to hourly, then daily (l. 364).
- **Products** (Table 3, l. 399-417): FORESEE (1/6 degree), FORESEE-HUN v1.0 (0.1 degree; built from HUCLIM and EURO-CORDEX), and two 1 km products from FORESEE-HUN (bilinear, and an elevation-based downscaling with SRTM v4.1 90 m). Radiation and VPD only for the 1/6 and 0.1 degree products (l. 417, 1218). Not ERA5-Land or E-OBS.
- **Figure 4, pooled six sites** (rendered page 14; l. 722; bias is Macro minus Micro, l. 569). RMSE (C) / bias (C) / r:
  - Tmin: 1/6 degree 3.85 / -1.52 / 0.80; 0.1 degree 2.41 / -0.94 / 0.91; 1 km DEM 3.90 / -1.48 / 0.79; 1 km no DEM 3.84 / -1.52 / 0.80.
  - Tmean: 2.91 / -0.69 / 0.90; 1.19 / -0.32 / 0.98; 2.93 / -0.64 / 0.90; 2.90 / -0.68 / 0.90.
  - Tmax: 3.25 / -0.18 / 0.92; 1.32 / 0.00 / 0.98; 3.25 / -0.11 / 0.92; 3.25 / -0.15 / 0.92.
  - The 0.1 degree product agrees best; the 1 km products did not consistently beat the coarser ones; the DEM correction made only minor differences (l. 36, 802-806).
- **Radiation and VPD:** global radiation r 0.79 to 0.84, a moderate positive bias at 0.1 degree (l. 940, 949); VPD moderate agreement, larger deviations at high VPD, no VPD statistics in the text (l. 873). Measured VPD = es(T)(1 - RH/100), es = 0.6108 exp(17.27 T / (T + 237.3)) kPa (FAO-56; l. 540-546).
- **Terrain:** exploratory mean absolute r (MTAS) of error against site variables, 0.1 degree product only: TPI 0.569, elevation 0.530, aspect 0.481, slope 0.419 (l. 1005). Elevation against error: Tmin r = 0.90, Tmean 0.96, VPD -0.89; TPI against precipitation error -0.90 (l. 1018-1023); n is not stated (six sites at most). Largest errors at Eger-Nagy-Eged-hegy, steep, 347 m; site tables are supplementary and were not available (l. 1289). Within-vineyard Tmin range up to 10 C on one day is cited from de Resseguier (l. 1110).
- **Leaf wetness:** listed among the measured variables (Table 2, l. 302), but no data, threshold or result appears.
- **Data:** station data on request from the author only (l. 1366); no repository or licence; product access not printed.

## Contradiction carried, not resolved

The sign of the Tmin bias. Figure 4 prints negative biases (-0.94 to -1.52 C, Macro minus Micro, so the grid reads colder than the vineyard). The text says gridded Tmin is overestimated across all methods (l. 734), also that the Tmin bias is generally negative (l. 776), and also that it is predominantly positive (l. 785). Only the figure's numbers and the l. 776 sentence agree. Use the figure's sign only with that caveat. RMSE and r are not affected.

## Dependence

- FORESEE-HUN is built on HUCLIM and EURO-CORDEX with bias and discontinuity correction (l. 399-401); both 1 km products come from FORESEE-HUN (l. 413), so they are not independent of it. No model shaped the station data, and nothing printed says a product was fitted to these stations.

## Bearing (2026-10-18)

Strand 2 (weather for the sweep) and strand 4 (measured vineyard microclimate):

- **Sweep:** a gridded daily minimum can be 2.4 to 3.9 C off in RMSE at a hilly site, with a bias of about 1 to 1.5 C; a finer grid (0.1 degree) cut RMSE but a 1 km elevation downscaling did not. Weather taken from a grid for a sweep should carry a site offset and spread for minimum temperature that grows with relief; it cannot be read from the grid. A VPD or humidity-hour count from gridded inputs inherits this.
- **Sensor placement:** the error tracks elevation and position (TPI), so stations placed to span the elevation and position range of a block will show the bias; six sites over about 200 m of relief are the evidence.
- **Limits:** six sites, 21 months; pooled statistics only; the sign of the bias is contested inside the paper; no leaf wetness.

---
id: bonnardot2012
citation: Bonnardot, V., Carey, V., Madelin, M., Cautenet, S., Coetzee, Z. & Quénol, H. 2012. Spatial variability of night temperatures at a fine scale over the Stellenbosch wine district, South Africa. J. Int. Sci. Vigne Vin 46(1):1-13
doi: 10.20870/oeno-one.2012.46.1.1504
read: 2026-11-03, abstract and the observed-data section (two-column text, so quotes are single-column fragments), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py; closes the 2026-10-18 lead
status: read
diseases: []
crops: [grapevine]
regions: [South Africa (Stellenbosch wine district)]
processes: [night minimum temperature, radiative night, cold-air pooling, elevation gradient, advective night, vineyard loggers]
records: []
datasets: []
files: [dr1103_bonnardot2012.pdf (the 2026-11-03 drop)]
---

# Bonnardot et al. 2012: night minimum temperatures at 40 vineyard loggers over the Stellenbosch district

A South African study of January-March 2009 night minima at 40 vineyard loggers, with a radiative and an advective case night and a mesoscale model run (not read).

**Read this first.**
- The gradients are district-scale (6 to 12 km, 135 to 418 m of elevation), not hollow-scale. They are per-metre values 14 to 20 times below the 0.6 °C/m assumed in Agrarium; they do not test it for a 5 to 100 m hollow.
- The PDF is a Wayback capture of the OENO One file. The text runs to page 13 and the reference list, so it is not truncated. The two-column layout interleaves lines in the extraction.
- This closes the 2026-10-18 lead.

## What it holds

- **Design:** minimum temperatures at 40 data loggers in vineyards of the Stellenbosch Wine of Origin District, January-March 2009; 16 automatic weather stations used to validate a 200 m mesoscale run (abstract, l. 28-40, not quoted).
- **Mean spread:** the mean difference between minimum temperatures at the measurement points was 3.2 °C over the three months (l. 302).
- **Clearest night (5 March 2009):** the greatest difference in minimum temperature between sites was 14 °C (l. 302-310, abstract l. 33). Minimum temperature correlated with elevation in the vineyards, R2 = 0.89, warmer at altitude (l. 312).
- **Lowest minimum that night:** 11.8 °C, in a vineyard at 27 m in the Eerste River Valley (l. 296). Difference to the Helderberg slopes 11.6 °C over 12 km and 418 m of elevation (l. 301).
- **Simonsberg western slopes:** 10.6 °C over 6 km and 12.2 °C over 12 km (l. 305).
- **Helderberg Basin:** the greatest difference was 8.2 °C over 185 m of elevation, 135 m (13.9 °C) to 320 m (22.1 °C) (l. 307). That is about 0.044 °C/m (arithmetic, not printed), of which about 1.2 °C is an ordinary lapse (arithmetic).
- **Stated gradients:** 1 to 2 °C per km and 3 to 4 °C per 100 m of elevation (l. 312), said to match other non-agricultural sites (Gustavsson 1995, cited).
- **Advective night (28 January 2009):** the spread between coolest and warmest site fell to nearly 8 °C (l. 317).

## Dependence

- Own logger observations (January-March 2009). The mesoscale model (RAMS, 200 m) is used separately and was not read here. Gustavsson 1995 is cited for the gradient and is a lead to check. A shared author (Quénol) with other notes is a flag only.

## Bearing (2026-11-03)

- **micro.coldpool_c_per_m (0.6) in Agrarium:** the best vineyard-logger gradient found, 3 to 4 °C per 100 m, is 0.03 to 0.04 °C/m, and the 8.2 °C over 185 m is 0.044 °C/m. Observation over slopes of kilometres, not a hollow; it neither supports nor tests a per-metre value for shallow hollows.
- **micro.coldpool_max_c (4):** a district-wide spread of 14 °C on the clearest night, well above 4 °C, but across 418 m of elevation and 12 km, so it is an upper bound on a site-to-site spread, not a hollow depth deficit.
- **micro.calm_wind_ms / decoupling:** the spread falls from 14 to nearly 8 °C on the advective night. No wind speed or cloud fraction is printed in the part read, so no threshold.

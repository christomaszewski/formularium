---
id: alfieri2018roughness
citation: "Alfieri, J.G., Kustas, W.P., Nieto, H., Prueger, J.H., Hipps, L.E., McKee, L.G., Gao, F. & Los, S. 2018. Influence of wind direction on the surface roughness of vineyards. Irrigation Science 37:359-373 (online 27 November 2018; volume year 2019)"
doi: 10.1007/s00271-018-0610-z
read: 2026-10-25, abstract only (Springer preview page), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 2 of 2 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [United States, California Central Valley]
processes: [canopy flow, wind, roughness length, displacement height, wind direction, row orientation, two-source energy balance, GRAPEX]
records: []
datasets: []
files: []
---

# Alfieri et al. 2018: roughness length of vineyards follows wind direction, but the energy-balance model hardly notices

The journal paper after `alfieri2016ams`: GRAPEX wind data from 2014 to 2016, and a test of what direction-dependent roughness does to modelled heat fluxes.

**Read this first.** Abstract only (the full text is closed). The abstract names the sigmoidal relation but prints no values for it; the 0.15 m and 0.3 m figures are in the earlier conference abstract `alfieri2016ams`, from different years.

## What it holds

- GRAPEX data from 2014 to 2016. Little variation in d_0 was found during the growing season, but z_0 followed a well-defined sigmoidal relation with wind direction (l. 44).
- The two-source energy balance model (TSEB) with these vineyard relations (TSEBVIN) was compared with an open-canopy parameterisation (TSEBOPN). The mean absolute differences were 0.44 m in d_0 and 0.25 m in z_0, both more than 45%, yet the turbulent fluxes differed by only 13 W m-2, or 10% (l. 44).
- The authors conclude that TSEB is largely insensitive to the roughness values tested and recommend the standard model (l. 44).

## Dependence

None recorded. Builds on the same GRAPEX project as `alfieri2016ams` (not independent) and the TSEB model; authors shared with `nieto2019` and `alfieri2022` (a flag).

## Bearing (2026-10-25)

- **dm.row_barrier (2, range 1-4):** confirms, over more years, that roughness depends on wind direction relative to the rows (a sigmoid), but the values are not in what was read. For the size of the effect use `alfieri2016ams` (about 0.3 m against 0.15 m). It is a momentum measurement, not a dispersal one.
- The authors' own finding is that the direction effect matters little for fluxes (13 W m-2, 10%). That is a statement about evapotranspiration, not about spore transport.
- Kind of result: measurement plus model comparison, in an abstract.

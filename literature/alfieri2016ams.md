---
id: alfieri2016ams
citation: "Alfieri, J.G., Kustas, W.P., Gao, F., Prueger, J.H. & Hipps, L.E. 2016. The influence of canopy architecture on the effective surface roughness of vineyards. 96th AMS Annual Meeting (New Orleans, 13 January 2016), 30th Conference on Hydrology, abstract 584"
doi:
read: 2026-10-25, abstract only (AMS web programme page), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [United States, California Central Valley]
processes: [canopy flow, wind, roughness length, displacement height, row orientation, wind direction, GRAPEX]
records: []
datasets: []
files: []
---

# Alfieri et al. 2016 (AMS abstract): vineyard roughness length is about 0.15 m for wind along the rows and 0.3 m across them

A conference abstract from the first two GRAPEX seasons; the journal paper that followed is `alfieri2018roughness`.

**Read this first.** Abstract only, from a meeting programme page (no paper). Its numbers are printed as approximations ("~", "near", "averaging") and come from 2013 and 2014; the later paper used 2014 to 2016.

## What it holds

- Two vineyard sites in California's Central Valley, 2013 and 2014 (GRAPEX). Wind from three heights (2.5, 3.75 and 8 m above ground) in neutral conditions gave the displacement height d_0 and the roughness length z_0 (l. 28).
- d_0 rose from about 0.75 m to about 1.5 m within 10 days of bud burst and then stayed constant for the rest of the season (l. 28).
- z_0 depended on wind direction: it rose sigmoidally from a minimum averaging 0.15 m with wind parallel to the rows to a maximum near 0.3 m with wind perpendicular to them (l. 28). That is a factor of 2 (arithmetic, not printed).

## Dependence

None recorded. The later `alfieri2018roughness` is the journal version of the same project, so the two are not independent. Authors are shared with `nieto2019`, `alfieri2022` and `agam2020egu` (a flag).

## Bearing (2026-10-25)

- **dm.row_barrier (2, range 1-4):** a measured across-to-along ratio of about 2 in momentum roughness (0.3 m against 0.15 m) for wide-row California vineyards. It has the same size as the assumed 2, but it describes the wind above and through the rows, not the flight of sporangia. An aerodynamic ratio is not a dispersal ratio.
- **Canopy wind (SWEB Eq 15):** nothing on wind inside the canopy. The d_0 values are for the whole canopy and no canopy height is printed in the abstract.
- Kind of result: measurement, in an abstract.

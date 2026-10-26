---
id: agam2020egu
citation: "Agam, N., Levi, Y., Alfieri, J. & Prueger, J. 2020. The effect of row orientation on below-canopy turbulence characteristics in a wine-vineyard. EGU General Assembly 2020, EGU2020-1898 (abstract, not presented)"
doi: 10.5194/egusphere-egu2020-1898
read: 2026-10-25, abstract only (EGU meeting abstract page), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Israel, Judean foothills]
processes: [canopy flow, wind, row orientation, below-canopy turbulence, dew]
records: []
datasets: []
files: []
---

# Agam et al. 2020: below-canopy wind in two Israeli vineyards, one with rows along the prevailing wind and one across it

A meeting abstract (not presented) on how row orientation changes wind and temperature profiles below the vine canopy.

**Read this first.** Abstract only, and it prints no wind speeds or ratios. The remark that wind may reduce dew is a hypothesis, not a result.

## What it holds

- Two adjacent vineyards in the Judean foothills, Israel, with rows NE-SW and SE-NW. With a NW prevailing wind, the wind typically blows across the first and along the second (l. 36).
- Four fast-response 2D sonic anemometers at 10, 40, 140 and 250 cm above the ground, sampled at 20 Hz; thermocouple poles stood in the middle of the inter-row (l. 36). The abstract does not say where the sonics stood.
- The below-canopy wind regime differed with orientation, mostly below 2.5 m. Wind was higher, with smaller vertical gradients, in the vineyard parallel to the prevailing wind. Temperature gradients were mostly larger in the perpendicular vineyard (l. 36). No ratio is given.
- The authors' hypothesis: at night, high momentum flux may reduce or even prevent dew on the vine canopy, so lowering the chance of fungal disease (l. 36). The abstract does not test it.

## Dependence

None recorded. Two authors (Alfieri, Prueger) are shared with the GRAPEX notes `alfieri2016ams` and `alfieri2018roughness`; this is a flag only, since the site (Israel) and the data are different.

## Bearing (2026-10-25)

- **dm.row_barrier (2, range 1-4):** supports only the sign: air below the canopy moves more freely along the rows than across them, in one Israeli pair of vineyards. No number, and it is a wind statistic, not a dispersal distance. An aerodynamic ratio is not a dispersal ratio.
- **micro.evap_wind_per_ms (0.3, assumed):** the dew hypothesis points the same way (more wind, less wetness) but is untested here. Nothing is measured on drying.

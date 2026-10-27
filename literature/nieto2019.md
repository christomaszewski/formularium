---
id: nieto2019
citation: Nieto, H., Kustas, W.P., Alfieri, J.G., Gao, F., Hipps, L.E., Los, S., Prueger, J.H., McKee, L.G. & Anderson, M.C. 2019. Impact of different within-canopy wind attenuation formulations on modelling sensible heat flux using TSEB. Irrigation Science 37:315-331
doi: 10.1007/s00271-018-0611-y
read: 2026-10-25, abstract only (Springer preview page), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 2 of 2 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [United States, California Central Valley]
processes: [canopy flow, wind, in-canopy wind attenuation, wind profile, sensible heat flux, two-source energy balance]
records: []
datasets: []
files: []
---

# Nieto et al. 2019: a vineyard-specific in-canopy wind profile, tested against wind measured between the rows

The paper closest to what SWEB's canopy wind needs, but only its abstract was read.

**Read this first.** Abstract only. The attenuation coefficient and the measured wind ratios are in the full text, which is closed. The one number in the abstract is an error in sensible heat flux, not in wind.

## What it holds

- The unique vertical structure and clumped plants of vineyards and orchards are likely to make the wind profile inside the canopy air space deviate from how it is usually modelled (l. 44).
- The study evaluates a new profile that uses the vertical variation of plant biomass in a vineyard, and compares it with a simpler attenuation through a homogeneous canopy (l. 44).
- Both were checked against measured wind speed in a vineyard inter-row and against turbulent fluxes from a two-source energy balance model (TSEB) (l. 44). The abstract names California's Central Valley as the setting of interest, and the acknowledgements credit field data collection during GRAPEX, a Central Valley campaign (l. 593).
- The new profile improved sensible heat flux estimates, with RMSE falling from 42 to 35 W m-2, when the vine canopy was in early growth and strongly clumped (l. 44; found by grep, not in the reading JSON).

## Dependence

None recorded in the abstract. The reference formula is the homogeneous-canopy exponential attenuation (see `cammalleri2010` for its Goudriaan form). Authors are shared with `alfieri2016ams`, `alfieri2018roughness` and `alfieri2022` (a flag).

## Bearing (2026-10-25)

- **Canopy wind (SWEB Eq 15):** a vineyard-specific replacement exists and was tested on measured inter-row wind, but no coefficient or ratio can be taken from the abstract. Chasing the full text (closed; a USDA reprint may exist) would settle more than any other paper in this strand.
- **Mid-canopy to open wind:** the measured ratios are in the paper, not in what was read.
- Kind of result: model evaluation against measurements, in an abstract.

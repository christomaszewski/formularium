---
id: sungmin2019
citation: Sungmin O & Foelsche, U. 2019. Assessment of spatial uncertainty of heavy rainfall at catchment scale using a dense gauge network. Hydrol. Earth Syst. Sci. 23:2863-2875
doi: 10.5194/hess-23-2863-2019
read: 2026-11-03, the abstract and sections 2 and 3 on correlation (the hourly correlation values are in Figs 3 and 4 only), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Austria (Feldbach, WegenerNet)]
processes: [rain spatial correlation, dense gauge network, heavy rain, variogram, catchment scale]
records: []
datasets: []
files: [dr1103_sungmin2019.pdf (the 2026-11-03 drop)]
---

# Sungmin O & Foelsche 2019: spatial uncertainty of heavy rain from a dense gauge network

Spatial correlation of rain between gauges of the WegenerNet in south-east Austria, for accumulations from 5 min to 24 h.

**Read this first.** The hourly correlation against distance exists only as curves in Figs 3 and 4; no text value for 1 h at 3 km. The site is Alpine foreland Austria, not Mediterranean.

## What it holds

- **Network (l. 145):** 150 tipping-bucket gauges, with inter-gauge distances from 0.7 to 23.4 km (l. 146). Dataset: WegenerNet Feldbach region, 20 km by 15 km, 10 years (licence not read).
- **Fit (l. 173):** r(h) = c1 exp(-(h/c2)^c3), a three-parameter exponential, fitted to 1-km bins up to 15 km, for accumulation times of 5 min to 24 h.
- **Nugget c1, cold season (l. 217):** 0.71 to 0.98 across timescales.
- **Nugget c1, warm season (l. 218):** 0.85 to 0.99 across timescales.
- The 1 h value of c1 and the decay lengths are in the figures only.

## Dependence

- Own analysis of the WegenerNet data. None else recorded.

## Bearing (2026-11-03)

- **Station-to-vineyard rain differences (Q5):** the paper shows the form of the decay (exponential type, nugget below 1, so gauges a short distance apart already differ). It gives no number for 1 to 15 km at 1 h in text; read Figs 3 and 4 in the PDF to get one. Kind of evidence: own measurement, another climate.
- It does not bear on a gauge's own catch (station_rain_factor); it bears on how far a station's rain stands for a vineyard away from it.

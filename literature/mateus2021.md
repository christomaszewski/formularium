---
id: mateus2021
citation: Mateus, P., Mendes, V. B. & Plecha, S. M. 2021. HGPT2: An ERA5-Based Global Model to Estimate Relative Humidity. Remote Sensing 13:2179
doi: 10.3390/rs13112179
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [global]
processes: [relative humidity, ERA5 climatology model, harmonic fit, GNSS tropospheric delay]
records: []
datasets: []
files: [pedro_2021.pdf (the 2026-10-18 drop)]
---

# Mateus et al. 2021: HGPT2, a global ERA5-based hourly relative humidity model

A global model of hourly relative humidity fitted to 20 years of ERA5 (0.25 degree, 1 h) with annual, semi-annual and quarterly terms on time segments (l. 18-24). Built for GNSS delay; no record.

## What it holds

- **Method:** time segmentation with annual, semi-annual and quarterly periodicities (l. 22-24); Wexler saturation equations used for humidity (l. 153, 211).
- **Test:** 282 moisture sensors near GNSS stations in 2020 (l. 24-25); 35 IGS GNSS sites for the delay effect (l. 27).
- **Result:** mean global relative humidity RMSE 7.17 % (inland 8.2 %, oceans 6.5 %) (l. 548-549); mean global bias 0.9 % (l. 552). The abstract says RMSE and bias fall against older delay models (l. 28-30).

## Dependence

- Builds on ERA5, the Wexler equations and GAMIT/GLOBK.

## Bearing (2026-10-18)

- **Strand s2 and s5:** an RH error figure of about 7 % RMSE for a climatology-style model against ground sensors. A simulator could take the order of magnitude as the RH uncertainty a reanalysis-derived humidity brings near the 90 % wetness threshold; the sensors are not vineyard sensors and near-saturation accuracy was not located.
- Triage-grade: not read in full.

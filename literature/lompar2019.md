---
id: lompar2019
citation: Lompar, M., Lalić, B., Dekić, L. & Petrić, M. 2019. Filling Gaps in Hourly Air Temperature Data Using Debiased ERA5 Data. Atmosphere 10:13
doi: 10.3390/atmos10010013
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [Italy, Austria and other sites]
processes: [gap filling, ERA5 debiasing, hourly air temperature]
records: []
datasets: []
files: [milo__2019.pdf (the 2026-10-18 drop)]
---

# Lompar et al. 2019: filling hourly temperature gaps with debiased ERA5

ERA5 temperature is debiased against in situ data to fill gaps, tested on five stations of
  different landscapes and latitudes.

## What it holds

- **Method:** debiasing of ERA5 with in situ measured temperature, tested for lowland,
  mountain, desert, island and tropical sites (l. 21-25).
- **Result:** mean RMSE over all gap lengths from 1.1 C at Montecristo to 1.9 C at Gumpenstein
  (l. 26-27).
- **Data:** Gumpenstein 2014 to 2017, mountains, 700 m (Table 1, l. 150); Montecristo 2016,
  island (l. 152).

## Dependence

- Uses ERA5 (CY41R2) and in situ temperature for debiasing (record).

## Bearing (2026-10-18)

- s2 and s5: a gap-filling recipe for station temperature, error 1.1 to 1.9 C for all gap
  lengths. A sweep generator or a sensor-failure model could take the debiasing and the size of
  the error. Temperature only; no humidity. Not read in full.

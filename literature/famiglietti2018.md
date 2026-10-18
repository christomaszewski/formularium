---
id: famiglietti2018
citation: Famiglietti, C. A., Fisher, J. B., Halverson, G. & Borbas, E. E. 2018. Global Validation of MODIS Near-Surface Air and Dew Point Temperatures. Geophysical Research Letters 45:7772-7780
doi: 10.1029/2018GL077813
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [global (109 FLUXNET sites)]
processes: [satellite air temperature, dew point temperature, validation, hypsometric interpolation]
records: []
datasets: []
files: [caroline_2018.pdf (the 2026-10-18 drop)]
---

# Famiglietti et al. 2018: MODIS air and dew point temperature against FLUXNET

Daily 5 km MODIS air and dew point temperatures, from MOD07 profiles interpolated to surface
  pressure, are checked against 109 FLUXNET sites over 2001 to 2014.

## What it holds

- **Data:** MOD07 Level-2 profiles interpolated hypsometrically to surface pressure; 109
  FLUXNET sites on six continents; 14 years, 2001 to 2014 (l. 19-22).
- **Air temperature:** R2 0.89, RMSE 3.47 C (l. 23-24).
- **Dew point:** R2 0.76, RMSE 5.04 C, bias 0.79 C (l. 25-26), with differences by climate
  zone.

## Dependence

- MODIS Collection 6.1 Terra MOD07 and MOD35, NCEP surface pressure (record).

## Bearing (2026-10-18)

- s2: a dew point error of 5 C RMSE at daily scale is too large to set leaf wetness; it shows
  how coarse satellite humidity is against a vineyard need. A simulator could use it as a bound
  on the error of satellite-derived humidity. Not read in full.

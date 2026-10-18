---
id: reynolds2016
citation: Reynolds, D. W., Coleman, T., Gottas, D. J. & LeFebvre, T. 2016. Utilization of real-time vineyard observations to produce downscaled temperature forecasts for frost protection operations. Journal of Operational Meteorology 4(1):121 (article number as printed)
doi: 10.15191/nwajom.2016.0401
read: 2026-10-18, LIGHT (header, abstract, Sect. 1-2, Table 4), by a reading agent (claude-haiku-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py; no page image checked
status: read
diseases: []
crops: [grapevine]
regions: [Sonoma and Mendocino Counties, California]
processes: [frost forecast, bias correction, temperature forecast, vineyard weather stations]
records: []
datasets: []
files: [david_2016.pdf (the 2026-10-18 drop)]
---

# Reynolds et al. 2016: vineyard observations for downscaled frost forecasts

The Frost Forecast System (FFS) of NOAA and the NWS: forecasts of temperature, dew point and
derived relative humidity are bias-corrected against real-time observations from 72 vineyard
stations by a 30-day regression at each grid point (l. 29-34, 449). It forecasts; it does not
generate weather series. No record.

## What it holds

- **Observations:** 72 vineyard sites, received within 3 h (l. 392); NOAA HMT adds 32 hourly
  stations, 17 surface and 15 inversion towers with sensors at 1.5 and 10.5 m (l. 383-387);
  12 of the 72 publish actual minimum and maximum, up to 0.5 °C from the hourly-derived
  values (l. 437).
- **Method:** 30-day linear regression of model T and Td on hourly observation grids, per
  grid point (l. 34, 449); no coefficients printed. Guidance: NDFD, MOS, GFS40, SREF, NAM,
  CONS; analog and consensus products.
- **Result:** skill in overnight minimum temperature, for lows ≤ 2 °C, improves by a factor of
  3-4 for most guidance (l. 35-36); verification on 40 sites, 15 March to 15 May 2014 and
  20 February to 15 May 2015 (l. 523, 612); in 2014 only 3 of the 40 stations fell below
  0 °C (l. 640). Ukiah frost days (≤ 0 °C), 1900-2012 average: February 7.5, March 4.5,
  April 1.6, May 0.2 (Table 4, l. 689).
- **Not printed:** the regression coefficients, the analog metric, the wet-bulb formula, any
  range of overnight minima across sensors, any wetness threshold.

## Dependence

- Corrects NWS model output against vineyard data; the vineyard stations are the target.
  Roebber 2010's consensus method is cited, not read.

## Bearing (2026-10-18)

For Agrarium's sweep (thousands of seasons of hourly weather driving a leaf-wetness model
whose engine counterpart is RH ≥ 90 %):

- **Variables and co-variation:** a forecast of temperature, dew point and humidity at one
  lead time; no wind, no wind direction, no rain generation, no weather series for a sweep.
- **Near saturation or wet hours:** not validated on humidity near saturation or wet hours;
  verified on minimum temperature (MAE by lead time).
- **Where fitted and tested:** Russian River Basin vineyards, Sonoma and Mendocino Counties;
  2014 and 2015 frost seasons.
- **Code and licence:** none; the system is public in real time, with no licence printed.
- **Can it run:** no, and it has nothing to run for a sweep. Its use is the 72-station
  vineyard network as a source of real vineyard temperature, with a 0.5 °C uncertainty for the
  hourly-derived minima.

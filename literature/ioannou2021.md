---
id: ioannou2021
citation: Ioannou, K., Karampatzakis, D., Amanatidis, P., Aggelopoulos, V. & Karmiris, I. 2021. Low-Cost Automatic Weather Stations in the Internet of Things. Information 12:146
doi: 10.3390/info12040146
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [Greece]
processes: [automatic weather station, low-cost sensor, temperature sensor error]
records: []
datasets: []
files: [__2021.pdf (the 2026-10-18 drop)]
---

# Ioannou et al. 2021: low-cost automatic weather stations in the IoT

A review of automatic weather station technology (WMO categories, edge computing, LPWAN) with a small testbed (AgroComp) whose one measured test compares three cheap temperature sensors with a mercury thermometer and a national station.

## What it holds

- **Test:** MCP9808, BMP180 and DHT22 on a Raspberry Pi, hourly readings for 17 days, against a mercury thermometer at the same place and the Hellenic National Meteorological Service station (l. 727-737).
- **Differences from the mercury thermometer** (Table 1, l. 764-770): the BMP row is near zero (0.055 on day 1, 0.879 on day 4); the MCP row is about -0.7 to -1.5; the DHT row is -1.9 to -3.0 as printed (mean differences). The sign convention is as printed; the table text does not state which way the DHT22 reads.
- **Against the national station, 12 km away** (l. 784): standard error of estimate 1.374 for BMP180, 1.455 for MCP9808, 1.574 for DHT22 (Table 2, l. 798-800); the text sets 1.3 degrees as the usable accuracy for BMP180 (l. 781-782).
- **Not printed:** no RH, leaf wetness, drift over time or field failure rate.

## Dependence

- WMO AWS guidelines (WMO-No. 8 and the AWS-LC notes); sensor datasheets. No dataset is reused.

## Bearing (2026-10-18)

- **Strand s5 (sensor error), gap d_sensor_failure:** gives a 17-day bias and scatter of three cheap air-temperature sensors (up to about 3 degrees for the DHT22), usable as an order of magnitude for a bias term; it does not give a failure rate. Not read in full; only the first 150 lines and Section 3.3.

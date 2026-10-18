---
id: smith2022
citation: Smith, M. T., Ross, M., Ssematimba, J., Alvarado, P. A., Álvarez, M., Bainomugisha, E. & Wilkinson, R. 2022. Modelling calibration uncertainty in networks of environmental sensors. arXiv:2205.01988v2 [cs.LG] (preprint, 9 May 2022)
doi: not printed
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [Kampala, Uganda]
processes: [sensor calibration, Gaussian process, variational inference, low-cost sensor network]
records: []
datasets: []
files: [michael_2022.pdf (the 2026-10-18 drop)]
---

# Smith et al. 2022: calibration uncertainty across a sensor network

A variational Bayesian model that carries calibration through a network of low-cost sensors
  with mobile sensors, tested on synthetic and Kampala PM2.5 data.

## What it holds

- **Method:** variational model of calibration across a network, transferring it with mobile
  low-cost sensors (l. 16-30); keywords include Gaussian processes (l. 38).
- **Result:** performs better than multi-hop calibration on synthetic and real air-pollution
  data (l. 27-30); NMSE for raw, multi-hop and variational on 10 synthetic datasets is in Table
  1 (l. 647).
- **Data:** PM2.5 sensors in Kampala, a tropical high-humidity city (l. 64); not temperature or
  humidity.

## Dependence

- Compares against the multi-hop calibration method (l. 30, 665).

## Bearing (2026-10-18)

- s5 (sensor error): a way to carry drift and calibration uncertainty through many cheap
  sensors with a few roving ones; a simulator of a vineyard sensor network could borrow the
  structure, not the numbers (PM2.5). Not read in full.

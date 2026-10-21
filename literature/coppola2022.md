---
id: coppola2022
citation: Coppola, M., Noaille, L., Pierlot, C., Ouvinha de Oliveira, R., Gaveau, N., Rondeau, M., Mohimont, L., Steffenel, L.A., Sindaco, S. & Salmon, T. [year not printed; the file key says 2022]. Innovative Vineyards Environmental Monitoring System Using Deep Edge AI. Book chapter 4.1, pages 261-278 (volume title, year and volume not printed in the text)
doi:
read: 2026-10-21, lightly: abstract, introduction, Sections 4.1.2-4.1.6 (related work, edge intelligence, LoRaWAN comparison, monitoring system, conclusion); references not read; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Champagne]
processes: [LoRaWAN, edge AI, low-power sensor node, soil moisture]
records: []
datasets: []
files: [coppola2022.pdf (the 2026-10-21 drop)]
---

# Coppola et al. 2022: a LoRaWAN vineyard node with an in-sensor machine-learning core, with no field results

A book chapter describing a soil-and-weather node for Vranken-Pommery vineyards in Champagne, built on an ST microcontroller and the LSM6DSOX sensor with decision trees in the sensor.

**Read this first.** Descriptive only: no measurement, error, loss, failure or price is reported. Its power saving (10 to 1000 times) and LoRaWAN range ("to 20 km") are claims or table entries with no source and no test.

## What it holds

- **Node** (l. 519-520, 553-555): TEROS12 soil-moisture sensor (METER Group) chosen for sensor-to-sensor variability under 1 % "at a reasonable cost" (no source or test shown); the node measures weather, soil, crop water status and soil salinity, with no sensor list.
- **Deployment** (l. 568-570): sensors in multiple Vranken-Pommery vineyards; counts, dates and sites not given.
- **Energy** (l. 301, 549; claims): LPWAN nodes can reach 10 years or more depending on the battery; the edge-ML architecture targets 10 to 1000 times energy saving. Neither is measured.
- **Range** (l. 460; Table 4.1.1): LoRaWAN "to 20 km" in open environment, no source named. The table's cost row is symbols only.

## Dependence

- Uses ST Microelectronics products (STM32WL, LSM6DSOX) and the METER TEROS12 sensor; the LoRaWAN, Sigfox, NB-IoT and LTE-M comparison has no source printed (l. 452-482). None recorded otherwise.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Gives:** context for a LoRaWAN soil node in a Champagne vineyard and a pointer to the TEROS12 sensor.
- **Not shown:** data yield or packet delivery, failures, battery or solar life (measured or calculated), tested radio range, maintenance, costs (no currency or price printed).
- **Kind of result:** a design chapter; do not use it for any number in the menu.

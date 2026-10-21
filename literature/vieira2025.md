---
id: vieira2025
citation: Vieira, A., Silva, N., Pascoal, D. & Morais, R. 2025. A Versatile and Low-Cost IoT Solution for Bioclimatic Monitoring in Precision Viticulture. Future Internet 18:16 (published 27 December 2025; the running header prints 2026)
doi: 10.3390/fi18010016
read: 2026-10-21, lightly: abstract, Sections 1-2 (node), 3.1-3.5 (sensor quality, communications, energy, cost), conclusions; Tables 1-3 in full; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Portugal, Vila Real, Douro]
processes: [sensor error, low-cost IoT node, LoRaWAN, packet delivery, leaf wetness, relative humidity, air temperature, cost]
records: []
datasets: []
files: [vieira2025.pdf (the 2026-10-21 drop)]
---

# Vieira et al. 2025: a solar LoRaWAN vineyard node (about 260 EUR) against a METER station

A node with DHT20 air T/RH, soil probes, a wind and rain assembly and a resistive leaf-wetness sensor, run 14 days beside a METER Group station; reports bias, packet delivery and cost.

**Read this first.** Fourteen days only (14 to 28 August 2025, l. 591), no rain in that window (l. 598); rain was analysed over a window extended to 3 September. The DHT20 accuracy is not printed. The leaf-wetness comparison is in normalised units and has R2 0.115. One node; multi-node tests were not done (l. 890-892).

## What it holds

- **Table 3, node minus reference, 15-min pairs** (l. 677-682): air temperature bias -0.79 degC (95 % CI -0.92 to -0.74), RMSE 1.36 degC, R2 0.986 (N 553); RH bias -1.99 %RH (CI -2.63 to -1.28), RMSE 4.54 %RH, R2 0.963 (N 553); soil temperature bias -0.70 degC; wind speed bias +4.18 km h-1 (CI 3.45 to 5.09), partly the 2 s cup-count window (l. 724-727); rain RMSE 0.08 mm on N 80 event windows; leaf wetness normalised bias +0.37, R2 0.115 (N 549).
- **Communications** (l. 849-855): 1309 of 1345 expected uplinks delivered, packet-delivery ratio 97.32 %; the co-located METER station had 97.11 % coverage; longest gap 2 h 15 min (l. 595). LoRaWAN EU868 duty cycle below 0.02 % (l. 861).
- **Energy** (l. 920): about 2.51 Wh per day; solar panel 0.9 W maximum, battery 3.7 V, 2200 mAh (l. 391, 395); year-round autonomy not shown.
- **Price** (Tables 1-2; l. 498, 505-506, 1005): node 258.77 EUR as built, about 260 EUR in the abstract; prices collected November 2024 to February 2025, indicative. A comparable METER set about 1900 EUR, ZL6 logger 837 EUR, cloud about 220 EUR per year.
- **Not measured:** RH above 90 % or wet periods (the "RHmax above 90-95 % with leaf wetness" statement is an agronomic remark, not a tested error, l. 825); drift; sensor failure rate; error against wind or radiation.

## Dependence

- None recorded. The reference is a commercial METER station (ATMOS-22, PHYTOS-31, TEROS-21, ZL6; l. 999-1005); the Watermark 200SS range is from its spec sheet (ref 43); the wind-bias explanation draws on cup-anemometer literature (refs 54-55).

## Bearing (2026-10-21)

Sensor menu of D48 and its observation operators.

- **Error model supported:** a bias with a confidence interval per variable for a roughly 260 EUR vineyard node (air temperature -0.79 degC, RH -1.99 %RH, wind +4.18 km h-1), and a packet-delivery ratio of about 97 % at a 15-min cycle that the reference station matched. Usable as the data-loss and packet-delivery figure for a LoRaWAN node, for a 14-day summer window.
- **Not measured:** error above 90 %RH, wet periods, radiation error against wind, drift, multi-node delivery, gateway distance.
- **Kind of result:** a short field comparison with a bootstrap confidence interval, one Douro vineyard, dry weather.

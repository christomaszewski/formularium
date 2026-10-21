---
id: valente2020
citation: Valente, A., Silva, S., Duarte, D., Cabral Pinto, F. & Soares, S. 2020. Low-Cost LoRaWAN Node for Agro-Intelligence IoT. Electronics 9:987
doi: 10.3390/electronics9060987
read: 2026-10-21, lightly: abstract, introduction (skimmed), Section 2 (node design and sensors), Section 4 (deployment, text and captions), Sections 5.2 (power, Equation 3, Table 2) and 5.3 (cost), conclusions; figure data and references not read; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 21 of 21 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Portugal, Alto Douro Wine Region]
processes: [LoRaWAN, low-cost IoT node, solar power, battery life, cost, soil moisture, weather station]
records: []
datasets: []
files: [valente2020.pdf (the 2026-10-21 drop)]
---

# Valente et al. 2020: three solar LoRaWAN vineyard nodes costing about 37.5 EUR without a sensor

Three SDI-12 nodes (soil, wind, weather station) on one Douro farm, hourly uplink to The Things Network, with a calculated power budget and a cost table.

**Read this first.** Table 2 (state times and currents) and Equation (3) are overprinted in the text layer; which state has which current is uncertain, so none of Table 2 is copied. The 0.382 mA figure is calculated from Eq. (3) and Table 2, so it is as uncertain as they are. No packet delivery, loss, failure or error figure is printed. Only one week of data (12 to 19 April 2020) is shown, in figures.

## What it holds

- **Field** (l. 243-246, 524-527, 560): three nodes on one farm in the Alto Douro; node 1 with 5TE and ATMOS22, node 2 with a Watermark soil-tension sensor, node 3 with an ATMOS41 weather station; hourly uplink via a Lorix One gateway to The Things Network; location withheld.
- **Power** (l. 37, 518, 1277; calculated): 2000 mAh LiPo with a solar panel; maximum consumption about 400 uA (abstract); worst-case average current 0.382 mA for the ATMOS41 node by Eq. (3), PDF page 14. If sensors were switched off between readings the node would draw less than 90 uA (l. 1284, calculated).
- **Battery in the field** (l. 1287-1288; measured): node 3, the longest in the field, kept its battery at full charge for at least six months; no reading below 3.7 V.
- **Range:** none printed; the abstract says consumption depends on distance to the gateway (l. 35).
- **Cost** (l. 1309-1312; euros, values from December 2019): battery 5, solar panel 3, antenna 7, electronics 20, PCB 1, box 1.5, about 37.5 in all; about 46.5 with an I2C SHT35 sensor; the lowest market alternative cited, SenseCap, 78.83 (Digi-Key price).

## Dependence

- Uses LoRaWAN and the SDI-12 sensor protocol. Cited commercial figures for comparison: TekBox sleep currents, DecentLab node under 300 uA without sensors (l. 1279-1281). None recorded beyond that.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Battery or solar life:** calculated 0.382 mA worst case; measured only as a battery that stayed full for at least six months (node 3).
- **Costs:** about 37.5 EUR (46.5 with a temperature and humidity sensor), December 2019.
- **Not shown:** data yield or packet delivery, failures (what, how often), radio range, maintenance, sensor error. Kind of result: a design paper with a three-node, one-week data demonstration and a six-month battery observation.

---
id: lloret2021
citation: Lloret, J., Sendra, S., Garcia, L. & Jimenez, J.M. 2021. A Wireless Sensor Network Deployment for Soil Moisture Monitoring in Precision Agriculture. Sensors 21:7243
doi: 10.3390/s21217243
read: 2026-10-21, lightly: abstract, introduction, Section 3.5 (sensor comparison, Table 5), Section 5 (orange-grove RSSI tests, Figures 14-18, Equations 6-9), conclusions; sensor design and protocol sections by keyword; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [citrus]
regions: [Spain, Valencia]
processes: [wireless sensor network, soil moisture, RSSI, radio range, vegetation loss, cost]
records: []
datasets: []
files: [lloret2021.pdf (the 2021 paper; not the held lloret2011 vineyard paper)]
---

# Lloret et al. 2021: an ESP32 soil-moisture node for citrus (about 2 USD per sensor) and its radio loss in an orange grove

A node with four coil-type soil-moisture sensors, and a Wi-Fi RSSI test among orange trees at four emitter heights.

**Read this first.** Different paper from lloret2011 (the vineyard image-processing network). The text layer of the RSSI fit equations (6)-(9) is overprinted: the coefficients for 1.5 m and 2 m are unchecked and are not copied. The field data are RSSI only; no soil readings, no packet delivery.

## What it holds

- **Node** (l. 18, 22, 619): four soil-moisture sensors per node at different depths, each two coils on a plastic pipe; best prototype winding ratio 1:2 (15 and 30 spires) at 93 kHz; ESP32 DevKit radio with Wi-Fi.
- **Field test** (l. 1707, 1712, 1715, 1719): several ESP32 nodes (count not printed) in a cultivated citrus plot, trees 4 m apart, sunny, about 20 degC; emitters at 0.5, 1, 1.5 and 2 m, receivers on the ground, at 0.5 m and at 1.5 m.
- **Radio** (l. 1726, 1728, 2169): the near-ground receiver (0.5 m) gave the highest and most stable RSSI; denser foliage gave larger fluctuations; emitters at 0.5 or 1 m with a near-ground receiver are best. Fits for 0.5 m (Eq. 6, PDF page 20: -7.182 ln d - 45.276) and 1 m (Eq. 7: -7.69 ln d - 44.194), RSSI against distance in m.
- **Soil sensor** (l. 2377): accuracy close to 95 % after laboratory calibration with soil samples.
- **Costs** (Table 5, l. 1287, 1293, 1302, 1322; dollars as printed, year not printed): own sensor $2.15 with pipe and wire; a microprocessor module $10 to $15; commercial sensors from $58 to $72 up to $219.

## Dependence

- The RSSI-distance fit follows the authors' earlier heuristic signal-attenuation model (their ref. 7, Garcia et al.). Commercial sensor prices are cited from data sheets (refs 42, 45). The authors share Lloret and Sendra with lloret2011: a flag only.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Radio range and vegetation loss:** RSSI against distance among trees up to about 20 m, by emitter height; foliage density matters. Useful only for a Wi-Fi-class link, not LoRaWAN.
- **Costs:** $2.15 per sensor and $10 to $15 per module, in dollars, year not printed.
- **Not shown:** data yield, packet delivery, failures, battery or solar life, maintenance (failure handling is a design intent only, l. 511). Kind of result: a design paper with a bench calibration and one field RSSI test.

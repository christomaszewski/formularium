---
id: khaleefah2025
citation: Khaleefah, R.M. 2025. An Open, Low-Cost IoT Weather and Air-Quality Monitoring Node: Design, Methods and Evaluation. International Journal of Engineering Research & Technology 14(8) (August 2025; article IJERTV14IS080085; pages not printed)
doi:
read: 2026-10-21, lightly: abstract, hardware and bill of materials (Table I), firmware, evaluation plan, results (Table III and text), threats to validity, risks and conclusions; introduction skimmed; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Iraq, Baghdad]
processes: [low-cost IoT node, packet delivery, MQTT, sensor error, air temperature, relative humidity, cost]
records: []
datasets: []
files: [khaleefah2025.pdf (the 2026-10-21 drop)]
---

# Khaleefah 2025: a Wi-Fi ESP weather node (about 25-35 USD) tested for five sessions in Baghdad

A DHT22 and BMP280 node reporting over MQTT and HTTPS, checked against a handheld thermo-hygrometer and airport METAR in three indoor and two outdoor sessions of 2 to 6 h.

**Read this first.** Urban Baghdad, a shaded balcony and a teaching laboratory; no crop. One site, short sessions, favourable Wi-Fi, a handheld reference that is not traceable (l. 468-472). Table I and Table III and Equation 3 are partly garbled in the text layer; no table value or equation is copied. The cost does not reconcile: the text says about 25 to 35 USD without a particulate sensor (l. 195-197), but the Table I line ranges add to about 32 to 66 USD by the reader's sum (the table prints no total). Both are unchecked.

## What it holds

- **Accuracy** (l. 31, 355-358, 394-395): against the handheld reference, temperature MAE 0.4 to 0.6 degC after a one-point offset and RH MAE 2.0 to 3.0 %RH after a two-point adjustment (five sessions); pressure bias 1.0 to 1.5 hPa against METAR. Outdoors, radiation bias and calibration residuals dominated.
- **Delivery** (l. 359, 378, 382): connectivity over 99 % over multi-hour runs; packet delivery ratio above 99.2 % for MQTT and 98.5 % for HTTPS; median latency 1.1 to 1.4 s (MQTT) and 1.4 to 1.9 s (HTTPS) at 30 to 60 s cadence on uncongested Wi-Fi.
- **Failures** (l. 383, 533): reconnection after a Wi-Fi access-point loss favoured MQTT; no failure counts are printed. Power loss, outages and drift are listed as risks, not tested.
- **Power** (l. 111): a small Li-ion battery and charge controller for brief outages outdoors; no battery life or energy figure.
- **Range:** Wi-Fi only; no range figure.

## Dependence

- Builds on BME280-based low-cost stations (Suparta et al., ref. 9), on prior MQTT-versus-HTTPS comparison work (ref. 1) and on co-location practice (refs 5, 10). None recorded in equations.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Packet delivery and error:** 98.5 % to 99.2 % delivery and temperature and RH errors of a DHT22 node on a good Wi-Fi link, short runs, one site. It is a Wi-Fi link, not LoRaWAN, so read it as a best case.
- **Costs:** about 25 to 35 USD in the text, 2025 prices; the table disagrees (see above).
- **Not shown:** battery or solar life, radio range, maintenance, vineyard conditions, wet periods. Kind of result: a short co-location study with MAE against a handheld.

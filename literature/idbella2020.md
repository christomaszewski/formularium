---
id: idbella2020
citation: Idbella, M., Iadaresta, M., Gagliarde, G., Mennella, A., Mazzoleni, S. & Bonanomi, G. 2020. AgriLogger: A New Wireless Sensor for Monitoring Agrometeorological Data in Areas Lacking Communication Networks. Sensors 20:1589
doi: 10.3390/s20061589
read: 2026-10-21, lightly: abstract, introduction (skimmed), Section 2 (hardware, drone and gateway), Section 3.1 (battery, Tables 1-3), Section 3.2 (field test), conclusions; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Italy, Portici, Naples]
processes: [low-power logger, drone data collection, battery life, NB-IoT, air temperature, relative humidity, canopy microclimate]
records: []
datasets: []
files: [idbella2020.pdf (the 2026-10-21 drop)]
---

# Idbella et al. 2020: AgriLogger, a drone-read temperature and humidity logger with a calculated battery life above 10 years

A two-AA logger that stores hourly air temperature and RH on FRAM, is woken by a drone radio wave and uploads weekly; tried in two positions in a vineyard for 19 days.

**Read this first.** The battery life is calculated, not measured. Table 3's weekly consumption is printed twice in conflicting overlays (10 mAh and 1.04 mAh) and is garbled; it is not copied. The field test has two nodes and gives no error, loss or failure figure. No costs are printed.

## What it holds

- **Field test** (l. 33, 749, 906, 978): two sensors placed by hand inside and outside a vineyard canopy, 1 to 19 October (the text places the data in 2019, l. 709-727), one sample per hour; relative humidity inside the canopy reached 98 %.
- **Reliability claim** (l. 1157, 1190): the sensor "was able to collect and store" data for long periods; no loss or error rate is printed. The authors note possible transmission failures from the environment because of short range.
- **Battery** (l. 850, 866, 891, 894-895; calculated): two AA Duracell Plus cells (2000 mAh); 0.1 uA logger sleep current; life above 10 years at one sample per hour and one upload per week; self-discharge alone allows more than 16 years; design life taken as 5 years.
- **Range** (l. 257, 618): drone wake-up about 20 m; the NB-IoT gateway can be up to 15 km from the nearest LTE cell.
- **Limit** (l. 193, 1189): the collecting phase lasts 2 years, set by the 512 kbit memory.

## Dependence

- Extends the authors' MetroAgriFor conference paper on the same system (l. 19-22). The canopy-effect comparison cites a pine-forest study (ref. 29). Nothing borrowed in equations.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Battery:** calculated life above 10 years at hourly sampling; not measured in the field. Uploads are set weekly (l. 906-911); no maintenance or visit figure is printed.
- **Radio range:** 20 m drone wake-up; 15 km gateway to LTE cell (stated, not tested).
- **Not shown:** data yield, packet delivery, failures (what, how often), sensor error against a reference, costs. Kind of result: a device description with a 19-day two-node field demonstration.

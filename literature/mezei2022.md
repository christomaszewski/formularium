---
id: mezei2022
citation: Mezei, I., Lukić, M., Berbakov, L., Pavković, B. & Radovanović, B. 2022. Grapevine downy mildew warning system based on NB-IoT and energy harvesting technology. Electronics 11:356
doi: 10.3390/electronics11030356
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5); every quote checked at its line by verify_quotes.py, key numbers checked by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Serbia, Switzerland]
processes: [warning systems, incubation, sensors]
records: []
datasets: []
files: [electronics-11-00356.pdf]
---

# Mezei et al. 2022: a low-power warning system with a 3-10 trigger

## What it holds

- **Primary alarm** from BBCH 13: mean temperature above 10 °C and at least 10 mm of rain in
  48 h, shoots of 10 cm; night rain or wind above 3.4 m/s within 48 h starts incubation.
- **Incubation:** f(t) = 0.076t² - 3.453t + 42.925 days, fitted to Miller's incubation table
  as printed in Ostojić et al. 1983's manual (correlation 99.7 %), with a daily correction
  (eq. 1, garbled in the text copy).
- **Secondary alarm:** a favourable night (RH above 80 % and above 12 °C for at least 2 h),
  reset when RH stays below 60 % for 2 h.
- **Validation, 2020:** Rimski Šančevi and Vršački Vinogradi (Serbia) and Trient
  (Switzerland), against iMetos alarms and Brischetto et al. 2021's model; 'correlations' in
  Table 3 are counts of alarms that agreed (e.g. 4 of 8); no observed infections.

## Dependence

- The 3-10 rule's form (`rain-temperature-trigger`). Its incubation was fitted to Miller's
  table: whose data that table holds is not said. Compared with Brischetto et al. 2021,
  without observations.

## Bearing (2026-10-09)

- Computes the 3-10 rule's form and an incubation fitted to Miller's table (not
  Goidanich's). For Cooptera: a sensor-node design for low-power warning stations (sent
  2026-10-09).

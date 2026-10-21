---
id: dombrowski2021
citation: Dombrowski, O., Hendricks Franssen, H.-J., Brogi, C. & Bogena, H. R. 2021. Performance of the ATMOS41 All-in-One Weather Station for Weather Monitoring. Sensors 21:741
doi: 10.3390/s21030741
read: 2026-10-21, lightly: abstract, Sections 1 and 2.1-2.4, Section 3.1 and Tables 1-4, Section 3.2 in part, conclusions; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Germany, Selhausen]
processes: [sensor error, all-in-one weather station, air temperature, relative humidity, precipitation, radiation, data loss]
records: []
datasets: []
files: [dombrowski2021.pdf (the 2026-10-21 drop)]
---

# Dombrowski et al. 2021: three ATMOS41 all-in-one stations against an ICOS reference

Three ATMOS41 units (about EUR 1750 each) run beside a research-grade reference for 73 days, scored per variable. No record: a sensor-error paper.

**Read this first.** Table 2 (sensor specifications) is scrambled in the text layer, so which accuracy figure belongs to which unit is uncertain for precipitation and wind (l. 402-403, 427-430); the wind accuracy is not used here. The sign of the Atmos1 precipitation total difference (l. 958) is read from overprinted text and is unchecked. Table 4 is clean. Atmos1 is the 2017-version unit, the other two are newer.

## What it holds

- **Set-up** (l. 18, 241, 335, 540): three ATMOS41 against an ICOS backup station at Selhausen, 23 April to 5 July 2020 (73 days), 10-min data. Reference air temperature and RH at 2.5 m, 20 s instantaneous (l. 185); Pluvio2 weighing gauge for rain at 1 m.
- **Table 4, 73 days, Atmos1 / 2 / 3**: air temperature RMSE 0.53 / 0.49 / 0.45 degC, MBE -0.37 / -0.31 / -0.16 degC (l. 790). RH RMSE 4.33 / 3.36 / 3.39 %, MBE 1.37 / 0.25 / -0.36 % (l. 795). Radiation RMSE 56.46 / 31.88 / 32.28 W m-2, MBE -35.22 / -9.03 / -10.06 W m-2 (l. 782); the authors give about 3 % underestimation (l. 21, 882). Wind speed RMSE 0.84 / 0.88 / 0.82 m s-1 (l. 797).
- **Specifications as printed** (Table 2): air temperature +/-0.6 degC (l. 411), RH +/-3 %, varying with temperature and humidity (l. 416), radiation +/-5 % (l. 393), pressure +/-1.0 hPa (l. 422).
- **Precipitation**: 10-min RMSE 0.13 mm for all three units (l. 784); totals differ from the reference by 7.56 %, 0.67 % and 7.38 % (l. 958, signs see above). Optical gauge, 68 cm2 catch, 0.017 mm resolution (l. 396).
- **Wet and humid**: no error is split by RH above 90 % or by wet periods. Only remarks: slightly higher RH on rain events (l. 1134) and a noisier air temperature during rain (l. 1019-1022), no numbers.
- **Drift and loss**: the 2017 unit was said to be stable over three years with no calibration, but the comparison is "data not shown" (l. 739); recalibration every 2 years (l. 157). A 2-day gap in mid-June (l. 759); Atmos3 radiation lacks its first three weeks, a defective funnel (l. 760). No data-return rate.
- **Price** (l. 151, 181-182): ATMOS41 EUR 1750; ICOS level-one station about EUR 10,000. Currency EUR; the price year is not printed (received 16 December 2020, l. 39).

## Dependence

- None recorded between models. Reference practice follows the ICOS standard and WMO Guide No. 8; the 3 % radiation figure is the manufacturer's own test, cited (METER Group performance data, l. 882). The comparison with TAHMO Zurich (Anand & Molnar) is cited, not used.

## Bearing (2026-10-21)

Sensor menu of D48 and its observation operators.

- **Error model supported:** a station-grade unit with a stated bias and RMSE per variable: air temperature bias about -0.2 to -0.4 degC, RH bias -0.4 to +1.4 % with RMSE 3.4 to 4.3 %, rain totals within about 8 %, 10-min rain RMSE 0.13 mm. Inter-unit RH RMSE 1.38 to 3.49 % (l. 721) gives a unit-to-unit spread. Price EUR 1750 per station (year not printed).
- **Not measured:** RH above 90 %, wet periods, radiation error against wind (no split for the unshielded thermistor), a drift rate (data not shown), a packet-delivery figure (logged on site, no link). Data loss is only two anecdotes.
- **Kind of result:** a field comparison over a Central European spring and early summer, not vineyard canopy air.

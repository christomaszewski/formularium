---
id: lefevre2026
citation: Lefevre, A., Malet-Damour, B. & Rivière, G. 2026. Development of a Metrological Framework Based on Irradiance and Ventilation for the Characterization and Correction of Low-Cost Radiation Shield Errors. Metrology 6:50
doi: 10.3390/metrology6030050
read: 2026-10-21, lightly: abstract, Sections 1-5 (Tables 1-7 for the first rows; Table 6 in full only for S1); by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Reunion Island (France), Le Tampon]
processes: [sensor error, radiation shield, low-cost sensor, SHT31, relative humidity, air temperature, calibration]
records: []
datasets: []
files: [lefevre2026.pdf (the 2026-10-21 drop)]
---

# Lefevre, Malet-Damour & Rivière 2026: five low-cost shields with SHT31 sensors, errors against irradiance and ventilation

Five home-made shields (one fan-ventilated) each carrying an SHT31, set against a Campbell six-plate shield in a tropical climate, 24 April to 28 May 2026, with two correction models.

**Read this first.** The reference shield is shaded under a PV panel but not aspirated, and its RH accuracy is stated only for 0 to 80 %RH (l. 442-444), so the "error" is against an imperfect reference above 80 %RH. Table 6 was read in full only for S1; the correction results for S2 to S5 are not copied. The text layer of Table 4 is clean.

## What it holds

- **Set-up** (l. 187-215, 506): five SHT31 (datasheet +/-0.2 degC, +/-2 %RH, l. 199-201) in shields S1 saucer, S2 ASA multi-plate, S3 forced-ventilated, S4 sphere and S5 PVC chimney; 1-min data, 24 April to 28 May 2026, about 2 m above ground. Mean RH 82.8 %, 5th to 95th percentile 65.8 to 96.8 %, max 98.6 % (l. 514-516, 551); mean wind 0.73 m s-1, more than 25 % calm (l. 517).
- **Temperature** (Table 4; l. 24, 767-771): RMSE 0.68 degC (S3, bias +0.43 degC) to 1.18 degC (S5). Day (GHI above 20 W m-2) RMSE 1.00 to 1.67 degC; night below 0.30 degC for S1 to S4 (l. 838-853). Errors near zero below 300 W m-2 and largest above about 600 W m-2 with low wind (l. 2229-2231); bias above 2.5 degC (abstract, l. 29).
- **RH** (Table 4; l. 25, 751): RMSE 2.65 to 7.39 %RH; S1 bias -7.02 %RH. RH error follows temperature error at -3.1 to -3.7 %RH per degC (l. 2300); under high radiation S1 reads more than 11 %RH low, S4 and S5 8 to 10 (l. 2271-2274).
- **Correction** (Table 6, l. 2461; abstract l. 32-33): on the test week 21-28 May S1 RMSE fell from 0.58 to 0.34 degC (semi-empirical, 40.85 %); abstract: 50 % by the semi-empirical model, up to 66 % by Random Forest.
- **Prices** (Tables 1-2; l. 205, 419-423): shield materials 4.07 to 14.95 EUR (2026 prices, excluding tax; S3 with fan 14.95); SHT31 about 25 EUR (year not printed). Excludes logger, power and mount.
- **Not measured:** RH above 90 % is not split out and wet surfaces, prolonged rain and evaporation "could not be evaluated" (l. 2770); drift (5 weeks, one site); data loss or packet delivery (none reported).

## Dependence

- None recorded between models. The chamber check follows the authors' own earlier protocol (ref 14) and the shield design the WMO Ghardaia intercomparison (ref 31); Random Forest and polynomial fits are generic. Reference: Campbell 41303-5A with HygroVue5.

## Bearing (2026-10-21)

Sensor menu of D48 and its observation operators.

- **Error model supported:** a cheap SHT31 node: temperature bias that is zero at night and grows with irradiance above 600 W m-2 and falls with ventilation; RH error that is the mirror of it (-3.1 to -3.7 %RH per degC), so the two should be drawn together, not independently. Price tier under 20 EUR for a shield, about 25 EUR for the sensor.
- **Not measured:** behaviour above 90 %RH, wet periods, drift, data loss, packet delivery; the reference is itself unspecified above 80 %RH.
- **Kind of result:** a 5-week field comparison, tropical island, low rainfall (max 1.41 mm, l. 528), with a held-out test week.

---
id: aemet2010
citation: Agencia Estatal de Meteorología (AEMET). 2010. Valores climatológicos normales 1981-2010: Barcelona Aeropuerto (0076), Barcelona Fabra (0200E), Reus Aeropuerto (0016A). Web tables, AEMET
doi:
read: "2026-11-04, in full (three web tables transcribed to text by script, not PDFs), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: []
regions: [Spain (Barcelona El Prat, Barcelona Fabra, Reus)]
processes: [climate normals, air temperature, rain days, relative humidity, weather generator]
records: []
datasets: []
files: [dr1104_aemet2010.html (the 2026-11-04 drop), dr1104_aemet2010-2.html (the 2026-11-04 drop), dr1104_aemet2010-3.html (the 2026-11-04 drop)]
---

# AEMET 2010: 1981-2010 climate normals at El Prat, Fabra and Reus

Three web tables of monthly normals (1981-2010) from the Spanish weather service: El Prat airport (station 0076, 4 m), Observatori Fabra on Tibidabo (0200E) and Reus airport (0016A).

**Read this first.**
- These are web tables, not a paper; the three are one note. The page says the table can differ from AEMET's gridded maps. Reuse terms were not checked.
- The row label for the annual line is garbled to "Ao" (año). Columns, from the text header: T mean, TM mean daily maximum, Tm mean daily minimum (deg C), R rain (mm), H mean relative humidity (%), DR days with rain of 1 mm or more, DN snow, DT storm, DF fog, DH frost, DD clear days, I sun hours. Annual and September sunshine print as "-".
- All three are coastal or near-coastal stations, not the inland Penedès vineyards.

## What it holds

- **El Prat (0076), annual (l. 17):** T 16.1, TM 20.3, Tm 11.8 deg C; rain 588 mm; RH 69 %; 53.3 days of rain of 1 mm or more.
- **Fabra (0200E), annual (l. 17):** T 15.5, TM 19.2, Tm 11.7 deg C; rain 621 mm; RH 70 %; 57.1 rain days.
- **Reus (0016A), annual (l. 17):** T 16.1, TM 21.1, Tm 11.1 deg C; rain 500 mm; RH 68 %; 49.8 rain days.
- **Coldest and warmest months (l. 5, 11, 12):** El Prat January 9.2, July 23.9, August 24.4 deg C. Fabra 8.2, 23.8, 23.9. Reus 9.0, 24.2, 24.6. In the monthly T column (l. 5 to 16) August is the warmest month at all three; the table gives months, not day of year.
- **Daily range (l. 5, 11):** El Prat July TM 28.0, Tm 19.8 deg C; January 13.6 and 4.7. Fabra July 28.4 and 19.3. Reus July 29.3 and 19.1; January 14.1 and 3.9.
- **Summer rain (l. 11, 12):** July rain is 21 mm on 1.8 days at El Prat, 24 mm on 1.9 days at Fabra, 15 mm on 2.0 days at Reus. August is 62 mm on 4.5 days, 41 mm on 4.3 days and 42 mm on 3.6 days. Against the annual days (l. 17), July has under half the average month's rain days (arithmetic, not printed: 1.8 against 4.4 at El Prat).
- **Rain per rain day (arithmetic, not printed):** annual rain over annual rain days is about 11.0 mm at El Prat, 10.9 mm at Fabra and 10.0 mm at Reus. Treat as a mean over all days of 1 mm or more, with the rain of lighter days included in the total.
- **Humidity (l. 5, 11):** monthly RH is 70 % in January and 67 % in July at El Prat; 69 and 66 % at Fabra; 70 and 63 % at Reus.
- **Half-range of monthly T (arithmetic, not printed):** (August minus January) / 2 is 7.6 deg C at El Prat, 7.9 at Fabra and 7.8 at Reus.

## Dependence

None recorded. Station observations 1981-2010; no model.

## Bearing (2026-11-04)

- Agrarium weather generator (weather.t_annual_c, t_amplitude_c, t_peak_doy): published normals at three coastal stations, annual T 15.5 to 16.1 deg C and an August peak. Kind of evidence: official station averages, 30 years.
- weather.rain_summer_dip, rain days, rain per wet day and RH: July has few rain days (1.8 to 2.0) and August many more (3.6 to 4.5), so a single summer dip is July's, not July and August together. Coastal stations; the inland vineyards will differ.

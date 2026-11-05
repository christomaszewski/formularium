---
id: terradellas1996
citation: Terradellas Jubany, E. 1996. El viento en Barcelona durante el verano. Algunas aproximaciones para su predicción. III Simposio Nacional de Predicción, Instituto Nacional de Meteorología, Madrid, p. 509-514
doi:
read: "2026-11-04, in full (the text layer and the page-2 image for Table I), by a reading agent and a note writer; 9 of 9 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: []
regions: [Spain (Barcelona airport, Llobregat delta)]
processes: [wind direction, sea breeze, wind speed, summer wind regimes]
records: []
datasets: []
files: [dr1104_terradellas1996.pdf (the 2026-11-04 drop)]
---

# Terradellas 1996: summer wind at Barcelona airport, 3-hourly, 1975-84

A Spanish weather service symposium paper on Barcelona's summer wind: mean wind by hour, three day regimes, and a link to temperature and pressure for prediction.

**Read this first.**
- The text layer lost Table I (mean speed) and Table IV. Table I values below were read from the page image by the reading agent, not from the text layer. Table IV was not read. The name prints garbled in the text ("Jubanteny"); the author is given as in the reading agent's citation.
- One station: the airport, in the Llobregat delta about 10 km from the city (l. 49). Coastal, not the Penedès.

## What it holds

- **Data basis (l. 61):** 10 years, 1975 to 84, of 3-hourly synoptic observations. The regime counts use 16 July to 15 August 1979 to 89 (reading agent's reading of the header).
- **Direction of the mean vector, July, Table II (l. 101):** 48, 7, 356, 126, 164, 178, 180, 129 deg at 00, 03, ..., 21 UTC. North at night (7 and 356 deg), south from 12 to 18 UTC (164 to 180 deg).
- **Steadiness, July, Table III (l. 52):** k (length of mean vector over mean speed) is 0.40, 0.71, 0.85, 0.24, 0.65, 0.69, 0.55, 0.24 at 00 to 21 UTC. Most steady at 06 UTC (0.85, north) and at 12 to 15 UTC (0.65 to 0.69, south).
- **Mean speed, Table I, from the page image (garbled in text):** July at 00 to 21 UTC is 1.6, 1.7, 3.6, 6.0, 10.0, 10.6, 7.9, 2.7 kt. June is 1.5, 2.2, 3.9, 6.4, 10.4, 10.6, 7.6, 2.9. August is 1.7, 2.6, 4.2, 5.2, 9.1, 9.8, 6.6, 2.6. 1 kt = 0.514 m/s. The day peak, 10.6 kt, is about 5.4 m/s (arithmetic).
- **Day types (l. 82, 91, 94, 99):** breeze (180 to 220 deg in at least half of the observations 11 to 17 UTC) on 47 % of days; southeast on 14 %; levante (60 to 130 deg) on 21 % (l. 94); 18 % of days fit none of the three (l. 99).
- **In words (l. 58):** north winds dominate at night and south winds in the central hours of the day, because the breeze is of prime importance in these months.

## Dependence

Airport synoptic observations; no model.

## Bearing (2026-11-04)

- weather.wind_day_dir_deg (south to south-southwest at midday) and wind_night_dir_deg (north): measured July vectors at Barcelona airport, 1975-84.
- weather.wind_mean_ms and wind_night_factor: Table I gives a day peak near 10.6 kt (5.4 m/s) and a night value near 1.6 kt (0.8 m/s), a ratio of about 6 between peak and night (arithmetic); read from an image. Coastal site.
- weather.wind_dir_sd_deg: the 47 / 14 / 21 / 18 % regime split and k values give the scatter, not a directly fitted SD.

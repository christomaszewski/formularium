---
id: bonshoms2022
citation: Bonshoms, M., Ubeda, J., Liguori, G., Korner, P., Navarro, A. & Cruz, R. 2022. Validation of ERA5-Land temperature and relative humidity on four Peruvian glaciers using on-glacier observations. Journal of Mountain Science 19(7):1849-1873
doi: 10.1007/s11629-022-7388-4
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 27 of 27 quotes found at their lines by scripts/verify_quotes.py; Tables 4, 5 and 8 read from rendered pages 10 and 13 at 150 dpi
status: read
diseases: []
crops: []
regions: [Peru, Andes, Cordillera Blanca, Quelccaya, Coropuna]
processes: [reanalysis, ERA5-Land, air temperature, relative humidity, lapse rate, night humidity, saturation]
records: []
datasets: []
files: [mart__2022.pdf (the 2026-10-18 drop)]
---

# Bonshoms et al. 2022: ERA5-Land temperature and humidity on four Peruvian glaciers

ERA5-Land hourly (and monthly) 2 m temperature and relative humidity against on-glacier automatic stations, 2017-2019. No record: a reanalysis validation. It is a glacier at 4700-5800 m, not a vineyard; read for how the humidity error behaves.

## What it holds

- **Sites** (Table 3, l. 434): Artesonraju (CB), Chuecon (CC), Quelccaya (CV), Cavalca on Coropuna (CO). ERA5-Land grid points 129, 346, 771 and 933 m below the stations (4691 vs 4820; 4730 vs 5076; 4879 vs 5650; 4867 vs 5800 m a.s.l.). Hourly gaps in the main stations were filled from nearby stations (CB 14.5 % of T2m, 15.9 % of Rh2m; l. 523).
- **Hourly T2m, total period** (Table 5; l. 595), r / bias / RMSE / MAE (C): CB 0.83 / -0.2 / 1.9 / 1.5; CC 0.85 / 0.2 / 1.7 / 1.3; CV 0.80 / -0.4 / 2.1 / 1.6; CO 0.87 / 0.6 / 1.7 / 1.4. Wet season (DJFM) bias: CB 0.0, CC 0.6, CV -0.5, CO 1.1 C; dry season (MJJA): -0.4, -0.3, -0.4, -0.2 C, RMSE 1.8 to 2.4 C. ERA5-Land underestimates night T2m in the dry season (l. 995).
- **Hourly Rh2m, total period** (Table 8; l. 751), r / bias / RMSE / MAE (%): CB 0.58 / 1.7 / 16.6 / 12.3; CC 0.63 / 7.3 / 18.8 / 13.5; CV 0.58 / 2.2 / 18.6 / 11.9; CO 0.46 / 11.3 / 28.3 / 20.8. Dry season is worse: RMSE 21.4, 23.4, 23.1, 30.9 %; wet season 11.5, 13.3, 11.6, 25.4 %.
- **Pattern in Rh2m** (l. 804-806): ERA5-Land overestimates Rh2m at night and underestimates it by day, more so in the dry season; its points pile up at 100 % when the station is drier, so the reanalysis saturates more than the station.
- **Correlation:** hourly T2m r above 0.80, Rh2m about 0.4 to 0.6 (l. 49-50).
- **Lapse-rate correction** (l. 457-508): T2m corrected by a lapse rate from ERA5 free-air temperature between 600 hPa (about 4330 gpm) and 500 hPa (about 5760 gpm); not applied to Rh2m, because many ERA5 values lie outside 0-100 % and no useful gradient was found (l. 505). The mean lapse rate -6.5 C per km is said not to be recommended; Coropuna monthly values range from -5.6 to -8.4 C per km (cited, l. 482). Equation 6 is garbled in the text layer and not verified.
- **Glacier cooling** (l. 726-740): mean -1.1 C in the dry season (maximum -1.4 C at 14:00), -0.5 C in the wet season (maximum -1.2 C); the daily range is 0.7 C lower (wet) and 0.4 C lower (dry) than at the off-glacier station.
- **Gap filling** (Table 4): RMSE for T2m at the main / second station, linear interpolation 0.76 / 1.45 C, mice 1.00 / 1.81, gradient boosting 0.51 / 1.13; Rh2m 3.76 / 18.1 %, 5.09 / 23.51, 3.38 / 14.55.
- **Data:** on-glacier data are called unpublished (l. 1181); no access route or licence. ERA5-Land is on the Copernicus Climate Data Store, 1950 to near present (l. 355).

## Contradiction carried, not resolved

The abstract's monthly statistics (RMSE within +/-0.2 C for T2m and 3 to 7 % for Rh2m at the wet outer-tropical sites; Cavalca r 0.81, RMSE 13 %, MAE 11 %, bias 8.3 %; Artesonraju r 0.96, RMSE 3 %, bias -0.8 %; l. 58-73) were not found in any table the reader read, so they were not checked against a table. The hourly numbers above are from tables; the monthly ones are abstract only.

## Dependence

- ERA5-Land is the land component of ERA5 forced at higher resolution (l. 343-355); the lapse-rate correction uses ERA5 free-air temperatures. The stations are not said to be assimilated. Gap filling uses nearby stations, not ERA5. No shared calibration is printed.

## Bearing (2026-10-18)

Strand 2 (weather for the sweep), as a caution on gridded humidity:

- Reanalysis relative humidity is the weaker variable: hourly r 0.46 to 0.63 against 0.80 to 0.87 for temperature, RMSE 17 to 28 % RH. It is too humid at night and saturated too often, which is the part of the record a wetness-hour or humidity-threshold count uses. A sweep that takes humidity from a reanalysis should add a night-time positive humidity bias and a ceiling at 100 % that the station would not reach, not a symmetrical noise.
- Temperature needs an elevation correction; humidity has no accepted one here.
- **Limits:** glaciers, tropical high Andes, 2 years; the monthly figures are unchecked; not transferable in size to a vineyard.

---
id: igarashi2018
citation: Igarashi, Wagner Teigi, Silva, Marcelo Augusto de Aguiar e, Franca, Jose Alexandre de, Igarashi, Seiji & Saab, Otavio Jorge Grigoli Abi. 2018. Estimation of soybean leaf wetness from meteorological variables (Estimativa do molhamento foliar da soja a partir de variaveis meteorologicas). Pesquisa Agropecuaria Brasileira 53(10):1087-1092
doi: 10.1590/S0100-204X2018001000001
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py; Table 1 (journal p. 1089) and Table 2 (p. 1090) checked in the page images by the reading agent
status: read
diseases: []
crops: [soybean]
regions: [Brazil, Londrina]
processes: [leaf wetness, regression, canopy position, relative humidity]
records: []
datasets: []
files: [wagner_2018.pdf (the 2026-10-18 drop)]
---

# Igarashi et al. 2018: soybean leaf wetness from weather, by regression

Multiple linear regressions, 36 equations in 12 groups, of the percentage of time wet (LWP)
at 0.3, 0.6 and 0.9 m in a soybean canopy on a station's air temperature, relative humidity,
wind, and on wetness at 1.7 m, for days with and without rain. In Portuguese.

## What it holds

- **Setup** (l. 14-16, 77-97, 109-124): Londrina, Parana (23°34' S, 560 m); three seasons
  2011/2012-2013/2014; "electronic trees" 20 m apart, each with 16 wetness sensors (four at
  each of 0.3, 0.6, 0.9 and 1.7 m), painted with two coats of latex and heat treated after
  Sentelhas et al. 2004b, at 45 degrees; the standard station 50 m north of the crop at 1.7 m.
  Variables logged every 5 min and averaged to hours: 1,920 dry-day and 1,764 rainy-day
  records. The sensor make is not printed.
- **Relative humidity is a regressor** (l. 102-108, 170-172): mean RH (%) enters linearly with
  air temperature, wind and the minimum temperature; wetness is the response. No RH threshold
  appears in any equation.
- **Fit** (Table 1, l. 151-165): dry-day LWP at 0.3 m from station and crop variables
  R² 0.83 (eq. 1: 127.54954 - 6.24579 X2 + 2.96710 X3 + ...), with wetness at 1.7 m added 0.88
  to 0.94; station-only 0.71-0.79; eq. 15 (0.9 m, crop humidity and wetness at 1.7 m) R² 0.93, the best
  of the crop-only set. Eq. 9's intercept
  prints as 9621120, probably a typo, left as printed (l. 159). Rainy days: eq. 34, 0.3 m
  from 1.7 m alone, R² 0.73 (below the authors' 0.8 criterion, l. 122, 228).
- **No error statistic** except R² and p (below 2.2e-16); no bias, RMSE, or external test
  (l. 250). It cites Gleason et al. 1994 for RH above 90 % results being contradictory
  (l. 248), not tested; and Costa et al. 2015 reaching R² 0.8 only with radiation (l. 203).
- **Not printed:** the sensors' own accuracy; calibration; data availability.

## Dependence

- Fitted to the group's own hourly data; no other model's output. Sensor protocol after
  Sentelhas et al. 2004b (also `santos2008`).

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take. This is not a
sensor-error paper; it uses the wetness sensors as the truth.

- **Bias:** the position bias within a canopy: the same weather gives different wetness at
  0.3 to 1.7 m and the regression's R² falls without the 1.7 m reading (0.71-0.79 against
  0.88-0.94 with it). No bias in hours is printed.
- **Noise, drift, failure, threshold:** none; the sensor threshold and accuracy are not
  printed. Relative humidity is a linear regressor, not a threshold, so it gives no support
  for the engine's RH >= 90 % rule, nor against it.
- **Kind of result:** a field regression on three seasons at one site. Not a datasheet or
  a laboratory result.
- **Can it run:** yes, as printed, but only for soybean at Londrina and with its inputs.

---
id: waichler2003
citation: Waichler, S. R. & Wigmosta, M. S. 2003. Development of hourly meteorological values from daily data and significance to hydrological modeling at H. J. Andrews Experimental Forest. Journal of Hydrometeorology 4:251-263
doi: 10.1175/1525-7541(2003)4<251:DOHMVF>2.0.CO;2
read: 2026-10-27, lightly: abstract, the methods for humidity (2d), the relative humidity results (Table 3) and the hydrology comparison summary; temperature, radiation, precipitation and DHSVM sections not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py; the text layer prints minus signs as '2' in tables
status: read
diseases: []
crops: []
regions: [United States, Oregon]
processes: [daily-to-hourly disaggregation, relative humidity, dew point, categorical means, hydrological model forcing, evapotranspiration, model comparison]
records: []
datasets: []
files: [syn1027_waichler2003.pdf (the 2026-10-27 drop)]
---

# Waichler and Wigmosta 2003: five ways to make hourly relative humidity from daily data at one Oregon forest, and what the dew-point assumption does to evapotranspiration

Tests simple daily-to-hourly methods for temperature, rain, radiation, humidity and wind at the H. J. Andrews Experimental Forest, then drives a distributed hydrology model with the alternatives. No record: a method comparison; a deterministic estimator, not a generator. A context paper for gap filling.

**Read this first.** One primary station in a cool wet conifer forest in the Oregon Cascades, scored on hourly values pooled over all hours; no humid-hour count, no disease. Efficiency values for the dew-point methods are printed with a leading "2" for a minus sign in the text layer (garbled); only values printed without it are quoted. Table 3 labels its periods WY80-89 and WY90-98 (l. 348, 353) while the text says humidity used WY89-93 and WY94-98 because hourly RH starts on 8 July 1988 (l. 271-275); the labels were left as printed.

## What it holds

- **Site and data** (l. 17, 42-50, 89-103): H. J. Andrews, Oregon, a cool wet conifer forest (annual precipitation 2300 mm; the mean temperature is garbled in the text layer); hourly values for water years 1980 to 1998 estimated from daily data at the primary station PRIMET and compared with the hourly observations.
- **RH methods** (Table 1, l. 125-129; l. 288-340): 4a, dew point equals the daily minimum temperature, hourly RH as the ratio of saturation vapour pressures at the dew point and at air temperature; 4b, dew point from a regression on Tmin after Running et al. 1987 (a0 = 1.95, a1 = 0.938 for WY80-89, R2 0.88; l. 328); 4c and 4d, interpolation between daily maximum and minimum RH, 4d with a 2 h shift; 4e, a lookup of mean RH by month, hour and rain or no rain.
- **Scores for hourly RH, all hours pooled** (Table 3, l. 348-357): the minimal method 4a has a ratio of simulated to observed mean of 0.831 (WY80-89) and 0.832 (WY90-98), so hourly RH is about 17 % too low on average (arithmetic, not printed); its efficiency is negative (sign garbled). Efficiency against the grand mean: 4b 0.417 (l. 349), 4c 0.435 (l. 350), 4d 0.544 (l. 351) and 0.534 (l. 356), 4e 0.703 (l. 352) and 0.695 (l. 357), with bias ratio 1 for 4e.
- **Authors' ranking** (l. 336-340, 1392-1397): "the only method with efficiency consistently greater than zero" was the month-hour-rain lookup (4e), better than methods using daily Hmin and Hmax; humidity efficiency was higher in verification than in calibration; the least effective model uses Tmin = Tdew and "should be avoided if possible".
- **Hydrology** (l. 25-26, 504-508, 1418): of 14 meteorological input sets driving the distributed hydrology model, the Tmin = Tdew humidity gave "significantly higher evapotranspiration" and the largest annual water-balance differences came from the humidity model.
- **Humidity statistics checked:** hourly RH over all hours (bias ratio and first-degree efficiency, with calibration and verification periods). Not checked: hours above any RH threshold, dew point itself, spell lengths.

## Dependence

- Dew point equal to Tmin after Running et al. 1987 (as cited), Bristow and Campbell 1984 for transmittance, and the distributed hydrology model DHSVM as downstream judge. Interpolation formula 4c/4d is the one used as `bregaglio2012`'s MS 7 (the shared formula, not a shared author).

## Bearing (2026-10-27)

- **D45:** not a generator and no humid-hour check; it sits with `bregaglio2012` and `eccel2011` as evidence on estimators. It adds that the lookup beat the physical interpolation at this site, which is a hint that a conditional-mean table by month, hour and rain can be a strong filler.
- **D60, filling missing RH:** concordant with the others: Tmin as the dew point is the worst (about 17 % low on average here, where `eccel2011` finds it too high at humid-valley stations, so the sign depends on the climate); a month-hour-rain table is best on whole-sample efficiency here and costs only the three conditioning variables. Neither the table nor the interpolation is scored on hours at or above 90 %.
- **Not shown:** any score on high-RH hours, any vineyard or disease output, any station outside one Oregon forest.

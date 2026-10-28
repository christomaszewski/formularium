---
id: eccel2011
citation: Eccel, E. 2012 (online 2011). Estimating air humidity from temperature and precipitation measures for modelling applications. Meteorological Applications 19:118-128
doi: 10.1002/met.258
read: 2026-10-27, lightly: abstract, introduction, data and methods (2.1-2.3), results (Tables II-V) and discussion, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py; the text is two-column and interleaved, and the other numbers were checked by grep against the printed tables
status: read
diseases: []
crops: []
regions: [Italy, Trentino]
processes: [relative humidity, dew point, daily-to-hourly disaggregation, humidity estimation, MTCLIM, FAO-56, cross-validation, hours above RH threshold]
records: []
datasets: []
files: [syn1027_eccel2011.pdf (the 2026-10-27 drop)]
---

# Eccel 2011: relative humidity from minimum temperature and rain, and the count of hours at or above 90 %, at 23 stations

Motivated by grapevine downy mildew and Botrytis models that use RH (l. 40-66), it builds hourly relative humidity (RH) from daily minimum temperature (taken as the dew point, then lowered by an MTCLIM or FAO correction) and scores it against 23 Trentino stations, including the number of hours at or above 90 % RH. No record: a method with measured results, and the only paper in this strand that scores the humid-hour count.

**Read this first.** It is a deterministic daily-to-hourly estimator, not a stochastic generator. Table V's unit is printed "% hours | 1.0 = 100 %" (l. 476), so 1.3 means +130 % of the measured hour count. The measured RH is itself post-processed: the network applies a correction that sets the highest value of the previous 6 months to saturation (l. 154-160). Hourly scores are station means of signed errors, which cancel (l. 500-503).

## What it holds

- **Method** (l. 20, 202-250, 295-310): the premise is that near-ground vapour reaches saturation near the daily minimum temperature, so Td = Tmin (the "raw" model). Two corrections lower Td: MTCLIM, Td = Tn - k(Tday - Tn) with k fitted per station (l. 226); and FAO, a decrease of Tn that is a function of a drought index Id of rain over reference evapotranspiration, forced to zero when Id is 3 or more (l. 246). A wet day is one with at least 1 mm (l. 203-204). Hourly RH keeps the vapour pressure constant over the day and lets temperature change saturation.
- **Data** (l. 132-167, 144): 23 agricultural stations in Trentino, 2001-2009, May to August the focus; capacitive hygrometers rated +/-2 % RH up to 90 % and +/-3 % above (l. 144). Station elevations run from 83 to 797 m (Table I, l. 135-160).
- **Validation design** (l. 307-310): leave-one-year-out cross-validation over the 9 years, giving errors on each excluded year; the summer of 2003 (hot and dry) is a separate test. The correction constants are fitted per station, or averaged over stations for use at sites with no humidity record.
- **Premise checked** (l. 329-331): saturation (daily RH max within 3 % of 100) occurs on only about 21 % of days, autumn 35 % and spring 13 %.
- **Daily scores, raw model, May to August** (Table II, l. 348-355): mean error of daily-maximum RH +12.0 %RH over stations (worst station 20.1); RMSE of daily-maximum RH 17.4 %RH on dry days against 7.2 on wet days (l. 355, 353).
- **Daily scores, corrected, site-specific** (Table III, l. 393): FAO RMSE of daily-maximum RH 8.0 %RH (9.5 with averaged coefficients).
- **Hours with measured RH at or above 90 %** (Table IV, l. 448-450, 458-460): mean error in RH over those hours is -2.6 %RH (raw), -10.2 (FAO) and -9.3 (MTCLIM) for the whole year; for May to August -1.1, -9.3 and -10.3. The corrected models are about 10 %RH too dry in exactly the humid hours.
- **Count of hours at or above 90 %** (Table V, l. 482-486, May to August): mean error in count raw +1.3 (as printed, 130 %) with 2 of 23 stations within +/-10 %; FAO -0.5 and MTCLIM -0.7 with 0 stations; the average of raw and FAO 0.0 with 9 stations within +/-10 %, 5 within +/-30 % in the worst year (l. 485), and 7 stations in 2003. The zero mean is a cancellation: the maximum-year mean error is +0.4 (l. 485).
- **Acceptance** (l. 26-30, 526-536, 590): by the authors' double criterion (mean within 10 %, IQR within 30 %), 9 stations pass for each averaged model and 12 for at least one model; 7 pass the strictest standard, 6 with a 30 % band on the 95th percentile. The authors say 25 to 50 % of stations are satisfactory, and that site-specific calibration is required (l. 595). Performance depends on station mean summer RH (R2 0.37 for the raw model, l. 554; usable range roughly 58 to 67 %, l. 605).
- **Humidity statistics checked:** hours at or above 90 % RH (Tables IV and V), daily RH maximum and minimum (Tables II-III), whole-sample bias by season; dew point only as the model's internal variable; no daily cycle or monthly mean scores.

## Dependence

- Uses the MTCLIM correction (Numerical Terradynamic Simulation Group, University of Montana) and the FAO-56 suggestion (Allen et al. 1998, Annex 6), with Hargreaves reference evapotranspiration for Id (l. 229-233). The downy-mildew motive cites Hill 2000 and Rossi et al. 2008 (l. 39). No shared-author flag with other weather notes. Related by purpose to `bregaglio2012`, which scores whole-sample RH only.

## Bearing (2026-10-27)

- **D45:** this is the near miss that is a check on humid hours: it counts hours at or above 90 % against 23 real hourly records, but for a daily-to-hourly estimator, not a generator, on one alpine province. Result: not a pass; at most 9 of 23 stations are within 10 % of the measured count.
- **D60, filling missing RH:** do not use Tmin as the dew point (raw count error +1.3, which is +130 % on the printed unit, l. 482); calibrate per station; test the humid-hour count on a held-out year before trusting a filled record, and expect a quarter to a half of stations to pass (l. 29, 590). Averaging raw and corrected dew points removes the bias in the mean but not the scatter between stations.
- **Not shown:** a stochastic generator, a disease model run on the estimated RH, any region outside Trentino, or any check against an independent leaf-wetness sensor.

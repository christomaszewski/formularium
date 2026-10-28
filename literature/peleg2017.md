---
id: peleg2017
citation: Peleg, N., Fatichi, S., Paschalis, A., Molnar, P. & Burlando, P. 2017. An advanced stochastic weather generator for simulating 2-D high-resolution climate variables. Journal of Advances in Modeling Earth Systems 9:1595-1627
doi: 10.1002/2016MS000854
read: 2026-10-27, lightly: abstract, sections 2.5-2.6 (vapour pressure, relative humidity), 3 (case study data), 4.7 (vapour pressure and RH results), 4.10 (covariance) and 5 (limits); Supplement S1, including Figure S9 (the RH distribution), not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 18 of 18 quotes found at their lines by scripts/verify_quotes.py; the text is two-column and interleaved
status: read
diseases: []
crops: []
regions: [Switzerland, Swiss Alps, Engelberg]
processes: [weather generator, stochastic, vapour pressure deficit, relative humidity, dew point, reanalysis calibration, spatial generator, model validation]
records: []
datasets: []
files: [syn1027_peleg2017.pdf (the 2026-10-27 drop)]
---

# Peleg et al. 2017: AWE-GEN-2d, a gridded hourly weather generator; its relative humidity is a derived quantity and fails to follow rain

A stochastic generator of rain and cloud (2 km, 5 min) and of temperature, radiation, vapour pressure, pressure and wind (100 m, 1 h), calibrated and tested in the Engelberg region of the Swiss Alps. No record: a method, judged on four mountain and lake stations.

**Read this first.** The RH distribution (Figure S9, in the supplement) was not read; the main text gives only a verbal verdict. Figures 16 to 18 are plots, so the cycle errors come from the text, not from a table. The study area is complex alpine terrain, not a vineyard; Luzern (454 m) is the lowland station.

## What it holds

- **Scope and calibration** (l. 20, 728-745): the generator makes rain and cloud on a 2 km grid every 5 min and the other variables on 100 m every hour; calibrated with MeteoSwiss station data, MERRA reanalysis (500 hPa wind, cloud cover, 31 years; l. 743) and AERONET aerosol data. Stations: Altdorf, Engelberg 1036 m, Luzern 454 m, Pilatus 2106 m, Titlis 3040 m; vapour pressure 30 years, hourly (l. 741).
- **Humidity model** (l. 568-585): vapour pressure follows the point generator AWE-GEN (Fatichi et al. 2011): the modelled variable is the vapour pressure deficit, a cubic function of air temperature plus a linear term in shortwave radiation at lags of 1 and 2 h, plus an AR(1) stochastic part (l. 571-579); parameters are fitted monthly on observed deficits. Relative humidity is vapour pressure over saturation at the generated temperature (l. 585); dew point follows from a Magnus-Tetens equation.
- **Validation design** (l. 1108, 1168-1180): the mean of 50 simulated 30-year realisations is set against 30 observed years (1985-2014) at Luzern, Engelberg and Pilatus, and 10 years (2005-2015) at Titlis. Averaging realisations hides year-to-year spread and spell lengths.
- **Vapour pressure** (l. 1160, 1186-1188): seasonal cycle good at Luzern and Pilatus; under-estimated at Engelberg (May to September) and over-estimated at Titlis (March to October); mean bias -0.62 hPa at Engelberg and +0.52 hPa at Titlis.
- **Mean daily RH cycle** (l. 1190-1192): good at Luzern and Pilatus; under-estimated at Engelberg by up to 13 % difference (as printed); at Titlis the simulated rise starts 3 h early and the fall is steeper. Verdict: good at 2 of 4 stations.
- **RH distribution** (l. 1192-1195): shown in the supplement only; "satisfactorily" reproduced at Luzern, Pilatus and Titlis "with small overestimations of low relative humidity values", while at Engelberg "the probability distribution is biased toward lower values". The wrong end for this question: no count of hours at or above 90 % is given.
- **Rain and humidity** (Table 5, l. 1258, 1274-1276): at Engelberg, mean daily RH on rainy days is 0.84 observed against 0.70 simulated; on dry days 0.72 against 0.69. The authors: observed RH falls markedly from rainy to dry days while the simulated RH "remains similar", a consequence of a structure in which rain acts on other variables only implicitly through cloudiness (l. 1276).
- **Authors' overall verdict** (l. 32, 1322): accuracy "sufficient for many practical applications", but not all statistics are reproduced equally well at the four stations.
- **Humidity statistics checked:** monthly vapour pressure means, vapour pressure distribution, mean daily RH cycle, RH distribution (supplement, judged by eye, not read) and rainy-versus-dry-day mean RH. Not checked: hours at or above 90 %, spell lengths, dew point depression.

## Dependence

- AWE-GEN point generator (Fatichi et al. 2011) for vapour pressure and temperature; MERRA reanalysis for calibration; Dingman 1994 for saturation vapour pressure; Magnus-Tetens for dew point; the topographic input is the DHM25 model. Fatichi is an author of both AWE-GEN papers (a flag); `ivanov2007` is the point generator's precursor.

## Bearing (2026-10-27)

- **D45:** supports it with a sharper statement. No hours at or above 90 % are counted, and the humid class is where this generator is worst at Engelberg: rainy-day RH 0.70 simulated against 0.84 observed (l. 1258), and a distribution biased low there (l. 1195). It is the best-documented hourly generator with RH in this strand, so its absence of a humid-hour check is the finding.
- **D60:** a generator calibrated from reanalysis inherits this structure, where RH is a by-product of temperature and radiation and rain enters only through cloud. If its output is to feed leaf-wetness or RH-threshold rules, add an explicit rain-conditioned humidity process and score it on hours at or above 90 % and on spell lengths against real records. MERRA/ERA-type calibration of cloud and wind is a precedent (l. 743), not of humidity.
- **Not shown:** the supplementary RH distribution; hours at or above 90 %; any lowland vineyard climate; any disease model on its output.

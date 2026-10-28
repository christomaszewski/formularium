---
id: semenov2010
citation: Semenov, M. A., Donatelli, M., Stratonovitch, P., Chatzidaki, E. & Baruth, B. 2010. ELPIS: a dataset of local-scale daily climate scenarios for Europe. Climate Research 44:3-15
doi: 10.3354/cr00865
read: 2026-10-27, lightly: abstract, introduction, section 3.1 (LARS-WG), 3.2 (statistical tests) and 3.4 (derived variables); searched for humidity, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Europe]
processes: [weather generator, LARS-WG, climate scenario, daily weather, derived variables, relative humidity estimation, dataset]
records: []
datasets: []
files: [syn1027_semenov2010.pdf (the 2026-10-27 drop)]
---

# Semenov et al. 2010: ELPIS, LARS-WG site parameters for about 12,000 European grids; the generator makes no humidity

A dataset paper: LARS-WG parameters estimated from the CGMS gridded daily weather for about 12,000 25 km cells, 1982-2008, plus climate changes from 15 AR4 global models. A context paper. The dataset is of generator parameters (daily), not of weather records; distribution terms were not read.

**Read this first.** LARS-WG makes only four daily variables (precipitation, Tmax, Tmin, radiation); relative humidity is derived afterwards by separate software. The tests judge those four variables only. No humidity check in this paper.

## What it holds

- **Dataset** (l. 24-31, 86-91): parameters estimated for nearly 12,000 grids of 25 km from the CGMS dataset, 1982-2008, perturbed with 15 global models to give daily scenarios. The baseline needs 20 to 30 years of observed daily weather per site (l. 80).
- **Generator** (l. 259-261): LARS-WG version 5 "produces daily time series of maximum and minimum temperatures, precipitation and solar radiation", parameterised from observed daily weather.
- **Tests** (l. 257-295, 267): Kolmogorov-Smirnov tests of seasonal dry and wet series, of daily precipitation, Tmax, Tmin and radiation by month, and t-tests of monthly means, at a 0.01 level, counted by grid. About 0.012 of tests on wet series and 0.002 on dry series were significant, which the authors say matches the expected false positives (l. 289-295). Daily variables only.
- **Humidity is derived** (l. 483-500): minimum and maximum daily RH "were estimated using the modelling solutions evaluated by Bregaglio et al. (2010)" (l. 495), via CLIMA components; hourly data and leaf wetness, for disease models that need them, come from a CLIMA software component (l. 500). No check of the hourly values is reported in this paper.
- **Humidity statistics checked:** none.

## Dependence

- CGMS meteorological dataset (interpolated station data), AR4 multi-model ensemble, LARS-WG (Semenov and Stratonovitch 2010), CLIMA software components (Donatelli et al.), and the RH methods of Bregaglio et al. 2010, which are chapter 3 of `bregaglio2012` (shared authors: Donatelli with `bregaglio2012`, Semenov with `madgwick2011`: a flag, not a dependence).

## Bearing (2026-10-27)

- **D45:** supports it by omission: the most widely used daily generator in the impact literature produces no humidity, and its RH is a derived estimate whose hourly step is not tested here. No check on humid hours.
- **D60:** a precedent for a two-stage design (generate T, rain and radiation; derive RH afterwards by a ranked daily-to-hourly method), which `bregaglio2012` scores at 22 sites (EF 0.32 at best without observed daily RH) and `eccel2011` scores on hours at or above 90 %. Not a source of humid-hour realism.
- **Not shown:** any humidity statistic, any disease output.

---
id: gorner2021
citation: Görner, C., Franke, J., Kronenberg, R., Hellmuth, O. & Bernhofer, C. 2021. Multivariate non-parametric Euclidean distance model for hourly disaggregation of daily climate data. Theoretical and Applied Climatology 143:241-265
doi: 10.1007/s00704-020-03426-7
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 42 of 42 quotes found at their lines by scripts/verify_quotes.py; no page image checked (Eqs 3 and 6 lose symbols in the text layer)
status: read
diseases: []
crops: []
regions: [Saxony, Germany, De Bilt, Netherlands]
processes: [disaggregation, hourly weather, relative humidity, wind]
records: [gorner2021.edm]
datasets: [gorner2021.saxony_debilt]
files: [c__2020.pdf (the 2026-10-18 drop)]
---

# Görner et al. 2021: a Euclidean distance model for hourly disaggregation

A resampling method: the day to disaggregate is assumed to have occurred before, and the
most similar observed day (Euclidean distance on standardised daily values, equal weights)
lends its hourly course, scaled by the ratio of daily values.

## What it holds

- **Method** (l. 24-27, 299, 350-393, Eqs 1-6): temperature, precipitation, sunshine,
  relative humidity and wind speed together; selection S1 narrows windows of local
  observation time (±2 h, ±1 h, ±30 min, ±15 min); S2 adds DWD objective weather patterns
  (l. 366); validation leaves out the day and three days either side (l. 299); hourly value
  = basic day's value × RE, temperature shifted by dT (Eqs 4-6); RH above 100 % set to 100 %
  (l. 393). With seven elements, rain has 1/7 of the weight (l. 629), named as a reason for
  heavy rain being off by up to 15 % (Dresden) and 26 % (Fichtelberg) (l. 33).
- **Data** (l. 145-207): six Saxon DWD stations, September 1995 to August 2014; De Bilt
  (KNMI) January 1981 to December 2014; Dresden 222 m (lowland), Fichtelberg 1213 m
  (mountain).
- **Relative humidity** (Tables 2, 3, 5): Dresden (162,192 hourly values) observed mean 76.17 %,
  median 80.0 %, 95th percentile 100.0 %; S1 76.11, 79.5, r 0.88 (l. 589-590). Fichtelberg
  (98,969 values) observed mean 84.61 %, median 93.0 %; S1 83.97, median 90.2 %, r 0.82
  (l. 652-653). Hourly RH cut to 100 % in 3780 (S1) and 2844 (S2) values at Dresden
  (l. 576). De Bilt 1991-2014: RMSE 8.60 %, r 0.84, against MELODIST's 12.67 %, r 0.66
  on the same observations (l. 1418). Dresden RMSE 9.30 %, r 0.85; Saxon basic set 8.26 %,
  r 0.88 (l. 1421). Wind at De Bilt: RMSE 1.44 m/s, r 0.72 (l. 1463); Fichtelberg wind can
  have an inverse diurnal cycle (l. 1171). Temperature at De Bilt RMSE 1.93 °C (l. 1405).
- **Needs** at least 10 years of hourly data, 30 for a climatological context (l. 1547).
- **Not printed:** any code or data statement and licence; the exact OWP classes; the number
  of basic stations per run beyond those named. A citation year mismatch for MELODIST
  (2015 in text, 2016 in the list, l. 36).

## Dependence

- Analogue resampling of observed days; no other model's equation is computed. MELODIST is
  only compared with (`forster2016`).
- **Shared data:** De Bilt 1991-2014, the MELODIST validation record (l. 1440). Not a shared
  model.
- DWD objective weather patterns serve as a filter (l. 207).

## Bearing (2026-10-18)

For Agrarium's sweep (thousands of seasons of hourly weather driving a leaf-wetness model
whose engine counterpart is RH ≥ 90 %):

- **Variables and co-variation:** hourly temperature, precipitation, sunshine, relative
  humidity and wind speed from one observed day, so they keep that day's co-variation
  (rain with humidity and wind). No wind direction. It cannot make a day that was not
  observed, so a sweep of thousands of seasons needs a daily generator ahead of it.
- **Near saturation or wet hours:** partly. Observed and generated 95th percentiles are both
  100 %; the Fichtelberg high-end median is 2.8 points low (90.2 against 93.0 %); the
  100 % cap hit thousands of hours. Not validated on humidity near saturation as a
  hours-above-threshold count, and not on wet hours.
- **Where fitted and tested:** Dresden, Fichtelberg and four more Saxon stations
  (1995-2014); De Bilt (1981-2014).
- **Code and licence:** none stated.
- **Can it run:** not from the paper: no code; the method is described in Eqs 1-6 and could be
  re-implemented, but the OWP filter needs the DWD data.

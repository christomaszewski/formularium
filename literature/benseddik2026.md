---
id: benseddik2026
citation: Benseddik, Z., Bloomfield, H. & Rougé, C. 2026. Hourly disaggregation of daily wind projections: an analogue-based, spatially coherent approach to support energy applications. Environmental Research: Energy 3:025028
doi: 10.1088/2753-3751/ae772a
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [United Kingdom (twelve NUTS1 regions)]
processes: [disaggregation, analogue day, hourly wind, weather generator]
records: []
datasets: []
files: [zainab_2026.pdf (the 2026-10-18 drop)]
---

# Benseddik et al. 2026: analogue-day hourly disaggregation of daily wind over several sites

An analogue method that gives hourly wind at many sites from daily climate-model means: pick the historical day nearest in multi-site squared Euclidean distance, with inter-day continuity, and rescale (l. 63-69). No record.

## What it holds

- **Test:** 71 years of ERA5 (l. 70, 376) for twelve UK NUTS1 regions, split into training and a 15-year test set (l. 71-72).
- **Speed:** under one minute to disaggregate 15 years of daily means (l. 72).
- **Result:** the full hourly distribution is captured; hourly autocorrelation up to 0.95 at midnight when the analogue day changes (l. 74-75); drought durations and ramps are reproduced (l. 76-79).

## Dependence

- Builds on ERA5 and analogue selection by squared Euclidean distance over sites.

## Bearing (2026-10-18)

- **Strand s2 (weather for the sweep) and s6:** a spatially coherent analogue method for hourly series; it handles the midnight join between analogue days. A simulator could take the continuity rule, a known weak point of analogue disaggregation. Wind only, so rain and humidity co-variation is not tested.
- Triage-grade: not read in full.

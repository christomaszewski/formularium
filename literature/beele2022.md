---
id: beele2022
citation: Beele, E., Reyniers, M., Aerts, R. & Somers, B. 2022. Quality control and correction method for air temperature data from a citizen science weather station network in Leuven, Belgium. Earth System Science Data 14:4681-4717
doi: 10.5194/essd-14-4681-2022
read: 2026-10-21, lightly: abstract, Section 2 (network, stations, reference stations), Section 3 (quality-control levels 1-3), Section 4 (bias and random-forest model), Section 5 (application, Tables 10-11), Table A1 and Appendix D; remaining sections and most figures skimmed; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 27 of 27 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Belgium, Leuven]
processes: [sensor error, quality control, radiation bias, citizen weather stations, bias correction, random forest, data loss]
records: []
datasets: []
files: [beele2022.pdf (the 2026-10-21 drop)]
---

# Beele et al. 2022: a 106-station citizen network with a daytime warm bias of 0.15 K, corrected by quality control and a random forest

Fine Offset WH2600 stations in Leuven, checked against four reference units placed beside official RMI stations, with three quality-control levels and a radiation-driven bias correction.

**Read this first.** Urban gardens, not a crop; air temperature only is corrected. The correction model is trained on 60 % of the reference data, and a table in Appendix D applies it to the complete set, so those after-correction numbers are not all held-out (l. 1267-1270). No cost and no uptime figure are printed.

## What it holds

- **Network** (l. 162, 190, 198): 106 stations of one type across Leuven; 868 MHz to a base station that needs power and a LAN connection; the outdoor unit runs on three rechargeable batteries with a small solar panel (no battery life printed).
- **Bias** (l. 44, 544, 704): reference stations 0.15 +/- 0.56 K warmer than the official stations before correction and 0.00 +/- 0.28 K after (abstract); daytime +0.32 degC, night -0.10 degC. The cause is a passive shield without active ventilation and a wind vane shading the radiation sensor at low winter sun (l. 499, 521).
- **Correction** (l. 607): random forest RMSE 0.279 K on held-out data; boosted regression trees 0.319 K.
- **Data loss** (l. 355, 713, 835): steep jumps when a station reconnects after hitches, flagged as outliers; 201 reference observations flagged (0.054 %); 0.5 % to 1 % of Leuven.cool observations removed per year at level 1. Other crowd-sourced studies kept 30 % to 58 % of raw data (l. 843-870, cited).
- **Manufacturer specification** (Table A1, l. 1104-1119): 100 m transmission in the open, temperature +/-1 degC, RH +/-5 %, 16 s interval; overall the measured parameters stay within it (l. 1213).

## Dependence

- Builds on CrowdQC and CrowdQC+ (Napoly et al. 2018; Feichtinger et al. 2020, 2021), on Bell et al. 2015 on station-specific biases, and on random forest and boosted-tree models. No equations borrowed.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Failures and error:** a consumer-grade passive shield gives a radiation-dependent warm bias of 0.15 K (+0.32 K by day), reducible by a model to 0.28 K SD. A concrete error model for an uncorrected cheap air-temperature sensor; the 100 m wireless range is a manufacturer value.
- **Data loss:** flagged 0.6 to 0.7 % per year; not an uptime or packet-delivery figure.
- **Not shown:** costs, battery life, humidity error, wet periods, a vineyard. Kind of result: a multi-year network quality-control study with a held-out test of the correction.

---
id: binks2021
citation: Binks, O., Carle, H., Coughlin, I., da Costa, A. L. & Meir, P. 2021. Measuring the vertical profile of leaf wetness in a forest canopy. MethodsX 8:101332
doi: 10.1016/j.mex.2021.101332
read: 2026-10-26, a light reading from Europe PMC's JATS XML (no PDF held), by a reading agent (claude-haiku-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py; no page images
status: read
diseases: []
crops: []
regions: [Caxiuanã]
processes: [leaf wetness sensor, dew detection, rain detection, canopy profile]
records: []
datasets: []
files: [binks2021.xml (the 2026-10-25 other-sources drop)]
---

# Binks et al. 2021: dew and rain read off a wetness sensor's voltage trace

Eighteen Phytos 31 leaf wetness sensors on two rigs through an Amazon forest canopy, logged
every 15 min, and the threshold rules that turn each trace into dew and rain events: a
method with its accuracy stated, from a forest, for the sensing strand.

## What it holds

- **Setup** (l. 30-49): Phytos 31 (Meter) sensors, nine a rig at 4-36 m in Caxiuanã National
  Park, Brazil (canopy top about 30 m); a CR1000 logger at 28 m with an AM16/32B
  multiplexer, 15 min logging; data on Mendeley (l. 30). The text says 18 sensors once and
  17 once (l. 49, 53).
- **Dew rules** (l. 57): onset when the voltage rises 0.07-1.00 mV/min for at least 1.25 h
  (five steps); end when the mean five-step change falls below 0.5 mV for 1.25 h and the
  value is at or below the threshold.
- **Rain rules** (l. 59-62): onset at a rise above 100 mV in one 15 min step (over 6.67
  mV/min); end when the value falls below 110 % of the threshold; co-occurring dew handled
  by two analysis orders, A and B, from the co-publication (l. 64).
- **Validation** (l. 67-69): five random five-day periods, 62 sensor-periods against manual
  labels: agreement 0.90 on average (SD 0.10, median 0.91, range 0.65-1.00); 89 and 91 % for
  the two example panels; one co-occurring dew event missed.
- **Not printed:** the R script (supplement), the logger program, where the thresholds came
  from, how many people labelled.

## Dependence

- The interpretation and the analyses A and B belong to the co-publication in Agricultural
  and Forest Meteorology (Binks et al. 2021, ref. 2), not held: a lead. No model in the data.

## Bearing (2026-10-26)

- For Agrarium's wetness sensing (the 10-18 and 10-21 searches): a stated-accuracy rule set
  for reading dew and rain from a Phytos 31 trace, device-specific and from a forest; a lead
  for the observation operator, not a record.

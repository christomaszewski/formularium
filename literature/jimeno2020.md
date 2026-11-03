---
id: jimeno2020
citation: Jimeno-Sáez, P., Pulido-Velazquez, D., Collados-Lara, A.-J., Pardo-Igúzquiza, E., Senent-Aparicio, J. & Baena-Ruiz, L. 2020. A Preliminary Assessment of the "Undercatching" and the Precipitation Pattern in an Alpine Basin of Sierra Nevada (Spain). Water 12:1061
doi: 10.3390/w12041061
read: 2026-11-03, abstract and the discussion on undercatch, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 2 of 2 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Spain (Sierra Nevada)]
processes: [undercatch, precipitation correction, inverse hydrology, alpine basin]
records: []
datasets: []
files: [dr1103_jimeno2020.pdf (the 2026-11-03 drop)]
---

# Jimeno-Sáez et al. 2020: undercatch factors fitted for an alpine basin in Sierra Nevada

Precipitation multipliers fitted so a rainfall-runoff model reproduces streamflow in an alpine basin.

**Read this first.** The factors are fitted, not measured: they absorb every bias of the precipitation fields, including orographic gradients. They are not a gauge catch test and not a lowland value.

## What it holds

- **Fitted multipliers (l. 739):** 1.4 for liquid and 1.78 for solid precipitation, assumed "very significant undercatch".
- **Ordering (l. 578):** the undercatch of solid precipitation is greater than that of rain in their correction.

## Dependence

- Inverse hydrology: the factors are tuned against streamflow in a rainfall-runoff model. No gauge test.

## Bearing (2026-11-03)

- **sense.station_rain_factor (assumed 1.0, range 0.7 to 1.3):** what the two facts show: Spanish alpine gridded or gauge rain, once fitted to runoff, needed about 40 % more liquid. That is a bound for a mountain basin and a sign that gridded fields can be low there; it is not an overcatch or undercatch of a gauge. It does not move a lowland vineyard value. Kind of evidence: model fit, weak.

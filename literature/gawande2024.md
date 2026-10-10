---
id: gawande2024
citation: Gawande, Apeksha, Sherekar, Swati & Gawande, Ranjit. 2024. Grape Disease Dataset. Mendeley Data, version 1, 29 April 2024. CC BY 4.0
doi: 10.17632/94j4ws2325.1
read: 2026-10-09, the description and the whole CSV (Grape_Disease_Dataset.csv, 10,000 rows, sha256 1de5a1b5...), summarised by a script, by the main session
status: read
diseases: [downy mildew, powdery mildew, bacterial leaf spot]
crops: [grapevine]
regions: [not stated]
processes: [leaf wetness, sensors]
records: []
datasets: []
files: [Grape_Disease_Dataset.csv]
---

# Gawande et al. 2024: a "grape disease dataset" that holds no disease

Found by Chris as a possible training and evaluation set. It is not one.

## What it holds

- **One CSV:** Date, Time, Temperature, Humidity, LW. 10,000 readings, every 3 to 5 s.
  - 25 short sessions between 20 March and 5 August 2023, mostly minutes to an hour each.
    About 12 h in all.
- **No disease column, no labels, no observations.** The description's "5 categories" and
  "8 distinct classes, including 3 disease categories" (downy mildew, powdery mildew,
  bacterial leaf spot) are not in the file.
- **No site, variety or canopy position.** The authors are at Sant Gadge Baba Amravati
  University and a college in Maharashtra; where the sensors stood is not stated.
- **Values:**
  - Temperature 25.2-32.1 °C; RH 17-76 %, never reaching 90 %.
  - LW is a raw reading, apparently the NodeMCU's 0-1024 analogue scale (inferred). It is
    0 in 89 % of rows, and 100 or more in 5.
  - Time runs backwards twice.

## Dependence

- None: it computes no model and no model is fitted to it.

## Bearing (2026-10-09)

- **Useless for training or evaluating disease models:**
  - it records no outcome;
  - its 12 h never include the saturated, wet conditions in which downy mildew infects or
    sporulates;
  - its sampling is seconds-long bursts, not a season.
- At most, a test input for a logger importer that meets sub-minute rows and raw wetness
  counts.

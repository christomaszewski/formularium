---
id: gawande2024dib
citation: Gawande, A. & Sherekar, S. 2024. Grape dataset: A dataset for disease prediction and classification for machine learning applications through environmental parameters. Data in Brief 54:110546
doi: 10.1016/j.dib.2024.110546
read: 2026-10-27, lightly: abstract, specification table, sections 1-4 (value, background, data description, methods; economic-impact prose skipped; Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew, bacterial leaf spot]
crops: [grapevine]
regions: [India, Maharashtra, Nashik]
processes: [dataset, leaf wetness, IoT sensor node, disease classification, sensors]
records: []
datasets: []
files: [syn1027_gawande2024grape.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Gawande & Sherekar 2024: the data article for the Nashik "Grape Disease Dataset"

The data article for the Mendeley deposit that Formularium's literature/gawande2024 (the deposit's own note, 2026-10-09) found to hold no disease column. This note is for the article, which describes classes the deposit does not contain. No record: a dataset.

**Read this first.** The article says the data are "classified" into 8 classes with 3 disease categories (l. 45) but never says how a class was given to a sensor record: no scouting, no incidence, no dates, no time step (l. 17, 45). The deposit's note (literature/gawande2024, a different item from this article) reports that the CSV has only Date, Time, Temperature, Humidity and LW, with no label column, 10,000 readings every 3 to 5 s in 25 short sessions in 2023. Not outbreak ground truth.

## What it holds

- **Where to get it** (l. 21): Mendeley Data 10.17632/94j4ws2325.1. The article is CC BY (l. 5); the deposit's licence is stated in literature/gawande2024 as CC BY 4.0 and was not opened here.
- **Size** (l. 6): 10,000 records "of classified environmental parameters sensed by sensors classified into three categories, temperature, humidity, and leaf wetness". On this wording the "three categories" are the three sensed variables, not diseases (reading of the sentence, not stated by the authors).
- **Classes claimed** (l. 45, 17): "8 distinct classes, including 3 disease categories" (powdery mildew, downy mildew, bacterial leaf spot); the other five are not described in the lines read. The data were "analyzed to predict the instances of diseases ... using the algorithm" (l. 17).
- **Site** (l. 57): Malode Grape Farm, Eklahare, Nashik, Maharashtra, India. No variety, canopy position, season or years are stated in the lines read.
- **Instrument** (l. 72-74, 87-93): a low-cost node: DHT11 temperature and humidity sensor, a leaf-wetness sensor whose model is left blank in Table 1, and a NodeMCU ESP8266 board; a GSM module sends "Occurrence of diseases if any alerts messages" to farmers (l. 100).
- **How labels were made:** not stated. The alert line (l. 100) suggests an on-device rule, which is an inference; the deposit's note found no label column at all.

## Dependence

- None recorded: no model is named; the class assignment rule is not given. Both are by Gawande and Sherekar (the deposit also lists a third author), so they are not independent.

## Bearing (2026-10-27)

- **D60 tier 2 (leaf wetness included), but not usable for D58.** Real sensor values for T, RH and leaf wetness, yet no disease outcome, no scouting and no long record, so it can neither train nor test a risk model. A model fitted to its "disease" classes would learn an unexplained rule (if the labels exist at all), not disease.
- **What it could do:** a small set of raw readings from a cheap leaf-wetness sensor for sensor-noise or wetness-sensor behaviour (the deposit's note gives the value ranges); nothing for training synthetic-to-real transfer.
- **Not shown:** any link between a reading and an outbreak, a time step, a season length, a multi-year record.

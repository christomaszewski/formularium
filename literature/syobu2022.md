---
id: syobu2022
citation: Syobu, Shin-ichirou & Watanabe, Sachiko. 2022. Characteristics of Meteorological Conditions during a Severe Outbreak of Onion Downy Mildew and Metalaxyl Sensitivity of Peronospora destructor in Saga, Japan, in 2016. Horticulturae 8:578
doi: 10.3390/horticulturae8070578
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [onion]
regions: [Japan, Saga Prefecture]
processes: [infection, sporulation, season severity, leaf wetness, incubation, spray timing, fungicide resistance]
records: []
datasets: []
files: [p29.pdf]
---

# Syobu & Watanabe 2022: weather and metalaxyl sensitivity in an onion downy mildew outbreak

A light read (the deep-research B list).

## What it holds

- Onion downy mildew (Peronospora destructor) epidemic, Saga, Japan, 2016 (l. 15).
- Symptoms from late March 2016 (l. 19).
- Chlorothalonil + metalaxyl-M efficacy 18% (l. 1552) and 45% (l. 1558) in 2017 and 2018 trials.
- Metalaxyl EC50 above 200 µg ai/mL in four isolates (l. 1718); above 10 µg ai/mL in 8 of 11 fields (l. 1719).
- Model rule: sporangia assumed to survive 2 days when mean RH 09:00-18:00 is 55% or more (l. 434).
- Logit on model days: odds ratio 2.48 (l. 1359); AUC 0.70 (l. 1831); Youden cut-off 0.50 (l. 1845).
- Latent-period rate 1/25 per day at 10 C (l. 830), used to back-calculate infection dates.

## Dependence

- none, with flags. (1) Latent-period back-calculation (l. 820-836): infection dates are back-calculated from a temperature-indexed inverse sum of latent periods (rates in Table S4, not read; latent periods cited to DEFRA 2002 [23]). A shared form with incubation-table back-calculation, not its table; the engine's Goidanich and Rossi tables are for grapevine. (2) Wetness stand-in (l. 1811-1812; l. 466-492): RH 80% or more duration replaces leaf wetness, the same form as the RH-as-wetness stand-in, at a lower threshold. (3) Sporulation 4-24 C and 90% RH cited to Yarwood 1943, Hildebrand & Sutton 1982 and Sutton & Hildebrand (l. 346); Lalancette 1988 and Caffi 2013 are not cited. (4) Sporangia survival (l. 1828) cited to Bashi & Aylor 1983 and Palti 1989, not Blaeser & Weltzien 1979.

## Bearing (2026-10-10)

- A dataset for onion, not grapevine: observed disease in three seasons with station weather (2016-2018) that a truth could use for a different host; the engine borrows nothing from it.

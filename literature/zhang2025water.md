---
id: zhang2025water
citation: Zhang, Y., Pichon, L. & Tisseyre, B. 2025. A dataset of three vine water status indicators, weather records and soil available water capacity components collected from a rain-fed Mediterranean vineyard. Data in Brief 59:111295
doi: 10.1016/j.dib.2025.111295
read: 2026-10-27, lightly: abstract, specification table, data description and the limitations (Europe PMC full text; methods sections beyond that skimmed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine, Syrah, Grenache noir]
regions: [France, Hérault, Villeneuve-lès-Maguelone]
processes: [dataset, vine water status, predawn leaf water potential, shoot growth index, carbon isotope discrimination, soil available water capacity, weather record]
records: []
datasets: [zhang2025water.villeneuve]
files: [syn1027_zhang2025water.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Zhang et al. 2025: weekly vine water status (shoot growth index, predawn potential, d13C) in one rain-fed estate, with daily weather and soil

A data article pairing three water status indicators on 70 plots with daily weather and soil water-holding data for one dry year (2022). No record: a dataset.

**Read this first.** One vineyard and one year, and the authors say 2022 was particularly dry, so relationships between the indicators may change in wetter years (l. 225, paraphrased). The weather is daily only (five variables), from one station at the estate's centre (l. 7, 49).

## What it holds

- **Where to get it** (l. 23): Zenodo 10.5281/zenodo.13992359. Licence of the article: CC BY (l. 5). The Zenodo record's licence (CC BY 4.0) and size (Data.zip 0.1 MB) are the reading agent's look at the record, not in the paper.
- **Site** (l. 7, 20, 44, 180): a rain-fed vineyard in southern France 4 km north of the Mediterranean, at Villeneuve-lès-Maguelone with the same printed coordinates (43.547417; 3.8414769, l. 17) as Oger 2023's Field 1, in the domain that Gras 2023 covers; five fields, four of Syrah and one of Grenache noir (l. 180); 70 plots of 10 adjacent vines (l. 7, 45).
- **Year and time step** (l. 7): 2022 only. The shoot growth index iG-Apex was recorded weekly from 2022-06-10 to 2022-08-22 on the 70 plots; predawn leaf water potential weekly in 12 plots, between 3 and 5 a.m. with a pressure chamber; berry-juice carbon isotope ratio d13C on one date, 2022-08-23, from 100 berries per plot (l. 7).
- **Counts** (l. 7, 47): 761 iG-Apex measurements in 70 series, 720 predawn potential measurements in 60 series, and 70 single-date d13C values; iG-Apex was measured for each plot on 8 to 12 dates (l. 47).
- **Weather** (l. 7, 49): daily rainfall, relative humidity and mean, minimum and maximum air temperature, 365 rows from January 1 to December 31, 2022, one station at the estate's centre.
- **Soil** (l. 51): profile-wall analysis in 5 plots in 2 fields: horizon thickness, field capacity, permanent wilting point, bulk density and rock fragments, from which the soil available water capacity of each horizon was computed.
- **How labels were made** (l. 19, 111, 198): observed by instruments and people: iG-Apex by one operator with a smartphone application, predawn potential by two operators with a pressure chamber, d13C by laboratory analysis of the must sugars. The soil water capacity is computed from measured soil parameters.
- **Authors' limits** (l. 225): a single vineyard over one year, specific plant density and training, a dry vintage, and similar management in most fields.

## Dependence

- None recorded: measured values. The paper's related research article (Agric. Water Manag. 302, 2024, not read) fitted a predictive model of predawn potential from iG-Apex and weather on these data, so the set is the training data of that model. Same group and place as Gras 2023 (weather, yield) and Oger 2023 (yield components), so the three sets can be joined but are not independent.

## Bearing (2026-10-27)

- **D60 tiers 1 and soil moisture (tier 3 in D60's list); real-data side of D58 for water status.** Real, weekly plant water status over a dry summer with matched daily T, RH and rain, plus soil water capacity: the nearest thing here to a real judge for a vine water-status model driven by weather and soil. The simulator's water balance could be screened on synthetic seasons, then judged here, one site and one year at a time.
- **Not disease.** It gives no disease outcome or leaf wetness, so it cannot judge anything about downy mildew.
- **Limits:** one estate, one dry year, daily weather only, 12 plots with the reference method, a short archive.

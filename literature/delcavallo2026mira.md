---
id: delcavallo2026mira
citation: Del Cavallo, E., Bregaglio, S., Pepe, A.G., Manici, L.M. & Cervone, L. 2026. A georeferenced dataset for grapevine phenology and phytosanitary monitoring across Italy (MIRA). Zenodo dataset, version v1, published 2026-08-10
doi: 10.5281/zenodo.21534581
read: 2026-10-25, lightly (the deposit's README in full; the treatments and first-symptoms sheets and the station list analysed by script; the host, disease and trap sheets not analysed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy, Piedmont, Lombardy, Veneto, Liguria, Marche, Abruzzo, Basilicata, Lazio, Sardinia]
processes: [field monitoring, phenology, disease onset, spray records, spray interval, spray count]
records: []
datasets: []
files: [dr1025_delcavallo2026mira.pdf (the 2026-10-25 drop)]
---

# Del Cavallo et al. 2026: MIRA, an open Italian dataset of vineyard phenology, disease, traps and dated treatments

A data deposit (CREA, within the MISFITS project) of 77 monitored vineyards in Italy, 2020 to 2025, whose treatments table gives the date and product of each recorded spray.

**Read this first.** A dataset, not a paper: what was read is the deposit's README (its data dictionary and licence) and, by script, the data. Licence: Creative Commons Attribution 4.0 (CC BY 4.0), which allows reuse for any purpose with credit (l. 126). The README names no authors, title or DOI; those are taken from the Zenodo record as relayed by the reading agent, and the README leaves the companion data paper's DOI blank (l. 13), so the data paper was not available. The treatment records are incomplete in many station-seasons (some list a single dated spray), so any count from them is a lower bound and a gap between two listed dates may span unlisted sprays. Every figure marked below as computed was "computed by the reading agent from the deposit, not printed", and the product-to-downy-mildew classification (copper and named downy mildew products, sulfur-only products left out) is the reading agent's keyword rule on the product text.

## What it holds

- **Network:** 77 monitoring vineyards, 2020 to 2025 (l. 6), in 9 Italian regions (Abruzzo, Basilicata, Lazio, Liguria, Lombardy, Marche, Piedmont, Sardinia, Veneto); not Catalonia or any Spanish site (l. 7).
- **Tables:** stations (coordinates, altitude, monitored vineyard area, variety, sentinel status: l. 54-61), host phenology on the BBCH scale (l. 72), disease (incidence and severity by organism, e.g. downy mildew on leaves: l. 80-84), insect traps (l. 96), first-symptom onset dates (l. 105) and treatments. Sheet row counts, as counted by the reading agent and not printed: stations 77, host 24,057, disease 11,880, insect traps 5,399, first symptoms 184, treatments 421.
- **Treatments table:** station, date, type (fungicide, insecticide, acaricide), commercial product text and variety; no dose or area column and no active-substance column (l. 29, 115-118). Dates are given to the day (l. 115). Of the 421 rows, 386 are fungicide, 33 insecticide and 2 acaricide; 179 fall in 2021 and 124 in 2024 (computed by the reading agent from the deposit, not printed).
- **Computed by the reading agent from the deposit, not printed (spray counts):** 52 station-seasons have downy mildew-active products, with a median of 3 dated sprays (mean 4.3, maximum 17); 13 of 63 station-seasons list only one date, which is why the records look incomplete.
- **Computed by the reading agent from the deposit, not printed (intervals):** in the 21 station-seasons with 5 or more dates, gaps between sprays have a median of 10 days (IQR 7 to 13); over all 172 gaps the median is 10.5 days (IQR 7 to 14); the commonest gaps are 7 and 14 days.
- **Computed by the reading agent from the deposit, not printed (onset to spray):** from the first downy mildew leaf-symptom date to the next downy mildew spray record, a median of 8.5 days (n = 18 station-seasons, range 0 to 31); the previous spray came a median of 6 days before onset.

## Dependence

- Monitoring-network records entered by technicians through a mobile app (Zenodo record description, as relayed). The treatment dates are the technicians' entries, not farm accounts. Two authors (Bregaglio, Manici) also wrote the held dataset note `bregaglio2022data`; a shared author is only a flag.

## Bearing (2026-10-25)

- **Interval rule (spray.interval_days):** recorded gaps of 7 to 14 days, median 10 days in the better-recorded station-seasons, for Italian monitored vineyards 2020 to 2025. Supports a fixed-interval grower rule in the 10 to 14 day range. Kind: re-analysis of an open dataset (computed, not printed). Not shown: which products or label intervals set the gap, and any Catalan or Spanish farm.
- **Sprays per season (spray.per_season):** do not use the median of 3; the records are incomplete and the figure is a lower bound.
- **Warning-to-spray delay:** the 8.5-day onset-to-spray median is not a reaction time: growers were already on a schedule, and the first-symptom date is an observation, not a warning.
- **Compliance:** not measured; no warning or model output is in the deposit.

---
id: nefti2024data
citation: "Nefti, O., Chartier, N., Reboud, X., Peyrard, T. & Delière, L. 2024. French low-input winegrowing demonstration farms: a dataset of their operations traceability and sustainability performances. Data in Brief 54:110415"
doi: 10.1016/j.dib.2024.110415
read: 2026-10-25, in full (the 13-page data article, author copy), with the dataset itself (the operations workbook of 131,577 rows and the aggregated performance table) downloaded and analysed by script, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [France, Languedoc-Roussillon, Rhône-Provence, Bordeaux-Bergerac, Alsace-Lorraine, Bourgogne-Jura-Savoie, Champagne, Charentes, Sud-Ouest, Val de Loire]
processes: [spray records, spray count, spray interval, treatment frequency index, work rate, farm operations, low-input farming]
records: []
datasets: []
files: [dr1025_nefti2024data.pdf (the 2026-10-25 drop)]
---

# Nefti et al. 2024: the DEPHY FERME winegrowing dataset, 343 French low-input farms with dated spray records, 2017 to 2020

A Data in Brief article describing an open dataset (INRAE, Recherche Data Gouv, doi 10.57745/2HITDV, version 1.2) of farm operations, with one row per input per intervention, for 343 winegrowing farms of the French DEPHY demonstration network.

**Read this first.** A data article about a deposit, and the deposit was also analysed. What the data hold: for each farm and campaign (initial point plus 2017, 2018, 2019, 2020), one line per input per intervention with date, machinery, products and doses (l. 106, 186), and farm-level indicators including the Treatment Frequency Index (TFI) and, from the yearly meeting with the extension engineer, the farmer's own rating of downy mildew pressure and control (l. 449). Farm ids are anonymous 8-character codes with department and region, no coordinates (l. 126). Licence: the article is CC BY (l. 73); the dataset record's terms of use, read by the reading agent from the Dataverse record and not printed in the article, are CC BY 4.0. The farms are volunteers committed to cutting pesticide use, so their counts are lower than the national mean. Every figure marked "computed" below was computed by the reading agent from the deposit, not printed, and the downy mildew passes count rows whose target is downy mildew, weighted by passes, treated share and variety area share.

## What it holds

- **Sample:** 343 winegrowing farms of the DEPHY network, campaigns 2017 to 2020 (l. 101), chosen from 435 eligible farms as those with complete traceability for every campaign and an initial point (l. 270). Regions: Alsace-Lorraine, Bordeaux-Bergerac, Bourgogne-Jura-Savoie, Champagne, Charentes, Languedoc-Roussillon, Rhône-Provence, Sud-Ouest and Val de Loire (l. 135-137); the deposit's yearly table has 1,715 farm-period rows, with 24 Languedoc-Roussillon and 50 Rhône-Provence farms (counted by the reading agent, not printed).
- **Records:** raw farm operations (date, machinery, inputs, products, doses) plus farm-level indicators including the TFI (l. 106); one line per input per intervention per farm and campaign, with combined inputs sharing an intervention id (l. 186). Where: Recherche Data Gouv, the INRAE Dataverse, doi 10.57745/2HITDV (l. 145).
- **Farmer assessments:** downy mildew pressure and control self-assessments are missing for 7 % of farm-campaigns in 2017 to 2020 and absent for initial points (l. 449).
- **Work rates:** the work rate in h/ha of each mechanised operation, behind the workforce and cost indicators, comes from the French "Coûts des opérations culturales" reference (Hamiti and van Kempen 2017) and is not in the tables (l. 352).
- **Computed, Mediterranean France (24 Languedoc-Roussillon and 50 Rhône-Provence farms), downy mildew-targeted fungicide passes per farm-year:** conventional median 6 (IQR 5 to 7, n = 211 farm-years), organic median 7 (IQR 5.7 to 8.4, n = 83); the Pyrénées-Orientales department (66), conventional, median 6 (n = 44 farm-years, 11 farms). All DEPHY regions: conventional median 7 (Bordeaux-Bergerac 9, Alsace 6), organic 8 (Bordeaux-Bergerac 11, Charentes 11.5). Fungicide TFI median 8.0 conventional and 3.2 organic in the Mediterranean farms.
- **Computed, by the downy mildew pressure the farmer reported (Mediterranean):** conventional median passes 5 (no pressure), 6 (low), 6 (moderate), 7 (high); organic 6, 6.1, 6 and 9. The count rises by 1 to 3 passes in high-pressure years.
- **Computed, timing (Mediterranean):** first downy mildew spray median 5 May (IQR 25 April to 10 May), last median 19 July (IQR 5 to 30 July); gaps between consecutive single-date passes median 13 days for conventional (IQR 10 to 16, n = 840) and 10 days for organic (IQR 7 to 14, n = 492).

## Dependence

- TFI follows Brunet et al. 2008 with the French approved-dose references; work rates and costs come from the machinery cost reference (Hamiti and van Kempen 2017, an earlier edition of the reference held as `coc2023`). The farms are volunteers, so the data are not a random sample of French growers. Delière is also an author of `deliere2015` and of `nefti2024oeno`; a shared author is only a flag.

## Bearing (2026-10-25)

- **Sprays per season and interval (spray.per_season, spray.interval_days):** the recorded practice of volunteer low-input farms in Mediterranean France, 2017 to 2020: 5 to 7 downy mildew passes a year (median 6 conventional, 7 organic), a 13-day (conventional) or 10-day (organic) gap, first spray in early May. Supports a fixed-interval rule of 10 to 14 days with 5 to 7 passes in a normal year and 1 to 3 more in a high-pressure year. Kind: re-analysis of an open dataset (computed, not printed). The Pyrénées-Orientales conventional median of 6 is higher than the 3 passes of the official survey for the same basin (`draaf2021occ`); the farms differ (volunteers, 2017 to 2020 against 2016), and the difference is not explained here.
- **Compliance and delay:** not measured; the dataset holds what was sprayed, not what a warning said, and no warning-to-spray time.
- **Cost and labour:** the performance indicators include workforce and cost items built on the COC work rates (l. 352), but no per-pass cost was read here.
- **Not shown:** Catalonia, coordinates, trafficability or wind.

---
id: schneider2023
citation: Schneider, M., Schelte, T., Schmitz, F. & Körner, M. 2023. EuroCrops: The Largest Harmonized Open Crop Dataset Across the European Union. Scientific Data 10:612
doi: 10.1038/s41597-023-02517-0
read: 2026-10-27, lightly: abstract, the methods introduction, the country sections (France and Spain among them), data records and technical validation (Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [arable crops, permanent crops, grassland]
regions: [European Union, 16 countries]
processes: [dataset, crop parcels, land parcel identification system, taxonomy harmonisation, self-declared labels, remote sensing]
records: []
datasets: []
files: [syn1027_schneider2023eurocrops.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Schneider et al. 2023: EuroCrops, crop-parcel polygons with farmer-declared crop classes from 16 EU countries

A data descriptor for a harmonised set of agricultural parcel polygons whose crop classes come from farmers' subsidy declarations, translated into one hierarchical taxonomy (HCAT). No record: a dataset.

**Read this first.** The labels are farmers' self-declarations under the Common Agricultural Policy (l. 6), validated only by sparse in-situ controls (l. 298). The paper's text as read never names a vineyard or grape class: the word "vineyard" appears once, as an example of a very general class term (l. 209). Whether the HCAT has a vineyard class and which countries and years carry it must be checked in the mapping files (the reading agent's lead), not here.

## What it holds

- **Where to get it** (l. 233, 300): one shapefile per country or region on Zenodo (version 6 goes with this article, l. 300), with updates and mapping files on GitHub (github.com/maja601/EuroCrops, l. 233). No DOI is printed in the lines read.
- **Licence:** by country, as the paper gives it: Spain CC BY 4.0 (l. 221), Sweden CC BY 4.0 (l. 223), Estonia a CC BY-SA equivalent (l. 199), France an open licence on data.gouv.fr (l. 203), Slovenia without use restrictions but with attribution (l. 217), Romania an unlicensed coarse land-cover set (l. 215), Lithuania under its own copyright with registration (l. 209). The Zenodo record's licence was not read.
- **Scope** (l. 6): geo-referenced polygons from 16 EU countries with the crop species grown there.
- **Years:** vary by country; for example Austria 2015 to 2021 (l. 188), Slovenia 2019 to 2021 (l. 217), Slovakia 2020 to 2022 (l. 219), Sweden 2020 and 2021 (l. 223); most harmonised files are for 2021.
- **Variables** (l. 243, 296): the countries' own attribute tables plus three added attributes: the translated crop name, the matched HCAT name and the HCAT code (the "EC_trans_n", "EC_hcat_n" and "EC_hcat_c" columns of Table 6).
- **How labels were made:** self-declared by farmers for subsidy control (l. 6); the authors translated the class names by hand with an automatic step and a manual check, and asked each country to review the mapping: seven of 16 replied (l. 226-229, 231).
- **Class detail varies:** from 21 classes in the Spanish Navarra file (l. 221) to about 150 in Slovenia (l. 217) and roughly 170 in Slovakia (l. 219).
- **Weather, disease, phenology:** none. The set is a map of what is declared, with no time series per parcel in the lines read.

## Dependence

- Class labels are the countries' LPIS declarations; harmonisation is the authors' manual translation to HCAT (a model-free step). A follow-on, EuroCropsML (Sentinel-2 time series with these labels, Sci Data 2025), is a lead and was not read. None recorded otherwise.

## Bearing (2026-10-27)

- **Not a D60 input tier; a source of real parcel outlines and a label caution.** If a vineyard class exists in the files, they could supply real vineyard outlines for Agrarium's real-site step (D38), under the per-country licences and Agrarium's rule that real parcels stay private to their viewer. It gives no weather, disease or phenology to train or judge anything.
- **For satellite-based models, the labels are declarations, not surveys.** Any crop-type model trained on them learns the declaration, with the paper's own caveat about sparse checks.
- **Limits:** vineyard class not confirmed, one declared year per country in the harmonised files, no ground survey, licences that differ by country.

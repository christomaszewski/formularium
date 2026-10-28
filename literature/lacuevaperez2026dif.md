---
id: lacuevaperez2026dif
citation: Lacueva-Pérez, F.J., del Hoyo-Alonso, R., Labata-Lezaun, G., Barriuso-Vargas, J.J. & Ilarri-Artigas, S. 2026 (year from the access dates in its references). Description of dataset "A Multisource Grapevine Phenology Dataset for Smart Farming and AI Modeling". Data description deposited with the dataset (Zenodo); no journal
doi: 10.5281/zenodo.20124340
read: 2026-10-27, in full (the 25-page data description: specification table, file and variable lists, stage table; the companion journal article was not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Aragon, Calatayud, Cariñena, Campo de Borja]
processes: [dataset, phenology, BBCH stage, growing degree days, chilling, NDVI, Sentinel-2, reanalysis gap filling]
records: []
datasets: [lacuevaperez2026.aragon_phenology]
files: [syn1027_lacueva2025aragon.pdf (the 2026-10-27 drop)]
---

# Lacueva-Pérez et al. 2026: the data description of the Aragon multisource grapevine phenology dataset

The file-and-variable description that goes with the Aragon phenology CSV: weekly stage calls by plant-health technicians joined to station weather, heat and chill sums, and Sentinel-2 NDVI. No record: a dataset.

**Same dataset as lacuevaperez2026.** That note covers the Research Square data note (lacueva2026preprint in the drop), which describes the same dataset in more depth; the two documents have the same five authors and the same title stem. This one gives the layout; the preprint gives the design, the counts and the registry's defects. Where they differ it is flagged below.

**Read this first.** The stage labels come from the Red FARA registry, which has restricted access (l. 89-90); only the merged CSV is open. Station failures are replaced with ERA5 reanalysis (l. 96-97), a model, not a measurement; ECMWF forecasts serve predictions. The file carries weather for the 6 days after each record date (l. 220), which a stage classifier must not use as an input at prediction time.

## What it holds

- **Where to get it** (l. 71, 115-116): Zenodo; the description cites 10.5281/zenodo.17930723; the preprint cites the record zenodo.org/records/20124340 (preprint l. 650, 847), and the reading agent's look at the Zenodo record found 20124340 to be the latest version of the same record with CC BY 4.0, files DIF_GrapevinePehologyDataset.csv (492.6 MB), DIF_phenologicalstages.csv and this PDF (record, not in the description).
- **Licence:** the description states none. The preprint states CC BY 4.0 for the dataset (preprint l. 556-557).
- **Scope** (l. 13, 75-76, 109-110): three Protected Designations of Origin in Aragón, northeastern Spain (Calatayud, Cariñena, Campo de Borja), 2016-2022 (l. 16), built by merging 9 datasets from 8 sources (l. 87).
- **Rows** (l. 151): one row per parcel per date. The number of rows is not stated in the description; the preprint counts 18,231 registry samples for 2016-2022 (preprint l. 420) without saying that all are in the CSV.
- **Varieties** (l. 185): Cabernet Sauvignon, Chardonnay, Garnacha, Mazuela, Syrah, Tempranillo. A PDO_Somontano flag also appears in the variable list (l. 203, 431), although the text names three PDOs only.
- **Stage classes** (l. 394-405): a table of 10 entries, from BBCH 0 winter dormancy and 11, 15, 63, 65, 68, 71, 75, 77 to 81 beginning of ripening (l. 405). Nothing after the start of ripening is a class. The preprint instead says 9 of 17 stages were kept (preprint l. 411-412), "with added states 00 and 99" (preprint l. 366-367); this table shows no 99.
- **Weather and index columns** (l. 216-379): for each record date, daily min, max and mean temperature, radiation, mean relative humidity and a wind index by 8 sectors, for the date itself, the 13 days before and the 6 days after (l. 216-236); accumulated GDD (base 4.5 and 10 C; the cap above which heat stops adding is 35 C here, l. 246-247, and 40 C in the preprint, preprint l. 486-488), Winkler, Richardson and Utah chill sums, radiation and precipitation since season start and for the weeks before and after (l. 239-379); NDVI statistics (min, max, mean, standard deviation, median, difference) per parcel from Sentinel-2 (l. 210-215). No leaf wetness.
- **Weather sources** (l. 79, 96-97, 101-102): SIAR and Grapevine-project station networks; ERA5 (accessed via Open-Meteo) replaces station failures and ECMWF IFS forecasts are used to make predictions.
- **How labels were made** (l. 79, 89-90): qualitative field phenology observations by registry technicians (observed by people); heat and chill sums computed from temperature; NDVI computed from Sentinel-2.

## Dependence

- Stage labels depend on the Red FARA protocol (the preprint says it is the Baggiolini scale translated to BBCH). Gaps in weather depend on ERA5; forecasts on ECMWF IFS. The file is the one used to train the group's earlier models (l. 53), and the description points to Comput. Electron. Agric. 231:110018 (reference 9, l. 145-147; also l. 104) for the transformations; that article was not read. No shared-author flag beyond the group.

## Bearing (2026-10-27)

- **D60 tiers 1 and 2 plus satellite NDVI (tier 3); the one open real phenology set with weather that this strand found, for D58's phenology side.** Real weekly stage calls with matched T, RH, radiation, wind and rain over 7 seasons and three PDOs. It can judge a phenology or heat-sum variable (GDD base, chill rules) that the simulator has screened, which is what D58 asks of real data; it also shows a D60-style filled input (ERA5 for station gaps), with the fill rate not stated.
- **Not disease.** The stage classes end at BBCH 81; it carries no disease outcome (the same group's powdery mildew set is separate: Zenodo 10.5281/zenodo.20734058, 44,533 observations, record metadata only, not read).
- **Limits:** a restricted source registry; one region; stage calls are qualitative; the post-date weather columns invite leakage; the description is silent on licence and row count.

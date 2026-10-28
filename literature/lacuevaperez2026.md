---
id: lacuevaperez2026
citation: Lacueva Pérez, F.J., del Hoyo-Alonso, R., Labata-Lezaún, G., Barriuso-Vargas, J.J. & Ilarri-Artigas, S. 2026. Multisource Grapevine Phenology Dataset for Smart Farming and AI Modeling. Research Square preprint rs-9781395 v1 (Data Note, posted 2026-05-22; not peer reviewed)
doi: 10.21203/rs.3.rs-9781395/v1
read: 2026-10-27, lightly: abstract, introduction, section 2 (repository survey, Table 2), section 3 (design, 3.1-3.4, Table 3), section 4 FAIR evaluation and discussion, appendix A.1-A.3; the journal article on the models (Comput. Electron. Agric. 231:110018) was not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Aragon, Calatayud, Cariñena, Campo de Borja]
processes: [dataset, phenology, BBCH stage, weekly field observation, GDD, chilling, Sentinel-2 NDVI, reanalysis gap filling, FAIR]
records: []
datasets: [lacuevaperez2026.aragon_phenology]
files: [syn1027_lacueva2026preprint.pdf (the 2026-10-27 drop)]
---

# Lacueva Pérez et al. 2026: the Aragon multisource grapevine phenology dataset, 18,231 weekly stage calls with weather and NDVI (preprint)

A data note (Research Square preprint) that builds and describes a machine-learning-ready table of grapevine stage observations in three Aragon wine regions, 2016-2022, joined to station weather, heat and chill indices and Sentinel-2 NDVI. No record: a dataset.

**Same dataset as lacuevaperez2026dif.** That note covers the data description PDF deposited with the Zenodo files (lacueva2025aragon in the drop). Both describe Zenodo 10.5281/zenodo.20124340 (this preprint, l. 650, 847), with the same five authors; this one adds the design, the repository survey, the counts and the registry's defects. A discrepancy between the two is flagged in the other note.

**Read this first.** A preprint. Its Table 2 lists the California winegrape set (Parker et al. 2024) among "related phenology datasets" with budbreak, flowering, veraison and maturity and does not say they are modelled (l. 314-320); the reading agent's check of that paper shows the stage dates are model output (see parker2024). The stage labels come from a restricted registry (Red FARA), merged and translated from Baggiolini to BBCH by the authors (l. 403-409).

## What it holds

- **Where to get it** (l. 650, 847): Zenodo record 20124340, DOI 10.5281/zenodo.20124340 (a dataset reference in the list, l. 847); code on GitHub (l. 112-113, 345). Licence stated by the paper: CC BY 4.0 (l. 27, 556-557). The record's file sizes (CSV 492.6 MB) are from the description note.
- **Years, sites** (l. 308-311, 420): 18,231 phenology samples recorded in the Red FARA for 2016-2022 (l. 420) in three PDOs (Calatayud, Campo de Borja, Cariñena), about 8,500 km2 and about 18,000 ha of vineyard at 300 to 1,000 m (l. 308-309). The paper does not say that all 18,231 are in the released table.
- **Observation protocol** (l. 403, 338): the Aragon plant-health network samples weekly (plus or minus 3 days) under a protocol based on the Baggiolini scale; only 2016-2022 is used because Sentinel-2 starts in 2016; the text says data are available since 2010 (l. 404-406) and Table 3 says since 2009 (l. 338).
- **Stages** (l. 409-412, 366): 17 grapevine stages recorded, 9 kept for their link to powdery mildew, downy mildew, Botrytis and Lobesia botrana risk, with added states 00 and 99.
- **Weather** (l. 336-341, 477-483): 9 SIAR stations within 15 km of the PDOs since 2009 and 14 Grapevine-project stations since 2021, each every 30 minutes; temperature, precipitation, humidity, wind speed and direction; occasional gaps filled from ERA5 via Open-Meteo, precipitation halved to match 30 minutes (a model fill; the fill rate is not stated in the lines read).
- **Indices** (l. 484-499): GDD and Winkler with base 4.5 and 10 C and a 40 C cap (the description says 35 C), chill hours and the Utah model, a wind index in 8 sectors; 110 climatic variables, 591 with the values of each day two weeks before, one week before and one week after the index date (l. 494-499).
- **Satellite** (Table 3, l. 336-341): Sentinel-2 NDVI at 5 days since 2016.
- **Label quality** (l. 424-433): stage 99 is up to four times as frequent as stage 00 (l. 424); flowering stages 63, 65 and 68 are under-represented (l. 426); some parcels show stages that jump backward between visits (l. 431), and some jumps came from a bug in the registry's app, since corrected (l. 433). So the labels carry human and software noise.
- **Repository survey** (Table 1, l. 277-281): Zenodo returned 2 datasets for "grapevine phenology" out of 469,506; Mendeley 87 hits, mostly irrelevant. Cited as the authors' search, not checked.
- **How labels were made:** weekly visual stage calls by field technicians; weather gaps by ERA5 (model); heat and chill sums computed; NDVI computed. Nothing in the stage label is computed by a phenology model.

## Dependence

- Labels depend on the Red FARA protocol and on the authors' Baggiolini-to-BBCH translation. ERA5 fills weather gaps. The group's modelling article (Comput. Electron. Agric. 231:110018, not read) is where scores for models trained on this table would be; none are in this preprint's lines read. The group also made a powdery mildew table from the same registry (not read here).

## Bearing (2026-10-27)

- **D60 tiers 1 and 2 plus satellite NDVI; real-data side of D58 for phenology.** The one open set found with weekly real stage calls, matched T, RH, rain, radiation and wind over seven seasons. D58 could use it to judge a phenology or heat-sum variable the simulator has screened; D60 could use it to test a filled or synthetic weather input against 30-minute stations.
- **Not disease, and stages stop at start of ripening (BBCH 81).** The preprint chooses stages for pest-risk links, but carries no outbreak outcome.
- **Limits:** a preprint with no model scores in what was read; a restricted source registry (only the merged table is open); one region; label noise the authors flagged; time-shifted columns that include days after the record date, so any "prediction" must drop them; the fill rate of ERA5 is not stated.

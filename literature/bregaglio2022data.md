---
id: bregaglio2022data
citation: Bregaglio, Simone, Savian, Francesco, Raparelli, Elisabetta, Morelli, Danilo, Epifani, Rosanna, Fila, Gianni & Manici, Luisa M. 2022. Datasets of harmonized risk assessment of grapevine downy mildew and phenological observations in eight Italian regions (2012-2017). Data in Brief 43: 108409
doi: 10.1016/j.dib.2022.108409
read: 2026-10-22, in full (Europe PMC full text PMC9253452, no figures) by the main session; the Mendeley Data deposit not downloaded
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy, Abruzzo, Basilicata, Emilia-Romagna, Liguria, Lombardia, Marche, Sardegna, Veneto]
processes: [infection risk, phenology, warning service]
records: []
datasets: [bregaglio2022.bulletins]
files: [PMC9253452.xml (Europe PMC full text, the 2026-10-22 drop)]
---

# Bregaglio et al. 2022 (data paper): the bulletin risk classes and BBCH stages behind MISFITS

The data paper for the reference data of `bregaglio2022` (the MISFITS decision support system). Weekly bulletins from eight Italian regional plant protection services, 2012-2017, read by six evaluators into a five-class downy mildew infection risk, with the grapevine stages the bulletins report.

**Open data:** Mendeley Data, doi 10.17632/3jsh4y2bw4.1, CC BY 4.0 (l. 4, 29).

## What it holds

- 9,007 records (l. 47). Of these, 8,816 are risk classes on a five-point scale, from very low (1) to very high (5). They cover eight regions and 31 provinces (l. 55-58).
- 1,689 BBCH observations, for the main early and late varieties of each area (l. 36, 80). Some were transcribed and some inferred from the bulletin's description.
- **Criteria** (l. 79): the evaluators set each class from (i) symptoms in field surveys, (ii) host phenological susceptibility, (iii) the weather forecast, and the bulletin's own indication.
- "This dataset has been used to calibrate and evaluate the MISFITS-DSS" (l. 78).

## Dependence

- These are the classes `bregaglio2022`'s infection parameters were chosen against. That note records it, and also records that the classes were set partly from the bulletins' own model-based indications. So the data are risk as the services judged it, partly by model, not observed disease.
- The same group's octoPus random forest (`bregaglio2024`) was calibrated on provincial risk scores read from bulletins of 2012-2017. That note's account of those scores matches this dataset, but the octoPus paper's own data citation was not checked here: inferred, not stated.

## Bearing (2026-10-22)

- **Not a truth pattern** for Agrarium, for the reason above.
- **For Cooptera:** a check of when the regional services judged risk high, beside the engine's alerts, in 31 Italian provinces over six seasons. A model that shaped these classes would be favoured: the bulletins' models are unnamed.
- The BBCH observations (1,689, by province and early or late variety) are a phenology check independent of any disease model.

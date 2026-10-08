---
id: bregaglio2022
citation: Bregaglio, Simone, Savian, Francesco, Raparelli, Elisabetta, Morelli, Danilo, Epifani, Rosanna, Pietrangeli, Fabio, Nigro, Camilla, Bugiani, Riccardo, Pini, Stefano, Culatti, Paolo, Tognetti, Danilo, Spanna, Federico, Gerardi, Marco, Delillo, Irene, Bajocco, Sofia, Fanchini, Davide, Fila, Gianni, Ginaldi, Fabrizio & Manici, Luisa M. 2022. A public decision support system for the assessment of plant disease infection risk shared by Italian regions. Journal of Environmental Management 317:115365
doi: 10.1016/j.jenvman.2022.115365
read: 2026-10-08, abstract, sections 1-5, Tables 1-7 and captions, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy]
processes: [primary infection, secondary infection, phenology]
records: [magarey2005.generic]
datasets: []
files: [10-1016-j-jenvman-2022-115365.pdf]
---

# Bregaglio et al. 2022: MISFITS, a public infection-risk system for Italian regions

From CREA with nine regional plant protection services; downy mildew is the pilot disease.

## What it holds

- A decision support system built by CREA with nine regional plant protection services (l. 54); downy mildew is the pilot disease.
- Reference data: 1579 weekly regional bulletins, 31 NUTS-3 units, 2012-2017 (l. 162). Evaluators set a 5-point risk class, using the bulletin's own model-based indication where there was one (l. 176).
- Weather is ERA5-Land at 9 x 9 km (l. 185); leaf wetness is estimated with Kim et al. 2002.
- Primary infection starts at BBCH 01 (l. 236). Macrosporangia development uses Eq. 4, credited to Magarey et al. 2005 (l. 302).
- Table 5 defaults, from the METOS service (l. 347): TnM 10, ToM 18, TxM 24 deg C; LWnM 15 h, LWoM 24 h; RHnM 70 %; PrecZ 5 mm; TnPI 6, ToPI 28, TxPI 22 deg C; LWnPI 2 h, LWoPI 9 h (l. 391-407). TxPI is below ToPI as printed.
- Only phenology is fitted (1689 BBCH observations, l. 167). Infection parameters are screened by Morris and the best of 1000 sets is picked by Random Forest accuracy against the bulletin risk (88% balanced accuracy, l. 64).
- The authors say direct testing against field data is still needed (l. 680).

## Dependence

- **It computes Magarey et al. 2005's wetness function** (its eq. 4, l. 302): a borrowed equation, so kin to the engine's Magarey and Brischetto pieces.
- Its default parameters come from the METOS service, whose derivation is not stated (l. 347).
- **Its reference data were shaped by models:** evaluators set each risk class partly from the bulletin's own model-based indication (l. 176), the models unnamed. Its infection parameters were then chosen by accuracy against those classes: calibrated with unknown models, a flag to settle before trusting its parameters as independent.
- Bugiani and Spanna (regional services) are authors of the engine's Rossi pieces: flags.

## Bearing (2026-10-08)

- **Kin by a borrowed equation**, now recorded as such. Its 1579 weekly regional bulletins, 2012-2017, are not observations of disease but of risk as the services judged it, partly by model; not a pattern for a truth.

---
id: bregaglio2024
citation: Bregaglio, Simone, Rossi, Eugenio, Ascari, Lorenzo, Mongiano, Gabriele, Del Cavallo, Eleonora, Bajocco, Sofia, Manici, Luisa Maria, Pepe, Antonio Gerardo, Bassi, Chiara, Tiso, Rocchina, Pietrangeli, Fabio, Cattaneo, Giovanna, Nigro, Camilla, Gerardi, Marco Secondo, Bussotti, Simone, Sanchioni, Angela, Tognetti, Danilo, Sandra, Mariangela et al. (byline not seen in full). 2024. Releasing the octoPus, an open-source digital tool to promote Integrated Pest Management. bioRxiv preprint 2024.08.07.606987; published in Smart Agricultural Technology 2025 (doi 10.1016/j.atech.2025.101015) and, as a software paper, SoftwareX 2025 (doi 10.1016/j.softx.2025.102085), neither read
doi: 10.1101/2024.08.07.606987
read: 2026-10-13, in full (the preprint text; its supplement S1 with the model equations is not in the copy), by a reading agent (claude-haiku-5-5); 56 of 56 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy, 531 ERA5 cells, ten regions]
processes: [primary infection, forecasting, phenology, host susceptibility, model ensemble, decision support]
records: []
datasets: []
files: [bregaglio2024_biorxiv.pdf]
---

# Bregaglio et al. 2024: the octoPus, eight primary-infection models in one open tool

CREA's open-source downy mildew tool (the bioRxiv preprint; the Elsevier versions are
blocked from this machine, `INDEX.md` of the drop): a phenology and susceptibility model
("eyes"), eight primary-infection models from the literature run as an ensemble
("tentacles"), a random forest that turns them into a 1-5 risk ("brain") and an LLM that
writes the message ("mouth") (l. 193). Its value here is the list of the eight models and
their printed sources, and the comparison of their seasonal outputs across Italy.

## What it holds

- **Inputs:** ERA5 hourly reanalysis at 0.25°, 531 cells over Italy, 2000-2021, including a
  leaf wetness scaled 0-1 whose derivation is not printed (l. 232-234): model products,
  not observations.
- **Phenology and susceptibility:** a daily chilling-forcing model (Cesaraccio's dormancy
  coupled to Yan & Hunt 1999's forcing with cardinal temperatures 10, 20 and 35 °C),
  chilling requirement and BBCH thresholds fitted by downhill simplex to 2,189 BBCH
  records from ten regions, 2012-2017, one ERA5 cell a province for calibration and the
  others for validation; RMSE 9-10 d for leaf, inflorescence, flowering and fruit stages,
  16 d for maturity (l. 240-262, 414-416; 8.3-9.4 d against 10-10.5 for the group's
  earlier thermal-time model, l. 432). Susceptibility 0-100 % by BBCH phase from expert
  surveys (l. 265-266).
- **The eight models, as printed** (Table 1's footnote, l. 312; rules in the text):
  Rule310, the 3-10 rule credited to Baldacci 1947 (daily temperature above 10 °C, more
  than 10 mm in 48 h, BBCH above 10; l. 319); Laore, an hourly temperature × wetness index
  with threshold 13 here, from Reis et al. 2013 (l. 321); DM-Cast (Park et al. 1997), a
  Gaussian oospore-germination function at daily step (l. 324); EPI (Strizyk 1983; Tran
  Manh Sung, 1987 in the text and 1990 in the list) with its October-March oospore
  period (l. 326); UCSC, the hourly process model of Rossi et al. 2008 (l. 329); IPI
  (Gherardi 2001), a daily index summed to a threshold (l. 333); Misfits, the authors'
  own 2022 model (l. 346); Magarey (Magarey et al. 1991), a primary infection above 45
  degree-hours of wetness (l. 349-353). All run 1 April to 31 July with binary daily
  output (l. 353); their equations are in supplement S1, not in the text; parameter
  counts 1 to 10 (Table 1).
- **Their behaviour, 2001-2020:** seasonal infections in the order DM-Cast > IPI > EPI >
  UCSC > Rule310 > Laore > Misfits > Magarey (l. 488); in the Mild-Wet cluster from 7.6
  (Magarey) to 24.6 (EPI) a season, in the Cold-Wet DM-Cast 14.1 and UCSC 11.8 against
  under 5 for Laore, Misfits and Magarey (l. 493-505); four weather clusters from a PCA
  (82 % in two components; Hot-Dry 158 mm and 511 wet hours against Mild-Wet 385 mm and
  987 h; l. 459-475); very high simulated pressure in 2002, 2014, 2016, 2018, very low
  in 2003, 2005, 2006, 2017 (l. 585-604), checked against trade press and conference
  reports, since "official data on actual pathogen pressure are not available" (l. 612).
- **The random forest:** 1,781 provincial risk scores (1-5) read from regional bulletins by
  six evaluators, called "observed" (l. 362-364, 632); 70/30 split, four-fold
  cross-validation, RMSE 0.77 and R² 0.42, validation RMSE 0.74 and R² 0.46 (l. 368,
  622-624); importance: susceptibility 100, Rule310 82.7, Misfits 71.2, Magarey 41.1
  (l. 625). Llama 2 7B writes the advice (l. 373). The repository is named, no licence
  (l. 227, 741).
- **Cited leads:** Caffi et al. 2007's Sardinian comparison of Rule310, EPI, DM-Cast and
  UCSC, 1996-2004 (l. 533; `caffi2007` records the Siniscola data); Rossi et al. 2008's 3-8
  primary infections a season in Emilia-Romagna 1995-2006 (l. 610); Dalla Marta et al.
  2005's 3-29 in Tuscany 1995-2003 (l. 611, missing from the reference list).

## Dependence

- **Computes** Rule310, EPI, DM-Cast, UCSC (`rossi2008.primary`), IPI, Laore, Misfits and
  Magarey 1991's rule, in an ensemble; the engine's `rule_3_10` and `rossi2008.primary` are
  two of its eight; the phenology is a chilling-forcing threshold model fitted to regional
  BBCH records.
- **Calibrated on** bulletin readings (the random forest), which regional services issue
  from their own models and scouting: a model-shaped reference, unprinted provenance.
- **Authors:** Bugiani (`rossi2008`), Bregaglio (`bregaglio2013`, `bregaglio2022`): flags.

## Bearing (2026-10-13)

- A map of the Italian primary-infection models with their sources in one place, and the
  first side-by-side count of what they predict across climates: DM-Cast and EPI call
  three times as many infections as Magarey's rule in the same weather. For Agrarium's
  truth it is a list of what not to share; for Cooptera, a comparator ensemble. The
  equations live in a supplement and the code, not in this copy.

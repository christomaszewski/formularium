---
id: gonzalezdominguez2015
citation: González-Domínguez, Elisa, Caffi, Tito, Ciliberti, Nicola & Rossi, Vittorio. 2015. A mechanistic model of Botrytis cinerea on grapevines that includes weather, vine growth stage, and the main infection pathways. PLoS ONE 10(10):e0140444
doi: 10.1371/journal.pone.0140444
read: 2026-10-10, in full, equations 1-11 in the page images, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py
status: read
diseases: [grey mould]
crops: [grapevine]
regions: [Italy]
processes: [infection, sporulation, host susceptibility]
records: []
datasets: [gonzalezdominguez2015.epidemics]
files: [gonzalez2015_botrytis_plosone.pdf]
---

# González-Domínguez et al. 2015: a mechanistic Botrytis model from Piacenza

## What it holds

- Daily; two infection windows (flowering to fruit set, ripening), three pathways.
  Equations from Ciliberti et al. 2015 and Deytieux-Belleau 2009, e.g. mycelium growth
  (3.78 Teq^0.9 (1 - Teq))^0.475, infection (3.56 Teq^0.99 (1 - Teq))^0.71 / (1 +
  e^(1.85 - 0.19 WD)) x susceptibility. The authors say the equations "were not validated
  against independent data".
- 21 untreated epidemics in 12 vineyards, 2009-2014, with on-site hourly weather:
  discriminant analysis puts 17 of 21 in the right severity group, 15 of 21 cross-validated.
- Broome et al. 1995 and Nair & Allen 1993 are cited as unvalidated, not used.

## Dependence

- None on the engine's Broome index. Rossi and Caffi are engine authors: flags.

## Bearing (2026-10-10)

- For Cooptera: a Botrytis model independent of Broome's, with 21 epidemics of data.

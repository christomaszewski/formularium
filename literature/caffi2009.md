---
id: caffi2009
citation: Caffi, T., Rossi, V., Bugiani, R., Spanna, F., Flamini, L., Cossu, A. & Nigro, C. 2009. A model predicting primary infections of Plasmopara viticola in different grapevine-growing areas of Italy. Journal of Plant Pathology 91(3):535-548
doi:
read: 2026-10-08, pages 1-14 in full, from an OCR (the byline confirmed in Carisse et al. 2021's references), by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy]
processes: [primary infection, season onset]
records: [rossi2008.primary]
datasets: []
files: [20093361817.pdf]
---

# Caffi et al. 2009: the Rossi model of primary infections tested across Italy

From the Università Cattolica, Piacenza, with regional plant protection and agrometeorological services. The text copy in the drop holds only download watermarks; the reading agent made its own OCR of the PDF, to which the line numbers refer.

## What it holds

- Caffi et al. test the Rossi et al. 2008 mechanistic model (l. 118) against observed first onsets of downy mildew.
- Vineyards: 100, in six Italian regions, 1995-2007 (l. 270). An unsprayed plot of at least 500 m2 was inspected at least weekly from bud burst (l. 279, 283). Onset is a window between the last negative and first positive visit (l. 377). Weather came from the nearest station within 15 km (l. 295).
- First onsets ran from 7 May to 11 July; the mean was 26 May (l. 407, 412). Nine vineyards had no disease (l. 413).
- 922 simulations: 29% infections, 71% aborted (l. 424). In vineyards, TPP 1.00 and TNP 0.88 (657 of 748), FPP 0.12 (l. 764, 634).
- Potted vines: 42 groups on artificial leaf litter, 2005-2008 (l. 326); 20 groups infected (l. 869); TPP 0.95 (l. 874); FPP 0.27 (l. 989).
- Combined: sensitivity 0.99, specificity 0.87 (l. 1002).
- A score depends on the model: an onset explained by another successful simulation counts as accurate (l. 369).
- Aborted simulations are not verified in the field (l. 1077). No calibration was done (l. 1158).
- Use for onset observation (weekly windows), not as a formulation.

## Dependence

- **It evaluates the engine's `rossi2008.primary`** (l. 118); no calibration (l. 1158).
- Its scoring leans on the model: an observed onset counts as explained when another successful simulation explains it (l. 369).
- Caffi, Rossi, Bugiani and Spanna are authors of engine models: one group, flags.

## Bearing (2026-10-08)

- **Its observed onsets are data** a truth could be matched to: 100 vineyards in six regions, 1995-2007, first onsets 7 May to 11 July (l. 407-412), weekly windows (l. 377). The scores are the engine model's, and say how well the engine's primary infection did in Italy (sensitivity 0.99, specificity 0.87 combined, l. 1002).

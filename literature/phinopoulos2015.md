---
id: phinopoulos2015
citation: Phinopoulos, V., Cadima, J. & Lopes, C. M. 2015 (year not printed; the 19th GiESCO meeting). Estimation of leaf area in grapevine cv. Syrah using empirical models. Proceedings of the 19th International Meeting of Viticulture GiESCO, pp. 385-388
doi:
read: 2026-10-26, a light reading by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Eqs 3-5 and Fig. 1 (printed pp. 387-388) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Lisbon]
processes: [leaf area, allometry, shoot leaf area]
records: [phinopoulos2015.shoot_leaf_area]
datasets: [phinopoulos2015.lisbon]
files: [phinopoulos2014.pdf (the 2026-10-25 other-sources drop, from Repositório ULisboa)]
---

# Phinopoulos et al. 2015: Lopes & Pinto's shoot leaf area model refitted on Syrah

A single Syrah leaf's area from the sum of its two lateral veins, and primary and lateral
leaf area per shoot from the leaf count and the largest and smallest leaf, the Lopes & Pinto
2005 variables refitted in log-log form on 210 shoots sampled through 2013 at Lisbon.

## What it holds

- **Material** (l. 85-99): Syrah on 140 Ru at the ISA vineyard, Tapada da Ajuda, Lisbon
  (38°42' N), planted 1998, 3333 vines/ha, not irrigated in 2013; 30 fruiting shoots on
  seven dates from inflorescences visible to veraison, April to July 2013; laterals from the
  fourth date; leaf areas by a Delta-T meter to 1 cm²; leaves kept when the primary vein is
  at least 30 mm.
- **Variables** (l. 104-105): M1 = (L1 + S1)/2 and MSLA1 = M1 × NL1 as in Lopes & Pinto 2005.
- **Eq. 3, single leaf** (l. 144-147): ln LA1 = -6.436 + 2.167 ln V2S, V2S the sum of the two
  lateral vein lengths in mm; R² 0.97, n 2518, mean square error 13.6 cm². The linear fit
  in Fig. 1 A is LA1 = 1.1613 V2S - 79.275, R² 0.91.
- **Eq. 4, primary shoot** (l. 168-171): ln SLA1 = -0.067 + 1.018 ln MSLA1; R² 0.98, n 210,
  MSE 121.9 cm²; Fig. 1 B's linear fit SLA1 = 1.0543 MSLA1 + 12.501, R² 0.96.
- **Eq. 5, lateral shoot** (l. 189-192): ln SLA2 = 0.491 + 0.802 ln MSLA2 + 0.207 ln NL2 +
  0.048 ln S2; R² 0.98, n 120, MSE 104.9 cm²; NL2 and S2 add partial R² of 0.01 and 0.002.
- **Not printed:** the journal, year and DOI (the reference list cites Döring 2013 and the
  author's 2013 MSc thesis, so 2015, the 19th GiESCO), coefficient errors, what n 2518
  counts, the single lateral leaf model (data not shown, l. 152).

## Dependence

- **Fitted to** `phinopoulos2015.lisbon`, observed areas; nothing model-dated.
- **Shares the form** of `lopes2005.shoot_leaf_area` (the variables and the log-log fit,
  l. 19-20, 77-78, 163-164), with its own coefficients; Lopes is an author of both (a flag
  as well as a shared form).

## Bearing (2026-10-26)

- For Agrarium's leaf-area allometries (the 10-14 search): Lopes & Pinto's form holds for
  Syrah with a slope near 1 on MSLA1; the single-leaf vein relation is the piece for a leaf
  measured in the field. Kin by form to lopes2005 and sanchezdemiguel2011; not to the engine.

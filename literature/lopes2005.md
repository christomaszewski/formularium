---
id: lopes2005
citation: Lopes, C. & Pinto, P. A. 2005. Easy and accurate estimation of grapevine leaf area with simple mathematical models. Vitis 44(2):55-61
doi: 10.5073/vitis.2005.44.55-61
read: 2026-10-26, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; Eqs 8-11 and Tables 1-4 (printed pp. 57-59) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Alentejo, Évora, Dão]
processes: [leaf area, allometry, shoot leaf area]
records: [lopes2005.shoot_leaf_area]
datasets: [lopes2005.estremoz]
files: [lopes2005.pdf (the 2026-10-25 other-sources drop)]
---

# Lopes & Pinto 2005: leaf area per shoot from three leaf measurements

Primary and lateral leaf area of a shoot from the number of leaves and the areas of the
largest and smallest leaf, fitted on cv. Aragonez at Estremoz and checked on four other
sets. The form later refitted by Sánchez-de-Miguel et al. 2011 for Madrid.

## What it holds

- **Calibration shoots** (l. 80-121): Estremoz, Alentejo, 1997, 8-year-old Aragonez on 1103
  Paulsen; 30 shoots on each of six dates from April to August: 180 shoots, 107 with laterals.
- **Variables** (Eqs 1-2, l. 116-117): M1 = (L1 + S1)/2, the mean of the largest and smallest
  primary leaf areas, and MLA1 = M1 × NL1, the mean primary leaf area per shoot; the same for
  laterals (L2, S2, NL2, MLA2). Leaf areas by a Delta-T meter.
- **Eq. 8, primary, linear** (l. 225-226): LA1 = 49.1936 + 0.9958 MLA1 (cm²), R² 0.97, n 180,
  RMSE 150.6 cm². Chosen by stepwise regression (entry F 0.15); residuals grow with the
  predictor, so the log form follows.
- **Eq. 9, primary, log** (l. 259-260): LA1 = exp(0.0835 + 0.992 ln MLA1), R² 0.99, n 180,
  RMSE 152.7 cm². Natural logs, applied to both sides (l. 228, 258).
- **Eq. 10, lateral, linear** (l. 231-233, 327): LA2 = 78.01726 - 1.16773 L2 + 1.00848 MLA2,
  R² 0.97, n 107, RMSE 97.9 cm²; L2 adds a partial R² of 0.001 (l. 316-324).
- **Eq. 11, lateral, log** (l. 246-248): LA2 = exp(0.346 + 1.029 ln MLA2 - 0.125 ln L2),
  adjusted R² 0.98, n 107, RMSE 93.2 cm².
- **Validation** (l. 72-78, Tables 3-4): Aragonez at Évora 1997 (130 shoots; 156 in
  Table 4, unexplained), Cabernet-Sauvignon 2002 (80), Touriga Nacional 1994 (168) and Jaen
  2001 (230) in the Dão. Primary MA%E 7.1-8.8 %, EF 0.97 over 608 shoots (l. 339-343), all
  slopes above 1; lateral MA%E 6.1-15.5 % (l. 383-387).
- **Season** (Fig. 1): primary leaf area per shoot 0.06 to 0.24 m², laterals to 0.11 m².
- **Not printed:** coefficient standard errors, residual SD, how the validation areas were
  measured.

## Dependence

- **Fitted to** `lopes2005.estremoz`; validated on independent sets of the same region and
  season for Aragonez (l. 72-74). Observed areas, no model in the data.
- **Builds on** Lopes & Pinto 2000 (the predecessor shoot model) and the three-leaf method of
  Barbagallo et al. 1996 (cited). Schultz 1992 is cited for a vein method (l. 29) and a
  temperature-based leaf area model (l. 51).
- **Refitted by** Sánchez-de-Miguel et al. 2011 (`sanchezdemiguel2011.leaf_area`): the same
  log-log form on MLA, with base-10 powers printed there; the catalogue's note said "log10"
  of this form and is corrected to say the base differs (read here 2026-10-26).

## Bearing (2026-10-26)

- For Agrarium's `host.leaf_area_max_m2` and the allometry records (the 10-14 search): a
  printed, validated shoot-area allometry needing a leaf count and two leaf areas. Kin by
  form (allometry) to `sanchezdemiguel2011.leaf_area` and `lebon2004.leaf_development`; not
  to anything the engine runs.

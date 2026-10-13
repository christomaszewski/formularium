---
id: caffi2013
citation: Caffi, Tito, Gilardi, Giovanna, Monchiero, Matteo & Rossi, Vittorio. 2013. Production and release of asexual sporangia in Plasmopara viticola. Phytopathology 103(1):64-73
doi: 10.1094/PHYTO-04-12-0082-R
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 50 of 50 quotes found at their lines by scripts/verify_quotes.py; the abstract, Methods and the ROC and monomolecular results (pp. 64-65, 68) read in the page images by the main session; held since 2026-10-07 as the engine's sporulation source, read then by Agrarium without a note
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Piedmont, Grugliasco, Neive, Piacenza]
processes: [sporulation, sporangia production, sporangia release, airborne inoculum, infectious period]
records: [caffi2013.sporulation]
datasets: [caffi2013.piedmont]
files: [2013-caffi-10-1094-phyto-04-12-0082-r.pdf]
---

# Caffi et al. 2013: sporulation in the vineyard, and the three-moist-dark-hour rule

The source of the engine's `caffi2013.sporulation` ("sporulation nights: three moist dark
hours"). Held since 2026-10-07; this is its note, with the rule's exact terms, its data
and its printed accuracy.

## What it holds

- **Field data** (`caffi2013.piedmont`): two unsprayed 150-vine sections in Piedmont,
  Grugliasco (Moscato, planted 2001, 260 m, "usually very favorable" for downy mildew)
  and Neive (Barbera, planted 1965, 280 m), inspected every second or third day from
  about mid-May to mid-June or late July, 2008-2010; diseased leaves removed after each
  count so only fresh lesions were seen (l. 83-100). 100 assessments, 58 with new lesions,
  61,921 lesions, 14,761 of them sporulating (23.8 %); the share with sporangiophores
  averaged 41.3 % in 2008, 32.3 % in 2009 and 6.7 % in 2010 (l. 182-187). Hourly weather
  from the regional service's stations at the vineyard edges (l. 112), with a "climatic
  day" from 13:00 to 12:00 (p. 65).
- **The rule** (read in the images): "dark, moist hours" are the hours between 20:00 and
  07:00 with RH ≥ 80 %, rain > 0 mm or wetness duration > 30 min (abstract, Table 3
  footnote f); the Methods print the same with "and" and WD > 0.5 h (l. 121), a printed
  inconsistency the paper never resolves. In a ROC analysis across the 58 assessments,
  dark moist hours had AUROC 0.816 (P < 0.001), against 0.59-0.68 for temperature, RH,
  rain, wetness and VPD variables and 0.65 for hours of RH ≥ 80 % (Table 3, l. 213-218);
  the cut-off of ≥ 3 h gave overall accuracy 0.85, sensitivity 0.91, specificity 0.67,
  false-negative proportion 0.09, likelihood ratios 5.74 and 0.14 (l. 32, 220, 282-287).
  Sporulation was found in 0.6 % of assessments with no dark moist hours, 13.5 % with one,
  43.8 % with 11 or 12 (l. 219). No temperature bound belongs to the rule; a 90 % RH
  threshold did not predict sporulation (l. 479).
- **Production per lesion:** 227 inoculated lesions on potted Barbera at Piacenza and in
  the Moscato vineyard, 10 inoculations 2008-2010, 15 sporulation periods (l. 109-110,
  292); cumulative relative sporulation Y = 1 − (1 − 0.123)·exp(−0.427 X), standard
  errors 0.096 and 0.041, R² 0.97 (l. 286-288; X is the day of the event in the Methods,
  the duration in days in the Results, l. 171-172, 285); 382 to 2.7 million sporangia per
  mm² of lesion over an infectious period of 6.7 ± 0.6 d (2 to 10, median 7; l. 291,
  304); 35.5-68.0 % of harvested sporangia germinated (l. 297); per-lesion totals rose
  with average RH (r = 0.78, n = 15) and with the moist-hour ratio (ln Y = 6.31 X + 12.1,
  R² 0.64) and fell with maximum temperature (R² 0.35) (l. 351, 449-452).
- **Release:** a spore sampler at 150 cm in the Moscato vineyard, 2 July to 17 October
  2009, and samplers beside potted sources at Piacenza (l. 144-165); airborne sporangia
  on 271 of 297 days (91.2 %), 0.1 to 732 per m³ a day (median 3.6), rain on only 26 % of
  trapping days; caught in 1,816 of 3,514 two-hour periods (l. 358-362, 421). So rain is
  not needed for release; dew suffices (l. 543-545).
- **Cited models:** Lalancette et al. 1988 for the 10 and 30 °C sporulation limits (l. 56),
  Blaeser & Weltzien 1978 for the RH requirement (l. 55); MILVIT, DMCast and PLASMO
  (Orlandini 2008) rest on controlled-environment sporulation studies needing 4-7 h of RH
  above 90 % (l. 476, 488); Pearson & Goheen 1988's 4 h at 95-100 % RH in darkness
  (l. 475).

## Dependence

- **Fitted to its own field assessments** (`caffi2013.piedmont`), observed, with weather
  from regional stations: the rule's threshold was chosen by ROC on them (l. 213-220).
  No model dated anything.
- **Borrows no equation:** Lalancette 1988 and Blaeser & Weltzien 1978 are cited for
  qualitative points; Kennelly et al. 2007's lesion-washing method is used (l. 154).
- **The engine's piece:** `caffi2013.sporulation` is the ≥ 3 dark moist hours rule; its
  record now carries the printed thresholds, the dataset and the and/or inconsistency.
  `brischetto2021.*` computes it (recorded already); VitiMeteo's sporulation rule (4 h
  dark above 12 °C at RH > 92 %, `dubuis2012`) has the same form from Bläser & Weltzien.
- **Authors:** Caffi and Rossi: flags across the Piacenza models.

## Bearing (2026-10-12)

- The record is read and complete. For a truth: a night-sporulation rule of this form is
  the engine's; the paper's own numbers show it misses 9 % of sporulation events and
  calls a third of the dry nights sporulating, which is the error a truth must not share.
  The per-lesion production curve and the 6.7 d infectious period are independent
  quantities a truth could draw from, since no tool runs them.

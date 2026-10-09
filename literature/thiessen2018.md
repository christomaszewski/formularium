---
id: thiessen2018
citation: Thiessen, L. D., Neill, T. M. & Mahaffee, W. F. 2018. Assessment of Erysiphe necator ascospore release models for use in the Mediterranean climate of western Oregon. Plant Disease 102(8):1500-1508
doi: 10.1094/PDIS-10-17-1686-RE
read: 2026-10-08, in full (equations 1-5 partly garbled) by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, the rule and dependence by the main session
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Oregon]
processes: [ascospore release]
records: [thiessen2018.ascospores]
datasets: []
files: [10-1094-pdis-10-17-1686-re.pdf]
---

# Thiessen, Neill & Mahaffee 2018: ascospore release models in Oregon

From Oregon State University and USDA-ARS, Corvallis. The paper behind the engine's
`thiessen2018.ascospores`, which Formularium recorded as "not held".

## What it holds

- **Data:** chasmothecia from four vineyards on bark in outdoor arrays, with spore-trap rods
  read by qPCR twice a week through three dormant seasons, 2012-13 to 2014-15 (l. 95, 139,
  231-232): 1,945 array samples (l. 226). Test data: three traps by infested trunks at the
  research vineyard, 357 samples; an event is 2 of 3 traps positive (l. 152, 227).
- **Models tested** did poorly: the UC Davis index 52% accurate (l. 251), Gadoury & Pearson
  61% (l. 254-255), Moyer's and Caffi's binary forms 55% and 57% (l. 263, 272); Moyer's and
  Caffi's magnitudes had R² = 0 (l. 259-260, 269).
- **The Oregon model (eq. 5):** A = WT4 × P × R (l. 281): release when, within a 24-h
  period, leaf wetness lasts more than 6 h above 4 °C, rain exceeds 2.5 mm and RH exceeds
  80% (l. 276-278). Accuracy 66% (l. 284); Table 1 gives 15 true positives, 29 false
  positives, 12 false negatives and 63 true negatives (l. 314-315). The paper's
  "sensitivity" (68%) and "specificity" (56%) use swapped definitions (l. 165-166, 286).
- About 87% of ascospores were caught before bud break (l. 417). The authors call Gadoury
  & Pearson's, UC Davis's and their own about equally representative (l. 481).
- Ambiguities: the discussion says daily mean RH and rain of 2.5 mm or more (l. 484-485);
  the 24-h window is not defined. Moyer's and Caffi's equations are garbled in the text
  copy.

## Dependence

- The 4 °C and 2.5 mm thresholds are Gadoury & Pearson 1990a's release conditions (l. 34);
  the 6 h and 80% were chosen from variables "correlated with" the detections (l. 273-274),
  with no fit shown. The test vineyard also supplied chasmothecia to the arrays (l. 120,
  145).
- Mahaffee and Neill are flags for other papers (Heger 2026, Miller 2018).

## Bearing (2026-10-08)

- The engine's record can become `read`, with initials L. D., T. M. and W. F.; told to
  Cooptera, with the rule as printed so it can check its code against it.
- Its own test shows release models near chance in Oregon's winters: a truth's ascospore
  release should not lean on any of them without wide sweeps.

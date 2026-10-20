---
id: fedele2020b
citation: Fedele, G., González-Domínguez, E., Delière, L., Díez-Navajas, A. M. & Rossi, V. 2020. Consideration of latent infections improves the prediction of Botrytis bunch rot severity in vineyards. Plant Disease 104:1291-1297
doi: 10.1094/PDIS-11-19-2309-RE
read: 2026-10-20, in full, by a reading agent (claude-haiku-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [grey mould]
crops: [grapevine]
regions: [Italy, France, Spain]
processes: [model validation, latent infection, bunch rot severity]
records: [gonzalezdominguez2015.botrytis]
datasets: []
files: [fedele_2020.pdf (the 2026-10-20 drop)]
---

# Fedele et al. 2020: the Piacenza Botrytis model on 23 new epidemics, with latent infections

The González-Domínguez et al. 2015 model, run unchanged, against 23 untreated bunch rot
epidemics in Italy, France and Spain (1997-2018), with symptomless berries incubated to
reveal latent infections in the ten epidemics without field rot.

## What it holds

- Validates the González-Domínguez et al. (2015) Botrytis bunch rot model on 23 untreated
  epidemics (vineyard x year) in Italy, France and Spain, 1997-2018 (l. 24-26, 96-97).
- Field-only classification: 15 of 23 correct, accuracy 0.65 (l. 228); eight false alarms
  among 16 mild epidemics (l. 230).
- 10 epidemics with no field rot were tested by incubating 100 symptomless berries per
  epidemic (l. 78-81), 4 boxes of 25 berries, 25 C, 12 h light, 7 days (l. 90-92).
- Adding incubation severity to the observed class raises accuracy from 0.40 to 0.90 on
  those 10 (l. 244, 249) and from 0.65 to 0.87 on all 23 (l. 270).
- Overall false-positive proportion 0.27 on all 23 (Table 3, l. 314); the abstract gives
  0.24 (l. 30).
- The model is not re-specified here: no equations or coefficients are printed (l. 99-100).
- The model runs from GS53 to GS90 with a daily step, on hourly temperature, RH, wetness and
  rain (l. 101-104).
- Classes: severe DS >= 15%, intermediate 5-15%, mild DS < 5% (l. 29, 163).
- The 2015 model was earlier fitted and cross-validated on the same data (l. 73-79, 290-291;
  21 epidemics, >80% accuracy, cited).
- Calendar fungicide timings GS69, GS77, GS83 and before GS89 are the comparison (l. 61-64).
- Mild epidemics predicted severe can be unjustified sprays (l. 267-270).

## Dependence

- It runs the González-Domínguez et al. 2015 model unchanged (l. 99-100;
  `gonzalezdominguez2015.botrytis`) and prints none of its equations. The 23 epidemics are
  described as independent of the 2015 data (l. 24-26, 87-88). Rossi is an author of engine
  models: a flag.

## Bearing (2026-10-20)

- Added to `gonzalezdominguez2015.botrytis`'s flags: the first independent test of a
  Botrytis model the catalogue holds. For Agrarium, latent infection is what separates a
  model's 'severe' from the field's 'mild' (eight false alarms of 16), so a Botrytis truth
  needs a latent stage that the observation operator does not see.
- Table 1 lists the 23 epidemics' sites, years and cultivars (l. 121-143), field severities
  0-52.4 % (l. 179-180): a candidate dataset record if a Botrytis truth is built.

---
id: molitor2016
citation: Molitor, Daniel, Augenstein, Barbara, Mugnai, Laura, Rinaldi, Pietro Antonello, Sofia, Jorge, Hed, Bryan, Dubuis, Pierre-Henri, Jermini, Mauro, Kührer, Erhard, Bleyer, Gottfried, Hoffmann, Lucien & Beyer, Marco. 2016. Composition and evaluation of a novel web-based decision support system for grape black rot control. European Journal of Plant Pathology 144:785-798
doi: 10.1007/s10658-015-0835-0
read: 2026-10-10, in full, equations in the page images, by a reading agent (claude-haiku-5-5); 48 quotes checked by scripts/verify_quotes.py
status: read
diseases: [black rot]
crops: [grapevine]
regions: [Europe, United States]
processes: [infection, incubation, host susceptibility, decision support]
records: []
datasets: []
files: [molitor2016_vitimeteo_blackrot.pdf]
---

# Molitor et al. 2016: VitiMeteo black rot

## What it holds

- **Infection index:** wet degree-hours, 0 below 5 °C, T - 5 up to 20 °C, 15 above;
  classes below 85 none, 85-150 light, 150-300 moderate, above 300 severe; each dry hour
  cuts the sum by 30 %. Thresholds from Spotts 1977 via Ellis et al. 1986.
- **Cluster susceptibility:** y = 60.6899 exp(-0.5((x - 144.3964)/110.7321)²)/0.61, x
  degree-days above 10 °C from BBCH 68.
- **Incubation:** degree-days between 6 and 24 °C; leaf symptoms at 175 °C·d (r 0.997).
- **Evaluation:** 14 cases, 2012-2013, 8 locations: precision 0.60, sensitivity 0.77,
  accuracy 0.62. Table 4 and the text conflict with Table 3.

## Dependence

- None on the engine (no black rot model there). Its infection index is a wet degree-hour
  sum, the form of the engine's `wet-degree-hours-infection` pieces, for another disease.

## Bearing (2026-10-10)

- For Cooptera, if it adds black rot: a complete, documented model.

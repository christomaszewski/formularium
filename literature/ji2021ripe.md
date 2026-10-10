---
id: ji2021ripe
citation: Ji, Tao, Salotti, Irene, Dong, Chaoyang, Li, Ming & Rossi, Vittorio. 2021. Modeling the effects of the environment and the host plant on the ripe rot of grapes, caused by the Colletotrichum species. Plants 10:2288
doi: 10.3390/plants10112288
read: 2026-10-10, in full, equations in the page images, by a reading agent (claude-haiku-5-5); 58 quotes checked by scripts/verify_quotes.py
status: read
diseases: [ripe rot]
crops: [grapevine]
regions: [China, Japan, United States]
processes: [infection, sporulation, dispersal]
records: []
datasets: []
files: [cn_it_ripe_rot_model_2021.pdf]
---

# Ji et al. 2021: a mechanistic ripe rot model

## What it holds

- Primary inoculum (Weibull in degree-days, fitted to Fukaya's data), infection
  (temperature and wetness terms from published data), sporulation ((6.750 Teq^2 (1 -
  Teq))^1.128), dispersal by rain above 2 mm/h; latency, incubation and quiescence fixed.
- 19 epidemics, 1980-2014, in China, Japan and the USA: Spearman 0.878 with harvest
  incidence; severity CCC 0.975 after rescaling to each epidemic's harvest severity.
- Not independent: one epidemic shares Fukaya's data with equation 1, and the rain switch
  was changed after the evaluation.

## Dependence

- None on the engine's models.

## Bearing (2026-10-10)

- For Cooptera, if it adds ripe rot.

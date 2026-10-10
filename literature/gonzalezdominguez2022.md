---
id: gonzalezdominguez2022
citation: González-Domínguez, Elisa, Caffi, Tito, Paolini, Aurora, Mugnai, Laura, Latinović, Nedeljko, Latinović, Jelena, Languasco, Luca & Rossi, Vittorio. 2022. Development and validation of a mechanistic model that predicts infection by Diaporthe ampelina, the causal agent of Phomopsis cane and leaf spot of grapevines. Frontiers in Plant Science 13:872333
doi: 10.3389/fpls.2022.872333
read: 2026-10-09, in full, equations 1-4 in the page image, by a reading agent (claude-haiku-5-5); 58 quotes checked by scripts/verify_quotes.py
status: read
diseases: [Phomopsis cane and leaf spot]
crops: [grapevine]
regions: [Italy, Montenegro]
processes: [infection, inoculum maturation, dispersal, incubation, validation]
records: []
datasets: []
files: [q159.pdf]
---

# González-Domínguez et al. 2022: a Phomopsis infection model from Piacenza

Not downy mildew: Diaporthe ampelina.

## What it holds

- **Model:** daily, budbreak to harvest. Pycnidia mature (eq. 1, MATR = k exp(-5 exp(-0.297
  HTT))), conidia disperse at rain of at least 0.2 mm/h, infect with at least 5 h of
  wetness at 5-35 °C (eqs 3-4, coefficients from a supplement not in the file), and show
  after fixed incubations (12 days on leaves, 18 on shoots).
- **Hydrothermal time (eq. 2):** 79.93 Teq^3.89 (1 - Teq)^2.83, Teq = (T - 5)/30, on wet
  days.
- **Validation:** 11 epidemics in Italy (2019-2020) and Montenegro (2020). k was set per
  epidemic from the observed final incidence, so the CCC of 0.925 is not independent. With
  k = 1, AUROC 0.716 (leaves) and 0.749 (shoots).

## Dependence

- No engine model is computed. Rossi et al. 2008 is cited as a precedent for the ROC method.

## Bearing (2026-10-09)

- For Cooptera: a published Phomopsis model, a disease it does not cover. Not for the
  downy mildew truth.

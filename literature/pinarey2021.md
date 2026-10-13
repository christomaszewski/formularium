---
id: pinarey2021
citation: Piña-Rey, Alba, Ribeiro, Helena, Fernández-González, María, Abreu, Ilda & Rodríguez-Rajo, F. Javier. 2021. Phenological model to predict budbreak and flowering dates of four Vitis vinifera L. cultivars cultivated in DO. Ribeiro (North-West Spain). Plants 10(3):502
doi: 10.3390/plants10030502
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5), which checked Tables 1-3 and the equations on page images; 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Tables 1-3 (pp. 5-6) read in the page images by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Galicia, Ribeiro]
processes: [phenology, budburst, flowering]
records: [pinarey2021.gdd]
datasets: [pinarey2021.ribeiro]
files: [2021-pina-rey-10-3390-plants10030502.pdf]
---

# Piña-Rey et al. 2021: budburst and flowering of four Galician varieties by degree-days

Twelve years of budburst and flowering of Albariño, Godello, Loureira and Treixadura in
one Ribeiro vineyard, fitted with GDD, triangular and UniFORC forms in the Phenological
Modelling Platform, each variety's set tested on the other three. From Vigo and Porto.

## What it holds

- **Data** (`pinarey2021.ribeiro`): BBCH 09 and 61, 2008-2019, 20 plants a variety, a
  stage when half show it, visits every 6-7 days (3-4 at flowering); daily temperatures
  from a station in the vineyard, 140 m (l. 1005-1046); not shared (l. 1188).
- **Fits** (`pinarey2021.gdd`; Tables 1-2, pp. 5-6): GDD t0 and Tb per variety, budburst
  62/8, 49/5, 79/10, 49/5 and flowering 27/8, 52/6, 71/6, 52/7 (day of year, °C) for
  Albariño, Godello, Loureira, Treixadura; efficiencies 0.86-0.89 (budburst) and
  0.90-0.97 (flowering), RMSE 1.5-3.5 d. Triangular and UniFORC forms did no better and
  were dropped for their extra parameters (p. 5). Albariño's flowering Tb is 7 in Table 1
  and the text but 8 in Table 2; Loureira's t0 72 or 71.
- **Kept sets** (Table 3): Treixadura's for budburst (t0 49, Tb 5, F* 228.5 °C·d) and
  Godello's for flowering (t0 52, Tb 6, F* 626.1), within 3 d of the other varieties'
  dates in 60 % and 81 % of cases (l. 572-578); a global fit on all four, t0 63 and 52,
  Tb 7, efficiency 0.73 and 0.88, RMSE 4.2 and 3.0 d (l. 692-697, 994-995).

## Dependence

- **Borrows** Chuine, Cour & Rousseau 1998's framework and the Phenological Modelling
  Platform's simulated annealing; fitted to the authors' own observations, no model
  dated them. Cites `cortazar2010` for the north-south pattern.
- **Kin** by form to `cortazar2009.budburst`, `ramos2017.budburst` and `ramos2018.gdd`.

## Bearing (2026-10-13)

- A threshold model, not the requested form; its value is cultivar parameters for
  Atlantic Spain and the finding that the GDD form matched the more flexible ones.

---
id: garciatejera2022
citation: Garcia-Tejera, Omar, Marcos-Matamoros, Raül, Basile, Boris, Mataffo, Alessandro, Scognamiglio, Pasquale, Prieto, Henar, Mancha, Luis, Cabral, Inês, Queiroz, Jorge, Valente, Joana, Alves, Fernando, González-Reviriego, Nube, Hernández-Barrera, Sara, Mata, Mercè et al. 2022. A method for using monthly average temperatures in phenology models for grapevine (Vitis vinifera L.). OENO One 56(4):173-183
doi: 10.20870/oeno-one.2022.56.4.5401
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which read Eqs 3-5 on the page image; 29 of 29 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-5 (pp. 174-175), Table 2 (p. 178) and Table 3 (p. 179) read in the page images by the main session; the author list is cut at the fourteenth name
status: read
diseases: []
crops: [grapevine]
regions: [Lleida, Raïmat, Badajoz, Douro, Campania]
processes: [phenology, budburst, flowering, fruit set, veraison, seasonal forecast]
records: [garciatejera2022.spring_warming]
datasets: [garciatejera2022.plots]
files: [garciatejera2022_oeno.pdf]
---

# García-Tejera et al. 2022: running a degree-day model on monthly means

The Spring Warming sum fitted per site and cultivar on daily temperatures, then run on
monthly means through an "effective days" correction so that seasonal forecasts can
drive it: the same F* gives the same dates within a day on average. Raïmat, in Lleida,
is one of the four plots. From the Barcelona Supercomputing Center and partners.

## What it holds

- **Data** (`garciatejera2022.plots`): Raïmat (Tempranillo, Chardonnay), La Orden
  (Tempranillo, 2005-2017), Vilariça (Touriga Nacional), Mirabella Eclano (Aglianico),
  weekly Baggiolini stages (l. 317-358; Table 1).
- **Daily model** (Eqs 1-2, p. 174): Σ max(T − Tb, 0) from 1 January to F*, Tb 3.5 °C
  to bud break and 7.1 °C after, from Moncur et al. 1989 (l. 214-219); F* by inverse
  modelling per stage, site and cultivar (p. 175). Table 2 (p. 178;
  `garciatejera2022.spring_warming`): Raïmat Tempranillo 345, 425, 525, 1,443 °C·d and
  Chardonnay 274, 436, 530, 1,489 for bud break, bloom, fruit set and veraison; Vilariça
  499-1,648, La Orden 514-1,430, Mirabella Eclano 534-1,954.
- **Monthly method** (Eqs 3-5, p. 175): the month's rate (Tm − Tb) times the effective
  days n_days [1 − cdf(Tb; Tm, σ)], the normal distribution from each site's historical
  records, summed to the same F*; σ values not printed.
- **Scores** (Table 3, p. 179): RMSD over all sites, daily 5.4, 5.0, 6.0, 6.4 d and
  monthly 6.7, 4.4, 6.0, 5.9 d for the four stages; the two models agree (slope 1.00,
  intercept −2.32, R² 0.99, Fig. 5); mean residuals 0.5-1.0 d (daily) and 1.4-3.1 d
  (monthly), no bias at p 0.025 (Table 4, l. 827-862). La Orden 2017 missed fruit set and
  veraison by 21 and 17 d in both (l. 774-776). From 3 to 30 years of historical records
  changed little (p. 179).

## Dependence

- **Borrows** Hunter & Lechowicz 1992's Spring Warming (the GFV form of `parker2013.gfv`)
  and Moncur et al. 1989's bases; fitted to the partners' observed dates. The monthly
  method is the authors' own.

## Bearing (2026-10-13)

- Not the requested form: a heat sum to a threshold, fed by monthly means. For Agrarium
  two things matter: Raïmat's Tempranillo and Chardonnay F* (the nearest published set to
  the Penedès) and the proof that monthly means lose only about a day against daily
  input, which bears on what weather a phenology piece needs.

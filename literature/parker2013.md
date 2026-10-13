---
id: parker2013
citation: Parker, Amber, Garcia de Cortázar-Atauri, Inaki, Chuine, Isabelle, Barbeau, Gérard, Bois, Benjamin, Boursiquot, Jean-Michel, Cahurel, Jean-Yves, Claverie, Marion, Dufourcq, Thierry, Gény, Laurence, Guimberteau, Guy, Hofmann, Rainer W., Jacquet, Olivier, Lacombe, Thierry, Monamy, Christine, Ojeda, Hernan, Panigai, Laurent, Payan, Jean-Christophe, Rodriquez Lovelle, Bernard, Rouchaud, Eric, Schneider, Christophe, Spring, Jean-Laurent, Storchi, Paolo, Tomasi, Diego, Trambouze, William, Trought, Michael & van Leeuwen, Cornelis. 2013. Classification of varieties for their timing of flowering and veraison using a modelling approach: a case study for the grapevine species Vitis vinifera L. Agricultural and Forest Meteorology 180:249-264
doi: 10.1016/j.agrformet.2013.06.005
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py; Tables 1-2 and Eqs 1-2 (pp. 251-254) read in the page images by the main session; the long author list is the agent's transcription; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [France]
processes: [phenology, flowering, veraison]
records: [parker2013.gfv]
datasets: [parker2013.database]
files: [2013-parker-10-1016-j-agrformet-2013-06-005.pdf]
---

# Parker et al. 2013: GFV's critical sum F* for 104 varieties

The Grapevine Flowering Veraison model of `parker2011` (degree-days above 0 °C from day
60 to a critical sum F*) fitted variety by variety on the updated French database: a
classification of 95 varieties at flowering and 104 at veraison by their F*, with each
fit's error. A threshold model; the tables are the resource.

## What it holds

- **Data** (`parker2013.database`): Parker et al. 2011's database updated, 81 varieties,
  2,278 flowering and 2,088 veraison observations, 1960-2007, 123 locations, mostly
  France (l. 156-171).
- **Model** (`parker2013.gfv`; Eqs 1-2, p. 252): Sf = Σ max(x_t − 0, 0) from day 60 until
  F*, x_t the daily mean of Tmin and Tmax; F* fitted per variety by the Metropolis
  algorithm with a Fisher-test 95 % interval (l. 310-342); the Spring Warming form chosen
  by AIC over UniForc and UniChill in 2011 (l. 173-175); a 15-25 °C cap tried without
  gain (l. 289-292).
- **Tables 1-2** (pp. 251-254): F* with sites, observations, RMSE and efficiency.
  Flowering: Tempranillo 1,188 (one site, 5 observations, RMSE 2.5 d), Chardonnay 1,217
  (21 sites, 170, 4.9 d, EF 0.76), Merlot 1,269, Grenache 1,277, Syrah 1,279, Carignan
  1,288 (EF 0.87), Cabernet-Sauvignon 1,299 (5.2 d, 0.77); veraison: Tempranillo 2,484
  (EF 0.40), Chardonnay 2,547 (6.5 d, 0.82), Merlot 2,636, Cabernet-Sauvignon 2,689,
  Carignan 2,749, Grenache noir 2,761 (6.4 d, 0.87). The spread between earliest and
  latest variety is 291 °C·d at flowering (about 16 d at 18 °C) and 655 at veraison
  (l. 494-511). RMSE under a week for all but Arinarnoa at flowering and twelve
  varieties at veraison (l. 493, 509).
- **Precision:** about 20 observations at three or more sites give a confidence
  interval of 100 °C·d or less (p. 254). Site against year effects in Table 4 (the text's
  13.96 % for Syrah's veraison reads 3.28 % in the table, l. 705, 759).

## Dependence

- **Computes** GFV (`parker2011`, Hunter & Lechowicz 1992's Spring Warming form) on the
  observed database. García de Cortázar-Atauri, Chuine and van Leeuwen are authors of
  `cortazar2009`, `cortazar2010` and `daux2012`.

## Bearing (2026-10-13)

- A threshold model, but the one with the widest varietal table: F* for the
  international varieties grown in the Penedès, none for Xarel·lo, Macabeo or
  Parellada.

---
id: brunetto2018
citation: Brunetto, G., Garlete, L., Ceretta, C. A., Melo, G. W. B. de, Hammerschmitt, R. K. & Couto, R. da R. 2018. Decomposição e liberação de nutrientes de folhas e ramos de vinhedo (Decomposition and release of nutrients from leaves and pruned stems in vineyard). Revista Ciência Agrária 61:1-10
doi: 10.22491/rca.2018.2624
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 49 of 49 quotes found at their lines by the main session; Tables 4 and 5 read in the page images (pp. 7-8) by the reading agent, Table 4 values checked against them by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Santana do Livramento, Rio Grande do Sul, Brazil]
processes: [leaf litter decay, nutrient release, overwintering]
records: [brunetto2018.leaf_litter_decay]
datasets: [brunetto2018.santana]
files: [gustavo_2018.pdf (the 2026-10-18 drop)]
---

# Brunetto et al. 2018: decay of vineyard leaves and pruned stems

Litter bags of Cabernet Sauvignon leaves and pruned stems laid on the soil surface in a
vineyard, in the row and between rows, collected eight times over 210 days.

## What it holds

- **Site and design** (l. 75-141): Cabernet Sauvignon on SO4, planted 1978, 3.0 × 0.74 m,
  30°48′31″ S, 55°22′33″ W; climate Cfa, mean 18.4 °C, 1467 mm a year. 80 bags (40 leaves, 40
  stems), 20 × 20 cm, 1 mm nylon mesh, 30 g dry matter each (750 g m-2), placed on 16 April
  2009; five bags per material and position collected at 0, 30, 60, 90, 120, 150, 180 and
  210 days (to 16 November 2009). Monthly 2009 weather in Table 1 (no station named): May
  123.6 mm and 15.2 °C, September 269.4 mm and 13.3 °C, November 540.8 mm and 20.8 °C. The
  paper's header and abstract say May to November 2009; the bags were laid in April.
- **Model:** X = X0 exp(-k t), percent remaining against days, from Boer et al. (2007); half-life
  0.693 / k from Paul & Clark (1989) (l. 160-164).
- **Leaf mass, Table 4 (page 7):** in the row X0 96.17 %, k 0.003, half-life 231 d, R² 0.90;
  between rows X0 94.43 %, k 0.003, R² 0.92. The k column is printed in "g g-1" and is rounded
  to one significant figure; per day is implied. 15N excess in leaves: k 0.05, half-life
  13.86 d.
- **Other results:** leaves kept about 85 % (row) and 80 % (between rows) of their mass at
  30 days and about 45 % and 43 % of their carbon at 210 days (Fig. 1); the stems' mass
  half-life is 693 d (k 0.001, R² 0.87, Table 5). Position (row against between rows) made no
  difference to decay or release (abstract).
- **Table 5 not used.** The reader reported its P row printing half-life 231 d against k 0.002
  (which implies 347 d); the main session read the same row as k 0.002 with half-life 346.5, which
  is consistent. Table 5 was not used for the record. The soil is called a Hapludalf in the
  methods and an Ultisol in the discussion (l. 118).
- **Not printed:** litter or soil temperature and moisture by position, fitting software, the
  error of k, a data statement or licence.

## Dependence

- **Borrows** the exponential decay of Boer et al. (2007) and the half-life formula of Paul &
  Clark (1989). It cites the LIDEL litter model (Campbell et al. 2016) for factor lists only.
- **Data:** its own litter bags. No model is said to have shaped them.

## Bearing (2026-10-18)

For strand 1 (does the previous season's leaf litter persist to carry inoculum):

- **What it shows:** in a Brazilian subtropical vineyard, leaf litter on the soil surface loses
  half its mass in about 231 days through the southern autumn, winter and spring, and 15 to
  20 % of it within 30 days; pruned stems last about three times as long. It measures mass, not
  oospores, so it bounds how long the leaf substrate lasts, not how long the pathogen does.
- **Limits:** one site, one winter, subtropical, bags in 1 mm mesh. Not a temperate winter
  with snow or frost.
- **Take for the sweep:** a recorded decay form (`litter-decay`) that a litter-persistence
  assumption can be compared with. The rate is a fit to five bags per date, not a
  parameter for other climates.

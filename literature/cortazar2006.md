---
id: cortazar2006
citation: García de Cortázar-Atauri, Iñaki. 2006. Adaptation du modèle STICS à la vigne (Vitis vinifera L.) : utilisation dans le cadre d'une étude d'impact du changement climatique à l'échelle de la France. PhD thesis, École nationale supérieure agronomique de Montpellier (NNT 2006ENSA0030), defended 2006-12-22; HAL tel-04262126, 350 pages
doi:
read: 2026-10-13, the contents, chapter I's budburst article and the STICS phenology parameters (chapter II), by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Table 11 (thesis p. 43, PDF p. 64) and Tableau 13a (p. 128, PDF p. 149) read in the page images by the main session; held since 2026-10-07 as the cited source of cortazar2009.budburst
status: read
diseases: []
crops: [grapevine]
regions: [France, Angers, Champagne, Languedoc, Bordeaux, Alsace]
processes: [phenology, budburst, dormancy, chilling, degree-days, crop model]
records: [cortazar2009.budburst, cortazar2009.brin]
datasets: [phenoclim]
files: [2006-garcia-de-cortazar-url-garcia-de-cortazar-2006-thesis.pdf]
---

# García de Cortázar-Atauri 2006: the thesis behind the budburst models and STICS-vigne

The Montpellier thesis that adapts STICS to grapevine; its chapter I reprints the budburst
model comparison later published as `cortazar2009` (submitted to Agricultural and Forest
Meteorology in 2005, l. 1166), and chapter II sets STICS's phenology parameters per
cultivar. In French, the budburst article in English. Read for Table 11, which the
catalogue cites.

## What it holds

- **Table 11 (p. 43 of the article, PDF p. 64; the catalogue's cited table):** for ten
  cultivars on PHENOCLIM 1970-2002 (l. 1329; `phenoclim`), the parameters and
  leave-one-out RMSEP of RIOU, ND, GDD at 10 °C, BRIN and GDD at 5 °C. GDD at 5 °C from
  1 January: G_dc 220.1 (Chardonnay) to 321.3 (Grenache) °C·d, RMSEP 7.4 (Merlot) to
  14.6 (Chasselas) d; BRIN C_c 94.3 (Ugni Blanc) to 108.2 (Riesling), G_hc 6,576.7
  (Chardonnay) to 9,174.3 (Grenache) degree-hours, RMSEP 8.2 to 14.2 d. The same values
  as the 2009 paper's Table 8, now read in the page image.
- **The article's settings:** GDD from 1 January (l. 1429); chilling from 1 August
  (l. 1528); BRIN's post-dormancy base 5 °C after a test of 0-10 °C (l. 1825);
  quasi-Newton least squares in Matlab (l. 1610), final parameters on the whole sample
  per cultivar (l. 1583); the three classic models erred by 9-25 d (l. 1207), BRIN by
  8-14 (l. 1834), which the author credits to the base temperature (l. 1980). Cabernet
  Sauvignon's dormancy breaks on 15 December on average, SD 13 d (l. 1844).
- **Tableau 13a (p. 128, PDF p. 149):** STICS's phenology parameters for eight cultivars:
  Q10 2.17 (the text says 2.13 at l. 5419), chilling from day 213, the cold-action
  threshold JVC 66.8 (Cabernet Franc) to 107.5 (Chenin), STDORDEBOUR (degree-hours base
  5 to budburst) 6,576.7 (Chardonnay) to 11,548.0 (Cabernet Franc), and the base-10
  degree-day sums between later stages (STAMFLAX 926.6-1,142.0; STLEVDRP 292.4-420).
  Tableau 13b: budburst to physiological maturity 1,649 (Chenin) to 1,926 (Grenache)
  °C·d base 10.
- **Definitions:** simulated budburst is 50 % of buds burst, flowering 50 % of flowers
  open (l. 1126); flowering plays no active role in STICS (l. 1127).

## Dependence

- **Fitted to** PHENOCLIM's observed dates; BRIN borrows Bidabé 1965a,b and Richardson
  et al. 1974 (`bidabe1965.cold_action`, `richardson1974.forcing_hours`), printed in the
  bibliography as the catalogue cites them (l. 12222-12226, 12798-12799).
- **Same data and values** as `cortazar2009`; the thesis is the earlier print.

## Bearing (2026-10-13)

- Closes the catalogue's trail: `cortazar2009.budburst`'s Table 11 is real, at thesis
  p. 43, and its GDD at 5 °C sums are now Published values read from the page.
- STICS's cultivar sets (Tableau 13a) are a second source of the same BRIN parameters,
  with Cabernet Franc and Chenin added.

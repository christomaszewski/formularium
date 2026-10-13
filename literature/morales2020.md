---
id: morales2020
citation: Morales-Castilla, Ignacio, García de Cortázar-Atauri, Iñaki, Cook, Benjamin I., Lacombe, Thierry, Parker, Amber, van Leeuwen, Cornelis, Nicholas, Kimberly A. & Wolkovich, Elizabeth M. 2020. Diversity buffers winegrowing regions from climate change losses. Proceedings of the National Academy of Sciences 117(6):2864-2869
doi: 10.1073/pnas.1906731117
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [global, France]
processes: [phenology, climate projection, cultivar suitability]
records: []
datasets: []
files: [2020-morales-castilla-10-1073-pnas-1906731117.pdf]
---

# Morales-Castilla et al. 2020: cultivar turnover against projected losses

Eleven cultivars' phenology modelled (Smoothed-Utah chilling, then Wang & Engel forcing)
on the Parker database and run on CESM warming levels to map where each stays suitable:
56 % of today's regions lost at +2 °C without changing cultivar, 24 % with. The model's
equations and fitted values are in the supplement.

## What it holds

- **Data:** 517 budbreak, 757 flowering and 688 veraison dates (E-L 4, 23, 35) at 62
  mostly French locations, 1956-2015, part of Parker et al. 2011's database with stations
  within 5 km and 100 m (l. 636-670); BEST gridded Tmin and Tmax (r 0.982 against
  stations) and the CESM Large Ensemble under RCP8.5 at +2 °C (2039-2048) and +4 °C
  (2076-2085) against 1970-1979 (l. 673-702).
- **Model:** chilling by Smoothed-Utah (Richardson 1974, Bonhomme et al. 2010), forcing by
  Wang & Engel 1998 to budbreak, flowering and veraison, 0 and 40 °C fixed, one optimum
  per stage and the units per stage and cultivar fitted (l. 657-670); maturity by a
  bioclimatic envelope over 1950-1980 (l. 685-701). Equations and values: SI Appendix.
- **Cultivars:** Cabernet-Sauvignon, Chasselas, Chardonnay, Grenache, Merlot, Monastrell,
  Pinot noir, Riesling, Sauvignon blanc, Syrah, Ugni blanc, 35 % of the planted area
  (l. 145-149).
- **Result:** 56 % of regions lost at +2 °C and 85 % at +4 °C without turnover; 24 % at
  +2 °C with it (l. 155-158, 251).

## Dependence

- **Borrows** Wang & Engel and Smoothed-Utah; fitted to Parker's observed dates
  (`parker2013.database` kin). García de Cortázar-Atauri, Parker and van Leeuwen again.

## Bearing (2026-10-13)

- Threshold models; the cultivar list overlaps the Penedès internationals. The fitted
  values would need the supplement.

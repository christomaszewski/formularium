---
id: lulu2008turf
citation: Lulu, Jorge, Sentelhas, Paulo Cesar, Pedro Júnior, Mário José, Pezzopane, José Ricardo Macedo & Blain, Gabriel Constantino. 2008. Estimating leaf wetness duration over turfgrass, and in a 'Niagara Rosada' vineyard, in a subtropical environment. Scientia Agricola 65 (special issue):10-17
doi: 
read: 2026-10-10, in full, by a reading agent (claude-haiku-5-5); 46 quotes checked by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [São Paulo]
processes: [leaf wetness]
records: [sentelhas2008.wetness]
datasets: [lulu2008.jundiai]
files: [leaf-wetness-turfgrass-vineyard-2008.pdf]
---

# Lulu et al. 2008 (Sci. Agric.): four wetness models on turf and in a vineyard

Chapter 3 of [lulu2008thesis](lulu2008thesis.md).

## What it holds

- Jundiaí, 115 days (November 2005 to March 2006). Models: hours with RH above 90 %
  (20-min intervals / 3), dew-point depression (2.0 and 3.8 °C), CART (thresholds 14.46 and
  37.00) and Penman-Monteith (dew store 0.8 mm).
- Turf, all days (Table 2): mean error and MAE, Penman-Monteith 2.30 and 2.60 h, RH > 90 %
  -2.78 and 2.86 h, dew-point depression -2.04 and 2.33 h, CART -1.09 and 1.68 h.
- Vineyard top (south-west): CART R² 0.87, d 0.96, mean error 0.65 h; the printed c
  (0.9332) does not follow from d and R².
- CART was adapted to 20-min data here (Sentelhas 2004's note says 15).

## Dependence

- RH > 90 % and dew-point depression are the forms of `sentelhas2008.wetness`; different
  data. Sentelhas is an author of both: a flag.

## Bearing (2026-10-10)

- Errors of RH-threshold wetness in a subtropical vineyard: hours above 90 % RH
  under-count wetness by about 2.8 h a day on turf.

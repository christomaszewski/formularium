---
id: saxena2023
citation: Saxena, Aseem, Pesantez-Cabrera, Paola, Ballapragada, Rohan, Keller, Markus & Fern, Alan. 2023. Multi-task learning for budbreak prediction. arXiv preprint 2301.01815v1
doi:
read: 2026-10-13, in full (a five-page preprint), by a reading agent (claude-haiku-5-5); 47 of 47 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Washington, Prosser]
processes: [phenology, budburst, machine learning]
records: []
datasets: [ferguson2014.prosser]
files: [2023-saxena-arxiv-2301-01815.pdf]
---

# Saxena et al. 2023: a recurrent network predicting budbreak day by day

A gated recurrent network fed daily weather that outputs, each day, the probability that
budbreak has happened, trained on Washington State's Prosser records for 18 cultivars,
with the cultivars sharing one network through multi-task heads or embeddings. No heat
sum, no coefficients, no code.

## What it holds

- **Data:** budbreak (50 % of buds green, after Ferguson et al. 2014 and Zapata et al.
  2017) for 31 cultivars at IAREC and the Roza farm, Prosser, 1988-2022, the series
  behind `ferguson2014.prosser`; 18 cultivars with 4-30 years used (Table 1: Cabernet
  Sauvignon 29, Sauvignon Blanc 11, Syrah 4) (l. 60-109, 148-150). Daily temperature,
  humidity, dew point, rain and wind from AgWeatherNet, gaps interpolated (l. 78-83,
  177-179).
- **Model:** the label is 0 before budbreak and 1 after (l. 127); two dense layers (1024,
  2048), a GRU with 2048 units, a dense output; 400 epochs, Adam at 0.001, batch 12
  (l. 140-143, 187-188); binary cross-entropy (l. 185). Variants share cultivars by a
  head each (MultiH) or a one-hot embedding added, concatenated or multiplied (l. 146-174).
  The predicted day is the first with probability above 0.5 (l. 231).
- **Test:** two random seasons held out per trial, three trials, averaged (l. 181-183):
  not by year. Table 3's median absolute error 7 d (single task) against 3-3.5 d
  (multi-head, additive and concatenated embeddings) and 5 d (multiplicative), with
  counts beyond 3 days, a week, two weeks and a month (l. 214-219) that do not nest;
  Table 2's per-cultivar gains are in cross-entropy, not days (l. 162-175).
- **No comparison** with existing budbreak models, "not accessible" (l. 54); planned
  deployment on AgWeatherNet for 2023-2024 (l. 237); no data or code statement.

## Dependence

- **Fitted to** WSU's observed dates; no model dated them. Keller is an author of
  `ferguson2014`, whose Prosser series it shares.

## Bearing (2026-10-13)

- The machine-learning form on Chris's list: a 3-day median error on random held-out
  seasons at one site, unreproducible from the paper (no weights, no code), and untested
  against a degree-day model. A design to note, not a model to record.

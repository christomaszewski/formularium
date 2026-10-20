---
id: saubin2024
citation: Saubin, M., Coville, J., Xhaard, C., Frey, P., Soubeyrand, S., Halkett, F. & Fabre, F. 2024. A mechanistic-statistical approach to infer dispersal and demography from invasion dynamics, applied to a plant pathogen. Peer Community Journal 4:e9
doi: 10.24072/pcjournal.356
read: 2026-10-20, LIGHT, by a reading agent (claude-haiku-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [poplar rust]
crops: [poplar]
regions: [Durance valley, French Alps]
processes: [dispersal kernel, invasion, landscape spread]
records: []
datasets: []
files: [saubin_2024.pdf (the 2026-10-20 drop)]
---

# Saubin et al. 2024: dispersal and growth of poplar rust inferred from its yearly invasion of a valley

An integro-differential invasion model with exponential-power, exponential or Gaussian
kernels (or reaction-diffusion), fitted to 2008 rust counts at 12-45 sites along about 200
km of the Durance valley.

## What it holds

- Pathogen: Melampsora larici-populina, poplar rust, on wild poplars along the Durance
  valley, French Alps (l. 217, 557-560).
- Model: reaction-diffusion (R.D.) or integro-differential (I.D.) invasion model with
  logistic growth (rendered p. 4). The I.D. kernel is the exponential-power family J, tail
  exponent tau (l. 249-265, Eq 1). Mean distance lambda = alpha Gamma(2/tau)/Gamma(1/tau).
- Data: 2008; 12 sites along nearly 200 km, every three weeks from July to November, seven
  survey rounds (l. 67-68, 583-584). Oct. 22: 45 sites (l. 585). Raw sampling 40 to 150
  trees per site (l. 638); refined 20 twigs (l. 648); 97 count values (l. 2410). No model
  dated the counts.
- Model choice (Table 3, l. 665-668): exponential-power AIC 5163; exponential 5461; Gaussian
  5493; R.D. 6190.
- Fitted (Table 4; l. 916, 673): mean dispersal distance 1.94 km (CI 1.78 to 2.12); tau 0.24
  (0.243; CI 0.226 to 0.260).
- Growth rates upstream 0.085 and downstream 0.023 (l. 675); gamma 4.82 and sigma^2 1.29 (l.
  676).
- Simulations: correct kernel selection 78% for exponential-power data (l. 483).
- Cited: Fabre et al. 2021 review gives 213 m for M. fijiensis ascospores, attributed to
  Rieux et al. 2014 (l. 918-920). rieux_2014 gives D1000 = 213.83 m (its l. 300): a lead,
  not a fact here.
- Data: code and counts on Zenodo (DOI 10.5281/zenodo.7906840) and Recherche Data Gouv (DOI
  10.57745/RDTJSF) (l. 1094-1097).
- Gap: the text has seven rounds (l. 584), Appendix D.4 has t = 1 to 6 (l. 2411).

## Dependence

- Its own fit to survey counts; no model dated the counts. Code and data on Zenodo
  (10.5281/zenodo.7906840) and Recherche Data Gouv (10.57745/RDTJSF) (l. 1094-1097).

## Bearing (2026-10-20)

- For spread between parcels and regions (t6): a fat-tailed exponential-power kernel again
  wins (AIC 5163 against 5461 exponential), mean dispersal 1.94 km a generation, and the
  method infers it from snapshots of an invasion, the kind of data a cooperative's scouting
  would give. Poplar rust, not a vine disease.

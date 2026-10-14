---
id: yang2023b
citation: Yang, C., Menz, C., Reis, S., Machado, N., Santos, J. A. & Torres-Matallana, J. A. 2023. Calibration for an Ensemble of Grapevine Phenology Models under Different Optimization Algorithms. Agronomy 13(3):679
doi: 10.3390/agronomy13030679
read: 2026-10-14, the full text lightly, by a reading agent (claude-haiku-5-5); 57 of 57 quotes found at their lines by scripts/verify_quotes.py; Table 1 (page 4) and Table 2 (page 6) read in rendered pages; the supplement (Tables S1-S2, Figures S1-S4) not held
status: read
diseases: []
crops: [grapevine]
regions: [Douro]
processes: [phenology, flowering, calibration]
records: []
datasets: []
files: [chenyao_2023.pdf]
---

# Yang et al. 2023: five flowering models for two Douro varieties, three optimisers

Five literature models of full flowering (BBCH 65) for Touriga Franca (TF) and Touriga
Nacional (TN) in the Douro, each fitted with three optimisation algorithms (maximum
likelihood, simulated annealing, SCE-UA). The id carries a b because `yang2023` is Yang
et al. 2023 on Plasmopara viticola.

## What it holds

- **Models** (l. 350-371): GDD (Bonhomme 2000), Richardson (Richardson et al. 1974),
  Sigmoid (Hänninen 1990), Triangular (Chuine et al. 2013), Wang (Wang & Engel 1998). All
  sum a daily forcing rate from 1 January to a threshold F* (Eq. 1, l. 357, 369). No
  photoperiod or chilling term (l. 371).
- **Fit** (l. 412-427, 643-649): GDD fits F* only, base fixed at 0 °C; F* starts at
  1100-1300 °Cd for GDD and Richardson and 40-80 for the normalised models. Bounds were
  widened by 20 to 100 %, and 100 % was kept (l. 777).
- **Data** (l. 316-328): flowering at eight ADVID plots, four a variety, 2014-2021, 32
  observations a variety. Table 1 site means ± SD in DOY: TF 134 ± 5, 135 ± 4, 139 ± 4,
  130 ± 6; TN 139 ± 8, 139 ± 10, 131 ± 9, 129 ± 8 (page 4). Temperature is E-OBS v24.0e at
  0.1° (l. 334); April to June is the critical window (l. 343).
- **Fit quality, on the calibration data** (l. 38, 40, 769-770, 1126): ensemble median
  RMSE 5-6 d, MAE 4-5 d, bias 0-1 d, R² 0.5-0.6. After the 100 % widening GDD reaches
  6-7 d and the others 5-8 d. AIC below 135 (l. 1351).
- **Instability** (l. 1027-1031): parameter CV across algorithms up to 274 % (Wang Tb, TN);
  Sigmoid 25-95 %; GDD and Richardson 6 % or less. Sigmoid with SA gives F* 7.7 for TN, called
  unrealistically small (l. 1209; garbled layout).
- **Not held:** the fitted values (supplement Table S2, l. 1023) and per-model RMSE
  (Figures S2-S4).

## Dependence

- **Literature models, own code** (l. 350-351, 753). Sigmoid is said to have a structure
  similar to UniFORC (l. 441-442): a shared form to check. Richardson, Triangular and Wang
  share definitions of Tb and Tmax (l. 367-368). The GDD base of 0 °C is taken from
  Parker et al. 2011 and 2013 (l. 425). Fitted to the authors' own flowering dates, not to
  another model's output. Reis and Machado also appear in the group's earlier work: a flag.

## Bearing (2026-10-14)

- **Heat-sum-threshold, the engine's form:** all five models sum a forcing rate to a
  threshold, so every one is kin to the engine's degree-day pieces. Not a candidate for a
  truth phenology; read for the truth phenology search.
- **No record, no dataset:** the fitted values are in a supplement not held, and the only
  observed numbers printed are Table 1's site means. The error of 5-6 d is on the fitting
  data, not a test.

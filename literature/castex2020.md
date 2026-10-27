---
id: castex2020
citation: Castex, V., García de Cortázar-Atauri, I., Calanca, P., Beniston, M. & Moreau, J. 2020. Assembling and testing a generic phenological model to predict Lobesia botrana voltinism for impact studies. Ecological Modelling 420:108946 (author manuscript; year, volume and DOI not printed in it)
doi: 10.1016/j.ecolmodel.2020.108946
read: 2026-10-26, in full from the HAL author manuscript, by a reading agent (claude-haiku-5-5); 57 of 57 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-7 (pp. 10-11) and Tables 3-5 and 9 (pp. 14-15, 23) read in the page images by the agent, Eqs 1-7 and Table 9 also by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Spain, France, Switzerland]
processes: [grape berry moth, insect phenology, diapause, photoperiod, temperature response]
records: [castex2020.lgm]
datasets: [castex2020.traps]
files: [castex2020.pdf (the 2026-10-25 other-sources drop)]
---

# Castex et al. 2020: one generic model for Lobesia botrana flights from Andalusia to Alsace

The Lobesia Generic Model (LGM): an overwintering submodel in three phases, the diapause
one gated by day length, and an adult submodel with one Wang-Engel temperature response
for every generation, forcing summed to thresholds for the 10 % and 50 % points of each
flight. Trap data from 12 sites fit it; Table 9 prints the final parameters.

## What it holds

- **Data** (l. 260-268, 325-361): male trap catches at 12 sites from 36.710° N to 48.213° N
  and 0-692 m, 1997-2016, 51 of 90 records kept; 10 % and 50 % flight dates per generation
  from cumulative counts; daily Tmin, Tmax, Tmean from stations within 10-15 km (Staefa,
  site 11, 2004-2017).
- **Forcing** (Eqs 1-3, page image p. 10): F_s = Σ f(t_d) from d0 to ds; in diapause F =
  Σ f(t_d) g(P_d) or Σ (f + g), with g rising linearly from 0 at Plow to 1 at Phigh; the
  structure follows Baumgärtner et al. 2012 and Gutierrez et al. 2012 (l. 402, 443), with a
  12 h photoperiod threshold stopping the last generation (l. 232-233).
- **Temperature responses tested** (Eqs 4-7, p. 11): Richardson, triangular and Wang-Engel
  beta with α = ln 2 / ln((Tmax - Tmin)/(Topt - Tmin)); Wang chosen for the whole model
  (l. 979).
- **Final parameters** (Table 9, p. 23, WAllp): prediapause Tmin 2.45, Topt 14.36, Tmax
  27.69 °C, F 40.74; diapause 7.66, 15.04, 22.87, Plow 9.17 h, Phigh 14.25 h, F 28.35;
  post-diapause 11.39, 11.42, 20.00, F 1.47 (Topt within 0.03 °C of Tmin, as printed); adult
  flights 2.38, 23.13, 32.31, F 45.61 between generations (10-10 and 50-50) and 7.76 within
  (10-50). The text gives 2.4, 23.12 and 32.13 (l. 785).
- **Fit** (Tables 3, 5, 9): overwintering CAL EFF 0.74 on 39 points, VAL RMSE 9.07 d and
  EFF 0.08 on 12; adults between generations CAL RMSE 6.93 d, EFF 0.95, n 140, VAL 11.15 d,
  EFF 0.84, n 46; within a generation CAL 5.94 d, 0.98, 107, VAL 9.84 d, 0.96, 37. Random 75
  % CAL and 25 % VAL, then a cross-validated refit on all (l. 589-595). dt0 15 July
  (l. 555-556).
- **Not printed:** the year, volume and DOI; ESM2-ESM7 (not held); the F column's definition
  in Table 9; the full site-years.
- **Lead check:** nothing about BRIN, a Wang-Engel vine model, a weather generator or
  "1981-2017" is in this paper; those belong to castex2023.

## Dependence

- **Fitted to** `castex2020.traps`, observed catches and station weather; no model dated
  them. Flight points derived by cumulative sums (l. 348-355).
- **Borrows** the overwintering structure and the additive photoperiod form from Baumgärtner
  et al. 2012 (l. 402, 443; the paper's own simplification, ESM2) and Gutierrez et al. 2012's
  parameters, which it finds worse (EFF -0.05, l. 868); Wang & Engel 1998's beta.
- **Computed by** castex2023 (held) for the 2100 projections. García de Cortázar-Atauri
  again: a flag beside `cortazar2009.brin`.

## Bearing (2026-10-26)

- For Cooptera's grape berry moth work and the 10-20 search's insect strand: the one
  Lobesia model with its parameters printed, runnable from Table 9 and Eqs 1-3 and 6-7. Kin
  by form to the engine's `cortazar2009.brin` and the heat-sum phenology records
  (rate-temperature response, forcing to a threshold), with the day-length gate a form of
  its own.

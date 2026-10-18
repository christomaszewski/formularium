---
id: paulescu2023
citation: Paulescu, E. & Paulescu, M. 2023. Minute-scale models for the diffuse fraction of global solar radiation balanced between accuracy and accessibility. Applied Sciences 13:6558
doi: 10.3390/app13116558
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by the main session; Eqs 5-6 (p. 5), A2 (p. 11) and A4-A8 (p. 12) read in page images by the reading agent; Eqs 5-6 checked in the page image by the main session
status: read
diseases: []
crops: []
regions: [Payerne, 36 BSRN stations worldwide]
processes: [diffuse fraction, clearness index, solar radiation separation, minute-scale]
records: [paulescu2023.minute_separation]
datasets: [paulescu2023.payerne]
files: [eugenia_2023.pdf (the 2026-10-18 drop)]
---

# Paulescu & Paulescu 2023: minute-scale diffuse fraction models

Two new rational-function models for the diffuse fraction kd of global horizontal
irradiance (GHI) at 1-minute steps, fitted on one station-year and tested on 36 stations.

## What it holds

- **M2** (Eq. 6, page 5): kd = (1 - 2.525 kt + 1.834 kt² - 0.204 (kt khour)²) / (1 - 2.578 kt
  + 1.902 kt² + 1.054 (kt kday)²), with kt the one-minute clearness index and khour, kday
  the hourly and daily ones, all from GHI. Fit R² 0.917, nMBE 0.007 (l. 313).
- **M1** (Eq. 5): eight predictors (kt, dKtc, kde, kday, khour, a persistence term psi, the
  clear-sky irradiance Gcs in MJ h-1 m-2, Kcsi); numerator coefficients 7.217, -0.656 (power
  0.5), 7.947, 0.187, -2.747, -15.379; denominator 1.655, 14.008, 17.477, 0.16. Fit R² 0.929,
  nMBE 0.011. Which data these fit statistics come from is not named.
- **Data** (l. 186-259): BSRN 1-min GHI, DHI and DNI, solar elevation above 5° only. D_FIT:
  Payerne, Switzerland (46.815 °N, 6.944 °E), 2020, 193,294 records. D_TEST: 36 BSRN stations
  between 45 °S and 58 °N, one year each from 2002 to 2021, nearly 7 million records;
  Payerne (2019) is 2.7 % of it, with no overlap in time. BSRN access date 15 May 2023,
  licence not printed.
- **Reference models:** PB (Paulescu & Blaga 2019; its Eq. A2 coefficients are printed:
  1.011925, -0.0316193, -0.0293827, -1.6567278, 1.8982144, -0.8547682, knots 0.367, 0.734,
  0.462), E2 (Engerer 2015), S1 and S3 (Starke et al. 2018, 2021), Y4 (Yang 2022, which
  computes E2). Their other coefficients are not printed here.
- **Results:** M1 ranks first at 16 stations (DNI) and 17 (DHI), M2 first at 5 (DHI). DNI
  nRMSE across all models 15.2 to 49.4 %; DHI nRMSE 23.7 % (S1) to 82.5 % (E2); M2 DHI nRMSE
  25.4 % (Toravere) to 52.9 % (Tamanrasset, bias +29.2 %). Arid sites are worst; S3 is best in
  the tropical zone. Per-station values are in Fig. 4, not extracted.
- **Not among the models compared:** Erbs 1982 (named at l. 150-151 as an early polynomial).

## Dependence

- **Predictor borrowing, not equations:** M1 gathers predictors of earlier models (dKtc and kde
  from E2, kday from PB, psi and Gcs from S1 and S3, khour from S3); M2 uses kt, kday and
  khour. Shared structure only; M1 and M2 are new equations.
- **Data:** fitted on Payerne 2020; Payerne is also a test station in a different year. The
  reference models' fitting stations overlap D_TEST (S3: 32 of 51, Y4: 5 of 7). No model is said
  to have shaped the data.
- **Authors:** Eugenia Paulescu is an author of PB; a flag only.

## Bearing (2026-10-18)

For the sweep's radiation inputs (splitting measured or generated global radiation into direct
and diffuse at short steps):

- **What it offers:** a three-predictor (M2) separation that needs only GHI at a minute step,
  with every coefficient printed; M1 is more accurate but needs a clear-sky model and
  several derived terms.
- **Limits:** minute data, which the sweep's hourly generator does not have; fitted on one
  Swiss station-year; worst in arid climates; validated on diffuse and direct irradiance
  with no humidity, wetness or canopy content.
- **Take:** none for the leaf-wetness hours; at an hourly step Erbs is the plainer choice
  and is not compared here.

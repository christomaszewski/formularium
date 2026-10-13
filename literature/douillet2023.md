---
id: douillet2023
citation: Douillet, Antonin. 2023. Étude pluriannuelle de la sporée aérienne de Plasmopara viticola par quantification moléculaire : un nouvel indicateur de risque des épidémies du mildiou de la vigne. PhD thesis, Université de Bordeaux (NNT 2023BORD0033), defended 2023-02-27; HAL tel-04970525, 258 pages
doi:
read: 2026-10-13, the abstracts, contents, the models section of the introduction, chapters 1-3 and annexes 1, 2 and 8, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; equations 6-9 (p. 96) and the IMPI algorithm (p. 99) read in the page images by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [airborne inoculum, sporangia survival, infection, forecasting, spray timing]
records: [brischetto2020.survival]
datasets: [douillet2023.grandeferrade]
files: [douillet2023_thesis.pdf]
---

# Douillet 2023: three years of airborne sporangia against Bordeaux epidemics

The thesis behind `douillet2022` (the LAMP method) and the VISA network: six rotating-arm
samplers read by LAMP through 2019-2021 at INRAE's Grande Ferrade vineyard, against
weekly disease ratings and the station's weather, with a weather indicator of infection
potential built to combine with them. In French.

## What it holds

- **Method (chapter 1, the 2022 paper):** LAMP against droplet digital PCR at Château
  Dillon 2020, 88 samples: sensitivity 0.80, specificity 0.75, kappa 0.53
  (l. 2805-2808); before 15 May, 37.5 % of samples positive by ddPCR against 8.3 % by
  LAMP (l. 2796); limit of quantification 3.34 sporangia/m³ (l. 2835). The 2.52
  sporangia/m³ risk threshold is Brischetto et al. 2020's (l. 2839).
- **Sampling (chapter 2):** no fixed daily rhythm of emission (the 09-13 h window held
  30.8 ± 26 % in 2021, l. 3142); capture height 30, 80 or 130 cm made no difference
  (l. 3409); continuous 24 h capture at 130 cm recommended (l. 3511). An hourly weather
  regression on captures failed; the data are not shown (l. 3289).
- **The series (chapter 3; `douillet2023.grandeferrade`):** six plots in three blocks,
  three sprayed and three under minimal protection (sprays from the first symptom seen,
  l. 3604-3607); 1 April to 30 September 2019-2021, matches changed three times a week,
  6.22 m³/h (l. 3841-3851); 48 h and 72 h samples split evenly over their days
  (l. 3855). Weekly ratings on six stands of three vines (l. 3872); the epidemic
  indicator is leaf frequency plus 0.1 times cluster intensity, over 110 (l. 3889).
  Season means 3.5 % (2019), 29.8 % (2020), 12.9 % (2021) (l. 4105). First symptoms
  2021: 17 June on the minimal plots, 22 June on the sprayed (l. 4137).
- **Sporangia survival (p. 96, eq. 8-9):** hourly mortality printed as
  (1/24)·(5.67 − 0.47·VPD + 0.01·VPD²), summed over 24 h, VPD in hPa by Tetens
  (l. 3682-3702), credited to Blaeser & Weltzien 1979 and Brischetto et al. 2020;
  survivors carried day to day give a "total" sporangia series beside the captured one
  (l. 3718).
- **IMPI, the weather indicator (p. 99):** hourly Et × Ee, Et 0 below 11 °C, linear to 1
  at 18 °C, 1 to 22 °C, linear to 0 at 30 °C (l. 3780-3784); Ee = 1 with rain above
  0.5 mm, RH ≥ 90 %, dew point above air temperature or wetness above 0.5 h
  (l. 3794-3798); summed daily. Built from the literature (Dalla Marta 2005, Caffi 2016
  and others named, l. 3773), not calibrated (l. 4714-4716); said to resemble Rossi et
  al. 2008a's hydro-thermal time in form (l. 3808).
- **Results:** before symptoms, the 7-day epidemic speed against IMPI alone R² 0.21-0.30
  and against IMPI × captured sporangia 0.73 (l. 4244-4245); after symptoms, on the
  minimal plots, R² 0.36 in Table 19 (l. 4486) but 0.16-0.17 in the discussion
  (l. 4681). Sporangia alone cannot forecast in-season risk (l. 5145); the usable
  horizon is under 14 days (l. 4997). VISA's first-spray rule in 2022 saved 1-4 early
  sprays at ten sites (l. 5076), 19 days' delay at one (annex 8, l. 7672; 21 in the
  discussion, l. 5073). A litter device gave 10, 0 and 1 pre-symptom positive days in
  2019-2021 (l. 6542).

## Dependence

- **Computes** Brischetto et al. 2020's sporangia mortality (`brischetto2020.survival`),
  with c2 = 0.01 as Blaeser & Weltzien 1979 print it, but as y/24 where Brischetto's is
  1/(24·y); which the thesis ran is not printed (a flag on the record). IMPI is the
  author's own piecewise form, uncalibrated; the hydro-thermal time is cited for
  resemblance, not computed.
- **Data:** the sporangia counts and ratings are observed; the "total" series is a
  model's (the mortality), and the daily split of 48-72 h samples is a rule. No
  infection date is back-calculated.
- **Authors:** no engine model.

## Bearing (2026-10-13)

- Cooptera's spore-trap operator: the thesis's own conclusion is that counts alone do
  not forecast, and their product with a weather window does (R² 0.73 before symptoms,
  on three years at one site). The 2022 VISA delay of 19 days is the field number.
- For `brischetto2020.survival`: a third transcription of Blaeser & Weltzien's curve,
  with the source's 0.01.

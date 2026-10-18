---
id: douillet2023
citation: Douillet, Antonin. 2023. Étude pluriannuelle de la sporée aérienne de Plasmopara viticola par quantification moléculaire : un nouvel indicateur de risque des épidémies du mildiou de la vigne. PhD thesis, Université de Bordeaux (NNT 2023BORD0033), defended 2023-02-27; HAL tel-04970525, 258 pages
doi:
read: 2026-10-13, the abstracts, contents, the models section of the introduction, chapters 1-3 and annexes 1, 2 and 8, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; equations 6-9 (p. 96) and the IMPI algorithm (p. 99) read in the page images by the main session; read again 2026-10-18, targeted (samplers, efficiency, limits), by a reading agent (claude-haiku-5-5); Chapter 2's height test read 2026-10-18
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

## Read again (2026-10-18)

A targeted reading for strand 5 (sensor error), by a reading agent (claude-haiku-5-5);
28 of 28 quotes found at their lines by scripts/verify_quotes.py; text layer only, no page
images. It adds, in the order of the sampler:

- **The sampler** (l. 2309-2311, 2523, 3102): a Sporestick (OptiSense), a rotating-arm
  impaction sampler at 2400 rpm with two wooden sticks coated with petroleum jelly at the ends
  of the arm, drawing 6.22 m³ of air per hour. At Château Dillon (Blanquefort) it hung 130 cm
  above the ground over Merlot from 13 March 2020 (l. 2517).
- **Catch efficiency is assumed, not measured** (l. 3019, 3046): the thesis uses Aylor
  1982's formula EC(u) = 0.86 / (1 + 0.442 St^-1.967), St = u v / (g L) (Equations 4-5, the
  formula as cited; the equation images were not rendered), and states that wind has no
  effect on the rotating arm's efficiency. No efficiency is reported. Repeatability of the
  rotating-arm capture "was not tested" (l. 3169).
- **Limits of the molecular count** (l. 2660, 2727-2731, 2835): the limit of detection is
  the concentration detected in 95 % of samples (the Forootan et al. 2017 approach): 50 to
  500 sporangia per mL of lysis solution (87.5 % to 100 % amplified); the limit of
  quantification is 500 sporangia per mL (CV 15.6 %), or 1000 sporangia stuck on the
  collectors. In air the detection limit is 0.33 to 3.34 sporangia per m³ sampled.
- **LAMP against ddPCR** (l. 2791-2807, Château Dillon 2020, 88 samples, 0 to 243 sporangia per
  m³, l. 2413): 68 % positive by ddPCR (60 of 88), 62 % by LAMP (55), 55 % by both; LAMP and
  ddPCR R² 0.52 on the field samples; likelihood ratios LR(+) 3.2 and LR(-) 0.27.
- **Counts of other studies** (l. 3253): Albelda 2005, Chavarria 2009, Fernandez Gonzalez 2009
  and Caffi 2013 report about ten sporangia per m³, an order below this thesis.
- **Onset dates** (l. 2345, 4133-4137): six plots at Grande Ferrade, 2019-2021. First symptoms
  2019 on 15 May on the minimal-protection plots only; 2020 on 2 May (block B) and 6 May
  (blocks A and C); 2021 on 17 June (minimal) and 22 June (sprayed). Positive captures after
  the first symptoms 89 % (2019), 97 % (2020), 94 % (2021) (l. 4113).
- **Weekly R² ranges** (l. 4245, 4372, 4681-4691): before symptoms, the 7-day epidemic speed
  against IMPI alone 0.21 and 0.30, against IMPI times captured sporangia 0.73 and 0.59; after
  symptoms, the same week 0.23 to 0.36 and the next week 0.10 to 0.26 (Table 19); on the
  minimal-protection plots 0.16 (measured) and 0.17 (total). The author calls the 7-day
  predictive power limited.

### Bearing (2026-10-18)

For strand 5: a spore sampler's observation error is a chain, none of it measured here: a
catch efficiency taken from a formula and assumed independent of wind (a model could take a
fixed efficiency, with no wind dependence, as the thesis does, and a stated uncertainty); a
molecular detection floor of about 0.3 to 3.3 sporangia per m³ (a threshold: counts below it
read as zero); and a counting error that
LAMP against ddPCR puts at sensitivity 0.80 and specificity 0.75 in the field. It is a
laboratory result for the limits and a field result for the agreement, one season at one
château, and nothing for drift or failure.

### Chapter 2: capture height (read 2026-10-18)

A targeted reading of Chapter 2, section II (printed pp. 88-92; l. 3347-3521), with the chapter summary and the discussion on p. 130, by a reading agent (claude-haiku-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py. Figures 28-32 were read by eye from the rendered pages.

- **Design** (l. 3370-3376, 3379-3380): three Sporestick samplers at 30, 80 and 130 cm on a training stake, on the westernmost row of organic plot SPM-A (2 August to 18 September 2019; 3 August to 3 September 2020) and of SPM-A and SPM-C (30 April to 30 August 2021), Grande Ferrade; sticks collected Monday, Wednesday and Friday. Response log10(sporangia per m3 + 1), Kruskal-Wallis then Dunnett with Bonferroni adjustment, per year (l. 3397-3402). No p-values, sample sizes or canopy height are printed.
- **No height effect** (l. 3409, 3446): not significant in any of the three years; every box carries the same letter in Figures 28-30. Medians read by eye on the log scale, 30 / 80 / 130 cm: 2019 about 0.1 / 0 / 0; 2020 about 0.15 / 0 / 0.66; 2021 about 0.07 / 0 / 0 (approximate, plus or minus about 0.1). End of August 2021 cumulative, by eye (l. 3484): bloc A about 7,300 / 4,950 / 5,900 sporangia per m3; bloc C about 5,150 / 3,900 / 4,250 (plus or minus about 200). The lowest sampler holds the highest cumulative total in both plots, and the 130 cm one is not the highest.
- **The 130 cm recommendation rests on first detection, not on significance** (l. 3413-3422, 3516-3518, 4822): in 2021 the first positive capture was at 130 cm in both plots (bloc A, 6 June, against 13 June at 30 cm and 22 June at 80 cm; bloc C, 2 May, against 29 May and 29 June); only the 2021 series began at the start of the season (l. 3418). The authors read this as a Gaussian plume with a strong source effect (Severns et al. 2019) and as confirming Van der Heyden et al. 2021's advice, say above the canopy "seems better" though not significant (l. 3516), and keep 130 cm. The early-season hypothesis of a lower sampler nearer the soil source is not validated (l. 4822).

Bearing for strand 5 (sampler placement): a capture-height effect on counts is not established by this test (a sampler-height offset of zero with an uncertainty, not a correction), the first-detection difference is two plots in one year and a reason to place the sampler above the canopy rather than a measured bias.

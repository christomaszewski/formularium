---
id: baratto2022
citation: Baratto, C., Ambrosio, G., Faglia, G. & Turina, M. 2022. Early detection of esca disease in asymptomatic vines by Raman spectroscopy. IEEE Sensors Journal 22(23):23286 (end page not read)
doi: 10.1109/JSEN.2022.3211616
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [esca]
crops: [grapevine]
regions: [Lombardy, Italy]
processes: [Raman spectroscopy, leaf spectra, PLS-DA classification, latent detection]
records: []
datasets: []
files: [baratto_2022.pdf (the 2026-10-20 drop)]
---

# Baratto et al. 2022: Raman leaf spectra for esca before symptoms

A proof-of-concept Raman and PLS-DA classifier separates healthy vines from esca-affected vines. It uses leaves from one vineyard, sampled on one date.

## What it holds

- **Site:** one vineyard of cv Marzemino in Brescia province, Lombardy (l. 86-88). One sampling on 28 June 2021 (l. 92). Healthy vines, symptomless branches and symptomatic branches were taken (l. 92-100).
- **Spectra:** six Raman spectra per leaf, at a 532 nm laser and 4 cm-1 resolution (l. 110-126).
- **Model:** PLS-DA on smoothed, baseline-corrected spectra (l. 130-133, 144). The bands near 1155 and 1520 cm-1 separate the classes (l. 212, 249, 278).
- **Result:** all test samples correctly classified (abstract, l. 24-25; l. 229). Validation was leave-one-group-out (l. 223-224) and a random 80/20 split (l. 265). No sample count and no error statistic are printed in the text read.

## Dependence

- PLS-DA, and the MATLAB Classification toolbox (l. 131-133).
- Carotenoid Raman band assignments from the literature (Table I, l. 151-152).

## Bearing (2026-10-20)

- Strand t4 (other grape diseases: esca). The leaf signal hints at a latent esca marker. One vineyard and one date cannot set a detection rate, and a simulator cannot use it yet.
- Not read in full.

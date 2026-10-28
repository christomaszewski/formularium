---
id: sandonispozo2026
citation: Sandonís-Pozo, L., Cheraïet, A., Féret, J.-B., Lablee, J.-L., Taylor, J. & Tisseyre, B. 2026. A Hybrid LiDAR-PROSAIL Approach for LAI Estimation in Vineyards. Smart Agricultural Technology 14:102007
doi: 10.1016/j.atech.2026.102007
read: 2026-10-27, lightly: abstract, introduction, the PROSAIL and validation methods, results 3.1 to 3.4 and the opening of the discussion (the HAL author's accepted manuscript, journal pre-proof), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Hérault, Grabels]
processes: [radiative transfer, PROSAIL, LiDAR, leaf area index, Sentinel-2, support vector machine, hybrid retrieval, look-up table]
records: []
datasets: []
files: [syn1027_sandonis2026.pdf (the 2026-10-27 drop)]
---

# Sandonís-Pozo et al. 2026: PROSAIL LAI from Sentinel-2 corrected by LiDAR structure in a Mediterranean vineyard

Inverts the 1-D PROSAIL model on Sentinel-2 reflectance for vineyard leaf area index (LAI) and corrects it with a support vector machine that takes a LiDAR leafiness index. No record: a method with a small destructive test. Filed under the first author's surname, joined: the key of the drop is sandonis2026.

**Read this first.** "Hybrid" here means a PROSAIL baseline plus a statistical correction from LiDAR (l. 514), not a model trained on simulated spectra; PROSAIL is a feature generator. The leave-one-plot-out validation covers only the LiDAR-index models (Table 6): the structural weights were estimated once on all 18 samples and kept fixed in the loop (l. 507 to 510), so the hybrid's R2 of 0.88 is not a clean out-of-sample figure. The authors say the aim is not to show that PROSAIL beats data-driven approaches (l. 888); no NDVI-regression baseline was compared in the text read.

## What it holds

- **Generator** (l. 93, 368, 369): the PROSAIL model (R package prosail), inverted on Sentinel-2 reflectance with LAI constrained to 0.2 to 3.5 and all other inputs set to "broad, physiologically plausible" ranges listed in the authors' code, not in the paper. The authors state that PROSAIL underestimates vineyard LAI because of the canopy architecture.
- **Real samples** (l. 237 to 239, 470, 474): one rainfed Mediterranean vineyard in southern France, 2023 season; three varieties (Cabernet Sauvignon, Petit Verdot, Chardonnay), three phenological stages, two destructive subplots each: 18 LAI samples in all, 1 m segments with all foliage removed and leaf area measured by planimeter.
- **Test** (l. 470, 507): the same 18 samples serve as reference for PROSAIL and the hybrid; the authors flag the small sample (n = 18).
- **PROSAIL alone against destructive LAI** (l. 102, 759, 773, 775, 781): R2 0.42 ("42 % of the variance"); LAI underestimated for every variety and stage; at the late stage measured LAI is 2.6 to 3.4 m2/m2 while PROSAIL stays near 1.0 to 1.1; Cabernet Sauvignon, late stage, 1.11 against 3.35 m2/m2.
- **Hybrid** (l. 101, 785): R2 0.88 against the destructive LAI, with differences from measured LAI between -0.44 and +0.37 m2/m2 (the unit continues on the next line).
- **Leave-one-plot-out, LiDAR-index models only** (Table 6, l. 736, 751, 753): unweighted index R2 0.24; global and stage-weighted indices 0.58 and 0.54; variety-weighted index R2 0.70, RMSE 0.28 (l. 753).
- **Reading** (l. 920): 3-D radiative-transfer models could represent row geometry but are computationally heavy.

## Dependence

- PROSAIL (Jacquemoud et al. 2009, per the reading agent), LiDAR scans of the rows and an SVM regression; the weights of the LiDAR index were fitted on all 18 samples. `kang2022` (held) is the lead on site-trained LAI models. Shares an author (Féret) with `morel2018`, a flag only.

## Bearing (2026-10-27)

- **D60 (several physical models per gap):** a field test, small, that a 1-D model cannot give vine LAI from Sentinel-2 without a structure term (R2 0.42, LAI 1.0 instead of 3.35), which matches `brown2024`'s finding for airborne imagery. For tier-3 canopy imagery sensors in Agrarium, a model with row structure is the one to simulate.
- **Not a simulator-trained model:** nothing is trained on synthetic spectra here; it does not show a gain from simulated training data.
- **Not shown:** an empirical NDVI baseline, a clean out-of-sample score for the hybrid, a second season or site, water status.

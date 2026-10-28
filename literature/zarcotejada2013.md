---
id: zarcotejada2013
citation: Zarco-Tejada, P.J., Guillén-Climent, M.L., Hernández-Clemente, R., Catalina, A., González, M.R. & Martín, P. 2013. Estimating leaf carotenoid content in vineyards using high resolution hyperspectral imagery acquired from an unmanned aerial vehicle (UAV). Agricultural and Forest Meteorology 171-172:281-294
doi: 10.1016/j.agrformet.2012.12.013
read: 2026-10-27, lightly: abstract, the field and airborne methods, the simulation and scaling-up sections, the results on synthetic spectra and on the 2009 to 2011 imagery, and the conclusions (the author's personal copy, pages 281 to 294), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Ribera del Duero]
processes: [radiative transfer, synthetic spectra, PROSPECT, SAILH, FLIGHT, UAV hyperspectral imagery, carotenoids, vegetation index, hybrid retrieval]
records: []
datasets: []
files: [syn1027_zarcotejada2013.pdf (the 2026-10-27 drop)]
---

# Zarco-Tejada et al. 2013: leaf carotenoids of Tempranillo vines from UAV imagery, with indices fitted on simulated spectra

Fits a relationship between two spectral indices and leaf carotenoid content on 1,000 synthetic spectra (PROSPECT-5 linked to infinite-reflectance formulas, SAILH or the 3-D FLIGHT vineyard scene), then applies it to UAV imagery of 12 vineyards over three years and compares with laboratory carotenoid values. No record: a method with a field test.

**Read this first.** "Hybrid" here means indices whose relationship was fitted on simulated spectra and then applied to imagery, not full model inversion. The simulator figure (r2 0.93) comes from 500 held-out draws of the same simulator; the field figures are much lower (0.2 to 0.64). The synthetic LAI range is narrow (1 to 3), and the reading agent notes small numbers of leaves per plot; the count was not transcribed.

## What it holds

- **Generator** (l. 492 to 494, 466): a synthetic spectra database of 1,000 random draws of leaf chlorophyll a+b and carotenoids, dry matter Cm (0 to 0.03), leaf structure N (1.6 to 1.8), LAI (1 to 3) and soil reflectance, through PROSPECT-5 linked to three infinite-reflectance formulations (R-infinity 1 to 3), SAILH and the Monte Carlo ray-tracing FLIGHT vineyard scene. 500 draws fit the relationship and 500 test it.
- **Real samples** (l. 45, 167): August 2009 to 2011, western Ribera del Duero, northern Spain; 12 production vineyards with two 10 m x 10 m study plots each (Tempranillo, l. 167); leaves destructively sampled for laboratory chlorophyll and carotenoids; UAV imagery from a 6-band multispectral camera (2009) and a 260-band hyperspectral imager (2010, 2011; 40 cm pixels).
- **Test:** the relationship applied to UAV pixels was compared with the laboratory carotenoid values of the field plots; no cross-validation of the simulator-fitted relationship is described in the parts read.
- **Inside the simulator** (l. 564, 568): carotenoid from R515/R570 alone, with chlorophyll varying, r2 0.51, RMSE 1.99 ug/cm2 (PROSPECT + SAILH); with R515/R570 and TCARI/OSAVI together, r2 0.93, RMSE 0.73 ug/cm2.
- **Leaf level** (l. 648): R515/R570 against laboratory carotenoids, r2 0.84.
- **On the UAV imagery against laboratory values** (l. 623, 624, 627, 629): over the three years, the simplest formulation (R-infinity 2) r2 0.41 to 0.64, RMSE 0.8 to 1.6 ug/cm2 (R-RMSE 8.9 to 15 %); SAILH r2 0.2 to 0.56, RMSE 1.08 to 4.6; FLIGHT r2 0.26 to 0.58, RMSE 1.25 to 2.91. The largest errors came from the 2009 multispectral imagery (l. 630); SAILH and FLIGHT reached RMSE below 1.3 ug/cm2 for the 2010 and 2011 hyperspectral imagery (l. 642).
- **Reading** (l. 784): the simpler formulations gave better results than the more complex canopy models.
- **Without simulated spectra:** not run; the leaf-level index relationship (r2 0.84) is the only empirical comparison.

## Dependence

- PROSPECT-5 (Féret et al. 2008, per the reading agent), SAILH, FLIGHT (North 1996), the R515/R570 index proposed earlier for conifers, and TCARI/OSAVI. The vineyard row model rowMCRM of the same group is cited. `brown2024` tests a related row-structure approach. No author is shared with `brown2024`, `morel2018` or `sandonispozo2026`, which use the PROSPECT family too.

## Bearing (2026-10-27)

- **D60:** a vine case where a physical model supplies the training of an index relationship, judged on 12 vineyards over three years against laboratory values, not against the simulator. The drop from r2 0.93 in the simulator to at most 0.64 in the field is the size of the gap for tier-3 canopy imagery sensors: simulator agreement does not establish the sensor.
- **More complex did not mean better:** the 3-D scene (FLIGHT) did not beat the simplest formula on the real imagery, which argues against assuming a richer rendered canopy gives a better sensor model.
- **Not shown:** a held-out vineyard or year for the fitted relationship, a count of leaves, disease, or water status.

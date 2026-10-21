---
id: adhikary2014
citation: Adhikary, S. K., Yilmaz, A. G. & Muttil, N. 2014. Optimal design of rain gauge network in the Middle Yarra River catchment, Australia. Hydrological Processes 2582-2599 (accepted manuscript; volume not recorded)
doi: 10.1002/hyp.10389
read: 2026-10-21, lightly: abstract, Introduction, Methodology, Study area, Results (Tables II-VI, Figures 2-7) and Conclusions, the reference list skimmed; the copy read is the accepted version, and the journal, year and DOI are from OpenAlex, 2026-10-21; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 26 of 26 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Australia, Victoria, Middle Yarra River]
processes: [sensor placement, rain gauges, ordinary kriging, kriging standard error, redundant stations, variogram]
records: []
datasets: []
files: [adhikary2014.pdf (the 2026-10-21 drop)]
---

# Adhikary, Yilmaz & Muttil 2014: placing rain gauges where the kriging error is highest

Moves one redundant gauge and adds two in a 19-gauge Victorian catchment by searching trial sites on kriging standard error maps. No record: a method.

**Read this first.** The search is manual: 15 trial combinations (Table III), not an optimiser. The only evaluation is two years (1997 El Nino, 2010 La Nina) of areal-mean rainfall (l. 48). Equations 1 to 4 and 6 are partly garbled in the text layer; Eq. 6 uses h_0i where the text says h_0j (garbled/unreconciled). Table III trial coordinates were not transcribed. The publisher version was not read.

## What it holds

- **Catchment** (l. 224, 252-260): 1511 km2; 19 Bureau of Meteorology gauges, of which 17 existed before 2011 and stations 18 and 19 were added in 2011.
- **Criterion** (l. 47, 506): reduction of the kriging standard error (KSE); relative error reduction RE = (KSE_old - KSE_new) / KSE_old x 100 (Eq. 8, PDF page 9).
- **Variogram** (l. 376, 558, 591): exponential, Gaussian and spherical models (Eq. 2-4) compared; lag 2.835 km (the minimum station spacing); the Gaussian model fitted best by R, RSS, RMSE and MAE. Leave-one-out cross-validation chose the model (l. 461).
- **Search** (l. 521, 776): find high-variance zones on the KSE map, locate one or more gauges there, recompute RE; stations 5 and 6 are called redundant from low-variance zones.
- **Result** (l. 888-915): Case 1, trial 7 (stations 18 and 19 moved to trial positions 18A and 19D) gives the largest KSE reduction; Case 2, relocating station 5 only (trial 13), gives the largest for El Nino; relocating 5 and 6 (trial 15) is similar but costlier. The optimal network is 19 stations.
- **Areal mean** (Table VI, l. 864-865): El Nino observed 1.946 mm, BoM network 1.905 mm; Case 2 optimal 1.949 mm (error 0.2 %). La Nina observed 3.541 mm, BoM 3.509 mm (0.9 %); Case 1 optimal 3.526 mm (0.4 %); Case 2 optimal 3.520 mm (0.6 %). The authors call the improvement at the mean daily scale insignificant (l. 881), and Case 1 improves La Nina only (l. 920).

## Dependence

- Follows Loof et al. (1994), who added stations by kriging with a fixed exponential variogram (l. 149); lognormal kriging variance after Cressie (1993) (Eq. 7); ArcGIS geostatistics (Johnston et al. 2001). Frames itself against kriging with simulated annealing and entropy with kriging (Introduction). Shared authors: none checked.

## Bearing (2026-10-21)

Scoring placements by kriging variance, for Agrarium's placement-methods study (PLAN 15, D48).

- **Representative-site clustering:** none. No clustering and no representative; sites are candidate trial positions read from a variance map. This is the kriging criterion for that arm: no random layout, entropy criterion or held-out comparison is run against it.
- **Takeable:** the variance-map-then-trial loop, using RE to rank candidate moves, and a way to flag redundant gauges from low-variance zones. Not shown: held-out gauge errors, random baselines, or any automatic optimiser.
- **Kind of result:** a worked case on one catchment, scored on two years' areal means; small gains.

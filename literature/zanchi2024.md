---
id: zanchi2024
citation: Zanchi, M., Zapperi, S. & La Porta, C. A. M. 2024. Optimized placement of sensor networks by machine learning for microclimate evaluation. Computers and Electronics in Agriculture 225:109305
doi: 10.1016/j.compag.2024.109305
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 39 of 39 quotes found at their lines by scripts/verify_quotes.py; Equations 1-9 and 13-15 read in the page images, Equations 10-12 and Table 1 from the text layer; Figure 3 values read by eye; the supplementary material was not read
status: read
diseases: []
crops: []
regions: [Italy, Lombardy, Bergamo]
processes: [sensor placement, microclimate, temperature maps, clustering, K-means, neural network forecast]
records: []
datasets: []
files: [r_10_1016_j_compag_2024_109305.pdf (the 2026-10-18 drop, second pass)]
---

# Zanchi, Zapperi & La Porta 2024: where to put microclimate sensors, by clustering modelled temperature maps

Chooses the layout of a temperature sensor network by clustering hourly 2 m temperature maps of a Lombardy foothill area, then tests four clusters with 20 loggers. No record: a method.

**Read this first.** The temperature maps that are clustered come from the authors' own earlier framework (Zanchi et al. 2023, Sci. Rep. 13:21062), whose neural network is trained on the same 25 sensors that the layout is meant to place (l. 238, 252-260). Placement and map therefore share calibration data: the layout is judged against a map that already encodes what those sensors saw. No reconstruction error per design is printed, and no comparison with a regular or random layout (check leads, l. 599-629 only give p-values and Tables 2-3). The code and data are on GitHub (dndg/MicroClimateOptSensorML, l. 34, 824) with no licence printed.

## What it holds

- **Maps** (l. 42, 137, 232, 251-260): hourly 2 m temperature maps, 4488 of them, 12 November 2022 to 22 June 2023, from a physical downscaling plus a feed-forward network (equations not printed here). Vegetation map handcrafted (l. 242-247).
- **Clustering** (l. 259-282, 470, 485): K-means on 50 principal components of the hourly series (90 % of variance, l. 266); K searched from 2 to 25; K-means beat Ward and complete linkage on MAE to the cluster centre and on silhouette. Centre = the grid point with least MAE to its cluster (Eq. 4). 17 clusters chosen by eye from the curve, cost the stated reason, not a fixed rule.
- **Fit** (Figure 3, read by eye; l. 478-479, 530): MAE to the centre about 0.30 degC at 2 clusters and about 0.18 degC at 25, falling faster to 17; silhouette low, about 0.12 to 0.19 for K-means from 10 to 25 clusters (the text says ideally 1). Fragmented clusters at the area edges, attributed to vegetation (l. 516).
- **Validation sensors** (l. 175-197, 569): 20 MEMS sensors, temperature +/-0.5 degC, RH +/-5 %, in wood shelters, 23 July to 15 August 2023; four clusters (0, 2, 6, 10) of 5 sensors each (l. 337).
- **Result** (l. 603-629): clusters 6 and 10 have a spread lower than the whole area's (Mann-Whitney p < 0.05, called representative); clusters 0 and 2 do not (p > 0.05). Removing the sensor at the vegetation border flips cluster 0 to p < 0.05. In the forecast check (l. 699-712) clusters 0, 6 and 10 differ from outside at p < 0.05, cluster 2 does not.
- **Forecaster** (l. 390-453, 663): Nhits (72 h of temperature and RH in, 24 h of temperature quantiles out, 17 quantiles, 6 stacks of 2 blocks, 128 neurons, up to 1000 epochs), trained on one ARPA station 2018-2020, validated 2021, tested 2022. Table 2 validity: 0.975 for the (0.01, 0.99) band down to 0.198 for (0.40, 0.60); Table 3 with transfer learning 0.960 to 0.213. The authors give the single-station training as a limitation (l. 719, 773).
- **Not printed:** reconstruction error per design; any regular or random layout for comparison; the 2 m model's equations or fit; wetness (temperature only; RH is an Nhits input only, l. 393).

## Dependence

- Shared calibration data: the 25-sensor series feeds the maps (via Zanchi et al. 2023) that define the clusters, and that series is also the Table 1 training set. Nhits is Challu et al. 2023, trained on an ARPA station and reused on the sensors without retraining, assuming comparable temperature patterns (l. 501-510). A shared author with Zanchi et al. 2022 (the Lombardy map) is a flag, not a dependence.

## Bearing (2026-10-18)

Strand 6 (methods), for sensor placement in Agrarium's sweep.

- **Takeable:** the recipe: cluster a modelled field of hourly values (PCA, K-means), put one sensor at each cluster's least-MAE point, and choose K from the MAE curve against cost. The 50-component, 90 % variance step and K = 17 are this site's values.
- **Not shown:** that the layout beats a regular or random one, or how large the reconstruction error is for any design. K is chosen by eye on a low-silhouette clustering, and the two failed clusters sat next to vegetation.
- **Wetness:** none. Temperature only, so a layout for wetness would need a modelled wetness or RH field to cluster; versus the engine's RH >= 90 % stand-in nothing is compared.
- **Kind of result:** a method with a small field check (20 loggers, 3 weeks of summer), validated by p-values.

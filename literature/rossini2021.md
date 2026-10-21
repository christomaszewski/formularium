---
id: rossini2021
citation: Rossini, P.R., Ciampitti, I.A., Hefley, T. & Patrignani, A. 2021. A soil moisture-based framework for guiding the number and location of soil moisture sensors in agricultural fields. Vadose Zone Journal 20:e20159
doi: 10.1002/vzj2.20159
read: 2026-10-21, lightly: abstract, introduction, methods (kriging, fuzzy C-means, silhouette, Jaccard, sensor location index), results and discussion, the sensitivity analysis and the conclusions, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [USA, Kansas]
processes: [sensor placement, soil moisture, fuzzy C-means, management zones, silhouette score, kriging, representative site]
records: []
datasets: []
files: [rossini2021.pdf (the 2026-10-21 drop)]
---

# Rossini et al. 2021: fuzzy C-means soil moisture zones, one sensor per zone, in three Kansas fields

Delineates management zones in each of three fields by fuzzy C-means on kriged soil moisture surveys, picks the number of zones by the silhouette score, and puts one soil moisture sensor at the cell of each zone with the highest sensor location index (SLI). No record: a method.

**Read this first.** The abstract says "a total of two SMS were sufficient" across the three studied fields (l. 43-44), which can mean two sensors in all or two per field; the results give two zones per field (l. 478-479) and Figure 7 shows one sensor per zone (l. 847-848), which reads as two per field. This is flagged as ambiguous. The denominator of Eq. 2 is not in the text layer and the product form of Eq. 4 is inferred from the prose (l. 334-335); both are recorded as unchecked. There is no held-out sensor test and no random baseline.

## What it holds

- **Method** (Sections 2.2 to 2.4, l. 225-338): 0 to 12 cm soil moisture surveyed with a handheld reflectometer (custom calibration RMSE 0.027 against 0.041 m3 m-3 for the factory one, l. 229), ordinary kriging on a 5 m grid (l. 255; exponential semivariogram best in 10 of 16 surveys, l. 247); each map is normalised to the field mean (Eq. 2, l. 276, garbled, unchecked); fuzzy C-means with 1 to 6 clusters (l. 260), the number chosen by the silhouette score, or fixed from a budget, in which case the silhouette step is skipped (l. 264).
- **Sensor location** (Eq. 4, p. 6, l. 325, garbled, unchecked): SLI is the distance of a cell to its zone boundary, scaled by the largest such distance in the zone, times the FCM membership grade; the cell with the highest SLI is the tentative sensor site (l. 335, 849).
- **Data** (l. 115-169, 355, 363): 16 surveys on three fields near Gypsum (28 ha) and Hutchinson (58 ha) and a third field (22 ha), Kansas, May 2017 to June 2019, 4,659 observations in all (l. 169). Field-average moisture was 0.247 to 0.314 m3 m-3 (l. 355) and its coefficient of variation 6.8 to 20.3 % (l. 363).
- **Results** (l. 478-479, 526-527, 625-626): two zones in every field; silhouette 0.60 to 0.68; zoning cut the intrazone standard deviation by about 50 %.
- **Sensitivity** (l. 764-767, 800-801, 858-863, 871-872): zones from only the wettest and driest survey against all 16 gave Jaccard 0.60 (field C, dry) to 0.93 (field B, wet), average 0.79, and moved the sensor site by 12 m (field A, dry) to 147 m (field C, wet). Elevation zones gave Jaccard 0.48 on average, and texture-based sensor sites were 37 to 463 m from the benchmark.

## Dependence

- Builds on fuzzy C-means (Bezdek 1981; the ffcmw Matlab code of Cococcioni), the silhouette criterion (Rousseeuw 1987), ordinary kriging, time stability (Vachaud et al. 1985), the Jaccard index and a distance transform (Maurer et al. 2003). None of the authors' own models are borrowed.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): representative-site, zone-based placement in a field.

- **Method:** features are normalised kriged soil moisture maps from repeated surveys (proxies such as elevation and texture were weaker, l. 800-801, 871); k is picked by silhouette (1 to 6) or from the budget; the representative is the cell with the highest SLI, i.e. the centre-most cell with a high membership grade. This is the closest match to a field-scale clustering recipe among these eight papers.
- **Validation:** none against a held-out sensor or a random layout. Checks are zone variance reduction (about 50 %, l. 625-626) and stability of zones and sites across surveys (Jaccard 0.79 average; sites moved 12 to 147 m, l. 858-863), with 16 surveys as the benchmark.
- **Not shown:** error of the monitored variable at unmeasured cells, a comparison with MI, kriging variance or random placement, and a sensor menu or a re-plan.

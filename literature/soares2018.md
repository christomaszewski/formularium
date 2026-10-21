---
id: soares2018
citation: Soares, J., Makar, P. A., Aklilu, Y. & Akingunola, A. 2018. The use of hierarchical clustering for the design of optimized monitoring networks. Atmospheric Chemistry and Physics 18:6543-6566
doi: 10.5194/acp-18-6543-2018
read: 2026-10-21, lightly: Sections 1 to 8, Tables 1-2 and the figure captions; the Supplement was not in the text, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Canada, Alberta, Saskatchewan]
processes: [sensor placement, hierarchical clustering, network redundancy, air quality monitoring, model as surrogate, data loss]
records: []
datasets: []
files: [soares2018.pdf (the 2026-10-21 drop)]
---

# Soares, Makar, Aklilu & Akingunola 2018: ranking air-quality monitors by hierarchical clustering of their series

Clusters hourly SO2 and NO2 series of Alberta monitors (and of model cells) with 1 - R and Euclidean dissimilarities, and reads redundancy off the dendrogram. No record: a method.

**Read this first.** No representative site is chosen per cluster, and the paper proposes no redundancy threshold (l. 384-385, 957). Three internal inconsistencies in the print are left unreconciled: (a) lines 773-775 say the model shows more clusters than the observations but print 21 (model) against 25 (observations) for SO2 at 1 - R 0.75 (garbled/unreconciled); (b) lines 812-813 place 17 stations in 14 coloured regions (garbled/unreconciled); (c) a 36-by-36 test subdomain (l. 280) against a 72 x 72 block for the maps (l. 757), possibly two different areas. The Supplement (Tables S1-S6, Figs S1-S15) was not read.

## What it holds

- **Method** (l. 293, 297-325): agglomerative clustering with the general averaging update, run on 1 - R (Pearson) and on Euclidean distance (l. 33); the closest pair merges first, repeat until two clusters remain. Hourly series, and series with the sub-daily, sub-weekly or sub-monthly signal removed by a KZ filter (l. 255).
- **Observations** (l. 150-151, 204, 212, 221): 39 continuous and 89 passive SO2 sites, 38 continuous and 88 passive NO2 sites. Passive sites with more than 25 % missing are rejected; continuous sites with more than 10 % of the year missing are rejected. Passive and continuous cross-comparison covers February 2009 to December 2015 (l. 204).
- **Clusters** (l. 372, 375, 396-397): NO2 shown at 1 - R levels 0.75, 0.65 and 0.55; 11 clusters at 0.55. After removing the sub-daily, sub-weekly and sub-monthly signal the same level gives 4, 3 and 2 clusters. Averaging loses airshed-specific clusters (l. 899).
- **Where it fails** (l. 567, 583): two sites 4 km apart have SO2 R = 0.81 but a Euclidean distance of 177 ppbv; a pair with the lowest 1 - R for NO2 has a Euclidean distance of 400 ppbv.
- **Model as surrogate** (l. 246, 724-725, 774): GEM-MACH, 2.5 km, August 2013 to July 2014. NO2 at 1 - R 0.65: 6 observation clusters against 10 model clusters; at 0.55: 11 against 13. SO2 at 0.75: 21 against 25 as printed (see above).
- **Optimised maps** (l. 757, 812-815, 845-846): over a 72 x 72 block of model cells, 17 stations for NO2 at 1 - R 0.65 and 17 for SO2 at 0.80. The authors call the maps a proof of concept.
- **Noise test** (l. 897-898): uniform noise of +/-0.5 ppbv (NO2) and +/-1 ppbv (SO2) added to the model series; SO2 clusters changed.

## Dependence

- Builds on Solazzo & Galmarini (2015) for clustering of station data, on Naes et al. (2010) for the linkage update (l. 293), on the Kolmogorov-Zurbenko filter (l. 238) and on Bari et al. (2015) for passive against continuous comparisons (l. 676). The model-derived maps depend on GEM-MACH output rather than on measurements. Shared authors: none checked.

## Bearing (2026-10-21)

Representative-site clustering, and the model-as-surrogate idea, for Agrarium's placement-methods study (PLAN 15, D48).

- **Features, k and representative:** the features are the pairwise 1 - R or Euclidean dissimilarities of each site's hourly (or filtered) series. k is not chosen: the dendrogram is cut at a stated dissimilarity (1 - R 0.55 to 0.80). No representative per cluster is selected; a candidate is any site or cell that joins a cluster at the chosen level (l. 315-318), so the method ranks redundancy, it does not place.
- **Validation:** none against held-out data, random layouts, entropy or kriging criteria (the reading found none). The checks are agreement of model-derived against observation-derived clusters and the noise test. Absolute thresholds are explicitly not offered (l. 957).
- **Takeable:** the 1 - R against Euclidean split (shape against level) for wetness-like series, and the use of a model field to cover unmonitored cells. Not shown: reconstruction error of any reduced network.
- **Kind of result:** a method demonstrated on one region and two gases, with unreconciled counts.

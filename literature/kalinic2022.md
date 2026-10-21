---
id: kalinic2022
citation: Kalinic, H., Catipovic, L. & Matic, F. 2022. Optimal Sensor Placement Using Learning Models: A Mediterranean Case Study. Remote Sensing 14:2989
doi: 10.3390/rs14132989
read: 2026-10-21, lightly: abstract, Sections 1 to 5, Tables 1-3 and the figure captions (figures not in the text layer), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Mediterranean Sea]
processes: [sensor placement, clustering, K-means, self-organising map, neural gas, wind reconstruction, random baseline]
records: []
datasets: []
files: [kalinic2022.pdf (the 2026-10-21 drop)]
---

# Kalinic, Catipovic & Matic 2022: sensor sites from cluster centres of ERA5 wind, against random sites

Picks 10 to 200 sensor sites among 1244 Mediterranean points by clustering their 6-hourly wind series and snapping each cluster centre to a real site, then reconstructs the other sites and compares with random sensors. No record: a method.

**Read this first.** Data and reconstruction errors come from ERA5, a reanalysis, not from measurements, so the "truth" is itself a model field. The random baseline is one draw per cohort size, with no spread (l. 589-593). The test set is a random 20 % of times (l. 168), so it comes from the same years as training. Two points are garbled/unreconciled: the data matrix is printed as 1244 by 179700 (l. 142) although 41 years at 6 h with two components gives about 119,800 columns by the reading agent's count; and the text calls each row a time's spatial vector (l. 143) although the 1244 rows are the sites. Equations 6, 9, 11, 12, 14 and 15 are partly garbled; Eq. 11 and 12 use inconsistent indices.

## What it holds

- **Data** (l. 121, 142, 131-140): ERA5 10 m wind u and v, 0.5-degree grid, 1244 sea points, 1979 to 2019, 6-hourly, concatenated u and v per site.
- **Selection** (l. 196, 205, 504): K-means, growing neural gas or self-organising map on the training data; the cluster centre is moved to the closest available site, which becomes the sensor. Cohorts of 10, 20, 50, 100 and 200 sensors (l. 442).
- **Reconstruction** (l. 393, 656): other sites are rebuilt from the sensors by KNN (k = 4, Gaussian kernel) or linear regression; with more than 20 sensors linear regression beats KNN.
- **K-means against random, linear regression, amplitude error in m/s** (Tables 1 and 3, l. 526-530, 589-593): 10 sensors 2.72 against 3.33; 20 sensors 2.16 against 2.53; 50 sensors 1.51 against 1.81; 100 sensors 1.13 against 1.37; 200 sensors 0.79 against 0.95. Mean wind amplitude is 5.55 m/s (l. 511).
- **KNN** (l. 530, 593): K-means 2.28 against random 2.78 m/s at 10 sensors; at 200 sensors 1.79 against 1.82 m/s, almost no gain.
- **Angular error** (l. 526, 589): 10 sensors, linear regression, 31.42 degrees for K-means against 39.80 degrees for random.
- **Shore term** (l. 464, 559, 672, 692): adding a distance-to-shore criterion with equal weight raises the K-means 10-sensor error from 2.72 to 2.98 m/s, up to about 10 % worse; only 372 sites lie within about 31 km of shore.
- **Conclusion** (l. 651, 749): K-means is best of the three; 10 points give an amplitude error under 3 m/s.

## Dependence

- Builds on the authors' earlier clustering work for sensor location in the Adriatic (refs 18-19) and on K-means, neural gas, growing neural gas and Kohonen maps. Data: ERA5 (Copernicus). A shared author with the Adriatic work is a flag, not a dependence.

## Bearing (2026-10-21)

Representative-site clustering, for Agrarium's placement-methods study (PLAN 15, D48).

- **Features, k and representative:** the features are each site's whole u,v time series (Euclidean distance). k is the number of sensors wanted (10, 20, 50, 100, 200), not chosen from the data. The representative is the available site closest to each cluster centre.
- **Validation:** held-out times (random 20 %) at the non-sensor sites, against random sensors. K-means beats random by about 0.2 to 0.6 m/s with linear regression (numbers above) and little with KNN at 200 sensors. No entropy, kriging, mutual-information or greedy comparison is run.
- **Takeable:** a cheap clustering recipe with a random baseline and a cost-term variant. Not shown: spread over random draws, or measurement (not reanalysis) data; the benefit shrinks as sensors grow.
- **Kind of result:** a method comparison on one modelled field with a one-draw baseline.

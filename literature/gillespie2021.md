---
id: gillespie2021
citation: Gillespie, G.D., McDonnell, K.P. & O'Hare, G.M.P. 2021. Can machine learning classification methods improve the prediction of leaf wetness in North-Western Europe compared to established empirical methods? Expert Systems with Applications 182:115255
doi: 10.1016/j.eswa.2021.115255
read: 2026-10-27, in full; Table 1 read in the page image (page 7 of the PDF), Tables 2-4 and the figures not read; by a reading agent and note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [cereals, broadacre crops]
regions: [United Kingdom, North-Western Europe]
processes: [leaf wetness, leaf wetness classification, RH threshold, CART, machine learning, time step 15 min]
records: []
datasets: []
files: [dr1027_gillespie2021.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Gillespie et al. 2021: seven classifiers against RH thresholds and CART for 15-min leaf wetness at UK stations

Machine-learning classifiers and published threshold rules are scored on wet or dry 15-min records from about 30 UK weather stations, 2014-2018.

**Read this first.** The file is the published article (Elsevier layout, volume 182, article 115255, open access CC BY; l. 35, l. 108) with a UCD repository cover sheet whose publication date is 2021-11-15 and which points to the publisher's DOI (l. 22); it is not an accepted manuscript. The abstract says 30 stations and the methods 31 (l. 238). The crop and the sensor height and angle are not stated; the paper concerns broadacre crops (cereals), not vines. The scores are accuracy and F1 per 15-min record, not hours per day.

## What it holds

- **Data:** 15 min records, 2014-01-01 to 2018-10-22, 3.23 million records; rainfall, air temperature, RH, wind speed and direction, solar radiation; stations in four regions of the UK (l. 247, l. 238).
- **Reference sensor:** a WET leaf wetness sensor with an output of 0-10; 0-3 is dry and 4-10 is wet (l. 197-198). Height and angle are not printed.
- **RH thresholds:** the widely used RH > 90 % was compared with 92 % and 95 % (95 % no better than 90 %, not shown) and with 87 % (van Jaarsveld) (l. 215-218).
- **CART (Kim et al. 2002 form):** wet if Inequality 1, 1.6064 sqrt(Tair) + 0.0036 Tair^2 + 0.1531 RH - 0.4599 Wind x DPD - 0.0035 Tair x RH > 14.4674, or Inequality 2, 0.7921 sqrt(Tair) + 0.0046 RH - 2.3889 Wind - 0.039 Tair x Wind + 1.0613 Wind x DPD > 37.0, with DPD the dew point depression (l. 233-237).
- **Extended RH (Wichink Kruit et al. 2004):** wet above 87 %, dry below 70 %; between, wet if RH rose by more than 3 % in the step, dry if it fell by more than 2 % (l. 242).
- **Method:** scikit-learn classifiers with default parameters, 80 / 20 random train / test split, 3-fold cross validation (l. 279). K-means (accuracy 44-67 %) was dropped (l. 312).
- **Table 1, all records (page image):** accuracy and F1: RH > 87 % 73.43 % and 0.76; RH > 90 % 76.69 % and 0.81; RH > 92 % 77.85 % and 0.83; CART 69.70 % and 0.80; MLP 80.03 % and 0.85; RF 78.24 % and 0.84; logistic regression 78.72 % (l. 389). So the 92 % threshold is within 2.2 points of the best classifier, and 90 % is 3.3 points below it (arithmetic, not printed).
- **Threshold effect:** raising 90 to 92 % adds 1.1 % accuracy and F1 0.81 to 0.83 (l. 417); the abstract gives an average gain of 1.12 % over regions and 4.85 % for ML over empirical.
- **Weaker empirical models:** CART and the extended RH models were worst, 63.78 to 69.7 % (l. 414-429); the authors say the CART from the US Midwest may not suit humid maritime climates.
- **Regional subsets:** empirical 78.88-81.80 %, ML 83.77-88.52 % (l. 449). Day-time (07:00-19:45) and night-time subsets were also fitted (l. 402, l. 500).
- **Release:** no data or code statement found; article is CC BY (l. 108).

## Dependence

- RH thresholds follow Sentelhas et al. 2008 and van Jaarsveld 2004; CART is Gleason et al. 1994 as extended by Kim et al. 2002 (same coefficients as park2019 and wang2019); extended RH is Wichink Kruit et al. 2004 (also in savage2012).
- Kin of sentelhas2008.wetness and cooptera.rh90_wetness (RH-threshold form). The ML models are own fits, random-split and so in sample for the same stations.

## Bearing (2026-10-27)

- **RH threshold error:** across UK stations with a WET sensor, an RH > 90 % rule scored 76.7 % accuracy (F1 0.81) per 15-min record and 92 % scored 77.9 % (F1 0.83); the best classifier gained 2-3 points more. The threshold that fits best in a humid maritime climate is above 90 %, unlike the greenhouse results in wang2019. Kind of result: measurement and re-fit, random split, cereals.
- **Time step:** 15 min, the step of the records; no hours-per-day error is given, so it cannot be compared with the 2-3 h of park2019 without a further calculation.
- **Not shown:** vines, sensor height and angle, a Penman-Monteith run.

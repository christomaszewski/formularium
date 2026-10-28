---
id: skelsey2021
citation: Skelsey, P. 2021. Forecasting risk of crop disease with anomaly detection algorithms. Phytopathology 111(2):321-332
doi: 10.1094/PHYTO-05-20-0185-R
read: 2026-10-27, in full (all sections except the reference list), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [potato late blight (Phytophthora infestans)]
crops: [potato]
regions: [United Kingdom, Great Britain]
processes: [forecasting, anomaly detection, one-class learning, outbreak-only data, nested cross-validation, Smith period, Hutton criteria, ensemble]
records: []
datasets: []
files: [syn1027_skelsey2020.pdf (the 2026-10-27 drop)]
---

# Skelsey 2021: anomaly detection learns the weather envelope of 1,049 potato late blight outbreaks (analogue crop)

Learns the weather conditions that precede reported outbreaks from outbreak records alone (no healthy fields), with five one-class algorithms and an ensemble, and scores how often an alert precedes an outbreak. No record: a method with measured results. (The reading key is skelsey2020, the year of acceptance; the paper is dated 2021.)

**Read this first.** Potato, not a vine, but the input set is the one the project's outbreak records offer: temperature and RH hours. The score is a hit rate on outbreaks with the alert rate set by hand; there are no healthy fields, so no false-alarm rate against disease-free days, and the folds are random outbreaks, not held-out years or regions. "RH >= 90%" is the paper's wetness proxy; the text layer prints it garbled as "RH ³ 90%".

## What it holds

- **Real data** (l. 15): 1,049 voluntarily reported potato late blight outbreaks in Great Britain, 2012 to 2017, with date, postcode-district centroid, genotype and stage. Reporters are agronomists and others who walk fields; the author lists reporting and sampling bias as untested.
- **Labels are observed** outbreaks (scout reports), not computed by a model (l. 15).
- **Inputs** (l. 15): hourly weather interpolated by the UK Met Office from its stations onto 9,000 postcode sectors, aggregated to postcode district; not on-site sensors. Only two daily variables: minimum temperature and hours with RH at or above 90%, over the 28 days before each outbreak.
- **Training** (l. 4): only outbreak-days; the algorithms "learn the envelope of weather conditions most associated with historic crop disease outbreaks". No negative class.
- **Validation** (l. 23): two nested cross-validation loops, outer to test generalisation and inner to tune hyperparameters; ten-fold over outbreaks, random; the same seasons sit in training and test.
- **Score and baselines** (l. 24, 29, 30): a forecast counts as successful if any alert fell in the 28 days before the outbreak. Hit rate in % (SD), Table 1: Smith Period 84.7 (3.6), Hutton Criteria 97.2 (1.1), the five learned models 96.0 to 97.0, ensemble 98.2 (0.7). Alert frequency in % of days: Smith Period 12.9, Hutton Criteria 31.8, learned models 13.9 to 14.4, ensemble 14.5. So the learned models match the Hutton hit rate at about 14% of days alerted against 32%.
- **Alert rate is chosen** (l. 24): the decision threshold is the 14.29th percentile of the anomaly scores, one alert in seven days in the pre-outbreak window, chosen from the frequency of calendar fungicide sprays.
- **Season and months** (l. 39, 40): hit rate varies by month by 10.5 to 21.1 points for the learned models; over the whole 1 May to 31 October season the ensemble alerts on 8.3% of days against 18.5% for Hutton Criteria.
- **Envelope** (l. 36, 24): the learned boundaries recover the hand-made rule: minimum temperature about 9 to 12 degC; the Smith Period is two consecutive days with a minimum of 10 degC and at least 11 h at RH 90% or more (the Hutton Criteria cut the wet requirement).
- **Synthetic data** (l. 55): none; the author names simulation studies of sampling and detection bias as future work.

## Dependence

- Labels observed. The baselines Smith Period and Hutton Criteria are RH-threshold wetness rules, and the learned envelope uses the same RH >= 90% hours as an input, so it is not independent of them. No process model computes any label. The reading flagged Hamer et al. 2020 (machine-learning powdery mildew forecast) as a lead.

## Bearing (2026-10-27)

- **D58 (variable search):** a ceiling for two variables from hourly series: a minimum-temperature and RH >= 90% hours envelope reaches the hit rate of the national rule (97%) with less than half its alerts. It is the closest design to the project's outbreak records, but the score cannot show a variable is real: no negatives, random folds, a chosen alert rate.
- **D60:** the outbreak-only design is what a simulator could test: a rare-event hit-rate and alert-rate score without healthy fields. Nothing synthetic here.
- **Not shown:** false alarms, held-out years or regions, or a vine.

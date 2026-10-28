---
id: castanoserna2025
citation: Castaño-Serna, J.S., Meno, L., Seijo, M.C. & Escuredo, O. 2025. Meta-Analysis on Criteria and Forecasting Models for Potato Late Blight Pathosystem: Assessing Robustness and Temporal Consistency. Agriculture 15(21):2242
doi: 10.3390/agriculture15212242
read: 2026-10-27, lightly: abstract, introduction, methods (generation and mechanism classes), results 3.1 and 3.2 and the conclusions, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [potato late blight (Phytophthora infestans)]
crops: [potato]
regions: [25 countries (pooled published trials)]
processes: [meta-analysis, forecasting, decision support, publication bias, temporal consistency, mechanistic vs data-driven]
records: []
datasets: []
files: [syn1027_castanoserna2025.pdf (the 2026-10-27 drop)]
---

# Castaño-Serna et al. 2025: meta-analysis of 271 potato late blight forecasting trials by model generation (analogue crop, review)

Pools the accuracy and fungicide-saving figures that 271 published trials reported for 59 late blight criteria and models, grouped by method generation and by how much host and pathogen state a model carries. No record: a review.

**Read this first.** Potato, not a vine. The accuracy figures are whatever each trial reported, with mixed definitions and validation designs; the review does not harmonise them. The authors' own funnel and Egger tests suggest the published figures are over-optimistic (l. 457). Nothing here is a held-out-year score.

## What it holds

- **Scope** (l. 9): 271 trials, 59 models, 25 countries, 106 years. The random-effects model used 57 effect sizes, with heterogeneity I2 of 84.7% for accuracy and 82.4% for fungicide reduction (l. 467).
- **Data and labels**: all cited from the trials; labels and validation differ by trial and are not described per trial in the parts read. No synthetic or augmented data: no trial is reported as trained on simulated epidemics.
- **Accuracy by generation** (l. 459, cited from the trials; named as the average of reported accuracy): G1 (climate rules) 48.90%, G2 (statistical) 71.91%, G3 (neural networks and complex algorithms, from 2007) 81.46%. G2 and G3 do not differ significantly (l. 463).
- **Accuracy by structure** (l. 459, cited): non-mechanistic (environmental variables only) 63.48%, semi-mechanistic 77.90%, mechanistic (host and pathogen variables) 82.10%; the semi-mechanistic and mechanistic groups do not differ significantly (l. 463).
- **Fungicide reduction** (l. 463, cited): 42.54% (G1), 32.90% (G2) and 50.36% (G3); the accuracy gain did not turn into fewer sprays in step.
- **Temporal consistency** (l. 556): "the decline in performance of some models over time (Wallin, Smith period, Blitecast, SimCast)" calls for recalibration. The authors conclude that models that simulate the pathogen's life cycle and take account of resistance and inoculum "show greater promise" (l. 556).

## Dependence

- Secondary source: every score belongs to the trial it cites. None recorded beyond that.

## Bearing (2026-10-27)

- **D58 (variable search):** a pooled, cross-study reading that host and pathogen state (resistance, inoculum) beat environment-only rules, 82.1% against 63.5% reported accuracy. It is not a held-out test: the figures mix designs and are probably flattered (l. 457). It agrees with carisse2021dt, which tested the same point on later years.
- **Skill ceiling:** reported accuracy of data-driven potato models averages 81.5% (G3); no trained-on-synthetic model is among the trials. It gives no ceiling for hourly temperature, humidity and rain alone.
- **Not shown:** anything about synthetic or augmented training data (D60), or any vine.

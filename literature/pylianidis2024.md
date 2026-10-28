---
id: pylianidis2024
citation: Pylianidis, C., Kallenberg, M.G.J. & Athanasiadis, I.N. 2024. Domain adaptation with transfer learning for pasture digital twins. Environmental Data Science 3:e8
doi: 10.1017/eds.2024.6
read: 2026-10-27, lightly: abstract, the evaluation section, the results text and the discussion of models and baselines; the figures (where the R2 values are) were not read; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grass pasture]
regions: [New Zealand]
processes: [pretraining, fine-tuning, transfer learning, metamodel, synthetic data, domain adaptation, digital twin, LSTM, crop model]
records: []
datasets: []
files: [syn1027_pylianidis2024.pdf (the 2026-10-27 drop)]
---

# Pylianidis et al. 2024: pretraining on one climate's APSIM pasture runs, fine-tuning on another's, entirely in silico (crops, pasture)

A long short-term memory (LSTM) metamodel of the nitrogen response rate of grass pasture is pretrained on APSIM simulations from one New Zealand climate in four set-ups of growing weather and management variety, then fine-tuned on a fixed number of simulations from two other climates. No record: a method, tested on simulated data only.

**Read this first.** No real observations anywhere: the target locations are also simulated, so "real data" never judge the model. The R2 values are in Figures 3, 4, A4 and A5, which were not read, so the text gives no score; the paper's own real-only (target-only) arm is omitted and reported only in passing. Pasture, not a vine or a disease.

## What it holds

- **Simulator** (l. 157, 136): APSIM pasture growth simulations from historical weather at sites with different climates, soil types and fertilisation treatments (fertilisation on the 5th, 15th and 25th of the month; 0 to 100 kg N/ha in steps of 20, l. 196-197). Calibration is not stated in the lines read.
- **Samples and sites** (l. 217-218): three locations, one origin (location 1, where pretraining takes place) and two targets selected to be dissimilar to the origin by a climate similarity index. The counts of simulations are in a figure (Figure A3) that was not read; the fine-tuning set is a fixed number of target samples (l. 423).
- **Validation design** (l. 225-227, 313, 430): sliding years; for the origin model, for example, training 1992-2001, validation 2002-2003 and test 2004-2005, then moved one year; averages across five seeds. Test years are 2 or 3 years after the training years. All tests are on simulations.
- **What the text says about scores** (l. 283, 287, 338, 340): fine-tuning raised the average R2 at the target for most set-ups; in the richest set-up (s4) there was no gain, or a loss in some years, at one location; the pretrained origin model alone had negative R2 at the new locations for the s1 set-up in all years (worse than predicting the mean); R2 varied strongly from year to year.
- **What helps** (l. 29): adding weather data to the pretraining set had a small effect on the fine-tuned model compared with adding management variety.
- **Real-only baseline: omitted** (l. 424-425): "target-only" models were left out of the study; preliminary tests showed them with negative R2 in all set-ups and high standard deviations (not tabulated). The authors suggest simpler architectures might change that.

## Dependence

- APSIM for the data; an LSTM encoder with a regression head. Builds on Pylianidis et al. 2022 (simulation-assisted learning for digital twins, cited, not read) and is the case study that `maestrini2022` points to. Authors in common with `kallenberg2023` and `maestrini2022` (a flag).

## Bearing (2026-10-27)

- **The pretrain-then-fine-tune design with a transfer between climates, tested with no real data at all.** It is evidence that fine-tuning usually helps within the simulator, and that the richest pretraining set can give no gain; it cannot say anything about real fields, so by D60 it is a robustness test, not evidence for a feature.
- **D45:** the metamodel is kin to the crop model that made its data. The target-only arm that would show whether pretraining helps was dropped because it scored negative R2: a result worth keeping in mind when a real-only arm in Agrarium is small.
- **Not shown:** any observation of a real pasture, a disease, or a numeric gain in the text.

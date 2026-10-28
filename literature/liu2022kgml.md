---
id: liu2022kgml
citation: Liu, L., Xu, S., Tang, J., Guan, K., Griffis, T.J., Erickson, M.D., Frie, A.L., Jia, X., Kim, T., Miller, L.T., Peng, B., Wu, S., Yang, Y., Zhou, W., Kumar, V. & Jin, Z. 2022. KGML-ag: a modeling framework of knowledge-guided machine learning to simulate agroecosystems: a case study of estimating N2O emission using data from mesocosm experiments. Geoscientific Model Development 15:2839-2858
doi: 10.5194/gmd-15-2839-2022
read: 2026-10-27, lightly: abstract, introduction, section 2.2 (synthetic data, mesocosm, pretraining strategy), results 3.1-3.4 with Tables 1-3, discussion 4.3; the supplement was not read; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [maize]
regions: [United States, Minnesota]
processes: [pretraining, synthetic data, knowledge-guided machine learning, GRU, emulator, N2O emission, data augmentation, leave-one-out]
records: []
datasets: []
files: [syn1027_liu2022kgml.pdf (the 2026-10-27 drop)]
---

# Liu et al. 2022: a GRU pretrained on 4.3 million ecosys samples, fine-tuned on six mesocosm chambers (crops, N2O)

KGML-ag: a hierarchical gated-recurrent network pretrained on output of the process model ecosys (nitrous oxide flux and 76 intermediate variables), then fine-tuned on measured N2O flux from corn mesocosm chambers, and compared with the same GRU without pretraining. This is a different paper from `liu2022` (grape segmentation). No record: a method with measured results.

**Read this first.** Crops, but a mesocosm, not a field: six chambers over three seasons (l. 268, 857), whose fluxes the authors say are at the high end of field values (l. 811). The only real-data check is leave-one-chamber-out. The net is judged on N2O, the variable ecosys also outputs; the hidden intermediate variables were judged poor on the real data (l. 483). The supplement was not read.

## What it holds

- **Simulator** (l. 46, 206-208): ecosys, a process model of agroecosystems. Whether it was calibrated to these chambers is not stated in the lines read; ecosys alone against the mesocosm N2O was not found in the text read. Synthetic set: 122 days (1 April to 31 July, l. 204) x 18 years x 99 counties x 20 N rates, about 4.3 million points (l. 206-207), split by county, 70 for training, 10 for validation, 19 for testing (l. 208).
- **Real data** (l. 266, 276, 387): six mesocosm chambers over three growing seasons (2016-2018); the real fine-tuning data and weather forcings were augmented 1000-fold by resampling hours of the day.
- **Validation design** (l. 268): leave-one-chamber-out: five chambers fine-tune, the sixth tests. New chambers, same experiment, so neither new years nor new sites in the field sense.
- **Emulation of the simulator** (l. 433, 449): on held-out synthetic counties the GRU reaches r2 0.98, RMSE 0.54 mg N m-2 d-1 with the 76 intermediate variables as inputs and r2 0.89, RMSE 1.37 without them. In-distribution scores.
- **Score on real N2O, with and without pretraining** (Table 3, l. 574, 576; text l. 479-481): the same GRU without pretraining (the real-only baseline) r2 0.78, RMSE 4.00; pretrained 0.80, 3.77 mg N m-2 d-1. The full KGML-ag1 reaches r2 0.81, RMSE 3.6 (l. 51, 477). Pretraining raised r2 by 0.02 for flux (l. 686) and cut RMSE by 0.23 (l. 688). No sweep of real sample size.
- **Where the gain shows** (l. 491): where there were no observations (before day 25) the pretrained model gave stable near-zero N2O; the real-only GRU gave anomalous peaks.
- **Augmentation** (l. 718, 724-726): without it all KGML-ag models lost accuracy; the maximum training epochs rose from 800 to 20,000 (printed 20 000) and the model overfit the small real set.
- **Hidden variables after fine-tuning** (l. 483): intermediate variables predicted at overall r2 0.37 (CO2), 0.39 (NO3), 0.60 (NH4) and 0.33 (soil water) in the leave-one-chamber-out test.
- **Cost and limits** (l. 764, 806, 857): KGML-ag runs in seconds against about half an hour for ecosys; the authors say it is limited by the observed data and needs testing on completely independent datasets.

## Dependence

- Pretrained on ecosys output; its intermediate variables are ecosys's; the pretraining labels for N2O are ecosys outputs. The architecture follows the group's physics-guided networks (`jia2021`, `read2019`; authors in common, a flag).

## Bearing (2026-10-27)

- **The pretraining effect is small and the real set is tiny:** r2 0.78 to 0.80 on six chambers, with no real-sample-size sweep. It is evidence that a crop-process teacher can be pretrained on, not that it helps much. For D45 the student is kin to ecosys by construction.
- **D58 in miniature:** the net's own hidden variables, which the simulator supplies, scored 0.33 to 0.60 against measured values after fine-tuning (l. 483). A variable the simulator supplies and real data can check may still be poor; one that real data cannot check cannot be judged at all.
- **Not shown:** field data, new years or sites, a disease, a calibrated simulator, or the process model's own score on the chambers.

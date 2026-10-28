---
id: lemaitre2026
citation: Lemaitre, J. & Lessler, J. 2026. Generative diffusion models for spatiotemporal influenza forecasting (Influpaint). arXiv:2604.24913v2 [cs.LG], 11 Sep 2026 (preprint)
doi: 10.48550/arXiv.2604.24913
read: 2026-10-27, lightly: abstract, section 3.3 and Table 1 (the training-data mix), the limitations paragraph, and the methods on the frame library; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [influenza]
crops: []
regions: [United States]
processes: [diffusion model, synthetic data, pretraining mix, hybrid training set, forecasting, scenario models, surveillance data, weighted interval score]
records: []
datasets: []
files: [syn1027_lemaitre2026.pdf (the 2026-10-27 drop)]
---

# Lemaitre and Lessler 2026: a diffusion model trained on surveillance plus simulated seasons, tested on two flu seasons (human disease, influenza)

Influpaint, a diffusion model that forecasts by inpainting a state-by-week incidence image, is trained on a mix of real influenza surveillance seasons and simulated seasons from mechanistic scenario models. Four training mixes are compared on the same forecasts. No record: a method. A preprint.

**Read this first.** Human influenza in the United States, not a plant. Only the training-data ablation (Table 1) was read for numbers; the per-horizon results and the real-time FluSight ranks were skimmed. The scenario trajectories come from rounds for the same seasons that the model is scored on (rounds 4 and 5 are for 2023-2024 and 2024-2025, l. 452-453); whether the scored seasons were left out of training is not stated in the lines read.

## What it holds

- **Simulators** (l. 450-460, 462): trajectories from the Flu Scenario Modeling Hub (round 4, 2023-2024, 4 models; round 5, 2024-2025, 7 models) and the flepiMoP model (round 1, 2022-2023), 20 trajectories per scenario per model kept; they are scenario projections, and nothing in the lines read says they were calibrated to the scored seasons. The frame library has 1,080 hub frames and 160 flepiMoP frames (1,240 simulated seasons, l. 204, 460).
- **Real data** (l. 462): 20 surveillance seasons, 13 years of FluView and 7 of FluSurv-NET hospitalisations.
- **Validation design** (l. 137, 196-197): retrospective forecasts, 1 to 4 weeks ahead, by state, over the two FluSight seasons 2023-2024 and 2024-2025; the model also entered the CDC FluSight challenge in real time for three seasons (l. 261-262).
- **Training mixes** (Table 1, l. 243-246): total weighted interval score over the two seasons (lower is better): 30 % surveillance / 70 % simulation 647,816; 70 / 30 mix 704,939 (8.82 % worse); surveillance only, 20 seasons, 707,704 (9.24 % worse; the real-only baseline); simulation only, 1,240 seasons, 724,125 (11.78 % worse than the best mix and 2.3 % worse than real-only, arithmetic, not printed). The mix is set by repeating the 20 real frames among the 1,240 simulated ones (l. 255).
- **Authors' reading** (l. 201-205, 368, 373-374): both hybrids beat single-source training; simulation-only was worse than real-only despite 62 times more seasons (arithmetic, not printed), which raises "concerns about the quality and diversity" of the synthetic data; the hybrid set "carries biases from both" sources.
- **Operational result** (l. 171-173): total WIS 185,441 in 2023-2024 (ranked 5th of 33) and 450,797 in 2024-2025 (ranked 8th of 43), against 197,834 and 554,066 for the FluSight ensemble.

## Dependence

- Trained on output of other groups' scenario models (Flu Scenario Modeling Hub; flepiMoP) and on CDC surveillance data. The scenario models are mechanistic and public; the lines read do not say whether they are independent of the surveillance data. No shared-author flag recorded here.

## Bearing (2026-10-27)

- **A mix beat either source alone, and simulated-only lost to real-only.** With 1,240 simulated seasons against 20 real ones, a 30 / 70 real-to-simulated mix scored 647,816 against 707,704 for real-only and 724,125 for simulation-only. For D60 (synthetic inputs for real data) this is the only paper in the strand that mixes the two at stated ratios and reports the mix as a variable; it is human influenza and a single pair of test seasons.
- **D45:** a model fitted on scenario-model output is kin to those models; the authors' own concern is the diversity of what the simulators produce, which is the thing a fraternal-twin OSSE (TRUTH-METHOD) would have to cover.
- **Not shown:** a plant, per-horizon scores in what was read, or whether the evaluation seasons were excluded from the simulated training seasons.

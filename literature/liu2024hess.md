---
id: liu2024hess
citation: Liu, J., Koch, J., Stisen, S., Troldborg, L. & Schneider, R.J.M. 2024. A national-scale hybrid model for enhanced streamflow estimation: consolidating a physically based hydrological model with long short-term memory (LSTM) networks. Hydrology and Earth System Sciences 28:2871-2893
doi: 10.5194/hess-28-2871-2024
read: 2026-10-27, lightly: abstract, the aim in the introduction, section 2.3 (the four hybrid schemes), section 2.4 (the split design), section 3.1 (Table 4) and the discussion of the schemes, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 18 of 18 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Denmark]
processes: [hybrid model, pretraining, fine-tuning, residual learning, LSTM, streamflow, process model as input, ungauged basins, new-station split]
records: []
datasets: []
files: [syn1027_liu2024hess.pdf (the 2026-10-27 drop)]
---

# Liu et al. 2024: four ways to join a national hydrological model to an LSTM, with real-only and pretrained arms in one table (rivers, Denmark)

Compares an LSTM trained on observed streamflow alone, an LSTM pretrained on the Danish National Water Resources Model (DKM) and fine-tuned, an LSTM given DKM output as an input, and two LSTMs that predict DKM's error (as a residual and as an error factor). No record: a method with measured results.

**Read this first.** Streamflow, not plants. The paper is the one place in the strand where pretraining on a process model loses to real-only training on real data, and where the other hybrid designs sit beside both in a single table. The simulator here is calibrated (below), unlike the lake and river teachers of `jia2021` and `jia2020`.

## What it holds

- **Simulator** (l. 74, 266, 300): DKM, a MIKE SHE-based national model, calibrated against daily streamflow from about 300 stations and groundwater heads (l. 266); whether its calibration stations overlap the test stations is not stated in the lines read. Its simulated streamflow for all 2,830 ID15 catchments (l. 131, 300) is the pretraining target; the sample count is not printed as a number of samples.
- **Real data** (l. 397-401): 318 gauged basins, randomly split into 254 training and 64 test basins; training years 2000-2010, testing 1990-1999, validation 2011-2019. The temporal experiment gives new years; the spatiotemporal experiment gives new stations and new years.
- **Mean NSE, new years / new stations** (Table 4, l. 509-511; higher is better): DKM alone 0.58 / 0.52; real-only LSTM (LSTM-rr) 0.76 / 0.60; pretrained on DKM and fine-tuned (LSTM-pf) 0.72 / 0.52; DKM output as input (LSTM-q) 0.80 / 0.64; residual model (LSTM-qr) 0.79 / 0.58; error-factor model (LSTM-qf) 0.72 / 0.55.
- **Pretraining lost to real-only** (l. 726, 729, 737): the authors say LSTM-pf performed worse than the other hybrids; they suggest pretraining on all 2,830 catchments and fine-tuning on only the gauged ones adds complexity and noise. Pretraining on gauged basins only gave performance comparable to the real-only LSTM, that is, no gain.
- **Hybrids over real-only** (Table 4, l. 510-511; l. 46-48, 433-434, 694): the abstract gives LSTM-q a mean NSE gain of 0.22 in gauged and 0.12 in ungauged basins over DKM (as in Table 4: 0.80 less 0.58 and 0.64 less 0.52, arithmetic). Against the real-only LSTM the hybrids raised performance but "did not alter" it significantly in the temporal split (l. 433). All LSTM models lost accuracy at new stations (l. 434). The authors' ranking in ungauged basins starts LSTM-q, then LSTM-qr, then LSTM-rr, then LSTM-qf (l. 694).
- **Authors' conclusion** (l. 725): a well-established process model is important for the performance of the hybrid schemes.

## Dependence

- Built on DKM (Danish National Water Resources Model) output and on the LSTM of the NeuralHydrology package; builds on Koch and Schneider 2022 (cited, not read), where pretraining on simulated flow is said to have helped. No shared-author flag recorded.

## Bearing (2026-10-27)

- **Pretraining is not a free gain:** on this data the pretrained net (0.72 / 0.52) was no better than the real-only net (0.76 / 0.60), while giving the network the process model's output as an input was the best arm (0.80 / 0.64). For the D45 placement pilot and D60, the design that feeds the simulator's output to the model as an input deserves a place beside pretraining, and a pretraining arm should always be run next to a real-only arm.
- **New stations are harder:** every LSTM lost accuracy there and pretraining fell back to the process model's score (0.52). A check on new years alone would have hidden that, so a result should say which split it used.
- **Not shown:** a plant, a disease, an uncalibrated teacher, or a reason for the pretraining loss beyond the authors' suggestion.

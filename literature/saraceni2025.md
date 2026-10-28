---
id: saraceni2025
citation: Saraceni, L., Motoi, I.M., Nardi, D. & Ciarfuglia, T.A. 2025. Self-Supervised Data Generation for Precision Agriculture: Blending Simulated Environments with Real Imagery. arXiv:2502.18320v1 [cs.CV] (preprint)
doi: 10.48550/arXiv.2502.18320
read: 2026-10-27, lightly: abstract, the dataset description, results (Table I) and the discussion, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine (table grape)]
regions: [none]
processes: [synthetic data, rendering, simulator, copy-paste augmentation, pseudo-labels, object detection, Segment Anything, covariate shift]
records: []
datasets: []
files: [syn1027_saraceni2025.pdf (the 2026-10-27 drop)]
---

# Saraceni et al. 2025: a Unity vineyard simulator with real grapes pasted onto the renders, for grape detection (preprint)

Renders table-grape vineyard images in a Unity simulator, pastes real grape instances (cut out by a base detector prompting Segment Anything) onto the simulated bunches, and trains YOLOv8 on the result with and without the real set. No record: a method; a preprint.

**Read this first.** A preprint (not peer reviewed). The "real" baseline is not human-labelled: its 2,400 frames carry pseudo-labels made by a detector (l. 369). The paper's summary says the combination "surpasses" the baseline; Table I shows it does on five of eight sequence-and-size cells and falls below it on three (arithmetic from the table, below). Each cell is one run; no spread is printed.

## What it holds

- **Generator** (l. 17, 372 to 381): a Unity-engine table-grape vineyard simulator gives 1,889 images with simulator ground-truth masks under four lights (209 low, 707 medium, 559 high, 416 strong backlight). "SyntheticPasted" uses the same images with real instances pasted on, rotated, rescaled and translated to align with the simulated bunches.
- **Real samples** (l. 369): "Pseudo", 2,400 real frames from video taken in 2021 with a RealSense camera, labels generated automatically. Unions: Synthetic + Pseudo and SyntheticPasted + Pseudo hold 4,289 images each (l. 379 to 386).
- **Test** (l. 394, 399): real table-grape sequences, re-adapted from a tracking benchmark: two CloseUp sequences of 300 frames each (2023) and two Overview sequences of 100 frames each (2021, more like the Pseudo frames). The authors name the covariate shift: different years, illumination, occlusion and camera distance.
- **mAP50, YOLOv8 nano / small, real-only (Pseudo)** (Table I, l. 314, 319, 324, 329): CloseUp1 0.454 / 0.496; CloseUp2 0.628 / 0.647; Overview1 0.741 / 0.746; Overview2 0.593 / 0.645.
- **mAP50, synthetic only** (l. 315, 325): CloseUp1 0.35 / 0.434, below the real baseline; Overview1 0.0553 / 0.285. The authors: synthetic-only training "results in a consistent loss" of precision and mAP, because the simulator images are far from photo-realistic, with dense foliage and many false positives (l. 355, 358).
- **mAP50, pasted synthetic + real** (l. 318, 323, 328, 333): CloseUp1 0.539 / 0.527; CloseUp2 0.701 / 0.665; Overview1 0.706 / 0.667; Overview2 0.667 / 0.614. Plain Synthetic + Pseudo on Overview1 small gives 0.752 against 0.746 for real-only (l. 326).
- **Count** (arithmetic, not printed): pasted + real beats real-only in five of the eight cells (both sizes on CloseUp1 and CloseUp2, nano on Overview2) and is below it in three (both sizes on Overview1, small on Overview2). The Overview sequences are the ones most like the real training frames.

## Dependence

- Unity simulator (CANOPIES project, per the reading agent), YOLOv5 and YOLOv8, Segment Anything. The pasted instances and the baseline's labels come from the same detector and the real frames, so the synthetic set is not independent of the real set. Shares three authors (Motoi, Nardi, Ciarfuglia) with `motoi2024`, a flag only.

## Bearing (2026-10-27)

- **Closest to Agrarium's viewer, a vineyard simulator with labels from the render:** a measured result that a simulator's renders alone lose to a real baseline, and that real pixels on rendered geometry plus the real set gain on the sequences that differ from the training frames (CloseUp, +0.07 to +0.09 mAP50 for the nano model; arithmetic, not printed) and not on the one that resembles them (Overview1). It supports D60's reading that synthetic imagery is an addition to real data, and D58's that the real sequences judge.
- **For tier-3 canopy imagery sensors:** the sensor model would be a camera view on the viewer's scene; here the same view collapses if it is the overview (0.0553 nano), so view and scale matter.
- **Not shown:** disease or lesions, human-labelled baselines, a repeat run, a different vineyard or cultivar, and pure rendering without pasted real pixels beating anything.

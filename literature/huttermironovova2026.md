---
id: huttermironovova2026
citation: Hutter-Mironovova, M. 2026. Sim-to-Real Fruit Detection Using Synthetic Data: Quantitative Evaluation and Embedded Deployment with Isaac Sim. arXiv:2603.28670v1 [cs.CV] (preprint)
doi: 10.48550/arXiv.2603.28670
read: 2026-10-27, in full (arXiv preprint, not peer reviewed; Tables 1 and 2 read from the text layer), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [fruit (plastic and real)]
regions: [none]
processes: [synthetic data, rendering, domain randomisation, object detection, sim-to-real, domain shift, embedded inference]
records: []
datasets: []
files: [syn1027_hutter2026.pdf (the 2026-10-27 drop)]
---

# Hutter-Mironovova 2026: Isaac Sim renders of fruit on a table, with 50 or 100 real images, scored under a domain shift (preprint)

YOLOv8s trained on real-only, synthetic-only and hybrid sets, scored on two sets of 100 real images, and deployed on a Jetson Orin NX. No record: a method, on a robotics bench scene and not a field. Filed under the first author's surname, joined: the key of the drop is hutter2026.

**Read this first.** A preprint, not peer reviewed. The scene is plastic or real fruit on a table in an industrial setting, not a plant canopy. The abstract and the results say hybrid models give "improved robustness" under shift (l. 22 to 23, 524, 623) compared with synthetic-only; the paper's own Table 2 shows the best hybrid equal to the 50-image real-only model (0.747 against 0.748) and better only than the 100-image one (0.743 against 0.703).

## What it holds

- **Generator** (l. 57, 58, per the reading agent for scene details): NVIDIA Isaac Sim scenes of fruit on a planar table with domain randomisation of light, pose, count, occlusion and camera jitter; 1,000 or 5,000 renders. YOLOv8s detector.
- **Real samples** (l. 81): real training sets of 50 and 100 images.
- **Test** (l. 319, 321): two fixed sets of real images, 100 each. T1: plastic fruit, same background as training (in domain). T2: real fruit and a different background (domain shift).
- **T1, mAP@0.5** (Table 1, l. 485 to 492): real-only 50 images 0.978 and 100 images 0.983; synthetic-only 1,000 renders 0.626 and 5,000 renders 0.656 (five times the renders, +0.03); hybrid 1,000 + 50 0.974 and 5,000 + 100 0.984. In domain the renders add nothing to real data. The authors: more synthetic data alone "does not lead to substantial improvements" (l. 478).
- **T2, mAP@0.5** (Table 2, l. 512 to 519): real-only 50 images 0.748 and 100 images 0.703 (more real images did not help under shift); synthetic-only 1,000 renders 0.565 and 5,000 renders 0.510 (more renders worse); hybrid 1,000 + 50 0.747, 1,000 + 100 0.743, 5,000 + 100 0.680.
- **Reading** (l. 495, 522, 528): all models drop under shift; synthetic data cannot replace real data here, but a hybrid set can cut the real annotation needed; the authors conclude that realism and quality matter more than quantity.
- No repeats or error bars appear in the tables read.

## Dependence

- NVIDIA Isaac Sim, YOLOv8s, and TensorRT on a Jetson Orin NX. No data release was found in the text read; the real images are the author's.

## Bearing (2026-10-27)

- **Same pattern as `fei2021`, on a simpler scene:** synthetic alone loses to real by 0.32 mAP@0.5 in domain (0.656 against 0.978) and by 0.18 under shift (0.565 against 0.748), both arithmetic, not printed; mixing gives back the real score and no more. For Agrarium's renders (D58, D60) this is a caution that a rendered set may add nothing once a few dozen real images exist.
- **More renders is not a fix:** 5,000 renders did worse under shift than 1,000 (0.510 against 0.565).
- **Not shown:** a plant, a canopy, disease, a field, a test set larger than 100 images.

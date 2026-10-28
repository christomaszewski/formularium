---
id: motoi2024
citation: Motoi, I.M., Belli, V., Carpineto, A., Nardi, D. & Ciarfuglia, T.A. 2024. Synthetic Data Generation for Anomaly Detection on Table Grapes. arXiv:2412.12949v1 [cs.CV] (preprint)
doi: 10.48550/arXiv.2412.12949
read: 2026-10-27, lightly: abstract, the data section, the experiments and results (Tables 1 to 3), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine (table grape)]
regions: [none]
processes: [synthetic data, copy-paste augmentation, anomaly detection, image classification, Segment Anything, edge detection]
records: []
datasets: []
files: [syn1027_motoi2024.pdf (the 2026-10-27 drop)]
---

# Motoi et al. 2024: pasting real anomalous berries onto healthy grape images to add training samples (preprint)

Builds synthetic anomalous grape-bunch patches by pasting one or three real anomalous berries, cut with a Dual-Canny edge filter and Segment Anything masks, onto normal berries, and tests a ResNet18 classifier with them added or substituted. No record: a method; a preprint.

**Read this first.** A preprint (not peer reviewed). The validation is a 3-fold cross-validation over 695 patches from one season (l. 184), so it is the same-set kind of test. The "anomaly" classes are visible mould, rot and pest damage found by one agronomist, not a named disease. The paste source is the real anomalous berries themselves, so the synthetic samples are not independent of the real set.

## What it holds

- **Generator** (l. 32 to 34, 285, per the reading agent for the details): cut-and-paste, not rendering. A Dual-Canny Edge Detection (DCED) filter finds anomalous berries and the Segment Anything Model masks them; one (single-berry) or three berries are blended onto a normal berry of a real image. One synthetic sample per real anomalous sample (l. 487 to 488).
- **Real samples** (l. 176 to 184): smartphone images from the 2021 growing season; 88 healthy-bunch and 41 anomalous images labelled by an expert agronomist; 512 x 512 patches, 529 good and 166 anomalous.
- **Test** (l. 184): 3-fold cross-validation over those patches, mean of the three folds; no held-out season or vineyard.
- **Baselines** (Table 1, l. 447): the DCED threshold alone, balanced accuracy 76.99; the ResNet18 trained on real patches 94.99 (F1 92.92, precision 93.99, recall 91.88), all in per cent.
- **Added synthetic samples, balanced accuracy** (Tables 2 and 3, l. 503 to 506, 530 to 533): single-berry additions of 10, 25, 50, 100 % give 95.35, 95.24, 95.35 and 94.74; three-berry additions give 95.03, 95.75, 95.53 and 95.02. The best gain is +0.76 points (three berries, 25 %; arithmetic, not printed), F1 93.70 against 92.92. No spread is printed in the tables read.
- **Substituted** (Table 3, l. 534 to 541): replacing 10, 25, 50 and 100 % of the real anomalous samples with synthetic ones gives 73.03, 87.3, 91.82 and 58.69; single-berry Table 2 gives 72.33, 87.69, 91.84 and 55.81 (l. 507 to 514). The authors: substitution "consistently led to a decrease" (l. 553), so synthetic samples help added "up to a certain limit" and cannot replace real ones (l. 556). The 10 % row is below the 50 % row; the paper gives no reason in the parts read.

## Dependence

- Segment Anything Model, ResNet18; the real anomalous berries are the source of the pasted ones.

## Bearing (2026-10-27)

- **Pasted real objects, not renders:** a gain of under one point of balanced accuracy on a same-season cross-validation (+0.36 to +0.76) is within what a repeat could change; it supports the caution that synthetic additions help up to a limit and never replace real samples (D60: synthetic outcomes test robustness, never establish a feature).
- **For rendered lesions:** this paper gives a pasting design, where the pasted object is real. Agrarium's renders would paste a rendered object, which `cooper2026` found does not help until restyled.
- **Not shown:** rendering, a named disease, a second season or vineyard, repeats, or a test on field images.

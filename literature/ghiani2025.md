---
id: ghiani2025
citation: Ghiani, Luca, Serra, Salvatorica, Sassu, Alberto, Deidda, Alessandro, Deidda, Antonio & Gambella, Filippo. 2025. Automated detection of downy mildew and powdery mildew symptoms for vineyard disease management. Smart Agricultural Technology 11:100877 (article number)
doi: 10.1016/j.atech.2025.100877
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Sardinia]
processes: [detection, observation]
records: []
datasets: []
files: [1-s2.0-S2772375525001108-main.pdf]
---

# Ghiani et al. 2025: automated detection of downy and powdery mildew symptoms

From the University of Sassari and CNR. Sardinia.

## What it holds

- Own data, Sardinia only: 753 images in 2021 (l. 225) and 1404 in 2022 (l. 249), taken May to July (l. 268). Mostly downy mildew from the Fenosu experimental farm near Oristano (l. 263); all powdery mildew from potted plants of only three varieties (l. 265), (l. 271).
- Expert box annotations: 2021 had 1696 powdery and 657 downy (l. 228), (l. 229); 2022 had 3915 powdery and 20,959 downy (l. 252), (l. 253). No severity, growth stage or per-image date is given.
- YOLOv5s, images resized to 800 x 800 (l. 286), (l. 300); a box counts as correct at IoU 0.45 (l. 572).
- 2022 split by file creation date within each folder, 710 / 347 / 347 images (l. 314), (l. 292), (l. 294). Test images share areas and days with training, so the authors call it still optimistic (l. 441).
- mAP: 0.703 on the 2022 test set (l. 385); 0.529 on all of 2021 (l. 397); 0.734 on a random split (l. 408); 0.370 when a random-split model meets 2021 (l. 386); 0.730 with 2021 added to training (l. 468).
- Random splits flatter the model most on unseen data. Within 2022 the gain is small (0.703 to 0.734) (l. 396).
- Detection of symptomatic leaves in photos taken at about 0.5 m to just over 1 m (l. 272). No true-severity or date axis. Observation role only.

## Dependence

- Its own images (2021-2022) and YOLOv5. Splits are within folders by file date (l. 309-314); the 2022 test images share areas and days with training. Its text says Exp. 3 gains "just over 0.30" on Exp. 1, the tables 0.031.
- No author of an engine model.

## Bearing (2026-10-08)

- Clear: how much a leaf-image detector's skill drops in a new season or place, for an image operator.

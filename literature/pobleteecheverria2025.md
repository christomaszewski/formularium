---
id: pobleteecheverria2025
citation: Poblete-Echeverría, C., Hernández, I., Iñiguez, R., Gutiérrez, S., Barrio, I. & Tardáguila, J. 2025. Using Artificial intelligence for automatic and fast detection of downy mildew symptoms in grapevine canopies. European Journal of Agronomy 170:127755
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Spain, La Rioja, Basque Country]
processes: [symptom detection, canopy imaging, deep learning, leaf counting, image annotation, sunlight conditions, infection level]
records: []
datasets: []
files: [pobleteecheverria2025-usingartificialintelli.pdf]
---

# Poblete-Echeverría et al. 2025: AI detection of downy mildew in vine canopies

A light read (the deep-research B list).

## What it holds

- 17,464 canopy RGB images from 18 plots in northern Spain, 2019, 2021 and 2022 (l. 99-101, 146-147).
- 224 images labelled by experts for leaves with clear symptoms; 80/20 train-test split (l. 219-224, 256-257).
- Sub-images of 1500 x 1500 px resized to 640 x 640, about 15 per image; augmentation to 16,410 sub-images (l. 259-263).
- Three cultivars, including HZZ (Hondarribi Zuri Zerratia) (l. 236, 175).
- Full-canopy test: mAP 67%, F1 0.69, IoU 62%, R2 0.93, NRMSE 0.36 (l. 42-44, 411, 520).
- Sub-image test at 640 x 640: NRMSE 0.57, R2 0.84 (l. 410).
- Test set of 14 plots (l. 521).
- A laboratory study reports mAP 89.5% (l. 474); the authors call their 67% lower (l. 355-356).

## Dependence

- none. An object detector (YOLOv4) for symptomatic leaves; the paper computes no epidemic, infection or incubation quantity and fits to no model's data.

## Bearing (2026-10-10)

- A vision-based symptom detector with a labelled canopy dataset from northern Spain; it offers an observation operator for leaf symptoms (what a camera sees), not an infection or incubation model.

---
id: szekely2024
citation: "Székely, D. E., Dobra, D., Dobre, A. E., Domşa, V., Drăghici, B. G., Ileni, T.-A., Konievic, R., Molnár, S., Sucala, P., Zah, E., Darabant, A. S., Sándor, A. & Tamás, L. 2024. Bacterial-fungicidal vine disease detection with proximal aerial images. Heliyon 10(14): e34017"
doi: 10.1016/j.heliyon.2024.e34017
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [downy mildew, powdery mildew, black rot, anthracnose, excoriosis]
crops: [grapevine]
regions: [Romania, Hungary, Croatia, France]
processes: [UAV imagery, low-altitude drone survey, YOLOv8 detection, segmentation, symptom labels, dataset]
records: []
datasets: []
files: [szekely_2024.pdf (the 2026-10-20 drop)]
---

# Székely et al. 2024: drone images of vine disease symptoms

A labelled set of 10,000 drone images of vines at 1 to 2 m, and YOLOv8 tests of leaf
symptom detection on it. The detector scores about 0.48 to 0.54 (mAP50), so the set is a
test bed rather than a finished observation model.

## What it holds

- Two DJI Mini 2 drones, flown 1 to 2 m above the canopy, May to October 2023, at sites in
  Romania, Hungary, Croatia and France (l. 50; Table 3). "10,000 images and more than
  100,000 annotated leaves" (l. 11).
- Diseases in the images: downy mildew, powdery mildew, black rot, anthracnose and
  excoriosis (l. 42). Mites and phylloxera are seen but not labelled (l. 43).
- Leaf detection (YOLOv8 nano, split by position): mAP50 0.477 (l. 81). YOLOv8 large
  reaches 0.540 (l. 83). Segmentation gives 0.49 (l. 81). Changing the train and test split
  changes the score (l. 84).
- Box counts in the experiments: 7,602 leaf boxes and 2,792 grape boxes (l. 82, 98). These
  are far fewer than the 100,000 leaves claimed in the abstract (l. 11). The text does not
  say which subset was used.
- Phones: 7 to 12 frames a second on Android and 12 to 18 on iOS, through the Roboflow API
  (l. 91).

## Dependence

- Detector: YOLOv8 (ref. 15) and its nano pre-trained weights (l. 80).
- Labelling tools: LabelImg, CVAT and Roboflow (l. 55 to 61). No shared dataset from
  another group is recorded.

## Bearing (2026-10-20)

- Strand t2 (observation), with t3 for the powdery mildew images. A public set of symptom
  boxes at 1 to 2 m could test a symptom-to-severity step. Its mAP50 says how well a model
  finds symptoms, not how much disease a vine carries.
- A vineyard simulator could use the site list and dates (Table 3) as a check on when
  symptoms show. Not read in full.

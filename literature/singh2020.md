---
id: singh2020
citation: Singh, D., Jain, N., Jain, P., Kayal, P., Kumawat, S. & Batra, N. 2020. PlantDoc: A Dataset for Visual Plant Disease Detection. CoDS COMAD 2020, January 5-7, 2020, Hyderabad, India (arXiv:1911.10317v1, the preprint copy read)
doi: 10.1145/3371158.3371196
read: 2026-10-27, lightly: abstract, the dataset description and Tables 1 to 3 (the arXiv preprint copy; the doi is the reading agent's and is not printed in that copy), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine, 13 plant species in all]
regions: [none]
processes: [dataset, image classification, lab-to-field gap, transfer learning, PlantVillage, leaf detection]
records: []
datasets: []
files: [syn1027_singh2020plantdoc.pdf (the 2026-10-27 drop)]
---

# Singh et al. 2020: PlantDoc, 2,598 internet-scraped plant disease images, and the lab-to-field drop of PlantVillage models (preprint copy)

A dataset paper: 2,598 web-scraped, hand-labelled images of 13 plant species and 27 classes, benchmarked with classifiers trained on PlantVillage and on PlantDoc itself. Nothing synthetic. No record: a dataset and a measured lab-to-real drop.

**Read this first.** The copy read is the arXiv preprint of the conference paper. Grape is among the 13 species (l. 69; the class labels shown in the figures are garbled in the text layer), but every accuracy below pools all classes; no grape-only figure is printed in the parts read. The 80/20 split of cropped leaf images is of the dataset's leaf crops (9,216 boxes cut from 2,598 photos, l. 261 to 262); the text read does not say whether crops of one photo stay on one side.

## What it holds

- **Data** (l. 21 to 24, 176, 261 to 262): 2,598 images across 13 species and 27 classes (17 disease, 10 healthy), scraped from the internet and labelled with boxes; cropping them gives the Cropped-PlantDoc set (C-PD) of 9,216 leaf images, "low-quality, small-size and varying backgrounds".
- **Motivation** (l. 17, 33): no sufficiently large non-lab disease set exists, and lab-controlled data cannot be used to classify or detect in real scenarios (the authors' claim).
- **Trained on PlantVillage (PVD), tested on all of C-PD** (Table 2, l. 238, 241, 244): VGG16 19.73 %, InceptionV3 30.78 %, InceptionResNetV2 39.87 % accuracy.
- **Trained on 80 % of C-PD, tested on the other 20 %** (l. 237, 243): VGG16 44.52 %, InceptionResNetV2 49.04 % (InceptionV3 46.67 %, l. 240 by the table).
- **PlantVillage pre-training, then fine-tuning on 80 % of C-PD** (l. 245; Table 2): InceptionResNetV2 70.53 %, the best; VGG16 60.41 % and InceptionV3 62.06 % (the table). About 21 points above training on C-PD alone for InceptionResNetV2 (70.53 minus 49.04; arithmetic, not printed).
- **Uncropped images** (Table 1, l. 272 to 274): VGG16 trained on PlantVillage scores 15.08 % on PlantDoc; PlantVillage pre-training then fine-tuning "doubled" accuracy (13.74 % to 29.73 %, the table).
- **Reasons given** (l. 357): background noise, images with leaves of several classes, and low resolution.
- **Leaf detection** (Table 3): mAP at 50 % IoU 38.9 for Faster R-CNN Inception-ResNet with COCO weights; MobileNet 32.8 with COCO, 22.4 with COCO plus PlantVillage.

## Dependence

- PlantVillage, ImageNet and COCO pre-training; VGG16, InceptionV3 and InceptionResNetV2. The dataset's licence was not checked.

## Bearing (2026-10-27)

- **The lab-to-field gap, re-measured on pooled species:** 19.73 to 39.87 % for PlantVillage-trained models on real-scene crops (`mohanty2016`: 31 %). It is the size of the shortfall to expect if Agrarium's rendered lesions were used to train a classifier and then shown real photos (D58: real data judge).
- **The useful pattern:** pre-training on a large controlled set and fine-tuning on real scenes gained 11 to 21 points over the real set alone (60.41 against 44.52; 70.53 against 49.04; arithmetic, not printed), which is the shape a render pre-training followed by real fine-tuning would take. It is a lab set here, not a render.
- **Not shown:** a grape-only score, rendered or generated images, a split by photo, or disease on vines in the field.

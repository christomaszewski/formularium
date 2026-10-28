---
id: mohanty2016
citation: Mohanty, S.P., Hughes, D.P. & Salathé, M. 2016. Using Deep Learning for Image-Based Plant Disease Detection. Frontiers in Plant Science 7:1419
doi: 10.3389/fpls.2016.01419
read: 2026-10-27, lightly: abstract, the split methods, the results on the two web-image test sets, the discussion of limitations and the head of Table 1, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [grape black rot, esca, grape leaf blight]
crops: [grapevine, 14 crop species in all]
regions: [none]
processes: [image classification, transfer learning, domain shift, lab-to-field gap, PlantVillage, dataset]
records: []
datasets: []
files: [syn1027_mohanty2016.pdf (the 2026-10-27 drop)]
---

# Mohanty et al. 2016: a deep classifier on 54,306 PlantVillage leaf photos, 99.35 % on a held-out split and about 31 % on web images

Trains AlexNet and GoogLeNet on PlantVillage lab photos of 14 crops (38 classes) and scores them on a random held-out split and on two small sets of web images. Nothing synthetic is used; it is the standard lab-to-field measurement that the strand cites. No record: a method and a measured gap.

**Read this first.** The two web sets (121 and 119 images) are described in the paper's supplement, which was not read; the text says only that they come from Bing Image Search and IPM Images with a visual check (l. 338 to 343). The result pools 38 classes, grape included, and gives no grape-only figure. Table 1 prints "TRAIN: 200%, TEST: 80%" and similar with an extra zero; read as 20 %, 40 % and 60 % by the layout (garbled).

## What it holds

- **Data** (l. 94, 26): 54,306 PlantVillage images of 14 crop species with 26 diseases or healthy, 38 classes, "collected under controlled conditions". The grape classes are black rot, black measles (esca), healthy and leaf blight (l. 139 to 140).
- **Split rule** (l. 155 to 157, 173 to 174): the paper has mappings of images of the same leaf (taken from different orientations) for 41,112 of the 54,306 images and says all images of one leaf go to either training or testing. For the other images (13,194 by arithmetic, not printed) the text read does not say how leaves are kept apart. This corrects the strand lead that the split puts the same leaf on both sides.
- **Held-out split** (l. 28, 332): 99.35 % accuracy on the best configuration (abstract). With an 80/20 split, colour images, mean F1: AlexNet with transfer 0.9927, from scratch 0.9782; GoogLeNet with transfer 0.9934, from scratch 0.9836 (l. 332). Grayscale, GoogLeNet transfer 0.9800 (l. 333).
- **Web images** (l. 343, 344, 347, 351, 352): two small verified sets, 121 (set 1) and 119 images (set 2); the best model scores 31.40 % on set 1 and 31.69 % on set 2 across the 38 classes, against 2.63 % for a random classifier; the right class is in the top 5 for 52.89 % and 65.61 %.
- **Reading** (l. 411 to 413, 417): tested on images "taken under conditions different from" training, accuracy falls "to just above 31 %"; the authors say a more diverse training set is needed.
- **Without synthetic data:** not applicable; this is the real-to-real lab-to-web comparison.

## Dependence

- PlantVillage (Hughes & Salathé 2015) and ImageNet-pretrained AlexNet and GoogLeNet. Shares an author with the PlantVillage dataset paper (a flag). Nothing here is computed from a simulator.

## Bearing (2026-10-27)

- **Why real held-out images judge a render-trained model (D58, D60):** the benchmark case that a score on a random split of lab photos (99.35 %) says little about images taken elsewhere (about 31 %); the same applies to any classifier fitted on Agrarium's rendered lesions.
- **Size of the gap:** about 68 points (99.35 minus 31.4; arithmetic, not printed) for pooled classes, from two test sets of about 120 images; `singh2020plantdoc`, `noyan2022` and `sun2024cross` repeat the measurement.
- **Not shown:** a grape-only lab-to-field figure, the origin of the web images by crop, and any rendering or generation.

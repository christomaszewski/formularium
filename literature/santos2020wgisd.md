---
id: santos2020wgisd
citation: Santos, T.T., de Souza, L.L., dos Santos, A.A. & Avila, S. 2020. Grape detection, segmentation, and tracking using deep neural networks and three-dimensional association. Computers and Electronics in Agriculture 170:105247 (arXiv:1907.11819, authors' accepted manuscript)
doi: 10.1016/j.compag.2020.105247
read: 2026-10-27, lightly: sections 1, 3.1 (the dataset), 3.3 (training), 3.4 (metrics), the result Tables 3 and 5 and Appendix A (the datasheet), from the arXiv preprint (authors' accepted manuscript, not the journal copy); the tracking and 3D-association sections not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine, Chardonnay, Cabernet Franc, Cabernet Sauvignon, Sauvignon Blanc, Syrah]
regions: [Brazil, São Paulo]
processes: [dataset, image segmentation, instance segmentation, object detection, data augmentation, grape cluster counting, structure from motion]
records: []
datasets: [santos2020wgisd.wgisd]
files: [syn1027_santos2020wgisd.pdf (the 2026-10-27 drop)]
---

# Santos et al. 2020: the Embrapa WGISD, 300 wine-grape images with 4,432 boxed clusters, and Mask R-CNN baselines

A method paper (grape cluster detection, instance segmentation and tracking) that introduces the public Embrapa Wine Grape Instance Segmentation Dataset (WGISD). No record: a dataset and a method. This is a different paper from Formularium's literature/santos2020 (a Plasmopara viticola genetics paper).

**Read this first.** Non-commercial in both statements but the two differ: the paper says CC BY-NC 4.0 (l. 383-384), and the reading agent found CC BY-NC-SA 4.0 on the Zenodo record (record, not in the paper). The headline scores are on a random 80/20 split by image (l. 488), with all five varieties in training and test, from one winery on one day per variety.

## What it holds

- **Where to get it** (l. 162): Zenodo 10.5281/zenodo.3361736 (reference to Santos et al. 2019). The record's one 1.3 GB archive and its licence are the reading agent's look at the record.
- **Licence as the paper states it** (l. 383-384): CC BY-NC 4.0 (Attribution-NonCommercial). Share-alike in the record would extend to derived material.
- **Size** (l. 347, Table 1 l. 368-373): 300 RGB images, 4,432 clusters with bounding boxes, 2,020 with binary masks on 137 images (l. 1496-1497); five varieties: Chardonnay, Cabernet Franc, Cabernet Sauvignon, Sauvignon Blanc, Syrah.
- **Site and dates** (l. 348, 368-373, 1553): one winery (Guaspari, Espírito Santo do Pinhal, São Paulo, Brazil), 2018-04-27 for four varieties and 2017-04-27 for Syrah (one year earlier, l. 372); a single visit per variety, no time series.
- **Capture** (l. 1558, 1562, 1568): frontal view of a trellis canopy with dual pruning (so lower density), a DSLR (240 images, all the Syrah) and a smartphone (60 images), images rescaled to 2048 x 1365 and 2048 x 1536 px.
- **Variables:** the cluster class only (no disease, phenology stage, maturity or weather); the grape cluster boxes and masks.
- **How labels were made:** by people. Boxes drawn with the labelImg tool (l. 1579, 1606) and masks from the authors' interactive tool built on graph matching over a watershed over-segmentation (l. 399-400); the annotation was done by three of the authors (l. 1573-1574).
- **Split and augmentation** (l. 488, 493-495, 497-503, 902): images assigned randomly in 80/20; for masks, 88 training images (1,307 clusters) and 22 validation images (305 clusters); 20 random augmentations per image (Gaussian blur, contrast normalisation, additive noise, pixel dropout) gave 1,848 training images (l. 902); the augmented copies are not independent. Evaluation on 58 images with 837 clusters for detection (l. 900) and 27 images with 408 clusters for masks (l. 648).
- **Scores, instance segmentation (Mask R-CNN, masked test set, Table 3)** (l. 805-811): F1 0.915 at IoU 0.3, 0.847 at 0.5, 0.678 at 0.7 and 0.068 at 0.9 (AP 0.855, 0.743, 0.478 and 0.008); the abstract's "up to 0.91" is the IoU 0.3 value (l. 36). Semantic segmentation overall F1 0.89 with no variety standing out (l. 896).
- **Scores, detection on 58 test images, IoU 0.5 (Table 5)** (l. 977): Mask R-CNN AP 0.719 and F1 0.840; YOLOv2 AP 0.478 and F1 0.652; YOLOv3 AP 0.394 and F1 0.579.

## Dependence

- Mask R-CNN (Matterport implementation, COCO-pretrained weights), YOLOv2 and YOLOv3; COLMAP structure-from-motion for the tracking step; the mask tool follows Noma et al. 2012. Labels are not model-made. Nothing synthetic in the data; imgaug augmentation in training only.

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); a check of rendered grape bunches and of augmentation.** A real, hand-labelled bunch set from one winery. It could test how closely a rendered cluster looks to a real one, and shows a worked case of augmentation (20 random photometric changes per image) that is judged on real held-out images, which is the pattern D58 asks for with real data as the judge.
- **For D58 and D60, no weather, no disease, no phenology stage.** Bunch counting only.
- **Limits:** one winery, one day per variety, random split by image, non-commercial licence, canopy with dual pruning that is not typical, the later versions of the set (Zenodo) not read.

---
id: muhammad2023
citation: Muhammad, A. (printed Abdullah Muhammad; the journal's citation block gives M. Abdullah), Salman, Z., Lee, K. & Han, D. 2023. Harnessing the power of diffusion models for plant disease image augmentation. Frontiers in Plant Science 14:1280496
doi: 10.3389/fpls.2023.1280496
read: 2026-10-27, lightly: abstract, dataset, the FID and KID results and the discussion with limitations, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [grape black rot, esca, grape leaf blight, tomato leaf diseases]
crops: [grapevine, tomato]
regions: [none]
processes: [diffusion model, RePaint, GAN, data augmentation, synthetic data, image generation, FID, PlantVillage]
records: []
datasets: []
files: [syn1027_muhammad2023.pdf (the 2026-10-27 drop)]
---

# Muhammad et al. 2023: RePaint diffusion against InstaGAN for leaf-disease image generation, scored by FID only

Generates diseased leaf images by inpainting with a diffusion model (RePaint) guided by leaf masks from a U-Net, and compares it with a mask-guided GAN (InstaGAN) by Frechet and Kernel Inception Distance. No record: a method; no classifier was trained on the generated images.

**Read this first.** The only score is an image distance (FID, KID) between generated and real PlantVillage lab photos. No downstream accuracy is reported, so it does not show that generated images help a model; the authors list this as a limit and leave integration with detection models to future work (l. 1062 to 1067). The abstract's comparison figures for DCGAN and LeafGAN are cited from other publications, not the authors' own runs (InstaGAN and RePaint are their own).

## What it holds

- **Generator** (l. 56, 680): RePaint (diffusion inpainting) and InstaGAN, both guided by segmentation masks; the masks come from a U-Net with a ResNet50 backbone with mean IoU 97.43 % (l. 680).
- **Real samples** (l. 56, 593, 595, 598): a PlantVillage subset of two tomato and three grape disease classes (the abstract), grape black rot 500 images, esca 400 and leaf blight 300; the paper's Table 3 scores nine tomato classes besides.
- **Test:** none on real held-out images by a model; the scoring compares generated images with real PlantVillage images of the same classes by FID and KID.
- **Scores, the authors' own runs** (Table 3, l. 61, 887 to 911): FID, InstaGAN against RePaint. Grape black rot 81.71 and 56.02; esca 105.89 and 68.83; leaf blight 155.25 and 82.30; grape average 114.28 and 69.05. Over all 12 classes (grape and tomato) the average FID is 206.02 for InstaGAN and 138.28 for RePaint (KID 0.159 and 0.089, per the abstract, l. 60 to 61). Tomato average 236.61 and 161.35 (l. 913).
- **Scores cited from other publications** (Table 6, l. 1016 to 1032, 1039): FID on the PlantVillage grape subset (black rot, black measles, leaf blight) for DCGAN 309.376, LeafGAN 178.256 and Fine Grained GAN 72.73, the closest to RePaint's 69.05 (arithmetic, not printed: a gap of 3.7). Whether those papers used the same images is not checked here.
- **Without synthetic data:** not applicable; no classifier or segmenter was trained.
- **Limits** (l. 1062, 1065, 1067): evaluation rests on FID; other metrics and human assessment are needed; integration with disease detection models is future work.

## Dependence

- PlantVillage lab images; U-Net masks; RePaint and InstaGAN. Comparison values for other generators are taken from other publications (cited, not rerun).

## Bearing (2026-10-27)

- **For generated lesion images:** it shows the usual scoring, an image distance, which says nothing about whether a classifier or segmenter trained on the images works on real ones. `cooper2026` and `mori2024` are the papers here that do train on generated disease images.
- **Grape:** one of the few papers on generated grape-leaf disease images, on PlantVillage lab photos. Under D58 (real data judge) this is image realism, not a judged variable.
- **Not shown:** a downstream result, a field image, or a comparison on images from another source.

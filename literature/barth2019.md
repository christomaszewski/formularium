---
id: barth2019
citation: Barth, R., IJsselmuiden, J., Hemming, J. & Van Henten, E.J. 2019. Synthetic bootstrapping of convolutional neural networks for semantic plant part segmentation. Computers and Electronics in Agriculture 161:291-304
doi: 10.1016/j.compag.2017.11.040
read: 2026-10-27, in full for the methods, experiments I to VII, discussion and conclusion (the Wageningen repository copy of the paper, whose first page carries no volume or pages: those are the reading agent's record; figure values in Figs 6, 8 to 11 and Appendix A are bar charts and not in the text layer), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 26 of 26 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [sweet pepper (Capsicum annuum)]
regions: [none stated]
processes: [synthetic data, rendering, 3D plant model, bootstrapping, fine-tuning, semantic segmentation, DeepLab, data augmentation]
records: []
datasets: []
files: [syn1027_barth2019.pdf (the 2026-10-27 drop)]
---

# Barth et al. 2019: rendered 3-D pepper plants pre-train a segmenter, and 30 real images fine-tune it

Renders pepper plants from random 3-D meshes, trains a DeepLab network on them, fine-tunes it on a few real greenhouse images and scores it on held-out real images. No record: a method with a small real test; the same group's follow-up with a GAN is `barth2018`.

**Read this first.** The real test set is 10 images of the same greenhouse and camera as the training images (l. 295); the headline numbers rest on it. Synthetic-only results on real images are in a figure and not in the text layer (l. 452: "not generalise properly"). Generalisation to other cameras, distances and a different season was judged by eye, with no ground truth (l. 624).

## What it holds

- **Generator** (l. 190 to 191, 288): random 3-D plant meshes drawn from 21 empirically measured plant parameters, with the greenhouse architecture, camera and light modelled on the real images (l. 192 to 193). 10,500 synthetic images in 6 scenes of 1,750; the first 5 scenes (8,750 images) train and the last scene validates and tests, so plants are unique across phases.
- **Real samples** (l. 41, 294 to 295): 50 real images of a crop in a commercial high-tech greenhouse (l. 186 to 187), with seven annotated part classes plus background. Images 1 to 30 train (fine-tune), 31 to 40 validate, 41 to 50 test.
- **Test:** the 10 held-out real images of the same set (different plants, same greenhouse and camera); for the synthetic baseline, synthetic test images.
- **Headline** (l. 41 to 43, 569, 579): after synthetic bootstrapping, 30 real images give the best result on all 7 classes, mean IOU 0.40; with 5 real images 0.306 (l. 569); going from 5 to 30 raised the mean IOU by 32 % relative, and the curve had not settled (l. 579 to 580).
- **Ceiling** (l. 714): trained and tested on synthetic images, mean IOU 0.53, which bounds what the real-image results can reach.
- **Without synthetic data** (l. 424, 452, 436, 686, 690): trained on synthetic images only and tested on real, it "could not generalise properly"; bootstrapping on an unrelated set (PASCAL VOC) then fine-tuning on 30 real images scored 15 % relative lower than synthetic bootstrapping and missed the rare classes (peduncles, cut peduncles). A real-only run is a figure.
- **Other results** (l. 561 to 562, 714): per-part binary classifiers lowered mean IOU by 17 % relative; leaf-class IOU rose from 0.4 (synthetic only) to 0.7 (fine-tuned), +75 %.
- **Reading** (l. 502, 697): returns flatten because the synthetic plant models capture limited variation (learning stabilises around 3,000 images, l. 47); synthetic bootstrapping helps when real data are few and rare parts matter.

## Dependence

- The renderer and dataset are the authors' own earlier work (a data paper cited in the reference list), tuned to the same crop and greenhouse as the test, so the sim-to-real gap measured is a small one. DeepLab architectures; PASCAL VOC as the unrelated bootstrap. Shares authors with `barth2018`.

## Bearing (2026-10-27)

- **Closest published pattern to a labelled-render pipeline from Agrarium's viewer:** rendered plants with free labels, pre-training, then a few dozen real images, judged on real held-out images: 0.40 mean IOU with 30 real images against a synthetic ceiling of 0.53. It supports D58 (the simulator screens, real data judge) and D60 (synthetic is an addition to real data).
- **What it does not give:** the gap here is small by construction (same greenhouse, same camera, generator tuned to it), the test is 10 images, and the other cameras were judged by eye.
- **Not shown:** disease or lesions (plant parts only), a vine, a field, or a repeated run.

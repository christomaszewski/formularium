---
id: barth2018
citation: Barth, R., Hemming, J. & Van Henten, E.J. 2018. Improved Part Segmentation Performance by Optimising Realism of Synthetic Images using Cycle Generative Adversarial Networks. arXiv:1803.06301v1 [cs.CV] (preprint)
doi: 10.48550/arXiv.1803.06301
read: 2026-10-27, lightly: abstract, the aims, the data description and the Part II results and conclusions (arXiv v1 preprint; the published 2020 journal version may differ in numbers), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 7 of 7 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [sweet pepper (Capsicum annuum)]
regions: [none stated]
processes: [synthetic data, rendering, CycleGAN, image translation, bootstrapping, fine-tuning, semantic segmentation, domain adaptation]
records: []
datasets: []
files: [syn1027_barth2018arxiv.pdf (the 2026-10-27 drop)]
---

# Barth et al. 2018: CycleGAN-translated pepper renders as a better bootstrap for part segmentation (arXiv preprint)

Translates rendered pepper images toward the real greenhouse domain with an unpaired CycleGAN, and compares CNNs bootstrapped on rendered or translated images, with and without fine-tuning on 30 real images. No record: a method; a preprint of a 2020 journal paper, and a separate study from `barth2019` (it reuses that paper's dataset and design).

**Read this first.** An arXiv v1 preprint. Most of the numbers below are in the discussion text and not in the facts the reading agent verified; they were found with grep and are cited by line. The real test is the same 10 images (41 to 50) as in `barth2019` (l. 920), so it is small. The preprint's numbers differ from `barth2019`'s for the same design (see below).

## What it holds

- **Generator** (l. 32, 259 to 263): the rendered Capsicum annuum dataset of `barth2019`; a CycleGAN trained on rendered images 1 to 1,000 and on 175 unannotated real images from the same acquisition (not in the released dataset); 50 annotated real images used for testing the translation. Mean colour-distribution correlation with the real data rose from 0.62 (rendered) to 0.90 (translated).
- **Real samples** (l. 920, 888 to 930): segmentation experiments use real images 1 to 30 for training or fine-tuning and 41 to 50 for testing; 8,750 rendered or translated images for bootstrapping.
- **Test:** 10 held-out real images of the same set; synthetic baselines are scored on synthetic images 8851 to 8900.
- **Scores, mean IOU** (l. 41 to 44, 1141 to 1194, 1230 to 1239): real images only (30), 0.41; rendered bootstrap then 30 real, 0.48; translated bootstrap then 30 real, 0.52 (+27 % over real-only and +8 % over the rendered bootstrap, l. 1194); rendered only, tested on real, 0.20; translated only, tested on real, 0.31 (+55 % over rendered only, l. 1182); ceilings on synthetic test images 0.64 (rendered) and 0.56 (translated).
- **Claim of the abstract** (l. 41 to 44): best 0.52 with translated bootstrapping and real fine-tuning; 0.31 without any real fine-tuning.
- **Limits** (l. 255): by the authors' earlier work, colour and texture translation often succeeds, but domains with large geometric variation translate less well.
- **Difference from `barth2019`** (l. 257, 1102 to 1103, 1150): this preprint upscales images to 1,000 x 1,000 pixels after a 424 x 424 crop, and says its synthetic-only result "approximately doubled" over the previous 424 x 424 results; its rendered-bootstrap figure is 0.48 against 0.40 in `barth2019`. The comparison is not like for like.

## Dependence

- The rendering pipeline and dataset of `barth2019`, the BAIR CycleGAN implementation (per the reading agent), DeepLab-type CNNs. Three authors are shared with `barth2019`, a flag, and the dataset is the same.

## Bearing (2026-10-27)

- **Restyling the renders helps and is trained on real images:** translating renders toward real photos gave +0.11 mean IOU without fine-tuning (0.20 to 0.31) and +0.04 with it (0.48 to 0.52; arithmetic, not printed). This parallels `fei2021` and `cooper2026`, where a restyle fitted on a few real images lifted rendered data. A restyle fitted on Agrarium's own renders would be kin to the truth's render (D45).
- **Evidence level:** one crop, one greenhouse, a 10-image test, a preprint.
- **Not shown:** disease, vines, a field, a held-out greenhouse, or a repeated run.

---
id: noyan2022
citation: Noyan, M.A. 2022. Uncovering bias in the PlantVillage dataset. arXiv:2206.04374v1 [cs.CV] (preprint)
doi: 10.48550/arXiv.2206.04374
read: 2026-10-27, in full (a short arXiv preprint, not peer reviewed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [none]
processes: [dataset bias, image classification, random forest, capture bias, PlantVillage, lab-to-field gap]
records: []
datasets: []
files: [syn1027_noyan2022.pdf (the 2026-10-27 drop)]
---

# Noyan 2022: eight background pixels predict the PlantVillage class at 49 % (preprint)

Trains a random forest on eight background pixels per PlantVillage image and scores it on a random 20 % split. Nothing synthetic is used; it is a caution about lab-photo sets. No record: a measured bias; a short preprint.

**Read this first.** A short preprint (not peer reviewed) with one experiment. The 38 classes of the standard PlantVillage release are the target; the paper does not say which crops make up the 49 %.

## What it holds

- **Transformation** (l. 144 to 148): eight pixels per image, four from the corners and four from the middles of the sides ("PlantVillage 8px"); these carry no disease information, only background colour and capture conditions, and are under 0.1 % of the whole background (l. 149).
- **Model and split** (l. 204): scikit-learn random forest with default settings, trained on a random 80 % of the images and tested on the other 20 %, to be comparable with other PlantVillage work.
- **Result** (l. 17, 18, 224): 49.0 % accuracy on the held-out 20 %, against 2.6 % for random guessing among 38 classes.
- **Control** (l. 225): the same 8-pixel model on MNIST gives 11.7 % against 10 % chance, so the method itself does not manufacture signal.
- **Reading** (l. 216): the author attributes it to capture bias and says the models "developed on this dataset" may transfer badly; the estimate is low because only a fraction of the background was used and the forest was untuned.
- **Cited, not the paper's own** (l. 62, 248, 249): Mohanty et al. 2016's fall from 99 % to 31 % on other online images (`mohanty2016`); and in the extended PlantVillage set of Ferentinos et al. 18 of 58 classes (31 %) are purely field data and 28 (48 %) purely laboratory, so a model can learn field against laboratory.

## Dependence

- PlantVillage and scikit-learn only. The paper's code was not checked.

## Bearing (2026-10-27)

- **For rendered training sets (D58, D60):** a render has a background, a lighting and a camera, all constant within a class if the pipeline is not randomised. This paper shows how little of an image a classifier needs to read the class off those; a model fitted on Agrarium's renders would have to be judged on real images with other backgrounds.
- **For random splits:** a random split of a lab set rewards capture conditions; it is the same warning as `hu2024`'s design and `mohanty2016`'s drop.
- **Not shown:** which classes carry the bias, how it behaves for a deep network, or any synthetic data.

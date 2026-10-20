---
id: morellos2022
citation: "Morellos, A., Pantazi, X. E., Paraskevas, C. & Moshou, D. 2022. Comparison of deep neural networks in detecting field grapevine diseases using transfer learning. Remote Sensing 14:4648"
doi: 10.3390/rs14184648
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [esca, powdery mildew]
crops: [grapevine]
regions: [Greece]
processes: [transfer learning, convolutional neural networks, leaf photo classification, field photos]
records: []
datasets: []
files: [morellos_2022.pdf (the 2026-10-20 drop)]
---

# Morellos et al. 2022: pretrained image networks for esca and powdery mildew in leaf photos

AlexNet, VGG-19 and Inception v3 are fine-tuned to sort vine leaves into healthy, esca and powdery-mildew classes, first on PlantVillage and then on field photos from one Greek estate.

## What it holds

- **Field set:** 154 photos from the Chatzivaritis estate, Goumenissa: 49 esca, 56 powdery mildew, 49 healthy (l. 672-674).
- **Field accuracy, fine-tuned:** Inception v3 83.3 %, VGG-19 76.7 %, AlexNet 66.7 % (l. 37-39).
- **PlantVillage validation, fine-tuned:** Inception v3 and VGG-19 100 %, AlexNet 87.5 % (l. 34-39).
- **Training mode:** fine-tuning gave better validation and test accuracy than feature extraction for all three networks (l. 27-29).

## Dependence

Uses three published networks (AlexNet, VGG-19, Inception v3), their ImageNet or PlantVillage weights, and the open PlantVillage grapevine subset of 4253 photos (l. 660-666). No other paper's output is an input.

## Bearing (2026-10-20)

- **Strand t2 (observation).** A leaf-photo classifier for scouting. Its accuracy is from 154 field photos at one estate, so it can stand in for a scout's class call, not for severity.
- **Not read in full.** A simulator could take the per-class confusion as an error rate on an observation step. The paper gives no lesion area, severity or spread output.

---
id: boulent2020
citation: Boulent, J., St-Charles, P-L., Foucher, S. & Théau, J. 2020. Automatic detection of Flavescence dorée symptoms across white grapevine varieties using deep learning. Frontiers in Artificial Intelligence 3:564878
doi: 10.3389/frai.2020.564878
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [Flavescence dorée]
crops: [grapevine]
regions: [Cognac and Limoux, France]
processes: [symptom detection, patch classification, fully convolutional segmentation, multi-variety testing]
records: []
datasets: []
files: [boulent_2020.pdf (the 2026-10-20 drop)]
---

# Boulent et al. 2020: Flavescence dorée symptoms in white varieties by deep learning

A ResNet-18 patch classifier, turned into a fully convolutional network, flags Flavescence dorée-like symptoms in field images. It works on Chardonnay but misses Ugni-Blanc unless it is trained on several varieties.

## What it holds

- On Chardonnay the true positive rate is 98.48% and the false positive rate 1.15% (l. 374; abstract l. 45).
- Trained on Chardonnay alone, the model reaches 8.3% true positive rate on Ugni-Blanc in the personal set and 0% on the FREDON Ugni-Blanc set (l. 431-432, 450, 453).
- Five other white varieties give mixed results (Table 4, l. 410).
- Images were taken in 2018 in Cognac and Limoux, France (l. 162-163). The external set is 34 images from FREDON Aquitaine (l. 215).

## Dependence

- Builds on a ResNet-18 pretrained on ImageNet (l. 181), and on the fully convolutional conversion (Shelhamer et al. 2017).
- Uses Guided Grad-CAM (Selvaraju et al. 2019) and UMAP (McInnes et al. 2018) to inspect the model.
- Cites earlier FD detection work (AL-Saddik et al. 2017; Albetis et al. 2018).

## Bearing (2026-10-20)

- Strand t2 (observation), with t4 for the disease. A growers' engine could take the screening step: flag suspect vines, then send them to a laboratory. The multi-variety result is the limit on any single-variety model.
- Not read in full.

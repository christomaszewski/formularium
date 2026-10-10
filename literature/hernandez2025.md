---
id: hernandez2025
citation: Hernández, Inés, Gutiérrez, Salvador, Barrio, Ignacio, Íñiguez, Rubén & Tardaguila, Javier. 2025. Automated localisation of early downy mildew symptoms in vineyards using proximal sensing and deep neural networks. Precision agriculture '25, pp. 349-355
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [northern Spain, La Rioja]
processes: [symptom detection, disease severity, canopy imaging, proximal sensing, spray timing]
records: []
datasets: []
files: [hernandez2025-proximal-sensing-dm-brill.pdf]
---

# Hernández et al. 2025: CNNs localise early downy mildew in vineyards

A light read (the deep-research B list).

## What it holds

- 224 RGB canopy images from fourteen commercial vineyards in northern Spain, taken in 2019 and 2021 (l. 62-65).
- Images were cut into 800 x 800 px windows; 34,124 sub-images, 14,754 with symptoms (l. 75-78).
- EfficientNetV2S gave accuracy 0.91 and F1 0.92; ViT-Base32 gave 0.77 accuracy (l. 149, Table 1).
- Localisation IoU is 0.82 on average, 0.80 on the go and 0.83 by hand (l. 169-170).
- Predicted symptomatic area against expert area: R2 0.88, NRMSE 15% (l. 174-175).
- CNNs outperformed vision transformers (l. 222).

## Dependence

- none. The paper computes no weather, infection, incubation, sporulation, wetness or phenology model. Its only disease link is the visual oil-spot description (l. 156) and a general citation to Gessler et al. 2011 for the disease's importance (l. 29). No shared equation, code, data or form with any engine model.

## Bearing (2026-10-10)

- Little for the truth or the engine: a symptom-detection vision method with no weather or epidemic component, which could be a future observation source for symptom area (the truth would still keep it separate from the engine).

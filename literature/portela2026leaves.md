---
id: portela2026leaves
citation: Portela, F., Carneiro, G., Ferreira, L., Paredes, C.A., Sousa, J.J., Peres, E., Morais, R. & Pádua, L. 2026. Dataset of RGB images of healthy grapevine leaves and with downy mildew, powdery mildew, Esca complex, and erineum mite symptoms. Data in Brief 66:112743 (volume from the record header, not printed in the body)
doi: 10.1016/j.dib.2026.112743
read: 2026-10-27, in full (Europe PMC full text; baseline-model tables not transcribed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew, esca, erineum mite]
crops: [grapevine, Loureiro, Viosinho, Malvasia Fina]
regions: [Portugal, Vinho Verde, Douro, Vila Real]
processes: [dataset, image classification, leaf images, visual annotation, field imaging]
records: []
datasets: [portela2026leaves.portugal]
files: [syn1027_portela2026leaves.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Portela et al. 2026: 5,267 field photographs of grape leaves with downy mildew, powdery mildew, esca or mite symptoms

A data article for smartphone photographs of single leaves taken on the vine in northern Portugal, with a baseline classification. No record: a dataset. This is a different paper from Formularium's literature/portela2026 (a separate item).

**Read this first.** The class is confounded with vineyard and date (l. 346; Table 2, l. 93-203): the 2024 images are healthy and downy mildew only, and powdery mildew is mostly photographed in October 2025. The headline score (accuracy and macro-F1 0.97, l. 254) is on a random 70/15/15 image split (l. 247), so it measures in-distribution recognition, not field generalisation. Labels are visible-symptom calls, with no laboratory test (l. 347).

## What it holds

- **Where to get it** (l. 34): Zenodo 10.5281/zenodo.17343473 (concept DOI); the reading agent's look at the DataCite record gave CC BY 4.0 and a version DOI 10.5281/zenodo.17343474 (record, not in the paper). The article is open access under CC BY (l. 11).
- **Size and classes** (l. 56, 203): healthy 1,122 (Loureiro 494, Viosinho 223, Malvasia Fina 405), downy mildew 1,006, powdery mildew 1,126, Esca complex 1,000, erineum mite 1,013 images, 5,267 in all (the sum is the reading agent's arithmetic).
- **Format** (l. 12, 59): JPEG at 3000 x 3000 px and 1024 x 1024 px; Redmi Note 12 Pro smartphone (l. 91), 20 to 40 cm from the leaf (l. 209).
- **Sites** (l. 26-32): four, all in northern Portugal: the University of Trás-os-Montes e Alto Douro at Folhadela, the Casa de Mateus Foundation, a school of agriculture at Ponte de Lima (50 m), and vineyards at Abaças (566 m); three cultivars named for healthy leaves.
- **Years and dates** (l. 59, Table 2 l. 93-203): the 2024 and 2025 growing seasons; 2024 has 5 dates from 2024-06-28 to 2024-08-23 with healthy and downy mildew only; 2025 has dates from 2025-06-03 to 2025-10-23. Powdery mildew is photographed from 2025-08-14 and mostly in October (583 images on 2025-10-14).
- **Time-stamps and weather** (l. 209, 347): image files carry EXIF timestamps and, when available, GPS (l. 209); no per-image weather, leaf age or canopy position was recorded (l. 347).
- **How labels were made** (l. 238, 347): visual inspection of symptoms, by the operator who photographed, with a second reviewer's check; no laboratory confirmation. Images often show the lamina fully visible, which the authors say reduces scene complexity compared with the field (l. 345).
- **Baseline** (l. 247, 254): train 70 %, validation 15 %, test 15 %, random; ConvNeXtV2 accuracy and macro-averaged F1 0.97, the best of three architectures (Swin-T and ViT-S were lower; their values are in Table 4, not transcribed).
- **Authors' suggestions** (l. 345): synthetic occlusions can be made from the 3000 x 3000 originals to approximate partly hidden leaves in the canopy.

## Dependence

- None recorded: labels are human visual calls; the baseline models are standard pretrained networks. The group also wrote the TLS-grapevine set (ferreira2026; shared authors) and a UAV downy-mildew progression paper (Agronomy 2025, not read).

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); a check of rendered or simulated leaves.** The most useful new real downy mildew image set here for the viewer: field photographs, with dates and sites, of the disease Agrarium simulates. Rendered lesions could be compared with these on appearance, and the dates plus site coordinates (l. 26-32, 209) would allow a join to a nearby station's weather, which the paper does not do.
- **For D58, little:** the labels are symptom calls on single leaves, with no incidence, severity or onset date, so they cannot judge a risk or onset variable; and class and date are entangled, so a classifier could learn the date.
- **Limits:** two seasons, four sites, a random split, one operator's labels, three cultivars, no laboratory confirmation.

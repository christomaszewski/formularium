---
id: kerkech2019
citation: Kerkech, Mohamed, Hafiane, Adel & Canals, Raphael. 2019. Vine disease detection in UAV multispectral images with deep learning segmentation approach. arXiv preprint arXiv:1912.05281
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, esca, flavescence doree]
crops: [grapevine]
regions: [France, Centre-Val de Loire]
processes: [symptom detection, image registration, segmentation, disease mapping, leaf wetness]
records: []
datasets: []
files: [q219.pdf, 2020-kerkech-10-1016-j-compag-2020-105446.pdf, kerkech_2020.pdf (the 2026-10-20 drop)]
---

# Kerkech et al. 2019: deep-learning mapping of vine disease from UAV images

A light read (the deep-research B list).

## What it holds

- Two Centre-Val de Loire vineyard plots, France: 1.8 ha and 1.5 ha, part of one plot left untreated so the disease could develop (l. 175-190).
- Flights at 25 m in summer 2018 with visible and 850 nm cameras; ground resolution 1 cm per pixel (l. 229-236).
- Four labelled classes (shadow, ground, healthy, symptom), with 105,515 and 98,895 patches; 85% train, 15% validate (l. 494-496).
- Leaf-level total accuracy: visible 85.13%, infrared 78.72%, union fusion 90.23% (l. 979-981).
- Grapevine-level union fusion symptom F1 is 92.81%, visible 91.50%, infrared 81.66% (l. 993-994).
- The disease is named 'Mildew' and is called 'late blight' once; no pathogen is named in the body (l. 189, 875).

- **Published version:** Computers and Electronics in Agriculture 174:105446 (2020), held in the library under the file name above since 2026-10-07; its DOI, 10.1016/j.compag.2020.105446, is the file name's, not printed in the copy's text layer. The note was written from the arXiv preprint; the published text was not re-read (2026-10-12).

## Dependence

- none

## Bearing (2026-10-10)

- A labelled UAV symptom map from one summer, two plots, with no weather or infection dates: it could check a truth's disease map, but it cannot time infection, so it is of little use to the truth's infection model or the Cooptera engine.

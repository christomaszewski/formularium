---
id: abdelghafour2021
citation: Abdelghafour, F., Keresztes, B., Deshayes, A., Germain, C. & Da Costa, J.-P. 2021. An annotated image dataset of downy mildew symptoms on Merlot grape variety. Data in Brief 37:107250
doi: 10.1016/j.dib.2021.107250
read: 2026-10-27, in full (a short data article, Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [France, Bordeaux]
processes: [dataset, image segmentation, proximal imaging, photo-interpretation, symptom annotation]
records: []
datasets: [abdelghafour2021.merlot]
files: [syn1027_abdelghafour2021merlot.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Abdelghafour et al. 2021: 99 field images of downy mildew on Merlot, 95 with pixel-class labels

A data article for a set of tractor-borne colour images of Merlot Noir vines with downy mildew, labelled pixel by pixel by hand. It is the data behind the same group's detector (Sensors 2020, a separate paper, not read here). No record: a dataset.

**Read this first.** The licence is CC BY-NC-ND 4.0 (l. 6), not CC BY as the 2026-10-22 catalogue says; "ND" bars sharing adapted material, which matters for augmented or re-rendered copies. The paper gives the data as "With the article" (l. 33-34); the Mendeley DOI the catalogue lists is not in the paper's text.

## What it holds

- **Where to get it** (l. 32-34): Data in Brief 37:107250, data accessibility "With the article" (a supplement of the paper). The catalogue's Mendeley DOI 10.17632/yxf2yv5ymt.1 is cited from the 2026-10-22 catalogue and was not checked.
- **Licence** (l. 6): the article is open access under CC BY-NC-ND (the paper states no separate licence for the images).
- **Size and format** (l. 27): 99 RGB images (2592 x 2048 px, about 4 px/mm), JPEG; 95 of them have an annotation PNG (l. 27), of which 23 are complete and 72 cover only mildew symptoms (l. 27). More than 5 x 10^6 pixels are annotated (l. 29; printed "5 x 106", the exponent lost in the text layer).
- **Classes** (l. 48): seven pixel classes, coded by grey value: downy mildew on leaves, downy mildew on grapes, healthy leaf, healthy grape, shoot, leaf border, other anomalies (deficiency, necrosis).
- **Site, year, time step** (l. 6, 31, 69): the INRAE experimental estate of the Grande Ferrade near Bordeaux; two 0.3 ha plots of Merlot Noir (l. 69); the plots were photographed weekly from the end of July 2018 (l. 69). The paper as read gives no per-image date.
- **Capture** (l. 29): daylight, from the middle of the row at 70 cm above ground and 50 cm from the canopy, flash-lit; images of the trellis plane.
- **Disease context** (l. 69): "The plants were affected only by downy mildew and abiotic stresses."
- **How labels were made** (l. 29): by people, photo-interpretation in GIMP; 95 images "randomly selected" to represent the plots' variability (l. 29).

## Dependence

- Labels are by human photo-interpretation, not by a model. The related research article (Abdelghafour et al. 2020, Sensors 20:4380) built a detector on these images; the data article does not report its scores. None recorded otherwise.

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); real-data side of D58 and a check of rendered output.** Real, hand-labelled downy mildew oilspots at pixel level, with other anomalies and healthy organs labelled too. The viewer's rendered lesions could be compared with these images by eye or by a colour-region statistic. It cannot say whether a simulated lesion count is right: there is no lesion count, date or weather per image in what was read.
- **Not a training set for a disease-risk model.** One estate, one season, 99 images; no weather link. A segmenter trained on it is an observation operator at best, and Agrarium's observation operators must not compute the engine's observation pieces (D44).
- **Licence limit:** NC-ND, so augmented or re-rendered copies should stay inside Agrarium's own checks.

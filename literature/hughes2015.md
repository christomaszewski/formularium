---
id: hughes2015
citation: Hughes, D.P. & Salathé, M. 2015. An open access repository of images on plant health to enable the development of mobile disease diagnostics. arXiv:1511.08060 (preprint; the table of classes is dated 2016-04-04)
doi: 10.48550/arXiv.1511.08060
read: 2026-10-27, in full (8 pages: introduction, methods, data records, Table 1, technical validation; a preprint), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [black rot, esca, leaf blight]
crops: [grapevine, apple, blueberry, cherry, maize, orange, peach, bell pepper, potato, raspberry, soybean, squash, strawberry, tomato]
regions: [United States]
processes: [dataset, image classification, mobile diagnosis, crowdsourcing, leaf images]
records: []
datasets: [hughes2015.plantvillage_grape]
files: [syn1027_hughes2015plantvillage.pdf (the 2026-10-27 drop)]
---

# Hughes & Salathé 2015: the PlantVillage image set, 54,309 leaf images of 14 crops, 4,063 of them grape

The preprint that describes PlantVillage: expert-labelled photographs of single detached leaves, released openly for mobile disease diagnosis. No record: a dataset. For grapevine it has no downy or powdery mildew class.

**Read this first.** The licence is CC BY-SA 3.0 "with the clarification that algorithms trained on the data fall under the same license" (l. 206-207): share-alike reaches trained models, so check before any model fitted on it enters Agrarium. The leaves were detached, laid on a grey or black sheet, then cropped and rotated tip-up (l. 225-236), and in many cases the experts had infected the crop themselves (l. 350-351). Table 1's grape row is garbled in the text layer: the healthy count 423 is read from the same row and checked by the class sum (1,180 + 1,384 + 1,076 + 423 = 4,063; arithmetic, not printed).

## What it holds

- **Where to get it** (l. 205-206, 250): www.plantvillage.org; the file mapping image URLs to classes was "to be deposited" after a competition, so no DOI is given. The 2026-10-22 catalogue lists the same site.
- **Licence** (l. 206-207): CC BY-SA 3.0 Unported, share-alike extended to trained algorithms. Paper and record are the same here (no separate repository record).
- **Size** (l. 242-244, 338): 54,309 images of 14 crop species as of 2016-04-04 (l. 338, 242); 17 fungal, 4 bacterial, 2 mold, 2 viral and 1 mite disease (26 in all, arithmetic, not printed).
- **Grape classes** (l. 283-290): 4,063 images; black rot (Guignardia bidwellii) 1,180; Phaeomoniella spp. 1,384 (the esca-associated genus; the gloss is the reading agent's, the paper names the genus only); Pseudocercospora vitis (leaf blight) 1,076; healthy 423 (l. 283). No downy or powdery mildew.
- **Sites and years** (l. 220-221): experimental research stations of US land-grant universities (Penn State, Florida State, Cornell and others), before April 2016; no per-image date, site or weather is given in what was read.
- **Capture** (l. 224-236): leaves removed from plants in trials with one disease, laid on grey or black paper, photographed outside in sun or cloud, typically 4-7 images per leaf as the leaf is rotated (l. 229), then cropped and oriented tip-up. Several images per leaf are not independent.
- **How labels were made** (l. 347-351): expert plant pathologists diagnosed in the field by standard phenotyping, and in many cases the experts infected the crop directly, so symptoms are strong and one disease per leaf. Observed by people, no laboratory test is described.

## Dependence

- None recorded: labels are expert diagnoses, no model. Later work (not in this paper) uses PlantVillage's lab-style backgrounds; this paper does not test transfer to field images (the reading agent's lead: Mohanty, Hughes & Salathé 2016, not read).

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); a check of rendered leaves, with a caution.** The classic example of a set whose accuracy overstates field performance: detached, cleaned, inoculated leaves. For Agrarium it shows what a training set of controlled images looks like, and why a model scored on a random split of it says nothing about vineyard canopies.
- **For D58, no weather and no downy mildew.** The grape classes are black rot, esca-associated and leaf blight, none of which the simulator models; nothing here can judge a weather-driven variable.
- **Limits:** a preprint; share-alike licence reaches trained models; the single-leaf framing; no dates or sites per image; images per leaf are correlated.

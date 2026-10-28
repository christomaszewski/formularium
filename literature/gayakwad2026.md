---
id: gayakwad2026
citation: Gayakwad, M., Mulla, T., Parashar, D., Shikalgar, A., Chavan, P., Wakurdekar, S., Jadhav, R., Kadam, A., Paygude, P. & Joshi, R. 2026. A curated dataset of 3,477 high-resolution Grapevine (Vitis vinifera) leaf images for automated detection of Black Rot, Esca, and Leaf Blight diseases. Scientific Data (volume and article number not legible in the text layer)
doi: 10.1038/s41597-026-07431-9
read: 2026-10-27, in full (Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [black rot, esca, leaf blight]
crops: [grapevine]
regions: [India, Maharashtra, Sangli, Tasgaon]
processes: [dataset, image classification, leaf images, expert annotation, metadata]
records: []
datasets: [gayakwad2026.gvlid]
files: [syn1027_gayakwad2026leaves.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Gayakwad et al. 2026: GVLiD, 3,477 grape leaf images of black rot, esca and leaf blight from 34 vineyards in Maharashtra

A Scientific Data descriptor for a leaf-image set with one expert's labels and a metadata file per image. No record: a dataset. It has no downy or powdery mildew class.

**Read this first.** The reference list looks unreliable (two entries share the page range 123-135 and one carries another journal's DOI; l. 272, 296, 298), so what the paper says about other datasets (for example Hermos, l. 12) is not used here. The four class counts sum to 3,478, not 3,477 (l. 223-226). The text gives the collection as July-November 2023 (l. 15) and the timeline as acquisition in August-September 2023 (l. 28).

## What it holds

- **Where to get it** (l. 246, 299): Mendeley Data, 10.17632/wkymf8bhcg.5 as printed in the reference list (l. 299), with its code at a GitHub project (l. 248). Licence of the article: CC BY 4.0 (l. 6); the deposit's own licence was not read.
- **Size** (l. 37, 40): 3,792 raw images, 3,477 after curation (91.7 %, l. 40), JPG at 1080 x 1080 px (l. 42).
- **Classes** (l. 223-226): black rot 809, esca 888, leaf blight 672, healthy 1,109.
- **Site, years** (l. 15): 34 vineyards at Tasgaon, Sangli district, Maharashtra, India, July-November 2023; one season, one district.
- **Capture** (l. 15-22): two phones (Samsung Galaxy S21 Ultra, Redmi Note 10 5G), both leaf sides, 20-45 degrees to the leaf and 25-40 cm away, in the vineyard and on a grey board.
- **Metadata** (l. 114, 133, 147): each image has a JSON record with vineyard ID, GPS, capture time, lighting, a one-word weather string (for example "Humid") and device; no measured weather.
- **How labels were made** (l. 15, 26, 31, 35): by one agricultural consultant with more than 18 years in viticulture, who verified each leaf's category before imaging (l. 26) and labelled by a decision tree of lesion features (l. 35). Observed by a person; no laboratory test is mentioned.
- **Label reliability** (l. 219-221): on 200 images re-annotated, Cohen's kappa 0.86 (second expert) and 0.92 (same expert after four weeks); about 3 % of images are flagged uncertain.
- **Split** (l. 227): the authors recommend a stratified 70/15/15 split, which is by class, not by vineyard or date.

## Dependence

- None recorded: labels by a person, no model. The authors write that a model trained on this set alone is likely to perform worse on leaves from other climates or cultivars (l. 237, paraphrased).

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); a check of rendered or simulated leaves, not a training set for risk.** Real leaf photographs of three diseases that Agrarium does not yet simulate (black rot, esca) and one that it does not include (no downy or powdery mildew), so they cannot test the downy-mildew lesion renderer. They could test a generic lesion-appearance classifier's domain gap (field against grey board).
- **For D58, no weather.** The metadata weather is a word, not a number, so it cannot judge a weather-driven variable.
- **Limits:** one district, one season, one labeller, a class-stratified split that lets vineyard and date leak across train and test, a sum that is off by one.

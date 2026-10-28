---
id: blekos2023
citation: Blekos, A., Chatzis, K., Kotaidou, M., Chatzis, T., Solachidis, V., Konstantinidis, D. & Dimitropoulos, K. 2023. A Grape Dataset for Instance Segmentation and Maturity Estimation. Agronomy 13(8):1995
doi: 10.3390/agronomy13081995
read: 2026-10-27, lightly: abstract, introduction, section 2 (other datasets, Table 2, the dataset, Tables 1, 4 and 5), data availability statement (training-method sections skimmed, not extracted), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine, table grape]
regions: [Greece]
processes: [dataset, image segmentation, instance segmentation, maturity estimation, object detection]
records: []
datasets: [blekos2023.certh]
files: [syn1027_blekos2023grape.pdf (the 2026-10-27 drop)]
---

# Blekos et al. 2023: the CERTH grape dataset, 2,502 table-grape images with bunch masks and a colour-based maturity class

A data paper with detector baselines. Bunches in 2,502 smartphone images of one Crimson Seedless vineyard are masked and given one of three maturity classes. No record: a dataset.

**Read this first.** "Maturity" is a human judgement of berry colour, helped by agronomists who knew the week of development and the days to harvest (l. 274-277); it is not Brix. The paper's Data Availability Statement only promises release (l. 770); the Zenodo record and its licence come from the reading agent's look at the repository, not from the paper.

## What it holds

- **Where to get it** (l. 770): the paper says the dataset "will be made publicly available after the publication". The reading agent found Zenodo 10.5281/zenodo.10777647, licence CC BY 4.0, two files, about 20 GB (record, not in the paper). The article itself is CC BY (MDPI, l. 59).
- **Images** (l. 21, 238-245): about 2,500 images (2,502, l. 237, 294) of the 'Crimson Seedless' table grape in one vineyard, during the 2022-2023 development and harvest period (l. 239); iPhone 11 Pro held between the rows at about 1 to 2 m (l. 240-242); all rescaled to 2160 x 3840 px (l. 245). The paper's lines read do not name the vineyard's place.
- **Labels** (l. 269-277, 293): masks drawn by human experts with the RITM interactive segmentation tool, a model that assists the annotator (l. 269-272); 9,832 labelled bunches (l. 293); three classes by berry colour from yellow to red (l. 274-277, 286).
- **Class counts** (Table 1, l. 315): immature 1,668; semi-mature 1,398; mature 6,766 (total 9,832). Class balance is skewed to mature (arithmetic, not printed: about 69 %).
- **Split** (l. 295): 2,000 training, 251 validation and 251 test images. The text does not say the split respects vineyard rows or dates; nothing suggests it does.
- **Baselines** (Table 4, l. 540, 552): in the three-class setting the best of the detectors tried is Mask2Former-Swin(S), mAP 52.3 % (boxes) and 51.5 % (masks); the weakest is YOLOv3-320, mAP 31.7 %. These are scores on a held-out part of the same vineyard and season.
- **Other public grape image sets** (Table 2, l. 351-379; text l. 205-217): Grape CS-ML (2018, 15 varieties, images paired with Brix and pH in the cited source, l. 123), Embrapa WGISD (2019, 300 images), AI4EU (2021, 250 images), wGrapeUNIPD-DL (2022; Table 2 says 271 images, the text says 373, l. 215: inconsistent in the paper), GrapesNet (2023, RGB and RGB-D, l. 217), and a bunch-condition set of 910 images augmented to about 10 K (Table 2 note; the augmented copies are not independent images). All cited from this paper.

## Dependence

- RITM-assisted masks (a model in the annotation loop); baselines are Mask R-CNN, Cascade Mask R-CNN, HTC, Mask2Former and YOLO variants. Nothing synthetic in the data. A shared-author flag with other notes here: none recorded.

## Bearing (2026-10-27)

- **D60 tier 3 (imagery), real-data side of D58.** A real, hand-masked bunch set with a colour-based ripeness label, in the same ripening window the viewer renders. It could test whether rendered bunches look like real ones in size, number per image and colour class; it carries no disease, no weather and no day-of-season tag in what was read.
- **Not a ripeness truth.** The label is a colour call, not sugar (Brix); Grape CS-ML is the cited set that pairs images with Brix and pH (l. 123) and was not opened. For phenology or ripening models the better real data are the weather-matched sets in this strand.
- **Limits:** one table-grape vineyard, one season, a random image split, an unnamed place; a wine-grape canopy may differ.

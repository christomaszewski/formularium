---
id: saccuti2025
citation: Saccuti, A., Graziosi, F. & Lodi Rizzini, D. 2025. A dataset for vineyard disease detection via multispectral imaging. Data in Brief 61:111712
doi: 10.1016/j.dib.2025.111712
read: 2026-10-27, lightly: abstract, specification table, sections 1-4 including the limitations (Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [flavescence dorée, esca]
crops: [grapevine, Ancellotta, Marani, Salamino]
regions: [Italy, Emilia-Romagna, Reggio Emilia, Correggio]
processes: [dataset, multispectral imaging, disease detection, proximal sensing, field imaging]
records: []
datasets: [saccuti2025.correggio]
files: [syn1027_saccuti2025multispectral.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Saccuti et al. 2025: 172 multispectral captures of vines with flavescence dorée, esca or neither, from two Emilia vineyards

A data article for hand-held, front-view six-band multispectral captures of single vines, with a per-plant label file. No record: a dataset. It has no downy or powdery mildew class.

**Read this first.** Labels are agronomists' visual calls; the paper notes that flavescence dorée is confirmed only by PCR in a laboratory (l. 34) and does not say these plants were PCR-tested. Plants showing only confounding symptoms such as sunburn or nutrient deficiency were labelled healthy (l. 88). The paper does not give the acquisition dates; it says the acquisition was late in the season, so that many diseased plants had other symptoms that obscured the target ones (l. 103).

## What it holds

- **Where to get it** (l. 22): Zenodo 10.5281/zenodo.14936376. Licence of the article: CC BY (l. 6). The Zenodo record's licence (CC BY 4.0) and its single archive of 4.8 GB are the reading agent's look at the record, not in the paper.
- **Size** (l. 52): 172 captures; a capture is one shot by each of the six cameras of the MicaSense RedEdge-P (l. 43). Session IDs and the number of captures per session are in Table 1 (l. 53-70): flavescence dorée, esca and healthy plants, plus calibration-panel sessions; session 0016 has plants with both diseases (l. 61).
- **Site** (l. 20): two vineyards of the Cantine Riunite cooperative at Correggio, Reggio Emilia, Emilia-Romagna; varieties Ancellotta, Marani and Salamino (the Lambrusco types, l. 38, 55).
- **Contents** (l. 43-49): raw camera files and logs, processed PNG images, a JSON annotation file with one entry per plant (label, vineyard location, acquisition period, vineyard type, number of captures, l. 47), and a Jupyter notebook of usage examples.
- **Capture** (l. 18): camera on a tripod, carried by hand along rows, in front of one plant at a time with several shots from different horizontal angles, and a downwelling light sensor; calibration-panel images before each new vineyard.
- **How labels were made** (l. 18, 88): by people, agronomists identifying healthy or diseased plants from visual features; no laboratory test is described.
- **Authors' limits** (l. 100-106): unbalanced numbers of diseased and healthy plants; late acquisition obscuring symptoms; no preview of shots, so some plants are off-centre; the light sensor may have been blocked between rows.
- **Related sets cited** (l. 37): an RGB set of grapevines with flavescence dorée and esca by Tardif et al. (not read) and Ryckewaert's hyperspectral leaves (see ryckewaert2023).

## Dependence

- None recorded: human labels, camera files. The authors name no earlier model output in the data.

## Bearing (2026-10-27)

- **D60 tier 3 (imagery); not for the downy mildew model.** Multispectral front views of whole plants with two other diseases. For Agrarium it could only check the spectral side of a rendered canopy (for example band ratios of healthy against symptomatic vines) and show how much confounding symptoms mislead a visual label.
- **For D58, no weather and no dates.** It cannot judge an onset or risk variable.
- **Limits:** 172 captures from two vineyards, acquisition dates not given, unbalanced classes, labels not PCR-confirmed, mixed-symptom plants.

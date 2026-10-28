---
id: ryckewaert2023
citation: Ryckewaert, M., Héran, D., Trani, J.-P., Mas-Garcia, S., Feilhes, C., Prezman, F., Serrano, E. & Bendoula, R. 2023. Hyperspectral images of grapevine leaves including healthy leaves and leaves with biotic and abiotic symptoms. Scientific Data 10:743
doi: 10.1038/s41597-023-02642-w
read: 2026-10-27, lightly: abstract, methods, data records, Tables 1-3, usage notes (the technical-validation PCA paragraphs skimmed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [flavescence dorée, downy mildew]
crops: [grapevine]
regions: [France, southern France]
processes: [dataset, hyperspectral imaging, leaf reflectance, symptom library, stress detection]
records: []
datasets: [ryckewaert2023.leaves]
files: [syn1027_ryckewaert2023hyperspectral.pdf (the 2026-10-27 drop)]
---

# Ryckewaert et al. 2023: hyperspectral images of 204 detached grape leaves, mainly flavescence dorée and healthy, with only 2 downy mildew leaves

A data descriptor for a symptom library of leaf reflectance cubes (400-900 nm) taken in the laboratory, with leaf chlorophyll and flavonol readings. No record: a dataset. It is not a downy mildew series.

**Read this first.** Downy mildew is 2 leaves (Table 2, l. 90), flavescence dorée 80 (l. 80), healthy 40 (l. 79). The 2026-10-22 catalogue paired this paper with Recherche Data Gouv 10.57745/av1eti; the paper's own data DOI is 10.57745/WW7TY7 (l. 506-507). The abstract says 205 leaves (l. 16) and the Methods 204 (l. 100-101). Table 1 sums to 160 infected and 45 healthy leaves, and Table 2 to 165 and 40, both 205 in all (arithmetic, not printed): the two tables disagree on the healthy count.

## What it holds

- **Where to get it** (l. 195, 506-507): the INRAE data repository, Recherche Data Gouv, 10.57745/WW7TY7 (reference 15).
- **Licence** (l. 525): the article is CC BY 4.0; the deposit's own licence was not opened.
- **Size** (l. 334-337): one reflectance cube of about 214 MB per leaf image, 512 x 512 px with 204 spectral bands; for about 204 leaves this is about 44 GB (arithmetic, not printed), so it is not a casual download.
- **Site and date** (l. 97): leaves collected during September 2020 in southern France (one coordinate pair printed); a single sampling month, no time series.
- **Varieties** (Table 1, l. 64-73): seven (Colombard, Duras, Fer, Gamay, Loin de l'oeil, Mauzac, Chardonnay).
- **Symptoms** (Table 2, l. 76-92): healthy 40; flavescence dorée 80; water stress 13; wood diseases 17; buffalo treehopper 17; green leafhopper 20; senescence 8; deficiency 1; chlorosis 1; discoloration 1; damage (hail, harvester) 5; downy mildew 2.
- **Imaging** (l. 119): laboratory hyperspectral camera, 400-900 nm, 7 nm spectral resolution (l. 119), halogen lamp, certified reflectance reference; detached leaves.
- **Per-leaf chemistry** (l. 113): Dualex readings of chlorophyll a + b (ug/cm2), epidermal flavonols and the nitrogen balance index, taken before sampling.
- **How labels were made** (l. 103): each leaf and its vine were diagnosed by a phytopathology expert; observed by a person, no model, no laboratory pathogen test is described in the lines read.
- **Authors' limits** (l. 456): class imbalance and a small number of images for deep learning.

## Dependence

- None recorded: expert diagnosis and instrument spectra. The set was first used in a flavescence dorée paper by the same lead author (The Analyst 2022, not read).

## Bearing (2026-10-27)

- **D60 tier 4 (research only).** A hyperspectral symptom library is outside the weather-and-sensor tiers. For Agrarium it could only check a spectral or leaf-optics piece (for example the viewer's leaf colour of healthy against symptomatic leaves) and give an idea of how many classes of stress look alike to a camera.
- **Not for D58 or the downy mildew model:** 2 downy mildew leaves, one month, one place, no weather, no outbreak outcome; do not use it as a downy mildew test set.
- **Limits:** class imbalance, tables that disagree by 5 leaves, detached leaves under a lamp, one sampling month, a 44 GB archive.

---
id: morel2018
citation: Morel, J., Jay, S., Féret, J.-B., Bakache, A., Bendoula, R., Carreel, F. & Gorretta, N. 2018. Exploring the potential of PROCOSINE and close-range hyperspectral imaging to study the effects of fungal diseases on leaf physiology. Scientific Reports 8:15933
doi: 10.1038/s41598-018-34429-0
read: 2026-10-27, lightly: abstract, introduction, results (inversion dynamics, LDA, Table 1), the discussion of limitations and the sample description in the methods, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [black leaf streak (Pseudocercospora fijiensis)]
crops: [banana]
regions: [none]
processes: [radiative transfer, model inversion, hyperspectral imaging, linear discriminant analysis, leaf biochemistry, disease stages]
records: []
datasets: []
files: [syn1027_morel2018.pdf (the 2026-10-27 drop)]
---

# Morel et al. 2018 (banana, not grapevine): PROCOSINE inversion on hyperspectral leaf disks to separate six disease stages

Inverts a leaf radiative-transfer model (PROSPECT-D coupled to COSINE) pixel by pixel on laboratory hyperspectral images of banana leaf disks and classifies disease stage from the fitted parameters with a linear discriminant analysis. No record: a method on lab disks.

**Read this first.** Another crop (banana) and laboratory leaf disks, not a canopy. Nothing is trained on simulated data: the model is inverted on each pixel, and the classifier is trained on the inverted parameters. The accuracy comes from two-fold cross-validation inside the same 12 areas, so pixels from one disk can fall in both folds; the authors state that no independent dataset and no statistical baseline were tested (l. 407 to 409).

## What it holds

- **Generator** (l. 20): the PROCOSINE radiative-transfer model (PROSPECT-D with COSINE), inverted on submillimetre hyperspectral images in the visible and near infrared; the inverted leaf biochemical and structural parameters are the features.
- **Real samples** (l. 448, 454, 456, 457): banana leaves (Musa AAA cv. Williams, Cavendish subgroup); 12 leaf disks, two per disease stage including the asymptomatic one, one expert-labelled area on each; 12 areas holding 5,941 pixels in all.
- **Test** (l. 266): a two-fold cross-validation computed from the LDA results inside those 12 areas; no held-out disk, no other leaves.
- **Score** (l. 28, 264): overall accuracy 78.7 % across six stages; producer accuracy by stage 81.0, 61.8, 69.0, 50.2, 95.7 and 95.4 %; errors mainly between the asymptomatic stage and the first visible ones.
- **Limits** (l. 407 to 411): a rigorous comparison with a purely statistical method (for example LDA on the raw spectra) needs a larger dataset and is left as future work; performance is not confirmed on an independent dataset; the inversion may be invalid where disease moves the leaf outside the range for which the model was validated.
- **Without the radiative-transfer step:** not run.

## Dependence

- PROSPECT-D and COSINE radiative-transfer models; LDA. Nothing else recorded.

## Bearing (2026-10-27)

- **D60:** an example of a physical model used as a feature extractor on real images, with an untested benefit; the paper itself says the hybrid-against-statistical comparison is still to do. It gives no number for how much a radiative-transfer step adds.
- **Tier-3 canopy imagery:** leaf-scale, lab-lit and small; it says nothing about canopy retrieval, row structure or field light.
- **Not shown:** grapevine, downy mildew, any field image, an independent test set, or a statistical baseline.

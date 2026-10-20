---
id: abdelghafour2020
citation: "Abdelghafour, F., Keresztes, B., Germain, C. & Da Costa, J.-P. 2020. In field detection of downy mildew symptoms with proximal colour imaging. Sensors 20:4380"
doi: 10.3390/s20164380
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [France (site not named in the first pages)]
processes: [colour imaging, leaf symptom segmentation, structure tensor descriptors, Gaussian mixture models, seed growth]
records: []
datasets: []
files: [abdelghafour_2020.pdf (the 2026-10-20 drop)]
---

# Abdelghafour et al. 2020: colour-camera detection of downy mildew symptoms in the field

A proximal colour-image method flags downy mildew leaf symptoms with structure-tensor and colour descriptors, modelled as Gaussian mixtures. It grows seeds into symptom areas.

## What it holds

- **Data:** 100 images of vines with downy mildew or abiotic stress, checked by leave-one-out cross-validation (l. 29-30).
- **Result:** pixel-level precision 83 % and recall 76 % at the chosen threshold, alpha = 0.2 (l. 31-32, 919-920).
- **Trade-off:** thresholds that keep precision above 80 % give recall of only 3 to 48 % (l. 813-814).

## Dependence

None recorded. The method is the authors' own: local structure tensors, a Log-Euclidean mapping, mixtures of Gaussians and seed growth (abstract).

## Bearing (2026-10-20)

- **Strand t2 (observation).** A symptom-area estimate from a camera at leaf or plot scale. Its 83 % and 76 % are pixel scores, not per-vine or per-field scores.
- **Not read in full.** A simulator could take the detected area fraction as an observation input, with its pixel error. It is not a severity model.

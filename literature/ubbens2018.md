---
id: ubbens2018
citation: Ubbens, J., Cieslak, M., Prusinkiewicz, P. & Stavness, I. 2018. The use of plant models in deep learning: an application to leaf counting in rosette plants. Plant Methods 14:6
doi: 10.1186/s13007-018-0273-z
read: 2026-10-27, in full (open-access journal PDF; Tables 1 to 4 read from the text layer), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [Arabidopsis]
regions: [none]
processes: [synthetic data, L-system, rendering, data augmentation, leaf counting, dataset shift, convolutional network]
records: []
datasets: []
files: [syn1027_ubbens2018.pdf (the 2026-10-27 drop)]
---

# Ubbens et al. 2018: L-system Arabidopsis rosettes rendered to augment, or replace, real images for leaf counting

Renders 1,000-image sets of Arabidopsis rosettes from an L-system plant model and trains a convolutional network to count leaves, with the synthetic images added to real ones or used alone, and tests on real images. No record: a method on a rosette, not a vine.

**Read this first.** The augmentation gain is read against an earlier paper's real-only figure (0.61), not a paired rerun in this paper (l. 322, 324). The within-set test is a random 80/20 split of each real set (l. 220), so it is a same-set test; the cross-set tests are the stronger ones. The real sets are small (120 and 165 images). The authors' abstract claim that the generator "mitigates" dataset shift rests on one pair of real sets whose phenotype distributions differ.

## What it holds

- **Generator** (l. 228, 185, 186): an L-system model run in the lpfg simulator of the Virtual Laboratory; sets of 1,000 rendered images each, with plant scale 1:1 to 1:2: S1 (12 to 20 leaves), S2 (5 to 13 leaves, soil background), S12 (5 to 20 leaves, varied background). Leaf counts are the label, so the labels are exact (the reading agent's summary).
- **Real samples** (l. 182, 183, 220): Ara2012, 120 images, 12 to 20 leaves; Ara2013-Canon, 165 images, 5 to 13 leaves; each split randomly 80 % train and 20 % test for a within-set run.
- **Augmentation** (l. 294, 322, 324): adding S2 (1,000 renders) to Ara2013-Canon training gives a mean absolute count difference of 0.48 (SD 0.58), R2 0.92, agreement 80 %, against 0.61 (SD 0.52) for an earlier paper's real-only run, which this paper cites. The text says a reduction of "approximately 27 %" (l. 294); 0.61 to 0.48 is 21 % (arithmetic, not printed).
- **Real to real, different sets** (Table 3, l. 333, 334): trained on Ara2013-Canon and tested on Ara2012, absolute error 5.45 leaves, R2 -4.79, agreement 0 %; the reverse, 5.39 leaves, R2 -6.15.
- **Synthetic only to real** (Table 3, l. 335, 336, 356): S12 tested on Ara2012, 1.38 leaves, R2 0.42, agreement 22 %; S12 on Ara2013-Canon, 1.82 leaves, R2 -0.33, agreement 20 %; S2 on Ara2013-Canon, 1.29 leaves, R2 0.26 (l. 356). Trained on real, tested on synthetic: 0.81, R2 0.82, so the synthetic set is easier (l. 357, 391).
- **Reading** (l. 337, 388, 392, 394, 397): synthetic-only beats real-trained when the two real sets differ in phenotype distribution; mixing real and synthetic sets of different distributions lets the network learn which is which and hurts generalisation, so it is advisable only if they overlap; synthetic data alone avoid that; a model that was not realistic enough degraded performance.

## Dependence

- An existing Arabidopsis L-system model from the Prusinkiewicz lab, re-implemented, with the leaf shape taken from an Ara2012 leaf and the background colour set to match real soil (the reading agent's summary). The real sets are the Plant Phenotyping Datasets. Cieslak is an author here and on `mounir2026` (a flag; the L-system lineage).

## Bearing (2026-10-27)

- **What it supports (D58, D60):** a plant-structure generator whose output is judged on real images, with a measured case where synthetic-only beat a real model that faced a different distribution (1.4 to 1.8 leaves error against 5.4), and a measured caution that mixing sets with different distributions can hurt. The labels (leaf count) come free from the model, as lesion counts would from Agrarium's truth.
- **For the viewer's renders:** the synthetic distribution must cover the real one; the real sets here span 5 to 20 leaves and the generator was set to the same range.
- **Not shown:** disease, a field image, a held-out real set larger than 165 images, or a paired real-only run.

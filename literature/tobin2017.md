---
id: tobin2017
citation: Tobin, J., Fong, R., Ray, A., Schneider, J., Zaremba, W. & Abbeel, P. 2017. Domain randomization for transferring deep neural networks from simulation to the real world. arXiv:1703.06907 [cs.RO] (version 1, 20 March 2017; published at IROS 2017)
doi: 10.48550/arXiv.1703.06907
read: 2026-10-27, lightly: abstract, introduction, the method (sections III and IV) and the results (localisation accuracy, ablations, the robot experiment); related work skimmed. The arXiv version 1 preprint was read. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [domain randomization, sim-to-real transfer, synthetic data, object localization, rendering, robotics]
records: []
datasets: []
files: [syn1027_tobin2017.pdf (the 2026-10-27 drop)]
---

# Tobin et al. 2017: train an object detector only on randomised renderings and it transfers to real camera images

A robotics image-detection result: a network trained only on simulated images with random textures, lighting, camera position and distractors localises objects on a table in real webcam images to about 1.5 cm. No record: a method with a measured sim-to-real test.

**Read this first.** Robotics, not vines or disease: camera images of tabletop shapes. Read as the arXiv preprint (version 1). The real images were used only at test time; the transfer lasted only as far as the randomisation covered the real scene's variation.

## What it holds

- **The idea** (l. 16-18): "With enough variability in" the simulator, the real world "may appear to the model as just another variation".
- **Headline** (l. 21, 29): a real-world detector "accurate to 1.5 cm and robust to distractors" and partial occlusions, trained only on simulated RGB images, "without pre-training on real images" (a first for robotic control, as the authors claim).
- **Real test set** (l. 246): 480 webcam images, 60 for each of eight geometric objects (20 alone, 20 with distractors, 20 partly occluded).
- **Accuracy** (l. 265-270): localisation within 1.5 cm on average in the real world; the detectors still fit the simulated data better, where error is 0.3 to 0.5 cm (about three to five times smaller, arithmetic, not printed).
- **Table II, full method on real images** (l. 324): error 1.3 cm (object alone), 1.8 cm (distractors) and 2.4 cm (occlusion), with standard deviations over test images (0.6, 1.7, 3.0).
- **A missing randomisation factor shows as real error** (l. 327): with no distractors in training, error is 1.5 cm for the object alone but 7.2 cm with distractors and 7.4 cm with occlusions on real images.
- **How much randomisation** (l. 273, 280): with 10,000 training examples fixed, performance degrades significantly with fewer than 1,000 unique random textures; in the low-data regime, texture randomisation matters more than randomising object positions.
- **Data size and pre-training** (l. 257, 261): relatively accurate detection from as few as 5,000 simulated samples, improving up to about 50,000; the authors' hypothesis that pre-training would be essential was not borne out with enough simulated data.
- **No validation on reality** (l. 317): no real data were available in training, so "no validation on real data can be done" while training.
- **Robot task** (l. 351-353): a Fetch robot picked up the target in 38 of 40 trials, including cluttered scenes.

## What TRUTH-METHOD says of it

TRUTH-METHOD's reference table: "Tobin et al. 2017, IROS (arXiv:1703.06907) | domain randomisation: reality as 'just another variation'" (status snippet).

Verdict: **confirmed.** The quoted phrase is the abstract's (l. 16-18). What it does not say: the idea is argued for images of rigid objects, and the transfer failed when one randomisation factor was left out (l. 327) or too few textures were used (l. 273).

## Dependence

- Randomisation ranges are set by the authors; a VGG-16 backbone; no physical model of reality is borrowed. Rendering is by a physics-engine renderer.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 1:** supports using an ensemble of families, not one, so that a real farm may look like "another variation"; the support is in a different domain, with images.
- **D60:** the real test error was 3 to 5 times the simulated error (l. 265-270), and the real-data gap was set by which variations the randomisation left out (l. 327). A synthetic-trained plant model needs a real test set held back and a list of what the simulator does not vary.
- **Not shown:** anything for weather, phenology or disease; whether randomising biology (rather than image appearance) transfers.

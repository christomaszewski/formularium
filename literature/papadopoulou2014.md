---
id: papadopoulou2014
citation: Papadopoulou, M., Raphael, B., Smith, I.F.C. & Sekhar, C. 2014. Hierarchical Sensor Placement Using Joint Entropy and the Effect of Modeling Error. Entropy 16:5078-5101
doi: 10.3390/e16095078
read: 2026-10-21, lightly: abstract, introduction, Section 2 (strategy, entropy, joint entropy, Algorithm 1), Section 3 (CFD set-up, modelling errors, results) and the conclusions, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Singapore]
processes: [sensor placement, joint entropy, modelling error, model falsification, computational fluid dynamics, wind speed]
records: []
datasets: []
files: [papadopoulou2014.pdf (the 2026-10-21 drop)]
---

# Papadopoulou, Raphael, Smith & Sekhar 2014: joint-entropy placement that counts modelling error, on CFD wind around a building

Picks wind sensors one at a time to maximise the joint entropy of an ensemble of CFD predictions, where each histogram interval is as wide as measurement error plus modelling error, and tests it on wind around a laboratory building in Singapore. No record: a method.

**Read this first.** There is no random-placement baseline and no held-out placement test: the only comparison is the authors' earlier sequential-entropy strategy at four sensors (l. 699-708), and performance is judged on one randomly chosen unseen location with simulated measurements drawn from models that match historical data elsewhere (l. 629-642). Eqs. 1 to 3, 6, 7 and 8 are partly lost in the text layer and are recorded as unchecked (Eq. 3, the mutual-information identity, is inferred from the standard form). Figures 8 to 11 and 13 to 16 carry their numbers only in the figures.

## What it holds

- **Method** (Algorithm 1, p. 7, l. 243-262; Eqs. 1 and 2, l. 294, 318): the first sensor is the location of maximum entropy; the models are then split into subsets by the interval each falls in, and each next sensor is the location with maximum entropy of its distribution over the subsets. Interval width is measurement error plus modelling error (l. 221), so differences within error count as the same. A tree keeps each step at "O(constant)" as stated (l. 276); a forward joint-entropy evaluation grows exponentially in the number of sensors (l. 332).
- **Set-up** (l. 344-349, 461-469, 530-532): BubbleZERO laboratory, NUS campus, Singapore; steady RANS CFD, 283 runs fitted by response surfaces (l. 463), 15 uncertain parameters, 63 candidate sensor locations (l. 466), 1024 candidate models. Measurement error is 0.1 m/s and 22.5 degrees for all sensors (l. 531).
- **Modelling error** (l. 500, 536): spatially varying systematic errors (for speed, from [-0.6, +0.4] to [-1, +0.8] m/s, l. 500) give a higher joint entropy gain than uniform ones. Stopping rule: an entropy increase under 0.5 is insignificant (l. 575); about 10 % of models remain after the 4th sensor (l. 584).
- **Wind speed, four sensors** (l. 649-652): prediction range down 54 %, 76 candidate models left of 1024, 88 % of simulated measurements inside the range at the unseen location. Sequential entropy placement [22], four sensors: range down 52 %, 136 models, 89 % inside (l. 705-708).
- **Wind direction** (l. 657-660, 685-687): four sensors, range down 36 %, 88 models, 42 % inside; six sensors, down 47 %, 69 models, 39 % inside. The authors conclude direction is not predicted with reasonable accuracy (l. 753).

## Dependence

- Builds on the entropy-based sequential placement of the authors' earlier work ([22], [23]), on model falsification by measurements (Goulet & Smith), on the authors' earlier modelling-error ranges ([33]) and on Papadimitriou & Lombaert for correlated systematic error. The authors are shared with that earlier work, a flag, not a dependence.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): joint entropy with model error, and scoring placements.

- **Takeable:** setting the histogram width from measurement plus model error is a way to put a sensor-error floor into an entropy criterion, and the falsification score (candidate models left) is a scoring idea for an ensemble of simulated seasons. The ensemble here is 1024 models and 63 sites, far below vine scale, and joint entropy is estimated by counting models in intervals.
- **Validation:** one unseen location, simulated measurements, one four-sensor comparison with the earlier sequential rule (gain 54 % against 52 % in range, 76 against 136 models, l. 649-708); no random draws, no held-out sites beyond that.
- **Not shown:** sensor cost (left as future work, l. 742), field measurements, a re-plan.

---
id: hughes2013
citation: Hughes, G., Burnett, F. J. & Havis, N. D. 2013. Disease risk curves. Phytopathology 103:1108-1114 (issue 11)
doi: 10.1094/PHYTO-12-12-0327-R
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [general]
processes: [warning scores, risk calibration]
records: []
datasets: []
files: [10-1094-phyto-12-12-0327-r.pdf]
---

# Hughes, Burnett & Havis 2013: disease risk curves

From SRUC, Edinburgh.

## What it holds

- A method paper on 'disease risk curves': a logistic curve from evidence to the probability that a crop needs treatment (l. 40-42).
- Example 1, Twengström et al. (1998) data: 805 untreated oilseed rape crops, 131 cases and 674 controls at 25% infected plants (l. 70-76). Fit p = 1/(1 + e^-(b0 + b1 X)), b0 = -6.773, b1 = 0.131 per risk point (l. 130-131). Thresholds of 40 and 50 points give 0.18 and 0.45 (l. 137-138).
- Example 2, Johnson et al. (1998), potato late blight at Hermiston: 28 years, 15 outbreaks (l. 70-72). Prior 15/28 = 0.536; LR 5.200 and 1.589 (l. 220-225). Naive Bayes overestimates the log-odds: 2.255 against 2.141 from logistic regression (l. 241).
- Example 3, barley Ramularia leaf spot: 306 crops, 207 cases; AUDPC known for 37 (l. 274-279). Risk 0.14 at AUDPC 0 and 0.30 at 75 (l. 290).
- Example 4, winter wheat eyespot: 299 crops, five case thresholds, 10 to 45% (l. 319, 334; Table 1, l. 404-413).
- Cases and controls are retrospective labels on untreated crops. No process model dated the data.
- It is evaluation and calibration arithmetic, and its first author wrote hughes2017 as well.

## Dependence

- Worked examples on published data (Twengström et al. 1998 and others); no fitting of its own beyond the curves. Hughes is an author of the engine's warning scores, a reference piece, which links nothing.

## Bearing (2026-10-08)

- Clear and a method: how to calibrate a risk index to a probability, for scoring the engine's warnings.

---
id: gutierrez2021
citation: Gutiérrez, Salvador, Hernández, Inés, Ceballos, Sara, Barrio, Ignacio, Díez-Navajas, Ana M. & Tardaguila, Javier. 2021. Deep learning for the differentiation of downy mildew and spider mite in grapevine under field conditions. Computers and Electronics in Agriculture 182:105991 (article number)
doi: 10.1016/j.compag.2021.105991
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 29 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew, spider mite]
crops: [grapevine]
regions: [Basque Country]
processes: [detection, observation]
records: []
datasets: []
files: [Deep-learning-for-the-differentiation-of-downy-mild_2021_Computers-and-Elect.pdf]
---

# Gutiérrez et al. 2021: telling downy mildew from spider mite on leaves

From the University of La Rioja and partners. One vineyard at Etxano, Bizkaia.

## What it holds

- Classification of single leaves as downy mildew, spider mite or healthy. It gives no severity, incidence or date.
- One commercial vineyard at Etxano, northern Spain (l. 103), photographed in one session, 11:00 to 14:00 on a partly cloudy day in early August; the year is not stated (l. 110). Sun and cloud, both canopy sides (l. 116); camera about 30 cm from the leaf (l. 137).
- Labels: one expert identified each leaf by eye in the field (l. 111). 841 images: 275 downy mildew, 258 spider mite, 308 healthy (l. 260).
- Split 75 % train and 25 % test, giving 167 test images (55 downy, 51 spider, 61 healthy) (l. 259). No leaf or plant grouping is described (l. 194).
- Preprocessing: hand-cropped leaf, GrabCut background removal (l. 173), 300 x 300 pixels (l. 181), hue threshold at 40 chosen from about 60 images (l. 160), (l. 167).
- CNN trained from scratch (l. 179).
- Three-class test accuracy 0.94 on the hue channel without threshold (l. 395); 0.85 to 0.86 with all HSV channels (l. 397), (l. 398).
- Pairs: downy mildew vs spider mite 0.91 (l. 413); healthy vs downy mildew 0.89 (l. 416).
- Small, single-day, single-site test: not evidence for other sites or seasons. Observation role only.

## Dependence

- 841 leaf images from one session, labelled by one expert; a CNN after hue thresholding chosen on about 60 images from the same session (not said to be excluded from testing).
- No author of an engine model.

## Bearing (2026-10-08)

- Clear, and optimistic: single-leaf classification in one session, no severity or date. An upper bound for an image operator, not a field rate.

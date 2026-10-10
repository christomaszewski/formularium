---
id: hernandez2024
citation: Hernández, Inés, Gutiérrez, Salvador, Barrio, Ignacio, Íñiguez, Rubén & Tardaguila, Javier. 2024. In-field disease symptom detection and localisation using explainable deep learning: Use case for downy mildew in grapevine. Computers and Electronics in Agriculture 226:109478
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Spain (La Rioja)]
processes: [symptom detection, image classification, disease localisation, field monitoring]
records: []
datasets: []
files: [hernandez2024-infielddiseasesymptomd.pdf]
---

# Hernández et al. 2024: explainable CNN localises downy mildew in vines

A light read (the deep-research B list).

## What it holds

- Images from 14 commercial vineyard plots in the field, taken statically and on the go (l. 37, 37).
- A sliding-window classifier compares CNNs and vision transformers, with transfer learning and augmentation (l. 38, 39).
- The best model, EfficientNetV2S, reached 91% accuracy and F1 0.92 on image areas (l. 43).
- Symptomatic areas were located with an IoU of 0.83, and predictions were explained with XAI (l. 44, 42).

## Dependence

- verdict: none; text: No engine model is named, computed, borrowed or fitted. This is an image classifier, not an infection or weather model; no shared-author flag.

## Bearing (2026-10-10)

- Offers a field scouting observation method (symptom images classified with 91% accuracy) that a truth could use as an observation source, not an infection model.

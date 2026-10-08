---
id: peddicord2025
citation: Peddicord, Layton, Xavier, Alencar, Cryer, Steven, Barr, Jeremiah & van der Heijden, Gerie. 2025. Scalable Prediction of Northern Corn Leaf Blight and Gray Leaf Spot Diseases to Predict Fungicide Spray Timing in Corn. Agronomy 15 (2):328
doi: 10.3390/agronomy15020328
read: 2026-10-08, the first pages and abstract, by a triage agent (claude-sonnet-5-5); header checked by the main session
status: read
diseases: [northern leaf blight, gray leaf spot]
crops: [corn]
regions: [US Midwest]
processes: [risk prediction]
records: []
datasets: []
files: [10-3390-agronomy15020328.pdf]
---

# Peddicord et al. 2025: corn leaf disease prediction

Research article, US Midwest (trial sites in Iowa and Illinois, among others).

## What it holds

- A Corteva system that predicts northern leaf blight and gray leaf spot in corn from hourly weather, soil and genetic-tolerance data and times fungicide sprays, using machine learning, with 150+ on-farm trials 2020-2023.
- Its methods section uses an hourly leaf wetness decision tree (taken from Kim et al., drawn only as a figure, so the text holds no equations) and a disease-unit rule for NLB (DU = 0 if LWD < 6 h, DU = LWD/6 if LWD ≥ 6 h, with RH ≥ 90% and 17 < T < 27 °C).
- Corn diseases only; no grapevine content.

## Dependence

- No formulation of its own that a tool could run.
- No author of a model the engine runs.

## Bearing (2026-10-08)

- Uses a CART-style wetness tree (after Kim et al.) and RH >= 90% disease units: corn only.

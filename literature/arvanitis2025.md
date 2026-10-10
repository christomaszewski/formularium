---
id: arvanitis2025
citation: Arvanitis, Nikolaos, Graziosi, Filippo, Athanasiou, Gina, Terpou, Antonia, Arvaniti, Olga & Zahariadis, Theodore. 2025. Utilizing TabPFN transformer with IoT environmental data for early prediction of grapevine diseases. AgriEngineering 7:173
doi: 10.3390/agriengineering7060173
read: 2026-10-10, methods and results (LIGHT), by a reading agent (claude-haiku-5-5); 30 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Emilia-Romagna]
processes: [forecasting]
records: []
datasets: []
files: [q317.pdf]
---

# Arvanitis et al. 2025: a tabular transformer on one vineyard's weather and spray log

## What it holds

- One 7 ha vineyard at Tebano (Faenza), daily IoT weather 2020-May 2024.
- **Labels:** the farm's fungicide applications, taken as proxies for disease; not observed
  symptoms.
- TabPFN reaches accuracy 0.967 for downy mildew on 326 test days; how the test set was
  split is described two ways.

## Dependence

- None.

## Bearing (2026-10-10)

- None: it learns when the grower sprayed. Recorded so that it is not read again.

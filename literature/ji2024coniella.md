---
id: ji2024coniella
citation: Ji, Tao, Languasco, Luca, Li, Ming & Rossi, Vittorio. 2024. Temperature-dependent sporulation of the fungus Coniella diplodiella, the causal agent of white rot of grapes. Plant Disease 108(7):1987-1992
doi: 10.1094/PDIS-11-23-2439-RE
read: 2026-10-10, in full, equations in the page images, by a reading agent (claude-haiku-5-5); 59 quotes checked by scripts/verify_quotes.py
status: read
diseases: [white rot]
crops: [grapevine]
regions: [Emilia-Romagna]
processes: [latency, sporulation]
records: [magarey2005.generic]
datasets: []
files: [cn_it_coniella_sporulation_2023.pdf]
---

# Ji et al. 2024: white rot latency and sporulation by temperature

## What it holds

- Latency to the first pycnidium: LP = LPmin / f(T), Magarey et al. 2005's f(T); LPmin 155
  h, Tmin 6, Topt 32, Tmax 45 °C; R² 0.83.
- Sporulation: a Duthie-type bell in temperature (Topt 18.2 °C) times 1 - exp(-(φt)^ψ);
  R² 0.92; 22 million conidia per berry at 20 °C by day 62.

## Dependence

- Computes `magarey2005.generic`'s temperature response for latency.

## Bearing (2026-10-10)

- For Cooptera, if it adds white rot.

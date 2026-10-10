---
id: ji2021coniella
citation: Ji, Tao, Languasco, Luca, Li, Ming & Rossi, Vittorio. 2021. Effects of temperature and wetness duration on infection by Coniella diplodiella, the fungus causing white rot of grape berries. Plants 10:1696
doi: 10.3390/plants10081696
read: 2026-10-10, in full, equations in the page images, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py
status: read
diseases: [white rot]
crops: [grapevine]
regions: [Emilia-Romagna]
processes: [infection, incubation]
records: [magarey2005.generic]
datasets: []
files: [cn_it_coniella_infection_2021.pdf]
---

# Ji et al. 2021: white rot (Coniella) infection by temperature and wetness

## What it holds

- Detached Chardonnay and Ortrugo berries, 10-35 °C, 1-24 h of wetness, three pathways.
- Infection: Y = (a Teq^b (1 - Teq))^c (1 - exp(-(m WD)^n)), Tmin 5, Tmax 40 °C; a 5.067,
  b 1.162, c 0.350, m 0.468, n 0.363; R² 0.93. Optimum 23.8 °C; 1 h of wetness suffices.
- Incubation: IP50 = IP50min / f(T) with Magarey et al. 2005's f(T): 16 h minimum on
  injured berries (Topt 30 °C), 101 h on uninjured.
- Equation 5 is printed inverted against its definition.

## Dependence

- Computes Magarey et al. 2005's temperature response (`magarey2005.generic`) for
  incubation. Rossi is an engine author: a flag.

## Bearing (2026-10-10)

- For Cooptera, if it adds white rot.

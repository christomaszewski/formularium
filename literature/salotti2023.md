---
id: salotti2023
citation: Salotti, Irene, Liang, Yu-Jie, Ji, Tao & Rossi, Vittorio. 2023. Development of a model for Colletotrichum diseases with calibration for phylogenetic clades on different host plants. Frontiers in Plant Science 14:1069092
doi: 10.3389/fpls.2023.1069092
read: 2026-10-10, in full, equations in the page images, by a reading agent (claude-haiku-5-5); 59 quotes checked by scripts/verify_quotes.py
status: read
diseases: [anthracnose, ripe rot]
crops: [grapevine]
regions: [Italy, United States, Canada, Japan]
processes: [infection, sporulation, dispersal, incubation, latency]
records: [magarey2005.generic]
datasets: []
files: [q062.pdf]
---

# Salotti et al. 2023: a Colletotrichum model calibrated by clade

## What it holds

- Hourly: sporulation k f(T) f'(WD), f(T) the Analytis beta form; wetness exp(-5.947
  exp(-0.067 WD)); rain-splash dispersal; infection by clade; incubation and latency by
  Magarey et al. 2005's function (acutatum IPmin 118.3 h, Topt 24.2 °C).
- Seven clades and C. coccodes, parameters per clade (Tables 3-4).
- 17 epidemics 1980-2019 on several hosts: CCC 0.928, RMSE 0.044.

## Dependence

- Computes `magarey2005.generic`'s temperature response for incubation and latency.

## Bearing (2026-10-10)

- For Cooptera, if it adds anthracnose or ripe rot.

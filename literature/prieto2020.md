---
id: prieto2020
citation: Prieto, J. A., Louarn, G., Perez Peña, J., Ojeda, H., Simonneau, T. & Lebon, E. 2020. A functional-structural plant model that simulates whole-canopy gas exchange of grapevine plants (Vitis vinifera L.) under different training systems. Annals of Botany 126(4):647-660
doi: 10.1093/aob/mcz203
read: 2026-10-28, the light-interception sections and the site and system description only (the gas-exchange parts were not read); by a reading agent and note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [light interception, 3D reconstruction, radiosity, training system, leaf gas exchange]
records: []
datasets: []
files: [dr1028_prieto2020.pdf (the 2026-10-28 requests drop; PMC7489073 author manuscript)]
---

# Prieto et al. 2020: whole-canopy gas exchange of vines, with light from a 3D radiosity model

A functional-structural model; only its light step matters here. It prints no light equation: light is a call to CARIBU on a 3D mock-up.

## What it holds

- **Site and systems** (l. 118-128): Syrah on SO4 at Montpellier (43°37' N, 3°52' E), planted 2000, rows NW-SE at 140° from north (l. 120-121); a free low single-wire system (LSW) and three VSP systems: 3.6 m between rows (VSPl), 1.8 m (VSPh) and VSPh trimmed at 1.2 m (VSPhs), vines 1.0 m apart (l. 126; Table 1 gives foliage heights, not read).
- **Light model** (l. 270-282): the 3D canopy of the digitised plant is copied into three rows of three plants; CARIBU (nested radiosity, Chelle & Andrieu 1998) gives direct light and scattered light on each leaf; diffuse sky in 46 turtle zones under a standard overcast sky; first checked against Monte Carlo ray tracing (Chelle & Andrieu 1998).
- **Check** (l. 336-343): simulated against measured daily fraction of intercepted light (hemispherical photographs, Louarn et al. 2008b), RMSE 4 %, about 2 mol/m²/d.

## Dependence

- Light: CARIBU (Chelle & Andrieu 1998), not printed here. Canopy: TOPVINE of `louarn2008`; shares authors (Louarn, Lebon) with `louarn2008` and `louarn2007`: a flag only. The 3D mock-ups and the photographs are the same group's data.

## Bearing (2026-10-28)

- Not buildable from print: no equation, no leaf-angle or LAD numbers in the pages read, light needs the digitised plants. Useful as a check value (RMSE 4 % of the intercepted fraction for a good 3D model) and for the system dimensions.

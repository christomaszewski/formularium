---
id: brischetto2021
citation: Brischetto, C., Bove, F., Fedele, G. & Rossi, V. 2021. A weather-driven model for predicting infections of grapevines by sporangia of Plasmopara viticola. Frontiers in Plant Science 12:636607
doi: 10.3389/fpls.2021.636607
read: 2026-10-07, the author line and Figure 2's caption; open access
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy]
processes: [sporulation, survival, dispersal, secondary infection]
records: [brischetto2021.secondary]
datasets: [blaeser1979, caffi2016]
files: []
---

# Brischetto et al. 2021: secondary infections by sporangia

## What it holds

- Authors: Chiara Brischetto, Federica Bove, Giorgia Fedele, Vittorio Rossi (Università
  Cattolica, Piacenza; Horta Srl).
- **Figure 2's caption names each piece's source:**
  - (A) sporulation: Lalancette et al. 1988a's model, rescaled by its number at 20 °C and
    24 h of wetness;
  - (B, C) survival of attached and detached sporangia: Brischetto et al. 2020 (vapour
    pressure deficit);
  - (D) minimal infection requirements: Magarey et al. 2005's model, with parameters
    estimated from Blaeser & Weltzien 1979 and Caffi et al. 2016 (R² 0.87): Wmin 2 h;
    Tmin 4.0, Topt 21.0, Tmax 30.2 °C;
  - (E) infection rate: Caffi et al. 2016.

## Dependence

- Computes Magarey 2005's equation, Caffi's sporulation conditions and Lalancette's bound
  (Cooptera's port: `magarey2005.generic`, `caffi2013.sporulation`,
  `lalancette1988.sporulation_bounds`).
- Calibrated on Blaeser & Weltzien 1979 and Caffi et al. 2016 (`calibrated_on`).

## Bearing (2026-10-07)

- An engine model; part of Agrarium's development family F1. Its Magarey parameters are in
  the catalogue as read values.

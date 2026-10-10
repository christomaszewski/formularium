---
id: monteiro2012
citation: Monteiro, José Eduardo B. A., Czermainski, Ana Beatriz C., Cavalcanti, Fábio R. & Evangelista, Sílvio R. M. 2012 (year not printed in the text). Esporulação e eficiência de infecção do míldio da videira em cenários de mudanças climáticas. Embrapa (series T027, per the file)
doi: 
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5), equations 1-3 in the page image; 56 quotes checked by scripts/verify_quotes.py; the coefficients compared with lalancette1988.infection by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Rio Grande do Sul]
processes: [infection, sporulation, climate change, leaf wetness]
records: [lalancette1988.infection]
datasets: []
files: [embrapa_monteiro_2012_T027_clima_favorabilidade.pdf]
---

# Monteiro et al. 2012: Lalancette's infection and sporulation under PRECIS scenarios

## What it holds

- **Base data:** ten years of daily records, 1976-1985, at Embrapa Uva e Vinho (Bento
  Gonçalves), September-December, 1,220 days. Futures for 2020-2050 under SRES A2 and B2
  add monthly PRECIS temperature deltas, with wetness held fixed.
- **Equations as printed:**
  - EI as in [monteiro2015](monteiro2015.md), intercept -0.061;
  - S = (-868164 + 114369T - 2828T²) x (1 + e^[(-8.96 + 1.16T - 0.029T²) + H(1.51 - 0.2T +
    0.0049T²)])², from Lalancette's sporulation paper, scaled 1.0 = 2.88 x 10^5 sporangia/cm²;
  - TI = EI x S.
  - H, hours of RH at or above 90 %, is set equal to wetness duration.
- **Wetness:** DPM = -27.61 + 0.533 RH - 1.089 wind - 0.087 Tmin, fitted to 730 hourly days
  (R² 0.72); the source of the hourly data is not named.
- **Results (2050 against 1976-85):** EI -3.4 % and S +8.6 % under B2; EI -3.0 % and S
  +12.2 % under A2. High-EI days 48.9 % against 46.3 %.
- **No validation.**

## Dependence

- Copies Lalancette's infection and sporulation models.
- Uses the RH >= 90 % rule as wetness for sporulation, the form of the engine's
  `cooptera.rh90_wetness` (`rh-threshold-wetness`).

## Bearing (2026-10-09)

- Model output only; context for climate-change work.

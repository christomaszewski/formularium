---
id: rodrigues2026
citation: Rodrigues, Vagner Weide. 2026. Modelos matemáticos para a evolução e o controle do míldio em vinhedos. Tese de doutorado, Programa de Pós-Graduação em Matemática Aplicada, Universidade Federal do Rio Grande do Sul (UFRGS), Porto Alegre. 183 pp. Advisor: Varriale
doi: 
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 82 quotes checked by scripts/verify_quotes.py; dependence judged by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Rio Grande do Sul]
processes: [infection, latency, spread, spray timing, biological control]
records: []
datasets: []
files: [modelos-matematicos-mildio-2026.pdf]
---

# Rodrigues 2026: compartment and lattice models of downy mildew, with no field data

A thesis in applied mathematics. Read in full where it states the model, its parameters
and its results; the rest by extraction.

## What it holds

- **Local model:** S, E, I, R and leaf area M, with short- and long-range sporangia (U, V);
  Holling type II infection; Gompertz leaf growth.
- **Parameters (Table 3.4):**
  - alpha 2,000, theta 0.8 and delta 50 per day from Mammeri et al. 2014 and Burie et al.
    2008, both powdery mildew;
  - latency 10 days and infectious period 7 days from Caffi et al. 2013;
  - K = 10 m² (pergola) and 5 m² (vertical trellis), cited to Appendix A, which does not
    give them;
  - beta, phi, eta, mu and xi assumed.
- **Weather:** Velasquez-Camacho et al. 2023's thresholds (6-26 °C, rain above 10 mm, RH
  above 90 %, wind above 9 m/s) are quoted and then left out of the model. No oospores; one
  initial focus.
- **Results:** R0 5.74 (pergola), 2.86 (trellis); endemic severity about 80 % and 63 %.
  Spray and Bacillus schedules compared by AACPD (Embrapa's recommended intervals and
  efficacies).
- **Printed slips:** two severity definitions (with and without the protected class); one
  20-day half-life giving decay rates of 0.035 and 0.001 per day; delta's unit.

## Dependence

- No engine model is computed. Caffi et al. 2013's latent and infectious durations are used;
  the engine's piece from that paper is its sporulation rule (`caffi2013.sporulation`),
  which the thesis does not use.

## Bearing (2026-10-09)

- Not usable as a truth: its biology is powdery mildew's, and nothing is fitted to downy
  mildew data.

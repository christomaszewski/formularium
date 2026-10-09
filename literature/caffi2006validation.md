---
id: caffi2006validation
citation: Caffi, T., Rossi, V., Bugiani, R., Spanna, F., Flamini, L., Cossu, A. & Nigro, C. 2006. Validation of a simulation model for Plasmopara viticola primary infections in different vine-growing areas across Italy. Proceedings of the Fifth International Workshop on Grapevine Downy and Powdery Mildew, San Michele all'Adige, Italy, 2006 (eds not printed; preface by C. Gessler and I. Pertot)
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5); every quote checked at its line by verify_quotes.py, key numbers checked by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Emilia-Romagna, Piedmont, Sardinia, Basilicata, Italy]
processes: [primary infection, validation]
records: [rossi2008.primary]
datasets: []
files: [PDMildew_Proceedings_ALL.pdf]
---

# Caffi et al. 2006: Rossi's primary-infection model in 77 vineyards

## What it holds

- 77 commercial vineyards in five Italian regions, 1995-2005: 736 runs; all 122 observed
  infections were simulated; every error was a false alarm (71 runs, 9.6 %); χ² 411.4 with
  Yates's correction (P < 0.001).
- By region: Emilia-Romagna 93 % accurate; Piedmont 153 simulations, 4 % overestimated;
  Basilicata 34 simulations, 91 % right; Sardinia, one vineyard over six years, 54
  simulations, 19 false alarms (35 %).
- The 'three tens' rule, in use for warnings, is called often unreliable; the authors
  suggest ignoring infections before the host is susceptible.

## Dependence

- Scores the engine's model; its authors are the model's.

## Bearing (2026-10-09)

- Validates the engine's `rossi2008.primary` on Italian data. Agrarium: these vineyards are
  scored with the model the engine runs; a truth matched to them would share their data
  (whether onsets were dated with Rossi's incubation is not said here).

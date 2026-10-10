---
id: salotti2026
citation: Salotti, Irene, Camardo Leggieri, Marco & Battilani, Paola. 2026. ALT-tomato: a process-based model for Alternaria disease complex addressing mycotoxin risk. Frontiers in Plant Science 17:1794763
doi: 10.3389/fpls.2026.1794763
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [alternaria disease complex, alternaria leaf spot, mycotoxin contamination]
crops: [tomato]
regions: [Italy, India, Canada, Foggia Italy]
processes: [infection, sporulation, wetness duration, relative humidity, temperature response, mycotoxin production, season severity, dispersal]
records: []
datasets: []
files: [q058.pdf]
---

# Salotti et al. 2026: process-based Alternaria model for tomato mycotoxin risk

A light read (the deep-research B list).

## What it holds

- ALT-tomato: a process model of Alternaria on tomato, covering conidia production, dispersal, infection, symptom development and toxin accumulation (l. 47-57).
- Three species parameterised: A. alternata, A. solani and A. tenuissima (l. 58).
- Validation on eight epidemics in Italy, India and Canada: CCC 0.98, RMSE 0.069 (l. 61-64).
- Drivers: T (°C), RH (%), wetness duration (h); infection needs T 5-35 °C and WD of at least 3 h; sporulation needs RH of at least 65 % (l. 173-197).
- Infection rate Rc = RcOPT x RcT x RcWD; RcOPT from Sun & Zeng 1994, modifiers from Loomis & Adams 1983 (l. 414-423).
- Flag: the cited Magarey 2005 and Rossi 2008 are named for simplification only (l. 756).

## Dependence

- Flag only, none computed. The text cites Magarey et al. 2005 and Rossi et al. 2008 (l. 756) for the idea that simpler population structure does not hurt robustness; it does not state that it borrows their equations. The infection rate Rc = RcOPT x RcT x RcWD (eq. 8, l. 421) multiplies a temperature modifier and a wetness-duration modifier, a form of the same kind as Magarey et al. 2005's generic infection response, which the brief lists as an engine model. RcT and RcWD are Alternaria-specific and drawn from Loomis & Adams 1983 and Sun & Zeng 1994, so the shared form is not established. Recommend a check of eq. 8-9 against Magarey 2005 before any kinship call. The RH >= 65 % sporulation rule and the 3 h wetness threshold are not the engine's RH >= 90 % stand-in.

## Bearing (2026-10-10)

- A tomato Alternaria process model with a temperature-times-wetness infection rate, of the form the brief lists for Magarey 2005, so a kinship check of eq. 8-9 is needed before any use; for the truth it offers the Alternaria mycotoxin side only as a flag.

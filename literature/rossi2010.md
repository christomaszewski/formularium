---
id: rossi2010
citation: Rossi, Vittorio, Caffi, Tito & Legler, Sara E. 2010. Dynamics of Ascospore Maturation and Discharge in Erysiphe necator, the Causal Agent of Grape Powdery Mildew. Phytopathology 100 (12):1321-1329
doi: 10.1094/PHYTO-05-10-0149
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Piacenza]
processes: [ascospore maturation, ascospore release]
records: []
datasets: []
files: [10-1094-phyto-05-10-0149.pdf]
---

# Rossi, Caffi & Legler 2010: ascospore maturation and discharge in Erysiphe necator

From the Università Cattolica (Piacenza).

## What it holds

- Chasmothecia were collected in unsprayed plots in northern Italy from mid-August to leaf fall, 2005-2008, and split into 3-5 cohorts a year (l. 78, 119). Cohorts overwintered outdoors at the University of Piacenza vineyard, with a weather station 2 m away (l. 72, 83).
- Before leaf fall 34% of chasmothecia held mature ascospores, 48% immature, 18% empty (l. 161, 163). 11% and 5% held mature ascospores between leaf fall and bud break, and after bud break (l. 19); the later group discharged ≈42% of ascospores (l. 378).
- Ascospores were trapped in 53 of 147 weekly periods (l. 217, 251). Most came with >2 mm rain (l. 31).
- Maturity model: y = 100 exp[-a exp(-b x)], x = degree-days base 10 C from bud break (l. 165, 166); a 1.95, b 1.91, R2 0.92 (l. 187); 90% mature at 153 DD, CI 100-210 (l. 29).
- Base 0 and 5 C and day counts fitted worse (l. 214). The fit uses the 2006-2008 springs (l. 271). The text prints x = DD; 153 DD only fits if x = DD/100.
- No earlier model dated the data. Not tested on independent data (l. 394).

## Dependence

- Its own chasmothecia counts (2005-2008); bud break observed. Maturity is a Gompertz in degree-days above 10 °C after bud break; the paper prints x = DD, though its a = 1.95 and b = 1.91 give 90% at 153 degree-days only if x is DD/100 (the reading agent's check).
- Rossi and Caffi: flags.

## Bearing (2026-10-08)

- A flag, not kin: no engine model computes it. A degree-day maturation of ascospores is not one of the engine's tagged forms (its ascospore rule is Thiessen's release rule). The authors say it is unconfirmed on independent data (l. 394).

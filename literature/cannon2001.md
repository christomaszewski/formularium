---
id: cannon2001
citation: Cannon, R.M. 2001. Sense and sensitivity - designing surveys based on an imperfect test (the text prints the dash as 'Ð'). Preventive Veterinary Medicine 49:141-163
doi:
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [Australia]
processes: [sampling, detection, observation]
records: [cannon2001.sensitivity]
datasets: []
files: [1-s2.0-S0167587701001842-main.pdf]
---

# Cannon 2001: designing surveys with an imperfect test

From Australia's Office of the Chief Veterinary Officer. The source of the engine's `cannon2001.sensitivity`.

## What it holds

- A theory paper on survey design with an imperfect test. No data are collected or fitted (l. 18).
- Sensitivity a (alpha) and specificity b (beta) are separate; lack of specificity is the harder problem (l. 57).
- With perfect specificity, the exact chance of no reactor is a sum over the number of diseased animals in the sample (Eq. 4.1, l. 497-505).
- Infinite population, perfect test: n = ln(1 - g) / ln(1 - p) (Eq. 4.5, l. 544-548).
- Infinite population, sensitivity a: n >= ln(1 - g) / ln(1 - a p), as in MacDiarmid (1987) (Eq. 4.6, l. 557-560). It overestimates for small herds (l. 562).
- Finite population, best form: n = [1 - (1 - g)^(1/D)] [N - (1/2)(aD - 1)] / a (Eq. 4.11, l. 618-622); error under 1 sample except at extremes.
- Area surveys chain the formulas: animal level, herd level a_h, survey level a_s = 1 - (1 - a_h p_h)^(n_h) (l. 663-733).
- Example from Garner et al. (1997): 163 herds, 5 animals each, no reactors, a = 100%: upper 95% limit for animal prevalence 0.37% (l. 736-740).
- Combining evidence: x = (g - a)/(1 - a) = 0.99 for g = 99.99%, a = 99% (l. 788).
- With false positives, tolerance t must rise as n rises (Sec. 5); decide on the maximum within-herd reactor proportion, not on the count of positive herds (l. 28, 982-998).

## Dependence

- The engine's own piece (eq. 4.6). Cannon calls it MacDiarmid 1987's formula with n and D interchanged (l. 560).

## Bearing (2026-10-08)

- The engine's observation piece, confirmed. A truth's scouts must not compute eq. 4.6 (D26); EFSA 2020's survey formula is the same form ([efsa2020](efsa2020.md)).

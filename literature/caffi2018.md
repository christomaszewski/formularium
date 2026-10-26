---
id: caffi2018
citation: Caffi, T. & Rossi, V. 2018. Fungicide models are key components of multiple modelling approaches for decision-making in crop protection. Phytopathologia Mediterranea 57(1):153-169
doi: 10.14601/Phytopathol_Mediterr-22471
read: 2026-10-25, lightly: the model sections (residue dynamics, the Arneson model, the Caffi and Rossi copper model, the fuzzy system, crop-adapted spraying) and the reference list; Figures 2 to 6 not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, apple scab]
crops: [grapevine, apple]
regions: [Italy, Castell'Arquato]
processes: [fungicide, residue decay, wash-off, growth dilution, protection period, efficacy model, copper, decision support, vite.net]
records: []
datasets: []
files: [dr1025_caffi2018.pdf (the 2026-10-25 drop)]
---

# Caffi & Rossi 2018: a review of fungicide residue and efficacy models, with the copper model for grapevine downy mildew used in vite.net

An open-access review that prints the structure Cooptera's E6 needs (first-order decay, rain wash-off and growth dilution of a fungicide deposit, then an efficacy curve) and gives copper parameters for grapevine.

**Read this first.**
- **Sign of beta.** Equation [6] is EF = EF0 / (1 + alpha exp(beta (t + ...))) with beta printed as -0.984 and -0.994 (l. 508, 502). With beta negative the exponential falls, so EF rises to EF0 and nothing declines. A decline needs beta positive. With beta = +0.984, alpha = 0.00005 and no rain or growth, EF is 0.95 at 7 d, 0.52 at 10 d and 0.13 at 12 d (arithmetic by the reading agent, rechecked by the note writer, not printed). The sign is quoted as printed; it needs Caffi et al. 2016 or the vite.net code.
- **Units of the growth term.** (Bt - B0)/B has no unit, while t and the rain term (sum of Rain x P/R) are in days. As printed, three new leaves (B) add 1 equivalent day, not P = 7 d. Whether a factor P is missing is not stated.
- **Copper parameters are cited, not obtained.** R = 10, 30, 40 mm and B = three leaves come from Kuflik et al. 2009, which was not obtained (l. 511, 514). The alpha and beta fits are the authors' own but unpublished (potted Barbera); the Arneson values (K, a) are apple-scab defaults for teaching, not vine data.
- Two-column layout; Figures 2 to 6 are images and were not read.

## What it holds

- **Frame:** rain is among the main factors that reduce the persistence of a deposit (l. 205); growth of the plant creates unprotected areas in a protectant's coating (l. 209, citing Lukens 1971); wash-off depends on the product, with Cabras et al. 2001 among the works cited (l. 249); drying and absorption time before rain can matter, "less than 0.5 or up to 8.0 h" depending on the product (l. 279, cited).
- **Arneson et al. 2002, an apple-scab teaching model (cited; Eqs. [1] to [4]):** decay C1t = C0 exp(-K t), t in days [1] (l. 326), with defaults K = 0.10 for protectants, 0.07 locally systemic, 0.06 to 0.05 systemic (l. 334), which leave half the residue after about 7, 10, 12 and 14 d (l. 338). Wash-off C2t = exp(-a ct sqrt(Rt)) [2] (l. 384), Rt daily rain in mm, with ct = exp[(C(t-1) - 1) x 3] [3] (l. 419), so removal gets harder as residue falls. Default a = 0.25 halves the residue at 10 mm and a = 0.12 at 40 mm (l. 392, 393). The wash-off equation applies to protectants only; a penetrant is not washed once absorbed, by default 70 % in the first 24 h and 15 % on each of days 2 and 3 (l. 394). Growth dilution C3t = 1/(Bt/B0) if Bt is at least B0, otherwise 1 [4] (l. 430).
- **Eq. [6] (Rossi, Caffi & Salinari 2012, cited as unpublished here):** EFt = EF0 / (1 + alpha x exp(beta x (t + sum(Rain) x P/R + (Bt - B0)/B))) (l. 449). Time, cumulative rain and biomass growth enter additively as equivalent days. R is the rain that removes all efficacy, P the persistence in days without rain, B the growth that removes all efficacy.
- **Copper fits (own, unpublished, potted Barbera):** pre-inoculation activity, sprays 12, 9, 6, 3 or 1 d before inoculation: EF0 = 1, alpha = 0.00005 (l. 507), beta = -0.984, R² = 0.986 (l. 508). Post-inoculation activity: EF0 = 1, alpha = 0.005, beta = -0.994, R² = 0.965 (l. 502); the unit of t is not stated (hours presumed).
- **Settings, not fits:** P = 7 d "based on commonly accepted technical knowledge" (l. 510); R = 10, 30 or 40 mm for copper at 30, 50 or 70 g Cu²⁺/hL, cited from Kuflik et al. 2009 (l. 511); B = three leaves, cited from Kuflik et al. 2009 (l. 514).
- **Field use:** in the fuzzy decision system a spray 1 to 2 d earlier that left 60 to 75 % protection was why experts held off treating on 21 of 2,754 days (l. 579). The leaf area to be treated rises from nearly zero at budburst to over 23,000 m² per ha at fruit set, cited from Siegfried et al. 2007 (l. 624).

## Dependence

- **Borrows:** Eqs. [1] to [5] from Arneson, Oren, Loria, Jenkins, Goodman & Cooper 2002 (apple scab model description); wash-off after Burchfield & Goenaga 1957 and Cohen & Steinmetz 1986; biomass dilution after Lukens 1971; Eq. [6] from Rossi, Caffi & Salinari 2012; R and B from Kuflik et al. 2009; the copper alpha and beta from Caffi et al., unpublished, and Caffi et al. 2016.
- **Authors:** Rossi and Caffi are authors of the engine's Rossi-family models: a flag only, not a dependence. `taibi2022` feeds its folpet rain curve into this model.

## Bearing (2026-10-25)

- **Structure for E6 (treat, protect, reassess):** decay, wash-off and growth dilution as separate multipliers, then an efficacy curve with equivalent days. Kind of result: a review and model (a published structure), with copper parameters that are cited or unpublished fits on potted vines. Do not code Eq. [6] until the sign and the units are settled.
- **Wash-off per mm:** Arneson's a = 0.25 and 0.12 are apple-scab defaults for protectants (analogue, no vine data). For vine copper the paper gives only R = 10 to 40 mm by dose, cited.
- **Decay with time and dilution by growth:** K = 0.10 per day for protectants is an apple default; for copper on vines, P = 7 d is an assumption and B = three leaves is cited. **Dose-efficacy:** R rises with dose (30, 50, 70 g Cu²⁺/hL give 10, 30, 40 mm), cited; no efficacy against deposit per area. Deposit variability through a canopy is not addressed.

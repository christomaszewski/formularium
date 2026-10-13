---
id: madden1999
citation: Madden, L. V. & Hughes, G. 1999. Sampling for plant disease incidence. Phytopathology 89(11):1088-1103
doi: 10.1094/PHYTO.1999.89.11.1088
read: 2026-10-12, in full but for the appendix, by a reading agent (claude-haiku-5-5); 54 of 54 quotes found at their lines by scripts/verify_quotes.py; eqs 12-13 and the Fig. 6 examples checked in the page image and recomputed by the main session; held since 2026-10-07 as the engine's sampling source and read then by Agrarium without a note
status: read
diseases: [downy mildew, eutypa dieback]
crops: [grapevine]
regions: [Ohio, California]
processes: [sampling, detection, spatial heterogeneity, incidence]
records: [madden1999.detection_bound]
datasets: [madden1995]
files: [1999-madden-10-1094-phyto-1999-89-11-1088.pdf]
---

# Madden & Hughes 1999: sampling for disease incidence, with the grape downy mildew data

A symposium paper on sampling theory for incidence (binomial, beta-binomial, the binary
power law, sequential plans), the source of the engine's detection bound
(`madden1999.detection_bound`, eqs 12-13) and of the 0.07 intracluster correlation the
catalogue takes for the Ohio downy mildew data (`madden1995`). Held since 2026-10-07;
this is its note.

## What it holds

- **Estimators:** incidence p̂ = ΣX/(nN) (eq. 1, l. 83-86); binomial standard error (eq.
  2, l. 101-103); beta-binomial variance with θ or ρ = θ/(1 + θ) (eqs 3a-d, l. 164,
  179-194); moment estimate of ρ from the sample variance (eqs 4-5, l. 161-175).
- **The detection bound** (read in the page image, p. 1093): when every sampled individual
  is disease free, the one-sided upper bound on incidence at significance P is p ≈
  −θ log(P) / (N log(1 + nθ)) for beta-binomial data (eq. 12) and p = 1 − P^(1/(nN)) for
  binomial data (eq. 13) (l. 405-412). Examples with n = 10, P = 0.05: N = 5 gives 0.058
  (binomial) and 0.086 (θ = 0.1); N = 20 gives 0.015 (binomial) and, as printed, 0.052
  for θ = 0.1 (l. 417-420). Recomputed: 0.0582, 0.0864, 0.0149 agree, but eq. 12 at
  N = 20, θ = 0.1 gives 0.0216, and Fig. 6B's beta-binomial curve reads about 0.02 at
  N = 20, so the printed 0.052 is a misprint, not the equation. Sample sizes for a bound of
  0.08: about 4 units (binomial) or 6 (θ = 0.1); for 0.005, about 60 or 86 (l. 538-541).
- **The grape downy mildew data** (Fig. 3, l. 208-214): Madden, Hughes & Ellis 1995's
  Ohio incidence, 3 years × 2 sampling times × 18 plots = 108 plot-dates, N = 15 shoots of
  about 15 leaves; binary power law fit A = 8.5, b = 1.3, R² = 0.90 (l. 214, 283, 818);
  the mean of the 108 moment estimates of ρ is 0.07 (l. 257, 284), which the paper uses
  only to illustrate a case, since b > 1 makes ρ vary with p (l. 258-261; ρ = 0.06 at
  p̂ = 0.10 from the fit, l. 853; predicted ρ below 0 under p = 0.012 or above 0.988,
  l. 265). The vineyards, years and location are not printed here.
- **Examples:** p̂ = 0.20, ρ = 0.07, n = N = 15 gives se 0.0375 (l. 355); N = 5, p̂ = 0.053
  gives the exact interval (0.007, 0.164) (l. 323-324), where the printed normal se 0.0354
  recomputes as 0.0364 from eq. 6a.
- **Eutypa dieback** (Fig. 1, l. 111-113, 178): 256 quadrats of 9 vines, p̂ = 0.28, ρ̂ =
  0.082 (the Fig. 9 caption says 0.05 for the same data, l. 732); a bootstrapped
  sequential plan on 22 data sets (Madden, Hughes & Munkvold 1996) stopped at 11 units on
  average (range 2-18) against a predicted 11.8 (l. 627-635).
- **SPRT on the grape fit** (A = 8.5, b = 1.3, n = 15): p̂ = 0.017 accepts p0 = 0.05, p̂ =
  0.23 accepts p1 = 0.15 (l. 818-828). The appendix (l. 1021-1065) was not read.

## Dependence

- **Its data:** the 1995 Ohio grape downy mildew incidence (`madden1995`) and the Eutypa
  counts of Munkvold, Duthie & Marois 1993, both observed; no model dated them.
- **The engine's piece:** eqs 12-13 are `madden1999.detection_bound`, an observation piece
  (D26) whose ρ comes from these data (`calibrated_on=madden1995`). The 0.07 is the
  paper's demonstration value; the paper's own advice is a ρ that varies with p through
  the binary power law (A = 8.5, b = 1.3).
- **Authors:** Madden wrote `madden2000`, `madden2018`, `madden2024glmm`, `madden2025` and
  the Lalancette papers: flags, and the shared data with `madden2018` (which reuses the
  grape rows).

## Bearing (2026-10-12)

- The catalogue record stands as read: eq. 12 as printed and checked at the paper's own
  N = 5 examples; the N = 20, θ = 0.1 value 0.052 in the text is a misprint (eq. 12 gives
  0.022). The 0.07 of `madden1995` is a mean the paper itself calls illustrative; a truth
  that wants Ohio-like heterogeneity should use the fitted law (A = 8.5, b = 1.3) rather
  than one ρ, as `madden2018` already suggests.

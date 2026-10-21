---
id: berliner1999
citation: Berliner, L.M., Lu, Z.-Q. & Snyder, C. 1999. Statistical Design for Adaptive Weather Observations. Journal of the Atmospheric Sciences 56:2536-2552 (pages from the running heads, l. 1 and 1084; the volume is printed, the issue is not)
doi: 10.1175/1520-0469(1999)056<2536:SDFAWO>2.0.CO;2
read: 2026-10-21, lightly: abstract, introduction, the statistical formulation, the A- and D-optimal approximations, the Lorenz-Emanuel example and the discussion (appendices read in part), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [none (simulated Lorenz 40-variable model)]
processes: [sensor placement, adaptive observation, A-optimal design, forecast error, Kalman update, Lorenz-Emanuel model, re-planning]
records: []
datasets: []
files: [berliner1999.pdf (the 2026-10-21 drop)]
---

# Berliner, Lu & Snyder 1999: choosing an extra observation to cut forecast error, in a 40-variable toy atmosphere

Frames "adaptive observation" as a Bayesian design problem, choosing where to take one extra observation now so that the forecast error at a later time is least, and tests A-optimal site choice on the Lorenz-Emanuel 40-variable model against published rules. No record: a method.

**Read this first.** The DOI is from OpenAlex: the text layer does not print it or the issue number, and the reader could not confirm them. The pages 2536 to 2552 are confirmed only by the running heads (l. 1, 1084). The criteria use linear, Gaussian and plug-in approximations (eqs. 2.22, 3.1 to 3.2; l. 407-410, 778-779), and the test is a simulated toy model with one adaptive observation. Eqs. 2.23 and 3.5 lose sub- and superscripts in the text layer and are recorded as unchecked. Figures 1 to 6 carry their results in figures; only prose numbers are recorded.

## What it holds

- **Criterion** (Eqs. 2.1, 2.4, 2.21, 2.24, l. 124, 143, 268, 279): expected squared forecast error E|X_2 - p(Y)|^2, which splits into the expected trace of the conditional covariance plus a second term; the design minimises the expected value of a function F of the forecast covariance B_2 (A-optimal: its trace, Eq. 2.24, p. 4, l. 279).
- **Update** (Eqs. 2.12 to 2.14, 2.20, l. 190-259): the Gaussian analysis covariance after the new observation is A_1 = B_1 - B_1 K^T (S + K B_1 K^T)^-1 K B_1, and the forecast covariance is B_2 = G A_1 G^T, with G the tangent-linear propagator evaluated at the analysis mean.
- **Single-site rule** (Eqs. 3.2 and 3.5, p. 6, l. 394, 416): under a plug-in approximation the A-optimal site minimises tr(G_0 A_1 G_0^T); the multi-site design is greedy, one site at a time (l. 370-372). The paper says the exact problem is intractable in high dimension (l. 275) and suggests designing on a few functions of the state (l. 297).
- **Test** (l. 629-640, 715): Lorenz-Emanuel model, n = 40 variables, F = 8; sites 21 to 40 observed every 12 h, sites 1 to 20 only intermittently; one ocean site is observed at the adaptive time, with d = 0.3, M = 20 and sigma_1 = sigma_2 = 0.5 (l. 715).
- **Results, two-day forecast** (l. 703-711): case 1, A-optimal saves 19.4 % of predictive MSE over the best-estimation approach (0.618 to 0.498); case 3, 31.4 % over Palmer et al. and only 8.4 % over Lorenz and Emanuel; case 4, 24.5 %.
- **Regret** (l. 719, 729): in case 1, site 7 (A-optimal at one and two days) loses 3.6 % against site 9 at half a day; in case 4, site 17 loses 30.7 % at half a day.

## Dependence

- Builds on optimal experimental design (Fedorov; Pukelsheim; Silvey) and Bayesian design (Chaloner & Verdinelli), and on the Lorenz and Emanuel (1998) model and rule. The comparators are Lorenz & Emanuel 1998 (largest variance of B_1), Palmer et al. 1998 (leading eigenvectors of B_2), Bishop & Toth 1996 and Langland & Rohaly 1996.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): the mid-season re-plan, and decision-focused design.

- **Method:** the target is the later forecast error, not the present field, so the design looks ahead through the model (G) before choosing where to add an observation. That is the shape of a re-plan: given the sensors already reporting, choose the next one for a later quantity. It is greedy and one site at a time.
- **Validation:** simulated truth, four cases, against four published rules; gains of 8.4 to 31.4 % at two days (l. 703-711). No random baseline, no held-out set beyond the forecast times, and no run times.
- **Not shown:** field data, sensor cost, thousands of sites (n = 40), or a non-Gaussian target such as wet hours.

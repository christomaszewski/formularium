---
id: castle2012
citation: Castle, M. D. & Gilligan, C. A. 2012. An epidemiological framework for modelling fungicide dynamics and control. PLoS ONE 7(8):e40941
doi: 10.1371/journal.pone.0040941
read: 2026-10-20, in full, equations and Table 2 in the page images (pp. 2-6), by a reading agent (claude-haiku-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [fungicide protection, protectant decay, epidemic model, spray timing]
records: []
datasets: []
files: [castle_2012.pdf (the 2026-10-20 drop)]
---

# Castle & Gilligan 2012: fungicide protection as a host class

A theory paper: a susceptible-protected-infected host model in which a protectant is
applied at rate pi, lost at rate delta (first order) and lets infection through at a
fraction epsilon, against the usual model that only scales infection down. No data.

## What it holds

- **Explicit model** (Eqs 5-7, non-dimensional 10-12): dS/dt = lambda(S+P)(1 - (S+P+I)) -
  pi S + delta P - S I; dP/dt = pi S - delta P - epsilon P I; dI/dt = I(S + epsilon P) - mu
  I. The implicit model treats every susceptible and scales infection by rho = (delta +
  epsilon pi)/(delta + pi) (l. 234-235).
- **Defaults** (Table 2): lambda 0.5 (l. 351), pi 0.1 (l. 355), delta 0.001 (l. 357), epsilon
  0.1 (l. 358), rho 0.109 (l. 360), kappa 2000 (l. 364), dimensionless and 'chosen primarily
  to highlight the characteristic properties' (l. 268-270); beta, the time unit, is not
  printed.
- **Result:** both models share R0 = rho/mu (Eq. 13, l. 365-376), but only the explicit one
  can hold an endemic state below R0 = 1 (bistability, Eq. 19, l. 396-401, 455-461), for
  highly effective, long-lasting, rarely applied fungicides (l. 453-456). A stochastic
  version keeps it (l. 598-615).
- The citation line prints 7(8): e40941 (l. 21); the page footers print Volume 8 (l. 79).

## Dependence

- None: no data fitted. Its assumptions follow Gilligan's epidemic framework (refs 22-23);
  the parameter ratios are justified from barley and wheat guides (refs 24-27, l. 271-273).

## Bearing (2026-10-20)

- For Cooptera's E6 (treatment protection in the policy) and Agrarium's grower: a
  protected state per host unit, entered at spraying and left at a first-order rate, is
  the minimal structure; treating protection as a scaled infection rate can miss
  outcomes. Rates must come from residue and wash-off data (see ishiguro1992).

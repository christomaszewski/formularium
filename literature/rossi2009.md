---
id: rossi2009
citation: Rossi, V., Giosuè, S. & Caffi, T. 2009. Modelling the dynamics of infections caused by sexual and asexual spores during Plasmopara viticola epidemics. Journal of Plant Pathology 91(3):615-627
doi: 10.4454/jpp.v91i3.553
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 53 of 53 quotes found at their lines by scripts/verify_quotes.py; equations 1-18 and the parameter paragraph read in the page images (pp. 618-619) by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Piacenza, Greece, Switzerland, France, Germany, Italy]
processes: [primary infection, secondary infection, oospore germination, epidemic structure, latent period, carrying capacity]
records: []
datasets: []
files: [rossi2009_jpp.pdf]
---

# Rossi, Giosuè & Caffi 2009: primary against secondary lesions through a season

Fetched 2026-10-12 from a Wayback capture of the journal's old site (the DOI no longer
resolves). The Piacenza group's model of how oosporic (primary) and clonal (secondary)
lesions share an epidemic, tested against the genotype surveys that `gobbin2005`,
`rumbou2004` and `gobbin2006` record. Not an engine model, but it reuses the group's
oospore germination form and sits between `rossi2008` and `brischetto2021`.

## What it holds

- **The model** (eqs 1-18, pp. 618-619, read in the images): Van der Plank's logistic as a
  difference equation with a 1 day step (l. 33). Total lesions y = y' + y'' (eq. 1);
  primary rate dy'/dt = ID'·D'·I'·k (eq. 4) with ID' = q·N' (eq. 5), q = Q·Σ S·G (eq. 6)
  and G = ∫ exp[−a·exp(−b·t)] dt, a Gompertz germination term in day of year (eq. 7);
  secondary rate dy''/dt = ID''·D''·I''·k (eq. 8) with ID'' = y^s·N'' (eq. 9) and
  y^s = y(t−p) − y(t−i−p) (eq. 10); carrying capacity Kmax = LAI·10000/LS (eq. 11), split
  into main and lateral shoots by logistic leaf growth (eqs 12-14); receptive sites
  K_s = ∫(K_t − y_t) over the last "or" days (eq. 15); k = 1 or K_s/(dy/dt) (eqs 16-17);
  dy/dt = dy'/dt + dy''/dt (eq. 18).
- **Values printed** (l. 311-372): Q 100 to 30,000 oospores/m² soil (from T. Caffi's
  unpublished leaf counts); S = 1; N' = 7 zoospores per sporangium (Lalancette et al.
  1987); a = 173.6, b = 0.119 "estimated using a non-linear regression analysis on
  published data" and credited to Rossi et al. 2008a (l. 321-324; see below); infection
  events as Bernoulli trials with probability 0.225 (about seven a month, Blaise & Gessler
  1990); D' ~ N(0.05, 0.025) and I' ~ N(0.1, 0.05), I' above Lalancette 1987's 0.06 for
  V. labrusca (l. 326-337); Pf 0.01-0.40 (D. Gobbin, personal communication); p = 8 and
  i = 15 days (Müller & Sleumer 1934); R 0.1-50 daughter lesions; LAI 2.5, lesion size 9
  cm², so Kmax = 2,778 lesions/m²; km 0.65, kl 0.35, c 4.77, d 0.063, e 6.80, f 0.082
  fitted by the authors to Palliotti et al. 2000's leaf data; or = 30 days (Wermelinger).
- **Evaluation** by "model structural adequacy" (Taper et al. 2008): 500 runs with inputs
  varied within plausible ranges (not printed per parameter, l. 297-301), Q, Pf and R then
  re-estimated from the simulated set (fitted Q 300 to about 32,000 oospores/m², R 4.2 to
  22.6; l. 648-656), and the predicted band compared with the observed primary shares of
  23 vineyards in Greece, Switzerland, France, Germany and Italy, 2000-2002, 6,246
  genotyped lesions (Table 2; the text says 86 samples, the table sums to 85; l. 396-401,
  425). Singletons are primary lesions, repeated genotypes secondary: observed, not
  modelled (l. 46). 13 of 23 epidemics were high-clonality (l. 503). The average
  simulated primary share falls from 1.0 to 0.32 by day 40 and 0.27 by day 80 (l.
  513-518); 89 % (low clonality), 93 % and 96 % of the observed points lie inside the band
  and the absolute differences stay below 0.05 (l. 549-552).
- **The Gompertz parameters:** this paper's a = 173.6, b = 0.119 with t in day of year are
  credited to Rossi et al. 2008a, which in its reference list is the Plant Pathology
  paper (Rossi, Caffi, Bugiani, Spanna & Dellavalle 2008, l. 782); that paper prints a
  Gompertz on hydro-thermal time with a = 15.9 and b = 0.653 (`rossi2008pp`), not these.
  Where 173.6 and 0.119 were fitted is therefore not printed.
- **Garbled or inconsistent:** the 5 % splash sentence is tied to σ = 0.05, which belongs
  to I' (l. 331); eq. [8] is cited for Kmax at l. 364 where eq. [11] is meant; Fig. 5's
  caption and the text give the low-clonality band's curves in opposite order; the 1988
  Lalancette suffixes a and b are the reverse of `rossi2008pp`'s.

## Dependence

- **Computes** the Piacenza group's Gompertz oospore germination form (eq. 7) with
  parameters credited to Rossi et al. 2008 (`rossi2008pp`'s form, other values); takes
  N' and I' from Lalancette et al. 1987 (`lalancette1988infection`'s companion); latent
  and infectious periods from Müller & Sleumer 1934; leaf growth fitted to Palliotti et
  al. 2000. Rossi et al. 2008b (the Ecological Modelling primary model, `rossi2008`) is
  cited, not computed (l. 94). Blaeser & Weltzien 1979 and Lalancette 1988a,b are named as
  the weather equations a fuller model would use for secondary infections (l. 695).
- **Fitted to** nothing observed: its parameters come from the literature and from the
  model's own simulated set; the 23-vineyard genotype data (`gobbin2005`, `rumbou2004`)
  are its test, shared with `rossi2013`.
- **Authors:** Rossi and Caffi (engine models `rossi2008.primary`, `caffi2013.sporulation`,
  `brischetto2021.*`): flags; the substantive link to the engine is the borrowed
  germination form.

## Bearing (2026-10-12)

- A process model of the two inoculum sources that a truth could run only after choosing
  its own germination curve: the Gompertz in day of year (a 173.6, b 0.119) is the
  engine family's form, and its printed source does not hold those values. The result
  worth keeping is the shape of the primary share, 1.0 at onset to about 0.3 by day 40
  and 0.27 by day 80 across the 23 European epidemics, which `rossi2013` restates.
- Not a candidate for the catalogue: no tool runs it, and its coefficients' provenance is
  open.

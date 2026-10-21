---
id: guestrin2005
citation: Guestrin, C., Krause, A. & Singh, A. P. 2005. Near-optimal sensor placements in Gaussian processes. Proceedings of the 22nd International Conference on Machine Learning (ICML 2005), Bonn, Germany, 265-272 (pages and DOI from Crossref, 2026-10-21)
doi: 10.1145/1102351.1102385
read: 2026-10-21, lightly (the note is written from the reading agent's facts and equations for all 8 PDF pages including the appendix; the main session checked none of the equations in the page images), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [USA, California, Berkeley; USA, Washington and Oregon]
processes: [sensor placement, mutual information, Gaussian process, submodular optimisation, local kernels, entropy criterion]
records: []
datasets: []
files: [guestrin05near.pdf (the 2026-10-21 drop)]
---

# Guestrin, Krause & Singh 2005: greedy mutual-information placement in a Gaussian process (conference version)

The ICML 2005 paper that `krause2008` extends: same mutual-information criterion and greedy
algorithm, with the guarantee, local-kernel speed-up and two data sets. No record: a method. No
printed page numbers in the text layer; pages below are PDF pages.

**Read this first.** Several displayed formulas are garbled in the text layer and were not
reconciled. Remark 7's threshold for entropy is printed as sigma^2 < 4 pi e with a "1" stacked
above it in the text layer; whether it is 1/(4 pi e) is not settled, and the appendix proof of the
same remark uses 1/(2 pi e) (l. 679, 1091). The exact layout of Algorithm 1's ratio (including
any outer power) is not recoverable (l. 605-607). The appendix step for the mesh width reads
"delta <= sigma^2 eps / (L R)" with R = k sigma^-2 M^2 + sigma^-2 k^2 M + 3 k^3 M sigma^-4
(l. 1083-1085), which does not match Corollary 5's printed denominator (l. 616). Treat the
constants as unreconciled; use `krause2008` (Corollary 6) for the bound, itself unchecked here.
Curve values and error magnitudes (Figs. 3-5) are only in figures.

## What it holds

- **Same as krause2008:** criterion MI(A) = I(A; V\A) = H(V\A) - H(V\A | A) over k-subsets of
  candidates S, V = S u U (Eq. 5, p. 3, l. 537); gain = H(Y|A) - H(Y|Abar) (p. 3, l. 573); the
  ratio-of-variances rule of Algorithm 1 (p. 4, l. 605); submodular (Lemma 3, l. 630); NP-complete
  (Theorem 2, l. 557-559); greedy gives I >= (1 - 1/e)(OPT - k eps) (Theorem 6, p. 4, l. 632-636),
  under a fine discretisation, with Corollary 5's mesh width for a Lipschitz kernel (l. 612-618).
  The greedy run also gives an upper bound on OPT (l. 640-644). Basic cost O(kn^4) (l. 691).
- **Bound, what differs:** this paper says the Nemhauser argument does not apply to entropy
  (Remark 7, l. 674-679, threshold garbled). Its online bound is the upper bound on OPT from the
  greedy run, used to bound other heuristics (l. 640-644, 942-944); the 2008 paper adds
  Proposition 8 and a sensor-failure treatment. Budgets are
  one sentence, cited to a tech report and not proved (l. 645-654). Local kernels:
  Algorithm 2 with I >= (1 - 1/e)(OPT - k eps1 - 2kn eps2 / sigma^4), time O(nd^3 + nk + kd^4)
  (Theorem 8, p. 5, l. 694-700); with a relaxed-heaps priority queue O(nd^3 + kd log n + kd^4)
  (l. 706-711). It does not present the lazy priority queue of stale gains that `krause2008` calls
  Algorithm 2.
- **Data, what differs:** Intel Berkeley lab, 54 sites, |V| = 54 (l. 49, 500, 527), training
  on 30 s samples over 5 consecutive days from 28 February 2004 and testing on the next two
  (l. 921-923); windows 8-9 am and 12-1 pm (l. 724-726); candidates restricted to deployed sites
  so that test data exist (l. 924-926). The `krause2008` note records 46 of 54 sensors and 3
  training days for what looks like the same set; the difference is not explained in either text.
  Precipitation: the same 167 regions about 50 km apart, 1949-1994, log-transformed, first two
  thirds for training, sigma^2 = 0.1 chosen by cross-validation (l. 1030-1045, 1078).
- **Scoring, what differs:** held-out days, average RMS error and test log-likelihood (l. 922-929,
  1049-1051); baselines are the best and mean of 100 random placements, pairwise exchange, random
  plus exchange, and greedy plus exchange (l. 927-941). There are no A-, D- or E-optimal designs,
  disk model or nonstationary kernel (the 2008 extras); Fig. 4 uses one isotropic Gaussian kernel
  with a quadratic trend fitted in geoR (l. 933-935). Findings: MI beat entropy at increasing set
  sizes (l. 931-932); greedy beat the best of 100 random placements (l. 930-931); at size 12 random
  plus exchange exceeded greedy (l. 936-940); on precipitation MI "significantly outperforms"
  entropy and entropy would need several more sensors (l. 1053-1059). Numbers are in figures only.
- **Local-kernel trade-off:** eps in [0.5, 1] suggested for the time/accuracy trade-off on
  precipitation (l. 1067-1069); 20-sensor subsets for the approximation-error plot (l. 1066-1067).

## Dependence

Builds on Nemhauser, Wolsey & Fisher 1978 (greedy bound), Ko, Lee & Queyranne 1995 (entropy
NP-completeness, Theorem 1), Krause & Guestrin 2005 (budgets), Ramakrishnan et al. 2005 (boundary
effect of entropy), Deshpande et al. 2004 (Gaussian model of sensor temperatures) and Widmann &
Bretherton 1999 (precipitation data). Extended by `krause2008`. Shared authors only: a flag. No crop
or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48), the information-theoretic method.

- Nothing here that `krause2008` does not give more fully; use this as the earlier, shorter
  statement of the greedy MI rule and the local-kernel speed-up. Content not in the `krause2008` note: the Intel-lab
  training and test split as printed here and the pairwise-exchange baselines.
- Not shown: decisions, alerts, sensor type, nonstationary covariance, failures; the constants of
  the bound are garbled, so cite Corollary 6 of `krause2008`.

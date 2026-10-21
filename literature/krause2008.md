---
id: krause2008
citation: Krause, A., Singh, A. & Guestrin, C. 2008. Near-optimal sensor placements in Gaussian processes: theory, efficient algorithms and empirical studies. Journal of Machine Learning Research 9:235-284
doi: 
read: 2026-10-21, in full (Sections 1-11 and Appendix A), by a reading agent (claude-sonnet-5-5); 70 of 70 quotes found at their lines by scripts/verify_quotes.py; Equations 1, 2, 6 and 9, Corollary 6, Theorems 7 and 9, Proposition 8, the budgeted rule and Algorithms 1-3 read in the page images by the main session (claude-opus-5-5); figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [USA, California, Berkeley; USA, Washington and Oregon]
processes: [sensor placement, mutual information, Gaussian process, submodular optimisation, lazy greedy, nonstationary covariance, sensor failure]
records: []
datasets: []
files: [krause2008.pdf (the 2026-10-21 drop)]
---

# Krause, Singh & Guestrin 2008: greedy mutual-information placement in a Gaussian process

Chooses k sensor sites from a covariance matrix by greedily maximising the mutual information
between the chosen and the unchosen sites, with a (1 - 1/e) guarantee, and scores it on held-out
temperature and precipitation data. No record: a method. Printed page = 234 + PDF page.

**Read this first.** The guarantee needs the candidate grid to be fine enough that MI stays
nearly monotone up to 2k sites (Lemma 5, Corollary 6); on a coarse candidate set the bound is not
proven, though the online bound (Proposition 8) still applies. The paper gives no procedure for its
nonstationary covariance (it cites Nott & Dunsmuir 2002 and gives none of its settings), and in
several experiments the empirical covariance of the same data is both the input and the ground
truth. Curve values, error magnitudes and bar heights are only in the figures.

## What it holds

- **Prediction** (Eqs. 1-2, p. 240, l. 690-692): GP posterior mean
  mu_y|A = mu_y + Sigma_yA Sigma_AA^-1 (x_A - mu_A), variance
  sigma^2_y|A = K(y,y) - Sigma_yA Sigma_AA^-1 Sigma_Ay; the variance does not depend on the values
  observed. Gaussian conditional entropy H(y|A) = 1/2 log(2 pi e sigma^2_y|A) (Eq. 5, l. 788).
- **Criterion** (p. 243, l. 839): MI(A) = H(V\A) - H(V\A | A) = I(A; V\A), after Caselton & Zidek
  1984. Greedy gain (Eq. 6, p. 245, l. 951): MI(A u y) - MI(A) = H(y|A) - H(y|Abar), Abar =
  V \ (A u y). Algorithm 1 (p. 245) picks y maximising
  delta_y = (sigma^2_y - Sigma_yA Sigma_AA^-1 Sigma_Ay) / (sigma^2_y - Sigma_yAbar Sigma_AbarAbar^-1 Sigma_Abary).
  Entropy alone (Eq. 4) keeps only the numerator and places sensors on the boundary; MI favours
  "central" sites (l. 90, 956). Entropy has no approximate monotonicity, so the bound does not carry over to it (l. 1968).
- **Guarantee:** MI is submodular (Lemma 3, l. 1019; "information never hurts"). Theorem 7 (p. 247):
  MI(A) >= (1 - 1/e)(OPT - k eps), under Lemma 5's fine discretisation; Corollary 6 gives the mesh
  width delta <= eps sigma^6 / (4kLM(sigma^2 + 2k^2 M + 6k^2 sigma^2)) for a Lipschitz kernel
  (constant L, M = max K(x,x), sensor noise variance >= sigma^2). Selecting k of n is NP-complete
  (Theorem 2, l. 898-900).
- **Online bound** (Proposition 8, p. 248): OPT <= MI(A_k) + sum of the k largest gains
  delta_y = MI(A_k u y) - MI(A_k) + k eps. On a 16-site subsample greedy stayed within 95 % of
  the optimum found by mixed integer programming (l. 889).
- **Costs** (sections 4.3, 5): Algorithm 1 is O(k n^4) (l. 1253). Lazy evaluation (Algorithm 2,
  p. 251: a priority queue of stale gains, exact by submodularity) cut MI evaluations from 7125 to
  1172 and time from 41.3 to 8.7 s for k = 50 of 167 sites (l. 2725-2726). Local kernels
  (Algorithm 3, p. 252): drop conditioning sites with |K(y,x)| <= eps; time O(nd^3 + kn + kd^4),
  d = sites within the kernel's reach (l. 1392); Theorem 9: MI(A) >= (1 - 1/e)(OPT - k eps_1 -
  2kn eps_2 / sigma^4). eps in [0.5, 1] was the best trade-off on the precipitation covariance
  (median variance 1.70; l. 2819, 2825). Storkey's compact kernel (Eq. 9, p. 251):
  K = [(2 pi - Delta)(1 + cos(Delta)/2) + (3/2) sin Delta] / (3 pi) for Delta = beta |x - y| <
  2 pi, else 0 (the text layer prints 3/2 as "23"; read in the image).
- **Non-uniform costs** (p. 248): with budget L, greedy on gain / cost c(y) plus enumeration of
  all subsets of at most three sites gives (1 - 1/e) OPT - 2L eps / c_min (Krause & Guestrin 2005).
- **Robustness** (section 6): sensor failures as expected MI over failure scenarios, enumerating
  none or one failure when failures are rare (l. 1448); without optimising for it, if each sensor
  works with probability >= rho, E[F(A)] >= rho F(B) (Proposition 11, l. 1462). GP parameter
  uncertainty: expected MI under a prior on theta, still submodular and the bounds still apply
  (l. 1481, 1509), but predictions lose their closed form (l. 1498).
- **Data and scoring:** Intel Berkeley lab, 46 of 54 temperature sensors, 30 s samples, 3 days
  from 28 February 2004 to train and the next 2 to test (l. 2098-2100); Pacific Northwest daily
  precipitation, 167 equal-area regions about 50 km apart, 1949-1994, log-transformed, daily
  mean removed, first two thirds train (l. 2108-2113); empirical covariance regularised with
  sigma^2 = 0.1, chosen by cross-validation (l. 2115, 2153). Scored by RMS error and test
  log-likelihood on held-out days; no error bars, since samples are autocorrelated (l. 2120).
  MI beat entropy in almost all cases (l. 2266) and the disk model (r = 5 m, l. 2198); against
  A-, D- and E-optimal designs on 12 held-out target sites, MI had the least RMS except for one
  sensor (l. 2554); D-optimal edged MI on a 111-site subsample, MI was best on all 167 (l. 2630).
  The best of 100 random placements stayed below greedy (l. 2707); random plus pairwise exchange
  once exceeded it, at 12 sensors (l. 2712).
- **Nonstationary covariance:** locally isotropic kernels around reference points, after Nott &
  Dunsmuir 2002 (l. 728), fitted from an initial deployment. A nonstationary GP from 10 sensors
  did as well as a stationary one from 40 (temperature, l. 2142); from 20 it beat a stationary
  one from 160 (precipitation, l. 2149). Placements on the empirical covariance did best (l. 2208).
- **Sequential placement:** with known GP parameters, placing sequentially and placing at once are
  equivalent; with uncertain parameters a closed-loop strategy is expected to do better
  (l. 2914). No value-of-information or decision criterion.

## Dependence

Builds on Caselton & Zidek 1984 (the MI criterion), Nemhauser, Wolsey & Fisher 1978 (the greedy
bound), Nott & Dunsmuir 2002 (nonstationary covariance), Storkey 1999 (Eq. 9), Krause & Guestrin
2005 (budgets) and Krause et al. 2006 (Proposition 11). Extends Guestrin, Krause & Singh 2005
(`guestrin2005`). No crop or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48), the information-theoretic method.

- **Takeable as is:** Algorithm 2 (lazy greedy) on the empirical covariance of the simulated seasons,
  which the paper itself used as input and as ground truth. Candidates are node sites S, targets
  are vines V; a vine is predicted with Eqs. 1-2. With hundreds of seasons the covariance is
  estimated directly, and its nonstationarity (hollows, slopes) needs no kernel model. The sigma^2
  regulariser (0.1 there, chosen by cross-validation) is a choice to make again here.
- **Scale:** the second entropy term conditions on all unchosen sites, O(n^3) per candidate. At
  25,000 vines that is impossible directly; the paper's answers are local kernels (truncation at
  |cov| <= eps) or a coarser V (aggregate vines into cells). Candidate sites are far fewer
  (hundreds), so the cost sits in V, not in k.
- **Scoring:** held-out seasons (they held out days), RMS against best-of-100 random placements,
  plus the online bound; failures by Proposition 11 or by scenarios of one lost node.
- **Not covered:** decisions, alerts, sensor choice per node beyond a cost per site, and the
  wetness variable itself (MI on a Gaussian model of wet hours or of a transformed series is a
  modelling choice the paper does not make).

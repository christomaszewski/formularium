---
id: leskovec2007
citation: Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J. & Glance, N. 2007. Cost-effective outbreak detection in networks. Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD'07), San Jose, California, 12-15 August 2007, 420-429 (pages and DOI from Crossref, 2026-10-21)
doi: 10.1145/1281192.1281239
read: 2026-10-21, in full (abstract, Sections 1-9 and references, 10 PDF pages; the proofs are in a technical report the text cites, not in this file), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py; the equations were not checked in the page images; figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [blogosphere, 2006 (not geographic); water distribution networks BWSN1 and BWSN2 and a US metropolitan area, not named (NW3)]
processes: [sensor placement, outbreak detection, submodular optimisation, CELF, lazy greedy, penalty reduction, cost-benefit greedy, online bound, multicriteria optimisation, held-out test]
records: []
datasets: []
files: [leskovec2007.pdf (the 2026-10-21 drop)]
---

# Leskovec, Krause, Guestrin, Faloutsos, VanBriesen & Glance 2007: cost-effective outbreak detection (CELF)

Casts "where to put sensors, or which blogs to read, to detect a spreading event early" as
maximising a submodular penalty reduction under a budget, and gives CELF (lazy greedy with a
cost-benefit rule), a bound for it and an online bound, tested on 45,000 blogs and on water networks.
No record: a method. The author list is as printed on the first page (l. 4-6; Glance at Nielsen
BuzzMetrics). No printed page numbers; pages below are PDF pages. Conference version: the proofs are
only cited to a technical report (CMU-ML-07-111).

**Read this first.** Two scoring regimes. For the blogs the paper tests on unseen data: it selects blogs
on the first six months of 2006 and evaluates them on the second six months (l. 527-534, Fig. 7,
curve values figure-only), and finds that CELF overfits. All other blog scores, and all water scores,
are on the data used to optimise: the 3.6 million simulated water scenarios serve both for placing
and for scoring, with no held-out set (l. 632-645). The blog data are observed cascades, not a spread
model (l. 301-303). Several summation signs and fractions are missing from the text layer and were
read from context (l. 109, 131, 148, 168, 225-227, 259).

## What it holds

- **Objective** (p. 2-3, l. 113-148): maximise R(A) subject to c(A) <= B (Eq. 1); expected penalty
  pi(A) = sum_i P(i) pi_i(T(i,A)), T(i,A) the first detection by any sensor in A; reward
  R_i(A) = pi_i(infinity) - pi_i(T(i,A)) and R(A) = sum_i P(i) R_i(A) = pi(empty) - pi(A). The
  penalty must be nondecreasing in time (l. 139). Three objectives: detection likelihood (penalty 0 if
  detected, 1 if not; l. 165), detection time (penalty min(t, Tmax); l. 170), population affected (the
  cascade size at detection; l. 177). Multicriteria by scalarisation, maximisers Pareto optimal (l. 168).
- **Guarantees:** R is submodular (Theorem 1, l. 136). Unit-cost greedy (Eq. 2) gives
  (1 - 1/e) of the optimum (Theorem 2, cited to Nemhauser et al. 1978, l. 202-204). With costs the
  benefit-to-cost rule (Eq. 3) alone can fail: an example where its reward tends to 0 while the
  optimum is B (l. 234); the better of the unit-cost and cost-benefit greedy runs gives
  (1/2)(1 - 1/e), about 31 % (Theorem 3, p. 4, l. 255-258, the "1/2" printed as "1 2"). Online bound
  for any placement (Theorem 4, Eq. 4, l. 213-227, partly garbled), computed by Algorithm 2 in 54 s for
  the 100-blog run (l. 567-568).
- **CELF** (Algorithm 1, p. 5, l. 280-304): lazy evaluation, using that gains cannot increase
  (l. 357); runs LazyForward with the unit-cost and the cost-benefit rule and keeps the better. O(B|V|)
  evaluations against Omega(B|V|^4) for Sviridenko's algorithm (l. 269-274). For 100 blogs, greedy took
  4.5 h and CELF 23 s, up to 700 times faster (l. 281, 566-567); an inverted index cut the blog data
  from 3.5 GB to 50 MB (l. 571). Score from the index: sum over detected scenarios of P(i) times the
  best single-sensor reduction (l. 259).
- **Blog data** (p. 5, l. 305-334): 45,000 blogs that had at least 3 in-links in the first 6 months
  of 2006, all their posts for 2006, 10.5 million posts, 16.2 million links (30 GB; about 1 million
  point inside the set); 346,209 non-trivial cascades, 17,589 with at least 10 nodes. Biased towards
  active blogs (l. 305).
- **Blog results:** after 100 blogs CELF is at most 13.8 % from optimal by the online bound
  (l. 446), and all three objectives at most 5 to 15 % (l. 455). With posts as cost, 1,500 posts give
  the population-affected score that 10,710 posts give under unit cost (l. 448). The best heuristics
  (in- and out-link counts) are 45 % worse than CELF under unit cost and CELF beats them by 41 % under
  the posts cost (l. 531, 550); random selection and post counts do poorly. Friday reading gives
  population affected 0.20 against 0.13 for the rest of the week (l. 520).
- **Held-out test (historic against future):** first six months select the blogs, the second six
  evaluate them on unseen cascades; the top curve in Fig. 7 selects directly on the future data
  (l. 532). CELF "overfits": it picks small blogs that join cascades by chance and generalises
  poorly (l. 542). Restricting it to blogs with at least one post per day (365 a year) shrinks the
  gap between the two curves and the future score does not drop, at some cost to the in-sample
  optimum (p. 7, Fig. 7(b); gap sizes figure-only).
- **Water** (p. 8, l. 596-659): BWSN1 (129 nodes), BWSN2 (12,527), NW3 (about 21,000 nodes, 25,000
  pipes); EPANET, 48 h at 5-minute steps, contamination in the first 24 h; 3.6 million scenarios;
  20 sensors in the BWSN setting (l. 615). CELF beats the best heuristic by 45 % (l. 634); "even the
  maximum over one hundred random trials performs far worse" (l. 639); the online bound is much
  tighter than the offline one (l. 644); detecting every scenario takes 2,263 sensors (l. 653). One
  simulation takes about 7 s and 14 KB, a month on about 40 machines gave 152 GB, and a 16 GB
  in-memory index sped the algorithms up at least 1000 times (l. 734-747); CELF is 10 times faster than
  plain greedy at 10 sensors (l. 750).
- **Influence maximisation:** the Triggering Model of Kempe, Kleinberg & Tardos (2003) is a special
  case (Theorem 5, p. 9, l. 688); proof only in the technical report.

## Dependence

Builds on Nemhauser, Wolsey & Fisher 1978 (greedy bound), Khuller, Moss & Naor 1999 (budgeted maximum
coverage, which Theorem 3 generalises), Sviridenko 2004 (the slower budgeted algorithm), Kempe et al.
2003 (influence), Glance et al. 2005 (the blog data), Ostfeld et al. (the BWSN challenge), Berry et al.
2006 (p-median, closest water work) and Rossman 1999 (EPANET). The water application is treated in
full in `krause2008b`, cited here as submitted (l. 798-802). Shared authors with `krause2008` and
`guestrin2005` only: a flag. No crop or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48), the scenario-based and cost-aware method,
read together with `krause2008b`.

- **Takeable as is:** CELF for a budgeted placement where nodes or sensors have different costs
  (running both the unit-cost and the cost-benefit greedy rule), the online bound for any placement,
  and the same three score types: detection likelihood, detection time and population affected,
  built from simulated event scenarios. A sensor menu can be handled as a cost per candidate.
- **Scoring:** the blog split gives the template for held-out scoring: pick on one set of scenarios,
  evaluate on another. Its finding is that an unconstrained greedy overfits to chance detections by
  small sites, which matters for a vineyard with a small simulated-season sample; a floor on a
  candidate's activity was the paper's remedy.
- **Not shown:** held-out water scenarios; false alarms or the correctness of alert days; a
  covariance model of variability; re-planning mid-season. Kind of result: a method with a
  guarantee, and in-sample plus one out-of-sample empirical comparison.

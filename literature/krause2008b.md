---
id: krause2008b
citation: Krause, A., Leskovec, J., Guestrin, C., VanBriesen, J. & Faloutsos, C. 2008. Efficient sensor placement optimization for securing large water distribution networks. Journal of Water Resources Planning and Management 134(6):516-526
doi: 10.1061/(ASCE)0733-9496(2008)134:6(516)
read: 2026-10-21, in full (title page, abstract, Sections 1-8, appendix proofs of Theorems 1 and 2, figure captions and Table 1) of the unmarked author manuscript (41 pages, no journal header, DOI or year printed; the journal citation and DOI are Crossref's (scripts/crossref_lookup.py, 2026-10-21), not printed in the text), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; the equations were not checked in the page images; figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [water distribution networks BWSN1 and BWSN2 (Battle of the Water Sensor Networks challenge, location not stated); a US metropolitan area, not named (NW3)]
processes: [sensor placement, submodular optimisation, lazy greedy, penalty reduction, detection time, detection likelihood, scenario simulation, multicriteria optimisation, sensor failure]
records: []
datasets: []
files: [krause08efficient.pdf (the 2026-10-21 drop)]
---

# Krause, Leskovec, Guestrin, VanBriesen & Faloutsos 2008: scenario-based sensor placement for water networks

Places k or a budget of sensors on a water distribution network by greedily maximising the
expected penalty reduction over simulated contamination scenarios, with a (1 - 1/e) guarantee,
an online bound and lazy evaluation, on networks of 129, 12,527 and about 21,000 nodes. No record:
a method. Printed page = PDF page (1-41 in the manuscript).

**Read this first.** The scores are on the optimisation set. All scenarios (37,152 for BWSN1,
3,602,776 for BWSN2) are both used to place sensors and used to report the scores; no held-out
scenarios are described (l. 139-141, 946, 948, 1810). The only independent check is the Battle of
the Water Sensor Networks organisers' evaluation of 15 entries, and the text does not say which
scenario set they used (l. 1195-1205). The copy read is an author manuscript, not the published
text, and has these printed inconsistencies: the Figure 2 caption gives panel (d) as Z3, but the
text and the panel label say Z2 (l. 1045, 1638, 1642-1643); l. 1022-1023 calls time to
detection Z3, though Z1 is detection time (l. 90-94, 224-226); NW3 has 150,000 scenarios in the
text (l. 1246) and 120,000 in Table 1 (l. 1810). Several summation signs are missing from the text
layer and were read from context (l. 289, 292, 405, 417, 528-534, 725). Figure values are figure-only.

## What it holds

- **Objective** (p. 6-7, l. 260-293): detection time of placement A under scenario i,
  T(A,i) = min over s in A of T(s,i); penalty reduction R(A,i) = pi_i(infinity) - pi_i(T(A,i));
  expected R(A) = sum over i of P(i) R(A,i), with uniform P(i) in the experiments (l. 244). Four
  objectives: detection time Z1 (penalty is the time, tmax if never detected, l. 299), expected
  population affected Z2, contaminated water consumed Z3, detection likelihood Z4 (l. 90-94).
  Each is normalised to R'_j = R_j / (expected penalty with no sensor) in [0, 1] (p. 9, l. 417).
- **Submodular** (Theorem 1, p. 8, l. 345; appendix l. 1512-1530): R is submodular and
  nondecreasing, a nonnegative sum of per-scenario terms; this needs penalties nondecreasing in
  detection time. Penalty minimisation has no offline approximation guarantee unless P = NP
  (Theorem 2, p. 14, l. 625; reduction from set cover, l. 1533-1557).
- **Guarantees:** greedy gives R(A_G) >= (1 - 1/e) R(A*) (p. 11, l. 480-484, cited to Nemhauser
  et al. 1978), costs O(k |S| T_eval) (l. 492). Budgeted costs: greedy with partial enumeration,
  also 1 - 1/e, stated without proof (l. 505-511). Online bound for any placement:
  R(A*) <= R(A) + the sum of the k largest gains delta_s (p. 12, l. 530-537). Online bounds put
  greedy within 95 % of optimal for Z3 at 20 sensors and at least 80 % for Z1 (BWSN2, l. 1069-1079);
  the offline bound is "meaningless" beyond 3 sensors for Z3 (l. 1063-1066).
- **Lazy evaluation** (p. 19-20, l. 881-921): stale gains are upper bounds by submodularity, so
  only the top candidate is recomputed; the result equals plain greedy. About 30 times faster at 20
  sensors (l. 917-918). Not named CELF here (that is `leskovec2007`). Score evaluation: for each
  scenario the reduction is that of the best single sensor in A (l. 869); undetected scenarios
  contribute 0. Table 1, 10 sensors: 0.05, 41.2 and 2.73 min for BWSN1, BWSN2 and NW3 (l. 1812).
- **Scenario data** (p. 16-17, l. 754-847): EPANET 2.0, 48 h at 5-minute steps, intrusions in
  the first 24 h at 288 start times per node; every node is a candidate sensor site and an
  intrusion site; 3.6 million scenarios; about 4 s per run, about 170 days serial, about 9 days on
  20 PCs (l. 800-810); 47 TB raw cut to 16 GB by a sparse store (l. 774, 792-796). NW3 greedy at 30
  sensors takes about 12 min (l. 1250), the bounds guarantee 91 % of optimum (l. 1258-1260).
- **Scoring:** 100 uniformly random placements per size, median and percentiles; "even the maximum
  over 100 random placements is worse than the greedy solution" (BWSN2, Z1; l. 1037-1039); degree,
  population, flow and diameter heuristics no better than random (l. 1047). On BWSN1 greedy equals
  the exact optimum from the mixed integer program up to 6 sensors (l. 1095-1098), and is within 98 %
  of the best found (annealing and a MIP bound) for Z2 up to 10 (l. 1118-1120). On NW3 the best of
  100 random placements is under 84 % of greedy, and 21 random sensors match 5 greedy ones at the
  median (l. 1262-1268).
- **Multicriteria:** scalarisation max sum_j lambda_j R_j(A) s.t. c(A) <= B, whose maximisers are
  Pareto optimal (p. 9, l. 405). Knee of the Z4 against Z2 trade-off at 20 sensors: 42 % of
  intrusions detected and the affected population cut by 78 %, from 1534 to 334 (l. 1161-1163); Z2
  alone cuts it 83 % but detects 34 % (l. 1165).
- **Adversarial and failures:** the worst-case score min over scenarios of R(A,i) is not submodular
  (l. 661); the transform R'(s,i) = 1 - exp(-R(s,i)/vartheta) is, once summed (p. 15, l. 668).
  2,263 sensors are needed to detect all 3.6 million scenarios, 23 if only scenarios affecting at
  least 500 nodes count (l. 1215-1229); adversarial score 40 % at 23 sensors, 60 % at 50 (l. 1233-1235).
  Sensor failure: expectation over failure scenarios, approximated by none or one failed sensor
  (p. 16, l. 725, 739).
- **BWSN result:** 26 of 30 non-dominated solutions, the best entry; next best Berry et al. with 21
  (l. 1205).

## Dependence

Builds on Nemhauser, Wolsey & Fisher 1978 (greedy bound), Nemhauser & Wolsey 1981 (the MIP with
constraint generation, used for bounds), Sviridenko 2004 and Krause & Guestrin 2005 (budgets), Kirkpatrick et
al. 1983 (annealing), Rossman 1999 (EPANET 2.0), Ostfeld et al. 2008 (the challenge, scenarios and
evaluation) and Berry et al. 2006 (p-median formulation, the closest prior work, l. 169-185). The same
formalism as `leskovec2007` (applied there to weblogs, l. 313-317). Shared authors with
`krause2008` and `guestrin2005` only: a flag; this paper has no Gaussian model. No crop or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48), the decision-focused and scenario-based
method; the strongest fit of the three papers for the "alert days right" objective.

- **Takeable as is:** the form R(A) = sum_i P(i) [pi_i(infinity) - pi_i(T(A,i))] with one scenario
  per simulated event or season, a detection time per candidate node and a per-scenario penalty
  (detection likelihood 0/1, detection time, or the population or area affected). Greedy over the
  candidate sites with lazy evaluation and the online bound for any placement, plus a budget by
  cost-benefit greedy. A sparse store of "which node detects which scenario, when" makes each score
  fast (l. 823-872).
- **What must be defined:** what "a node detects an event" means for a vineyard, and a penalty that
  is nondecreasing in detection time, since Theorem 1 needs it. An objective that also penalises false
  alert days, or counts days right and wrong, is not shown to be submodular here; the paper has only
  the cost of a late or missed detection. The worst-case and failure variants (l. 661-676, 725) are
  the template for losing a node.
- **Not shown:** scores on held-out scenarios. Agrarium should place on one set of simulated
  seasons and score on another; this paper cannot be cited for out-of-sample quality. Also not shown:
  continuous covariance prediction (see `krause2008`), a sensor menu beyond a cost per site, or a
  mid-season re-plan.

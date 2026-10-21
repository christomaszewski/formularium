---
id: clark2018
citation: Clark, E., Askham, T., Brunton, S.L. & Kutz, J.N. 2019. Greedy Sensor Placement With Cost Constraints. IEEE Sensors Journal 19(7):2642-2656
doi: 10.1109/JSEN.2018.2887044
read: 2026-10-21, lightly: abstract, problem formulation, the cost-aware QR algorithm, the three data sets and the application sections, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [global ocean (sea surface temperature)]
processes: [sensor placement, QR pivoting, sensor cost, cost-error trade-off, reconstruction, random baseline]
records: []
datasets: []
files: [clark2018.pdf (the 2026-10-21 drop)]
---

# Clark, Askham, Brunton & Kutz 2019: greedy QR sensor placement with a cost per site

Adds a per-site cost to column-pivoted QR sensor selection, so that each pivot trades error reduction against cost, and traces cost-error curves on faces, sea surface temperature and a cylinder flow. No record: a method.

**Read this first.** The issue is the April 2019 one (l. 1), although the article was published online on 17 December 2018 (l. 54-57); the running heads print pages 2642 to 2656 (l. 1, 800). Many equations (3, 4, 7 to 11, 16 to 18) are partly lost in the text layer and are recorded here as unchecked. Table II (run times) and the cost-error curves of Figures 5 to 13 are not in the text layer.

## What it holds

- **Problem** (Eqs. 5 and 6, p. 3, l. 235, 243): choose sensors J to minimise the training reconstruction error subject to a budget b on summed costs eta_j and a bound s on the size of the map; the relaxed form adds lambda times the summed cost, and varying lambda traces a cost-error curve. Test error uses the map fitted on the training set only (Eq. 4, l. 214, partly garbled, unchecked).
- **Rule** (Eq. 17, p. 5, l. 368, garbled, unchecked; Algorithm 1, l. 325-352): at each step pick the remaining column maximising its residual norm minus gamma times its cost; with gamma = 0 it is plain column-pivoted QR (l. 353-354). Cost O(mnp) for m samples, n sites and p sensors (l. 393-394).
- **Guarantee:** none for the cost version. Theorem 1 (Gu and Eisenstat; Eqs. 7 and 8, garbled, unchecked) holds for unweighted sets, and the paper says no such bound holds for the cost-constrained log-determinant objective (l. 311-318, 709-710).
- **Data and splits** (l. 409-412, 430-434, 445-450): faces, 32 x 32 = 1024 pixels, 80/20 random split with 20 cross-validations (interpolative) or the first 80 % as training (extrapolative); weekly SST, 1400 snapshots on a 360 x 180 grid, 1100 for training and 300 for testing, 10 cross-validations; cylinder flow, 151 snapshots on a 199 x 449 grid, 120 for training, 30 cross-validations.
- **Baselines** (l. 489, 463-465): 100 random sensor sets per method (Fig. 3); a test-set projection onto the first p SVD modes as a rough minimum error. QR "generally outperforms the best randomly-chosen sensors", though random sometimes wins at large p (l. 548).
- **Results:** cost can be lowered at marginal error increase in all three sets (l. 671). SST error "does not even reach 3%, even when the cost is zero" (l. 639). For the cylinder, the error curves at gamma = 0 and gamma = 15 are essentially identical (l. 689-693). Raw data as basis gave the lowest error at 100 sensors for faces and SST (l. 541-545); random combinations beat SVD modes for slow-decay data (l. 679-681).

## Dependence

- Builds on column-pivoted QR (Businger & Golub 1965), strong rank-revealing QR (Gu & Eisenstat), DEIM and Q-DEIM, and the submodular reviews of Krause & Golovin and Guestrin et al. Authors Brunton and Kutz are shared with `manohar2018`, a flag, not a dependence. No crop or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): cost-weighted placement.

- **Cost:** the takeable part is the pivot rule, residual norm minus gamma times site cost (Eq. 17), which is a one-parameter cost-error frontier from a single greedy run per gamma, usable on a sensor menu where each node type has a price. The costs there are Gaussian and step functions (gamma up to 1.9e5 and 6e4 for faces, l. 423), not real prices.
- **Validation:** held-out test sets by random and by contiguous split, against 100 random sensor sets per method (l. 489), reported as cost-error curves in figures. No wall-clock numbers in the text layer.
- **Not shown:** a guarantee, an MI or entropy criterion, field or crop data, any re-plan.

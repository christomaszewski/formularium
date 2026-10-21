---
id: manohar2018
citation: Manohar, K., Brunton, B.W., Kutz, J.N. & Brunton, S.L. 2018. Data-Driven Sparse Sensor Placement for Reconstruction. IEEE Control Systems Magazine 38(3):63-86 (the copy read is arXiv:1701.07569v2, 18 Aug 2017; volume, pages and DOI are from OpenAlex, not printed in the text)
doi: 10.1109/MCS.2018.2810460
read: 2026-10-21, lightly: abstract, the formulation sidebar, the POD and QR-pivoting sections, Table 1 and the three experiments (cylinder flow, faces, sea surface temperature), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [global ocean (sea surface temperature)]
processes: [sensor placement, QR pivoting, POD, D-optimal design, reconstruction, random baseline]
records: []
datasets: []
files: [manohar2018.pdf (the 2026-10-21 drop)]
---

# Manohar, Brunton, Kutz & Brunton 2018: sensors from QR pivoting on the POD modes of simulated and image data

Chooses p sensor sites by column-pivoted QR of a low-rank POD basis of past snapshots, a cheap greedy stand-in for D-optimal design, and tests it on a cylinder-flow simulation, a face database and sea surface temperature. No record: a method.

**Read this first.** The copy is the arXiv v2 preprint, not the magazine typeset version, so page and equation numbers may differ in print. Equations 15, 17, 19, 22, 24, 25 and 27 are partly lost in the text layer and are recorded here as unchecked. The cylinder, faces and SST results are in figures; the text gives few numbers, and the number of random draws is not printed (error bars only, l. 1147-1148).

## What it holds

- **Method** (Algorithm 1, p. 13, l. 769-778): for p = r sensors, QR with column pivoting of Psi_r^T (Eq. 22, l. 811, unchecked); for p > r, QR of Psi_r Psi_r^T (Eq. 23, l. 821). The pivots are an approximate greedy answer to the determinant criterion (Eq. 18, p. 12, l. 711), equivalent to D-optimal subset selection (Eq. 26, p. 14, l. 877). The oversampled case p > r is claimed as the authors' extension of Q-DEIM (l. 759). Reconstruction is a least-squares fit of the modal coefficients with the pseudoinverse (Eq. 15, p. 11, l. 673, garbled, unchecked).
- **Cost** (Table 1, l. 1029-1030): O(n r^2) for p = r and O(n^3) for p > r; convex relaxations need at least O(n^3) per iteration (l. 786). One QR gives all n pivots, reusable for any p (l. 789). No wall-clock times are printed.
- **Cylinder flow, Re = 100** (l. 1556, 1076, 1148, 1291): candidates cut from n = 89351 to n = 3600; 151 snapshots, the first 100 for training and the last 51 for validation; rank r = 42 and 42 QR sensors. QR sensors were "orders of magnitude more accurate" than random sensors (l. 1256); with p = 2r the error was 4x below DEIM's (l. 1490, 1570).
- **Faces, Extended Yale B, 1024 pixels** (l. 1593-1595, 1576): 166 QR pixels (16 %) for adequate reconstruction; least squares on 50 QR pixels (5 %) beat compressed sensing on 300 random pixels, which needed 600 for comparable recovery. Eigenfaces were trained on 32 random images per person and a held-out image was reconstructed.
- **Sea surface temperature, NOAA OISST v2, 1990 to 2016** (l. 1682, 1687, 1662, 1726): first 16 years (832 snapshots) for training, the rest for validation; optimal rank r = 302; random sensors with least squares or compressed sensing reconstructed poorly. Error values are in the figures only.
- **Noise** (l. 1494): the paper says POD-based sampling error grows in a bounded way with sensor noise.

## Dependence

- Builds on Q-DEIM (Drmac & Gugercin) and DEIM (Chaturantabut & Sorensen), on D-, A- and E-optimal design (Boyd & Vandenberghe; Joshi & Boyd), on compressed sensing (Donoho; Candes, Romberg & Tao) and on Sommariva & Vianello's QR for Fekete points. Authors Brunton and Kutz are shared with `clark2018`, a flag, not a dependence. No crop or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): an alternative to greedy mutual information, and a scale route.

- **Greedy MI alternative:** the criterion is linear reconstruction of the whole field from a low-rank basis of past snapshots (here, simulated seasons), not MI under a Gaussian model. It is a cheap representative-mode placement: for p = r the cost is O(n r^2) in the number of sites n (l. 1029), against the O(n^3) of the oversampled case (l. 1030) that would apply if n were the vines.
- **Validation:** held-out snapshots (51 cylinder snapshots, a held-out face, the SST years after the first 16), against random sensors (count of draws not printed) and DEIM; numbers are mostly in figures. The 5 % against 300-pixel comparison is the only quantified gain in the text.
- **Not shown:** sensor cost or noise differing by site, measured (not simulated or image) data with a biological variable, and any re-plan.

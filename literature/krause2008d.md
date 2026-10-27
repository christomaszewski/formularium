---
id: krause2008d
citation: Krause, A., McMahan, H. B., Guestrin, C. & Gupta, A. 2008. Robust submodular observation selection. Journal of Machine Learning Research 9:2761-2801
doi: 
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: []
regions: [USA]
processes: [sensor placement, robust optimisation, worst-case objective, submodular optimisation, Gaussian process, Saturate]
records: []
datasets: []
files: [krause2008jmlr.pdf (the 2026-10-25 other-sources drop)]
---

# Krause, McMahan, Guestrin & Gupta 2008 (JMLR): Saturate, the journal version

The journal version of the technical report read as krause2008c, with the same problem, algorithm, bounds and experiments in a shorter appendix and a different Section 8 layout.

## What it holds

- **Same method and results as krause2008c:** Saturate (Theorem 5, l. 536) with hardness
  results (Theorem 3, l. 339; Theorem 6, l. 606-608). Headline numbers: efficiency 69 % against
  52 % for the SDP design (l. 1412); 3424 water-network scenarios (l. 1437); 2 days of held-out
  data in Section 8.5 (l. 1654).
- **Appendices:** only Appendix A (proofs, l. 2020) is kept. The technical report's appendices B
  (scalarisation) and C (examples of submodular functions) are not in this version; scalarisation
  is a footnote (l. 1048-1049).
- **Section 8 layout:** the water network sits under 8.3 "Outbreak Detection" (l. 1418), not
  under its own 8.3 heading. The results are the same, including "did not improve the objective
  at all" for greedy on Z1 (l. 1442).
- **Figure numbers:** the sensor-failure experiment is Figure 12 here (l. 1623), Figure 11 in
  krause2008c.
- **Dates:** submitted 1/08, revised 9/08, published 12/08 (l. 1 header).

## Dependence

- **Builds on** the greedy bound of Nemhauser et al. (Theorem 2, l. 218) and the same data as
  krause2008c: the Intel temperature, Pacific Northwest precipitation, the NIMS lake deployment
  (l. 1094-1098) and the Battle of the Water Sensor Networks network (l. 1422-1425).

## Bearing (2026-10-26)

- classes.tsv names no search for this key. The method's bearing is as in krause2008c: a
  SATURATE placement that holds over several models, seasons or failure sets, for the placement
  methods study (D48).
- A vineyard simulator or growers' decision engine would take the method, not the water-network
  or sensor numbers. The paper was not read in full; this note covers the differences only.

---
id: crowley2025
citation: Crowley, G., Tait, S., Panoutsos, G., Speight, V. & Esnaola, I. 2025. Information-theoretic sensor placement for large sewer networks. Water Research 268(Pt B):122718
doi: 10.1016/j.watres.2024.122718
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full; a White Rose Research Online copy (its cover says Published Version, the body is a preprint layout, l. 11, 85)
status: read
diseases: []
crops: []
regions: [South of England, Bellinge Denmark]
processes: [sensor placement, mutual information, greedy algorithm]
records: []
datasets: []
files: [r_10_1016_j_watres_2024_122718.pdf (the 2026-10-18 drop)]
---

# Crowley et al. 2025: mutual-information sensor placement in sewer networks

Sensors are placed to maximise mutual information about network state, using a one-step modified greedy algorithm.

## What it holds

- **Method:** mutual information from a stochastic description of the network states; the greedy heuristic is run from every possible first placement (l. 46-52).
- **Networks:** a South of England sewer with 479 nodes and 567 links and Bellinge with 1020 nodes and 1015 links (l. 53-54); the text later says 1050 links for Bellinge (l. 931).
- **Check:** placements are tested by estimating unmonitored nodes with linear and neural models; they beat other heuristics in most cases and cluster sensors (l. 55-58). Flows come from SWMM simulation (l. 129).

## Dependence

- Uses SWMM (Rossman 2010), mutual information, and NSGA-II and greedy placement heuristics (l. 129, 151).

## Bearing (2026-10-18)

- Strand s6: a way to rank sensor layouts by information about unmonitored points; a simulator could use it to place vineyard loggers, but the data here are simulated sewer flows.
- Not read in full.

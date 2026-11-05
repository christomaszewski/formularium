---
id: ojwang2024
citation: Ojwang', A. M. E., Lloyd, A. L., Bhattacharyya, S., Chatterjee, S., Gent, D. H. & Ojiambo, P. S. 2024. Identifying highly connected sites for risk-based surveillance and control of cucurbit downy mildew in the eastern United States. PeerJ 12:e17649
doi: 10.7717/peerj.17649
read: "2026-11-04, the methods paragraph on the dispersal kernel only (Europe PMC full-text XML), by a reading agent and a note writer; 2 of 2 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: [cucurbit downy mildew]
crops: [cucurbits]
regions: [eastern United States]
processes: [dispersal kernel, power law, network, surveillance, wind]
records: []
datasets: []
files: [dr1104_ojwang2024.xml (the 2026-11-04 drop)]
---

# Ojwang' et al. 2024: a power-law dispersal kernel between cucurbit downy mildew sites, with b taken from earlier work

A network study of cucurbit downy mildew (Pseudoperonospora cubensis) in the eastern United States, 2008 to 2016, that links report sites by an inverse power-law kernel whose exponent it does not estimate.

**Read this first.**
- The exponent b is not a result of this paper. It is taken from Ojiambo et al. 2017 (PeerJ 5:e3465, per the reference list), so cite that paper for b, not this one.
- The scale is continental (links between sites across states), for a pathogen with long-distance spread, a cucurbit crop and wind-borne spores. It is an analogue for the shape of a kernel, not a value for a vineyard.
- Only the kernel paragraph was read; the network results were not.

## What it holds

- **Kernel (l. 148):** links between a source node and a sink node use an inverse power-law dispersal kernel, y = l^-b, where y is the probability of transmission and l the distance between nodes (haversine distance, km).
- **Exponent (l. 151):** b was not estimated here. Ojiambo et al. (2017) found b between 1.61 and 3.36 over the epidemic years 2008 to 2016, and the matching yearly b was used for each year.
- **Data:** disease reports from sentinel and non-sentinel sites, 2008 to 2016, the same epidemic data as the b estimates (l. 151).

## Dependence

- b comes from Ojiambo et al. 2017, fitted to the same 2008 to 2016 cucurbit downy mildew reports. The kernel form is credited to Andersen et al. 2019 (cited in the text). No engine model is computed.

## Bearing (2026-11-04)

- **dm.wind_scale_m:** a published power-law kernel for downy mildew spread at km scale (b from 1.61 to 3.36, cited from Ojiambo 2017). A shape analogue for Agrarium's dispersal scale; not a vineyard value and not a scale length in metres.
- Kind of evidence: a regional network model using a borrowed exponent; the primary source for b is Ojiambo et al. 2017, not read here.

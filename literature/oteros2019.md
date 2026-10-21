---
id: oteros2019
citation: Oteros, J., Sofiev, M., Smith, M., Clot, B., Damialis, A., Prank, M., et al. 2019. Building an automatic Pollen Monitoring Network (ePIN): Selection of optimal sites by clustering pollen stations. Science of the Total Environment (volume and pages not recorded)
doi: 10.1016/j.scitotenv.2019.06.131
read: 2026-10-21, lightly: abstract, Sections 1 to 4, Tables 1-3 and the figure captions, the R code read only for the clustering call; the text file has no journal, year or DOI, which are from OpenAlex, 2026-10-21; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Germany, Bavaria]
processes: [sensor placement, pollen monitoring, Ward clustering, correlation, representative site, population coverage]
records: []
datasets: []
files: [oteros2019.pdf (the 2026-10-21 drop)]
---

# Oteros et al. 2019: choosing 8 automatic pollen stations out of 27 Bavarian traps by Ward clustering

Clusters 26 pollen traps by the correlation of their daily counts in 2015, then keeps one station per sub-cluster, chosen by population served. No record: a method.

**Read this first.** The journal, year and DOI are not in the text file; they come from OpenAlex (2026-10-21) and have not been checked against the paper's first page. The supplement (Fig. S4 elbow plot, Fig. S2) was not in the text. The rule for going from 4 clusters to 8 sub-clusters is not given (l. 769, 788). The R code calls a normalisation (norm.ch) that is not defined in the text, so how the correlation matrix is normalised is unknown.

## What it holds

- **Pilot** (l. 81, 97, 304): 27 manual Hirst-type traps over Bavaria in 2015, built deliberately dense, reduced to 8 automatic stations. DEERLA is excluded from clustering for technical faults (l. 531), so 26 are clustered.
- **Features** (l. 521, 555, 558, 560): daily counts of 5 pollen types with more than 1000 grains per season on average; stations with at least 80 % of the season's data; correlations below 0.5 set to 0.
- **Distance** (l. 569-575): each station is described by its correlation with every other station, per pollen type; Ward's method on the Euclidean distance between those vectors. The authors note a correlation is not a metric (l. 575).
- **Clusters** (l. 767-788): the elbow plot suggests 4 main clusters; Ward clusters C1 12 stations, C2 6 (cold areas), C3 3 (outliers), C4 5. Eight sub-clusters are taken from the dendrogram, one station each (l. 843).
- **Representative** (l. 594-607): the station covering the highest population (within 0.5 % counts as a tie, then closest to the border); no two selected stations within 70 km; four manual stations are kept apart. DEOBER would have been chosen but was already manual, so DEGARM was taken (l. 853).
- **Coverage** (l. 337, 93, 1283): 25 km buffers around the 27 pre-selected sites cover 94 % of the population; the final network is stated to serve 13 million inhabitants; Table 1 gives coverage within 30 km per site.

## Dependence

- Ward's hierarchical grouping (R hclust, ward.D); the correlation-vector approach is cited to Oteros et al. 2013b (l. 569). Source footprints from the SILAM model (Sofiev et al.) were used to check source coverage (l. 384-388). Shared authors with the SILAM work: a flag only.

## Bearing (2026-10-21)

Representative-site clustering, for Agrarium's placement-methods study (PLAN 15, D48).

- **Features, k and representative:** features are each station's correlation vector with all other stations (per type, correlations below 0.5 zeroed). k comes from an elbow plot (4 main clusters) and then a dendrogram reading (8 sub-clusters), with no stated rule. The representative is not the cluster's medoid: it is the station serving most people, with a 70 km spacing rule. That is a coverage choice, not a signal choice.
- **Validation:** none. No held-out stations, no reconstruction error, no random, entropy or kriging comparison; the only score is population coverage. The claim that zones are homogeneous (l. 88-89) is untested.
- **Takeable:** a way to cluster stations by co-variation rather than by distance, and a constrained pick (spacing, existing sites) after clustering. Not shown: that the 8 stations reproduce what the 27 saw.
- **Kind of result:** an applied design on one season, one year of pollen data.

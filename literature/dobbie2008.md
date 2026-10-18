---
id: dobbie2008
citation: Dobbie, M. J., Henderson, B. L. & Stevens, D. L. Jr 2008. Sparse sampling: Spatial design for monitoring stream networks. Statistics Surveys 2:113-153
doi: 10.1214/07-SS032
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py; equations legible in the text layer, no page images needed
status: read
diseases: []
crops: []
regions: [not applicable]
processes: [spatial sampling design, monitoring network design, probability designs, spatial balance]
records: []
datasets: []
files: [dobbie_2008.pdf (the 2026-10-18 drop)]
---

# Dobbie et al. 2008: spatial designs for sparse stream-network monitoring

A review of spatial sampling designs for monitoring stream networks, especially ephemeral ones, so that practical and optimal designs can be chosen (l. 20-26). No record.

## What it holds

- **Review, not a study** (l. 50): no data of its own; Tables 1-6 are design types. A review of Stehman's (1999) criteria for a survey design (low estimated variance, calculable uncertainty, spatial balance, simplicity, cost-effectiveness; l. 236) and the five R's (l. 243). Simple random sampling is judged impractical for stream monitoring (l. 399).
- **Probability designs** (l. 446-587, 776-828): stratified and variable-probability sampling (a stratum with one member has inclusion probability 1; l. 557); systematic unaligned designs avoid periodicity (Caeiro et al. 2003, l. 446); the lineage RTS, then MD-NRTS, then GRTS (l. 776-794); GRTS has been used for the US EMAP stream programme for years (l. 809), with S-Plus and R code said to be free from the EMAP website (l. 818; no licence printed). Post-stratification for non-response (l. 828).
- **Model-based designs** (l. 843-1049): with known covariance, a regular grid is optimal for prediction (l. 843), a triangular grid minimises average or maximum prediction variance (McBratney 1981, l. 845). Random field Y(x) = mu(x) + S(x) (eq. 1, l. 853); kriging variance (l. 884-888) depends only on the positions and the semi-variogram, not on values (l. 882); average prediction variance (l. 903-917); Fisher information criterion (l. 953-958). Diggle & Lophaven (2006) Bayesian predictive design (eq. 2-3, l. 998-1005) for Kattegat surface salinity found a regular design is often not the best, no gain printed (l. 1021). No exact algorithm for the best site set (l. 1028); simulated annealing and a greedy sequential addition that lowers average kriging variance the most are used (l. 1029-1034); under a Gaussian field the entropy-optimal next site has the largest conditional variance (l. 1045).
- **Time and sensors** (l. 1245-1247, 1420-1423): revisiting sites is better for trend, new sites for status; split-panel designs are thought to satisfy both. For sensor networks a pilot on a few nodes is recommended, and nodes may sense only for limited periods (power).
- **Applications cited** (l. 1464-1553): Queensland river sites (Dixon 1999, three case studies), Queensland EHMP (first to third order streams are nearly 90 % of stream length), Murray-Darling Sustainable Rivers Audit (many dry sites), US National Surface Water Survey from 1983, EMAP, Oregon Coho, Lake Ontario, Mid-Atlantic streams. No sensor counts, no gains against regular or random designs in numbers.
- **Conclusion** (l. 1574): probability-based designs such as GRTS suit sparse sampling of stream networks.
- **Not found:** mutual information, value of information, sensor error or drift, a vineyard or microclimate case.
- **Citation slips in the paper:** text cites Overton & Stehman as [74] (that is Sarno 2005; Overton & Stehman is [67]); cites Martin et al. as [54] (McDonald 2003; Martin is [52]); Hansen et al. 1983 pages printed reversed. Recorded as printed.

## Dependence

- No equation is another's computed here; the paper reviews Cressie 1993, Muller 2000, Zimmerman 2006 and others. GRTS is a design lineage (each a generalisation of the one before), not a shared calibration. No data or model shaped any design.

## Bearing (2026-10-18)

Strand 6 (methods):

- **What Agrarium can take:** two ways to choose where a few sensors go in a block. (1) A spatially balanced probability design (GRTS-type), which keeps estimates design-based and unbiased without a model of the field. (2) A model-based choice that minimises average kriging variance, which needs a variogram (from a pilot or from the microclimate papers) and is solved by greedy addition or annealing, since no exact method exists. With a known covariance, a regular or triangular grid is the baseline to beat.
- **For the sweep:** the kriging variance depends only on positions, so layouts can be compared before any sensor is bought; a pilot on a few nodes first, as the paper advises.
- **Limits:** streams (network distance), not vineyard cold-air flow; no numbers on the gain of any design; the paper does not treat sensor error.

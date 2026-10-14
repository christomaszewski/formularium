---
id: pallas2009
citation: Pallas, B. 2009. Modélisation dynamique des interactions plante-environnement : application à l'étude des interactions entre les relations sources-puits et les processus de développement chez la vigne. PhD thesis, École Centrale Paris (HAL tel-00448756)
doi:
read: 2026-10-14, a targeted reading of the front matter (l. 1-60), Ch. I §3 (l. 1050-1060), Manuscript 1 (Pallas et al. 2008, Physiol. Plant. 134:49-63; abstract, methods, Tables 1-2, results, l. 2084-2918), the phyllochron sentence and Q/D caption of Manuscript 2 (l. 3966-3968, 5812-5822) and the water terms of Manuscript 3 (l. 6700-7062), by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; printed p. 53 (PDF p. 59, Eqs 6-8) read in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [shoot development, phyllochron, leaf area, source-sink, water status]
records: [pallas2008.shoot_development]
datasets: [pallas2008.montpellier_pots]
files: [beno_t_2009.pdf]
---

# Pallas 2009: shoot development of potted Syrah and Grenache N on thermal time

A French doctoral thesis (defended 22 September 2009, l. 60) on a source-sink model of the
vine (GreenLab). It reprints three papers. Manuscript 1 is Pallas, Louarn, Christophe, Lebon
& Lecoeur 2008, Physiologia Plantarum 134:49-63 (DOI 10.1111/j.1399-3054.2008.01100.x, printed
in the thesis), which the project could not get from the publisher (closed). The record is of
that 2008 paper, read here, so its id is pallas2008. Manuscripts 2 and 3 are read only for the
numbers below.

## What it holds

- **Experiments** (l. 2225-2255, 2313): potted Syrah (clone 174) and Grenache N (clone 224) on
  Fercal at Montpellier, in 2003, 2004 and 2006; 12 plants for each cluster-load treatment
  (0C, 1C, 2C, 6C); counted and measured through 1200 °Cd (l. 2313). Water was kept above
  75 % of transpirable soil water (l. 2246), so no water limit.
- **Thermal time** (Eq. 1, l. 2328-2329): the daily sum of the mean temperature above Tb =
  10 °C, from primary budburst, after Lebon et al. 2004. The text layer garbles the equation.
- **Primary-axis leaves** (Eq. 2, l. 2518, 2686): 0.044 leaf per °Cd for both cultivars, so
  about 23 °Cd a leaf (l. 6717). Syrah: leaves = 0.044 x + 2.75 (R² 0.991, n 481). Grenache
  N: leaves = 0.044 x + 3.50 (R² 0.987, n 441). Treatments pooled.
- **Secondary axes:** a lag of about six phyllochrons, almost 120 °Cd (l. 2587), and a mean
  of 126 °Cd, SD 32, pooled over cultivars and zones, with no treatment effect (l. 2603). An
  axis is finished after 200 °Cd without a new phytomer, nine primary phyllochrons (l. 2403;
  printed p. 53).
- **Leaf area from leaf length** (Eqs 6-7, printed p. 53, l. 2354-2360; L in mm, area in
  cm²): Syrah 0.011 L² + 0.1494 L (n 182, r² 0.97, Cve 0.13); Grenache N 0.0091 L² +
  0.2547 L (n 135, r² 0.95).
- **Secondary-axis leaf area from leaf number** (Eq. 8, printed p. 53, l. 2375-2376):
  a N² + b N, Syrah a 0.93, b 56.63 (n 42, r² 0.97); Grenache N a 1.03, b 52.68 (n 37,
  r² 0.98).
- **Cluster load** (l. 2436): cluster-to-leaf ratio from 16.7 m²/kg (Syrah 1C, exp. 2) down to
  1.98 m²/kg (6C). Table 1 row: Syrah 1C exp. 1, mean cluster dry weight 61.2 g, ratio
  12.1 m²/kg (l. 2454).
- **Plant state at 1200 °Cd** (Table 2, Syrah 0C, exp. 1, l. 2479): 51.4 phytomers on the
  primary axis, 0.53 m² primary leaf area, 3.7 m axis, 388 secondary phytomers, 3.18 m²
  secondary leaf area, 12.1 m secondary length. Other rows run 0.53-0.66 m² primary and
  2.89-3.99 m² secondary (l. 2479-2502). Table numbers are from the text layer.
- **Manuscript 2** (l. 5819): the probability that an axis keeps developing, on the source-sink
  ratio Q/D, P = 1/(1 + exp(-(x - a)/b)): P0 axes a 0.023, b 0.051 (r² 0.94); P1-P2 axes
  a 0.083, b 0.044 (r² 0.92).
- **Manuscript 3, water** (l. 6920-7010): the growth cycle is 23 °Cd well watered (l. 6966),
  lengthened by a sigmoid in the fraction of transpirable soil water: d = 23 (1 + a exp(b
  (FTSW + c))) (Eq. 21, l. 6970); the leaf-production probability has the same sigmoid in
  FTSW times Q/D terms (Eq. 22, l. 6981-6986). The three parameters of each are only
  symbols; the thesis says they were estimated from the literature (l. 7036-7062). The
  radiation-use water factor is 1/(1 + 6.20 exp(-6.36 (FTSW + 0.14))) (Eq. 24, l. 6936),
  Lebon et al. 2006's. Experiment 6 is Lebon's data at FTSW 0.74, 0.31 and 0.18, 803 °Cd
  (l. 6978-6980). The model's RRMSE is 12.2 % for total leaf area and 22.1 % for total dry
  mass (l. 7003-7004).
- **Not printed in what was read:** budburst dates, E-L 12, flowering, bunch counts, canopy
  height, width or porosity, a full-canopy leaf area, any infection threshold by leaf age.
  The text layer prints + as 1 and the minus sign as 2; Eqs 6-8 and Eq. 21-22 were checked in
  the page images.

## Dependence

- **Borrowed:** thermal time and Tb after Lebon et al. 2004 (l. 2329); the three-phase
  secondary-axis scheme and the 200 °Cd end after Louarn et al. 2007 (l. 2292, 2352, 2403);
  the leaf-length form after Schultz 1992 (l. 2351). Lebon et al. 2004, Louarn et al. 2007
  (both Annals of Botany) and Schultz 1992 could not be obtained from this VM; they are
  listed in literature/unread/2026-10-14-truth-phenology-closed.md.
- **Water terms of Manuscript 3:** the 23 °Cd cycle from Louarn et al. 2007, the FTSW sigmoid
  and Eq. 24 from Lebon et al. 2006, cited, not fitted here. Experiment 6 is Lebon's data:
  anything fitted to it shares calibration data with Lebon et al. 2006.
- **Shared structure:** Manuscripts 2 and 3 are GreenLab (Q/D source-sink, after Letort and
  Mathieu): assumptions of form shared with other GreenLab models. Shared authors (Lecoeur,
  Lebon, Louarn, Christophe) are a flag only.
- **Fitted** to the authors' own pot data; no other model's output.

## Bearing (2026-10-14)

- **Growth on thermal time, kin to the engine by form:** leaves a linear function of degree-days
  above 10 °C, secondary axes after a lag in °Cd. Said so, not hidden.
- **Usable numbers:** the phyllochron (0.044 leaves per °Cd, about 23 °Cd a leaf, base 10 °C),
  the secondary-axis lag (126 °Cd) and the leaf allometries. Potted vines with cluster loads,
  one shoot a plant, not a vineyard.
- **Water:** the one water-status form for phytomer timing the search found (Eq. 21), but its
  parameters are not printed, so it cannot be run from the thesis. The record leaves it out.

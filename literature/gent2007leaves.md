---
id: gent2007leaves
citation: Gent, David H., Turechek, William W. & Mahaffee, Walter F. 2007. Sequential Sampling for Estimation and Classification of the Incidence of Hop Powdery Mildew I: Leaf Sampling. Plant Disease 91(8):1002-1012
doi: 10.1094/PDIS-91-8-1002
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [powdery mildew]
crops: [hop]
regions: [Oregon, Washington]
processes: [sampling, observation]
records: []
datasets: []
files: [10-1094-pdis-91-8-1002.pdf]
---

# Gent, Turechek & Mahaffee 2007: sequential sampling of hop powdery mildew on leaves

From USDA-ARS (Corvallis) and Cornell.

## What it holds

- Sampling unit: 10 leaves from one plant; 100 (Oregon) or 75 (Washington) plants per transect; each leaf scored by eye for symptoms (l. 106, 108, 110).
- The plans use binary power law parameters fitted earlier to 198 assessments in 54 yards in 2000-2001 (l. 22, 89): ln(Ax) = 0.457, b = 1.099, so a = 0.198 (l. 253, 254, 255).
- Independent check: 27 yards (16 Oregon, 11 Washington), 2004-2005; 104 yard-level sets (l. 137, 139, 84). The refit there gives ln(Ax) = 0.621, b = 1.136, a = 0.255 (l. 268, 270).
- Wald's SPRT as modified by Madden and Hughes 1999 (l. 217). Thresholds pt = 0.025, 0.05, 0.10, 0.15 (l. 151). ASN at pt: 51, 33, 21, 9 (l. 428).
- Beta-binomial stop lines, row level: 93.8 or 96.2% correct at pt = 0.025 (l. 431); 95.2 or 95.7% at pt = 0.10 (l. 434). Always above 86% (l. 41).
- A decision is scored against the data set's own observed incidence (l. 266).
- Precision C = 0.1 cannot be reached at low incidence (l. 25).
- No model dates the data; symptoms are scored directly.

## Dependence

- Stop lines from the beta-binomial and the binary power law, with BPL parameters from Turechek & Mahaffee 2004, not fitted here; scored against each data set's own observed incidence.
- The binary power law is the form of the engine's sampling bound (Madden & Hughes 1999): the same structure for an observation piece.

## Bearing (2026-10-08)

- **Held out by structure** if the truth's scouts sampled this way (D26); its fitted heterogeneity is field data a scout's sampling could use. The authors note the parameters underestimate the validation sets' heterogeneity.

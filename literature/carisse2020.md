---
id: carisse2020
citation: Carisse, Odile, Levasseur, Audrey & Provost, Caroline. 2020. Influence of leaf wetness duration and temperature on infection of grape leaves by Elsinoë ampelina under controlled and vineyard conditions. Plant Disease 104(11):2817-2822
doi: 10.1094/PDIS-02-20-0262-RE
read: 2026-10-10, in full, equations in the page images, by a reading agent (claude-haiku-5-5); 48 quotes checked by scripts/verify_quotes.py; equation 6 evaluated by the main session in the page image (p. 2820)
status: read
diseases: [anthracnose]
crops: [grapevine]
regions: [Quebec]
processes: [infection, leaf wetness]
records: []
datasets: []
files: [ca_anthracnose_wetness_infection_2020.pdf]
---

# Carisse et al. 2020: anthracnose infection by wetness and temperature

## What it holds

- **Chamber:** Vidal, 0-24 h of wetness at 5-30 °C; optimum 25 °C, minimum wetness 4 h at
  25 °C and 6 h elsewhere (other minima elsewhere in the paper).
- **Model:** a Richards curve, RDS = A[1 - exp(-rw)]^(1/(1-m)), with A = -0.5506 + 0.1221T -
  0.0025T², r = (8.1517/T) exp[-0.5 (ln(T/28.5159)/0.6577)²] and m = 1.0553 (eq. 6).
- **The printed equation fails at one point** (computed 2026-10-10): at 25 °C, A = 0.94 and
  r = 0.32; at 4 h, [1 - e^(-1.28)]^(-18.1) x 0.94 = 339, where Fig. 1 shows about 0.09.
  With m above 1 the form needs a plus sign or a scale term; as printed it cannot have made
  Figs 1 or 3.
- **Vineyard:** 264 observations; the years are given as 2006-2008 and as 2016-2018; the
  risk chart's 93.9 % correct does not follow from the printed counts.

## Dependence

- None. Its wetness is measured by sensors with a 2 h dry-gap rule (Magarey et al. 1993).

## Bearing (2026-10-10)

- For Cooptera: an anthracnose infection model that cannot be used as printed.

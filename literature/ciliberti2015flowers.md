---
id: ciliberti2015flowers
citation: Ciliberti, Nicola, Fermaud, Marc, Languasco, Luca & Rossi, Vittorio. 2015. Influence of Fungal Strain, Temperature, and Wetness Duration on Infection of Grapevine Inflorescences and Young Berry Clusters by Botrytis cinerea. Phytopathology 105 (3):325-333
doi: 10.1094/PHYTO-05-14-0152-R
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [Botrytis bunch rot]
crops: [grapevine]
regions: [Piacenza]
processes: [infection]
records: []
datasets: []
files: [10-1094-phyto-05-14-0152-r.pdf]
---

# Ciliberti et al. 2015: Botrytis infection of inflorescences and young clusters

From the Università Cattolica (Piacenza) and INRA Bordeaux.

## What it holds

- Eight B. cinerea strains (transposa and vacuma) came from Bordeaux-region grapevine (1998) and Metaponto strawberry (2009) (l. 129, 128). Inflorescences and young clusters were taken from an unsprayed Barbera vineyard at Ziano Piacentino (l. 119).
- Strain, growth stage and their interaction explain 19.9, 31.7 and 36.9% of the variance; transposon genotype only 6.5% (l. 275, 276, 31).
- Temperature x wetness test: strains 18.13T and 18.21V, stages 55, 65, 73, 5-30 C, 0-48 h (l. 187, 188). Optimum is 20 C; lowest at 30 C, low at 5 C.
- Model 1: y = [a Teq^b (1 - Teq)]^c / [1 + exp(d - e x)], x = hours of wetness, Tmin 0 C, Tmax 35 C (l. 161, 479). Pooled: a 3.56, b 0.99, c 0.71, d 1.85, e 0.19, R2 0.72, MAE 0.12 (l. 472). Single cases R2 0.88-0.94 (l. 351).
- y is relative: incidence divided by that strain-stage's incidence after 48 h at 20 C (l. 151).
- The same form fits germination (Tmin 0, Tmax 40; a 4.414, b 0.982, c 0.852, d 3.089, e 0.490; R2 0.94; l. 240, 241, 242) and mycelial growth (R2 0.87; l. 288).
- Data are the authors' own laboratory counts; no earlier model produced or dated them (l. 174). Nair and Allen's 96% in 4 h at 20 C is a comparison only (l. 417).

## Dependence

- Its own inoculations; no model dated the data. The form is a beta in temperature times a logistic in wetness (l. 181-185), Tmin and Tmax fitted.
- Rossi, Languasco and Fermaud: Rossi and Languasco are authors of engine models (Brischetto 2020-2021). Under D19 it was kin for them; under D27 they are flags.

## Bearing (2026-10-08)

- **A flag now, not kin.** Its form is the question of D33 (a beta temperature response times a wetness function, like Magarey's); clear of the engine's Broome either way, whose form is a logit polynomial. The pooled equation rests on two strains.

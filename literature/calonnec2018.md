---
id: calonnec2018
citation: Calonnec, Agnes, Jolivet, Jerome, Vivin, Philippe & Schnee, Sylvain. 2018. Pathogenicity traits correlate with the susceptible Vitis vinifera leaf physiology transition in the biotroph fungus Erysiphe necator: an adaptation to plant ontogenic resistance. Frontiers in Plant Science 9:1808
doi: 10.3389/fpls.2018.01808
read: 2026-10-10, in full, Tables 4-5 in the page images, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [ontogenic resistance, infection, sporulation]
records: []
datasets: [calonnec2018.bordeaux]
files: [q186.pdf]
---

# Calonnec et al. 2018: leaf age and powdery mildew susceptibility

## What it holds

- **Material:** leaves of known age (days since a leaf reached 3 cm and was tagged) from
  two Bordeaux vineyards, Cabernet Sauvignon (2005) and Merlot (2009-2010); sprayed 6-20
  days before sampling, so not untreated.
- **Assay:** 22 mm discs, 22 °C, 12:12 h; infection efficiency at 72 h, sporulation by
  particle counter, colony diameter at 14 days.
- **Fits:**
  - infection efficiency = 0.606 exp(-0.086 x age in days) (Cabernet Sauvignon, R² 0.57);
  - Merlot: 0.63 exp(-0.095 age) and 0.38 exp(-0.067 age); a third fit is printed with an
    intercept of 2243, impossible for a proportion;
  - logit P(sporulation above 3,000/cm²) = 4.12 - 0.20 age: P = 0.8 at 13.3 days, 0.5 at
    20 days (n 497, AUC 0.927);
  - sporulation peaks on leaves 3-6 days old.
- Leaves gain about one per 21 degree-days above 10 °C. Susceptibility falls as leaves turn
  from sink to source (soluble sugars rise).

## Dependence

- None: powdery mildew, and no engine model.

## Bearing (2026-10-10)

- For Cooptera's powdery mildew, and for a truth's host: leaves lose susceptibility within
  about two weeks, by a measured curve.

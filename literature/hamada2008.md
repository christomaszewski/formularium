---
id: hamada2008
citation: Hamada, Emília, Ghini, Raquel, Rossi, Paulo, Pedro Júnior, Mário José & Fernandes, Jeferson Lobato. 2008. Climatic risk of grape downy mildew (Plasmopara viticola) for the State of São Paulo, Brazil. Scientia Agricola (Piracicaba) 65 (note)
doi: 
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5), equation 1 in the page image; 41 quotes checked by scripts/verify_quotes.py; the coefficients compared with lalancette1988.infection by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [São Paulo]
processes: [infection, climatic risk, leaf wetness]
records: [lalancette1988.infection]
datasets: []
files: [hamada2008_scientia_agricola.pdf]
---

# Hamada et al. 2008: Lalancette's infection efficiency mapped over São Paulo

## What it holds

- **What it maps:** downy mildew severity (lesions/cm²), September to April, across São
  Paulo State, with Lalancette et al. 1988's infection-efficiency model in a GIS.
- **The equation as printed:** IE = k(1 + e^-p)^(1/(1-m)), k = -0.71 + 0.018T - 0.0005T² +
  0.01, p = -0.24W + 0.070WT - 0.0021WT², m = 1.2; severity = IE x 11.2. Lalancette prints
  the intercept as -0.071; -0.71 is a misprint.
- **Inputs:** monthly mean temperature from Agritempo (58 São Paulo stations and 25
  neighbouring, 1961-2004, kriged to 0.01°), and CRU monthly RH, 1961-1990. Wetness comes
  from RH by an equation of Hamada et al. 2007, not printed here.
- **Results:** Jales 0.07-0.23 lesions/cm²; Jundiaí and São Miguel Arcanjo up to 0.70.
- **No validation** against observed disease.

## Dependence

- Computes Lalancette 1988's infection equation (copied, not refitted). That model is not
  on the engine's list; Magarey 2005's P. viticola row was fitted to the same data, but the
  engine runs Magarey with other parameters.

## Bearing (2026-10-09)

- A map of a model's output, not of disease. Of no use as a truth pattern.

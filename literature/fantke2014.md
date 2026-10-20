---
id: fantke2014
citation: Fantke, P., Gillespie, B. W., Juraske, R. & Jolliet, O. 2014. Estimating half-lives for pesticide dissipation from plants. Environmental Science & Technology 48:8588-8602
doi: 10.1021/es500434p
read: 2026-10-20, abstract, methods (Eqs 1-4) and results 3.1-3.3 with Table 1, by the main session; pp. 8589, 8591 and 8595 read in the page images (copy from a Wayback capture of the publisher's PDF)
status: read
diseases: []
crops: []
regions: []
processes: [fungicide residue, dissipation half-life, temperature dependence]
records: [fantke2014.plant_dissipation]
datasets: [fantke2013.halflives]
files: [fantke_2014.pdf (the 2026-10-20 drop)]
---

# Fantke et al. 2014: pesticide half-lives on plants, corrected for temperature

Regressions on 4,442 measured dissipation half-lives (333 pesticides, 183 plants): how
temperature shortens them, and a half-life at 20 °C for each pesticide on an average plant
in the field.

## What it holds

- **Temperature** (Model I, 1,030 half-lives with reported air temperature): log half-life
  falls by 0.01995 per K (Eq 1, p. 8589), so Q10 = 1.22, activation energy 14.25 kJ/mol and
  an Arrhenius factor of 1.02 per K (p. 8591); R²adj 0.638, RMSE 0.27. Temperature alone
  explains 23.2 % of the variance, substance 52 %, plant 26.8 %.
- **Half-lives at 20 °C** (Model II, Table 1): 0.21 days (plant-derived pyrethrins) to 30.8
  days (dalapon), 95 % between 0.9 and 18 days; for vineyard fungicides, e.g. mancozeb 4.69,
  folpet 5.19, metalaxyl 5.81, azoxystrobin 3.53, cymoxanil 1.61, dimethomorph 5.14,
  tebuconazole 7.67, penconazole 8.06 days.
- A third model (III) predicts half-lives from chemical class and properties for substances
  without data (R²adj 0.465).

## Dependence

- Fitted to the half-lives collated by Fantke & Juraske 2013 (not held), the same
  literature the PPDB's plant set was checked against (literature/lewis2017). No disease
  model.

## Bearing (2026-10-20)

- Recorded as `fantke2014.plant_dissipation` with the dataset `fantke2013.halflives`
  (Table 1's fungicide rows from the text layer, five checked in the page image). Kin
  report (cooptera@6f8d0a2): independent, as expected.
- For Agrarium's grower and Cooptera's E6: with `lewis2017.residue_dt50` it gives a
  fungicide residue that decays first-order at a rate set by the day's temperature; the
  vine-leaf values in the PPDB are longer than these average-plant half-lives, so the plant
  matters.

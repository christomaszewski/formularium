---
id: cortazar2010
citation: García de Cortázar-Atauri, I., Chuine, I., Donatelli, M., Parker, A. K. & Van Leeuwen, C. 2010. A curvilinear process-based phenological model to study impacts of climatic change on grapevine (Vitis vinifera L.). Agro2010, the XIth ESA Congress, Montpellier, pp. 907-908
doi:
read: 2026-10-13, in full (two pages, both read as images by the reading agent, claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; the venue and pages come from Piña-Rey et al. 2021's reference 64, since the copy prints none; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Europe, France]
processes: [phenology, flowering, veraison, maturity, climate projection]
records: []
datasets: []
files: [2010-cortazar-atauri-url-garcia-de-cortazar-2010-curvilinear-.pdf]
---

# García de Cortázar-Atauri et al. 2010: a Wang-Engel phenology model for Europe

A two-page congress paper: BRIN for budbreak, then Wang & Engel's curvilinear
temperature response for flowering, veraison and maturity, with Topt and F* fitted per
cultivar, run on generated weather over Europe for 2020 and 2050.

## What it holds

- **Model:** budbreak by BRIN (Bidabé's chilling, Richardson's forcing; l. 27-29, the
  parameters in the 2009 paper, l. 39); then Wang & Engel 1998's response with Tmin 0 °C
  and Tmax 40 °C fixed after Jones 2003 (l. 33), Topt and F* fitted (method not printed)
  to "a phenological dataset (Parker 2008)", a thesis the paper does not describe
  (l. 34); maturity set at 45 % of the flowering-to-maturity forcing (l. 35).
- **Table 1 (Topt °C / F*):** Chardonnay 30.3/18.8, 24.3/56.2, 24.3/46.0; Syrah
  32.0/12.5, 27.0/52.8, 27.0/43.2; Cabernet Sauvignon 30.2/20.3, 24.3/63.0, 24.3/51.5
  for budbreak-flowering, flowering-veraison and veraison-maturity (l. 50-54); which
  column is which stage is unclear in the layout (l. 41-44).
- **Runs:** LARS-WG weather from an ECMWF 1982-2008 baseline under HadCM3 A1B and B1 for
  2020 and 2050 (l. 66-70); outputs as days of change (l. 71). In some southern
  vineyards (Spain, Portugal, southern Italy, Greece) veraison and maturity did not
  advance or were delayed, which the authors credit to the curvilinear response
  (l. 94-96), against linear-model projections of over 30 d (l. 98).

## Dependence

- **Borrows** Wang & Engel 1998 and BRIN (`cortazar2009.brin`); fitted to Parker 2008's
  dataset, later the GFV data of `parker2011`. Jones 2003 and Bidabé are cited without
  reference entries.
- **Authors:** García de Cortázar-Atauri and Parker on `cortazar2009` and `parker2011`.

## Bearing (2026-10-13)

- A threshold model (heat to F*), not the requested form; the point for Agrarium is the
  warning that a curvilinear response can delay veraison in hot regions where a linear
  one advances it. The Topt and F* values are usable as a prior, with the data behind
  them unseen.

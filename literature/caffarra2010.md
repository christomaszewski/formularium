---
id: caffarra2010
citation: Caffarra, Amelia & Eccel, Emanuele. 2010. Increasing the robustness of phenological models for Vitis vinifera cv. Chardonnay. International Journal of Biometeorology 54(3):255-267
doi: 10.1007/s00484-009-0277-5
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which read Table 3 on the page image; 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Tables 3 and 4 (pp. 259, 261) read in the page images by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Trentino, Veneto, Piedmont]
processes: [phenology, budburst, flowering, veraison, dormancy, chilling]
records: [caffarra2010.chardonnay, chuine2000.unified]
datasets: [caffarra2010.conegliano]
files: [2010-caffarra-10-1007-s00484-009-0277-5.pdf]
---

# Caffarra & Eccel 2010: a chilling-forcing Chardonnay model with all its parameters

Chuine's Unified model cut to six parameters for budburst, then one forcing requirement
each for flowering and veraison, fitted on Conegliano's 39 years and tested on four
northern Italian series. A threshold model, but a complete printed one for a Penedès
cava variety, from the Fondazione Edmund Mach.

## What it holds

- **Data** (`caffarra2010.conegliano`): Conegliano (Susegana 1969-2000, Spresiano
  2001-2007), San Michele, Mezzocorona, Cembra and Carpeneto, BBCH 07, 65 and 85
  (l. 74-82, Table 1); gaps in daily temperature filled by regression (l. 86).
- **Model** (`caffarra2010.chardonnay`; Table 3, p. 259): chilling from 1 September as
  Σ 2/(1 + exp(a (Tm − c)²)), a bell peaking at c; forcing once the chilling sum
  passes Ccrit as Σ 1/(1 + exp(−0.26 (Tm − 16.06))), the sigmoid fixed on Pouget
  1968's Merlot data (Fig. 2, l. 224-228); budburst when the forcing sum reaches Fcrit =
  co1 exp(co2 × chilling), with chilling counted to day tc; flowering and veraison by
  the same forcing from the simulated previous stage (l. 243-247).
- **Parameters** (Table 4, p. 261): a 0.005, c 2.800 °C, co1 176.260, co2 −0.015, Ccrit
  78.692, tc 234 (21 April, l. 901); Fcrit 24.710 (flowering), 51.146 (veraison). Bounds
  from Pouget: Ccrit 5-100, c 0-10 (l. 218-222). Fitted by the Metropolis algorithm
  (l. 270).
- **Scores:** within Conegliano R² 0.36 (budburst), 0.79, 0.69 (l. 363); at the four
  other sites the models explained 33, 41 and 52 % of the variance beyond the site
  mean (l. 445-447; the discussion says 36 %, l. 892); at Cembra, the mountain site,
  flowering and veraison ran late 85 and 91 % of the time (l. 443). Better than linear
  models in the three warmest years at every site (Table 6).

## Dependence

- **Borrows** Chuine 2000's Unified model (`chuine2000.unified`, a trail record) and
  Pouget 1968's forcing data; fitted to observed dates, the later stages to simulated
  starts (a model's dates, l. 244). Kin to `cortazar2009.brin` by the chilling-then-
  forcing form. The 2011 projection paper (`caffarra2011`, pending) runs it.

## Bearing (2026-10-13)

- A threshold model; for Agrarium, the first complete chilling-forcing parameter set for
  Chardonnay in the catalogue, with its transfer error stated (a third to a half of the
  variance explained away from the calibration site).

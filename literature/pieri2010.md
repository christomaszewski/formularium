---
id: pieri2010
citation: Pieri, P. 2010. Modelling radiative balance in a row-crop canopy: Row-soil surface net radiation partition. Ecological Modelling 221(5):791-801
doi: 10.1016/j.ecolmodel.2009.11.019
read: 2026-10-30, in full; Eqs 1-5 and Figs 5, 8-12 read in page images (pp. 792-799); by a reading agent and note writer (claude-sonnet-5-5); 38 of 38 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Bordeaux, Graves]
processes: [net radiation, longwave radiation, view factors, row geometry, soil surface radiation, atmospheric emissivity, leaf temperature]
records: []
datasets: []
files: [dr1030_pieri2010.pdf (the 2026-10-30-missing drop, from Chris)]
---

# Pieri 2010 (row-soil partition): net radiation split between a vine row and the soil, with the longwave by view factors

The first of two papers on one model (by page order; neither title says "Part I", and this paper cites the other as "Pieri, in press", p. 791). It adds longwave exchange and a measured partition to Riou et al. 1989's shortwave row model, for the row as a whole and the inter-row soil as a whole. No position inside the inter-row and no leaf layers.

## What it holds

- **Balance** (Eq. 1, p. 792, page image): Rns = Rgs + F_SS Ra + F_FS eps_F sigma T_F^4 - eps_S sigma T_S^4; "a similar equation could be written about Rnv". eps_F = eps_S = 0.98, sigma 5.67e-8 W m-2 K-4 (l. 130 and next line). F_SS (sky to soil) and F_FS (foliage to soil) are not printed as formulas, and their normalisation (per m2 of soil or of ground) is not stated.
- **Shortwave** (Sec. 2.2, p. 792): Rgs and Rgv come from "a previously validated geometric model" (Riou et al. 1989, rectangular rows, porosity, leaf and soil albedo, direct and diffuse input). No shortwave equation is printed.
- **View factors** (Eq. 2, p. 793, page image): F_EW = tan(1/2 arctan(Hf/(D - w))), the factor from one wall to the opposite wall, by view-factor algebra of an enclosure (Ozisik 1981). Porosity p: a factor with the porous wall is multiplied by (1 - p); a factor with a surface behind the wall is multiplied by p (Fig. 1b). Other factors: "calculated from the same rationale", not printed.
- **Atmospheric radiation** (Sec. 2.3): Idso & Jackson 1969, air temperature only, corrected for the diurnal course after Arnfield 1979. Neither formula is printed here (Paper II Eq. 21 prints Idso-Jackson).
- **Temperatures:** air temperature near the leaves stands in for leaf temperature (shaded leaves near air; sunlit 5-10 K above, Fig. 2). Error at most about 15 W m-2 on the rows' emission (Fig. 3, day 209). Soil surface temperature extrapolated from a 6-level profile by a second-order difference (Eq. 3, p. 795, page image) and averaged over six positions; 1 K on Ts is about 1.3 % of emitted longwave; averaging temperatures instead of fluxes underestimates by 1-3 W m-2.
- **Site** (Sec. 3.1): near Bordeaux, Graves (44 deg 40' N, 0 deg 25' W), Cabernet Sauvignon, 5000 plants/ha, rows NE-SW, 27 deg off north-south, D 2 m, foliage 0.35 m wide from 0.4 to 1.6 m (Hf 1.2 m, Fig. 5), vines about 1 m apart; bare soil. Days 198-242 of an unprinted year. LAI 1.38 and 1.3 (days 214, 235; 2.75 m2 per m of row); LAI 2000 gave 1.14. Row porosity 0.25 (threshold on black-and-white pictures), leaf albedo 0.25 (spectrographic, 300-3000 nm), soil albedo 0.18; well watered (predawn about -0.1 MPa).
- **Sensors** (Sec. 3.2): Rg and Rn at 6 m; five net radiometers (Swissteco S1, Crouzet) at 0.27 m on a tram at 0.033 m/s on two 12 m rails, at 0.11, 0.52, 0.98, 1.52, 1.84 m from the east row axis; 30 min means of about 45 readings. Rns = 0.125 Rns1 + 0.25 Rns2 + 0.25 Rns3 + 0.25 Rns4 + 0.125 Rns5 (Eq. 4, p. 798). Rnv = Rn - Rns (Eq. 5).
- **Corrections to the data:** only the delay of direct light at sensor height against the soil (Fig. 8); the other errors (sensor shade, rails, height effects on longwave, sunlit-shade strips) were calculated and left, about 8 W m-2 (1.4 %) together.
- **Result:** mean error about 20 W m-2 on 30 min Rns, "without any significant bias"; calculated vs measured y = 1.01 x + 9.9, r2 0.98, n = 551, days 207-221 (Fig. 11, page image). Rns underestimated at night and on fully diffuse days (rain on day 211), so Rnv overestimated.
- **Partition:** on clear days the daily share of Rn going to the rows is 0.48, and the shortwave share Rgv/[(1 - a) Rg] is 0.55 (l. 653, Fig. 13). Net longwave puts Rnv above Rgv in early morning and most of the afternoon. Vineyard albedo 0.17 at its daytime minimum. Soil losses nearly balance gains from sky and rows except late afternoon.

## Dependence

- Computes Riou et al. 1989 (`riou1989.row_interception`) for the shortwave; its view factor is the one in `pieri2003.row_interception` Eq. 1. A shared equation with the truth's catalogue, not with the engine.
- Idso-Jackson and Arnfield are cited, not held. Rd/Rg: "an experimental relation, from direct measurements in the same region", not printed.
- Own data, one season; the soil parameters and porosity are set on the same plot and not fitted to Rns as far as the text says.
- Same group as `pieri2003`; Gaudillere reviewed it (acknowledgements). A flag only: the engine's `cortazar2009` records have Gaudillere as an author.

## Bearing (2026-10-30)

- Gives the row-versus-soil split of net radiation, not the sun reaching a lower leaf or a cluster; for that see `pieri2010b`. Useful as a check: a clear-day row share of net radiation near 0.5 at D/Hf 1.7 (arithmetic, not printed: D/Hf = 2/1.2).
- Shortwave must be coded from Riou 1989; its Eq. 17 and 27 are neither restated nor corrected here.

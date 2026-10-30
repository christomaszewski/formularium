---
id: gowdy2022
citation: Gowdy, M., Suter, B., Pieri, P., Marguerit, E., Destrac Irvine, A., Gambetta, G.A. & van Leeuwen, C. 2022. Variety-specific response of bulk stomatal conductance of grapevine canopies to changes in net radiation, atmospheric demand, and drought stress. OENO One 56(2):205-221
doi: 10.20870/oeno-one.2022.56.2.5435
read: 2026-10-27, in full; Eqs. 1-4 and Tables 1-2 read in page images (Eqs. 1-4 garbled in extraction); Figures 1-9 and Supplementary Tables S1-S4 not read; by a reading agent and note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Pessac-Leognan]
processes: [canopy conductance, bulk stomatal conductance, transpiration, sap flow, Penman-Monteith, vapour pressure deficit, predawn leaf water potential, net radiation absorbed by canopy]
records: []
datasets: []
files: [dr1027_gowdy2022.pdf (2026-10-27, from Chris)]
---

# Gowdy et al. 2022: whole-vine bulk stomatal conductance from sap flow, and its log-linear response to radiation, canopy VPD and predawn water potential in five varieties

Sap flow on 10 vines in a Bordeaux common garden gives canopy conductance by inverting a Penman-Monteith type equation; a regression of log10 conductance on absorbed radiation, canopy VPD and predawn water potential is fitted per variety.

**Read this first.** One season (30 June to 15 September 2020), two vines per variety, one site. The fit is on 15-minute data after dropping low-radiation, low-VPD and low-flux records (9 to 14 % of transpiration). Predawn potential is measured only six times and interpolated daily. The regression is printed as Eq. 6 for gbs but was fitted to log10(gbs) (Eq. 5); the units of the raw coefficients are not stated beside Table 2b (Rc in kW m-2 and Dc in kPa are, l. 256, grep; Psi in MPa is from the figure axes, page image).

## What it holds

- **Site and vines (l. 197):** VitAdapt common garden, 0.6 ha, Bordeaux; 52 varieties; 10 vines measured, two each of Cabernet-Sauvignon, Merlot, Tempranillo, Semillon and Ugni blanc; 30 June to 15 September 2020, 15-minute data.
- **Canopy (l. 136):** vertical shoot positioning, double Guyot; canopy 0.5 m to 1.5 m above ground and 0.4 m wide, hedged twice; rows north-south, 1.8 m by 1.0 m; SO4 rootstock. LAI from leaf counts and a leaf-size sample on three dates; porosity by phone camera (l. 153-173, grep).
- **Transpiration (l. 185):** heat balance sap flow gauges (Dynamax SGEX) on canes carrying at least 30 % of the vine, scaled by leaf area, divided by row spacing times vine spacing to give Ec in g s-1 m-2.
- **Canopy climate (l. 198):** Dc, the canopy VPD, measured at 1.15 m, the height above which flux is taken as well mixed; temperature and RH probes in radiation shields on a trellis wire at mean canopy height; global radiation hourly at a nearby station, interpolated to 15 min. Saturation vapour pressure by Teten's equation (l. 213, grep).
- **Water status (l. 229):** pressure chamber predawn leaf water potential on six dates 10 to 14 days apart, early July to early September; interpolated daily by LOESS. One rain event, 36 mm on 11 to 13 August 2020.
- **Filters (l. 222):** records dropped when Rc < 90 W m-2, Dc < 900 Pa or Ec below the vine's 30th percentile; this removes 9 to 14 % of transpiration (9 to 18 % at predawn potential below -4.0 bar).
- **gbs, Eqs. 1-4 (l. 273, l. 396; page images):** lambda Ec = [Delta Rc + rho Cp Dc / rbh] / [Delta + gamma (n + rbs / rbh)] (Eq. 1); rbs = (Delta Rc rbh + rho Cp Dc) / (lambda Ec gamma) - rbh (Delta/gamma - n) (Eq. 2); gbs = 1 / rbs (Eq. 3); rbh = rbl / (2 LAI) with rbl = 25 s m-1 (Eq. 4). Constants: n = 2 (stomata on one side), gamma = 65.8 Pa per degC, Delta = 145 Pa per degC, rho Cp = 1212 Pa per degC, lambda = 2257 J g-1, all at 20 degC.
- **Absorbed radiation (l. 358):** Rc is the shortwave flux absorbed by the canopy per unit ground area from Riou et al. 1989, using canopy dimensions, spacings, porosity, global radiation and solar angles; it is the net radiation input in Eq. 1.
- **Regression (l. 446):** log10(gbs) ~ (Rc + Dc + Psi_PD) * variety (Eq. 5), after a log10 transform because gbs is non-linear in Dc and Psi_PD and linear in Rc. rbh was dropped for collinearity with Psi_PD. Interaction terms were dropped for simplicity.
- **Fit (l. 488):** r2 0.701 (adjusted and predicted also 0.701), VIF 1.2, 1.2 and 1.1; n = 23388 records (l. 422). No RMSE is printed in the text read.
- **Standardized coefficients (Table 2a, page image; l. 644):** bRc, bDc, bPsi: Merlot 0.303, -0.558, 0.423; Semillon 0.225, -0.582, 0.458; Ugni blanc 0.256, -0.625, 0.485; Cabernet-Sauvignon 0.161, -0.560, 0.512; Tempranillo 0.255, -0.433, 0.773; intercept -0.036 in all.
- **Raw coefficients (Table 2b, page image; l. 646):** intercept 0.788 for all; bRc, bDc, bPsi: Merlot 1.110, -0.146, 0.066; Semillon 0.824, -0.153, 0.072; Ugni blanc 0.940, -0.164, 0.076; Cabernet-Sauvignon 0.589, -0.147, 0.080; Tempranillo 0.934, -0.114, 0.121. Back-transform by 10 to the power of the fit. At Rc 0.263 kW m-2 (the mean used in Figs. 5-7), Dc 1.5 kPa and Psi 0 MPa this gives about 7 mm s-1 for Merlot (arithmetic, not printed); Figure 5 (page image) reaches about 7 mm s-1 near 0 MPa.
- **Units for the raw fit (l. 666):** gbs in mm s-1; Rc in kW m-2 and Dc in kPa (l. 256, grep).
- **Transpiration runs (l. 733):** median daily transpiration 1.0 to 2.7 mm per day and maximum 2.5 to 5.5 mm per day by vine. In simulations Merlot had the largest seasonal total and Tempranillo or Cabernet-Sauvignon the smallest, in the order of the Psi coefficients (l. 736-740, grep).
- **Against the water balance model (l. 743):** generally good agreement with the Pieri and Bois 2007 model (after Lebon et al. 2003), which transpires more early and less late in the season.

## Dependence

- gbs is from Gowdy et al. 2022 (a separate paper, not held), a Penman-Monteith type equation in the Shuttleworth and Wallace 1985 two-layer scheme (Lhomme et al. 2012 form); rbl = 25 s m-1 is from Shuttleworth and Wallace 1985. No Jarvis function is used: the response is a log-linear regression with no interactions, fitted to this data.
- Rc follows Riou et al. 1989; Pieri 2010 (not held) is cited for canopy geometry. Comparison model: Pieri and Bois 2007 after Lebon et al. 2003, with T/Tmax against FTSW from Pieri and Gaudillere 2005.
- Authors: Pieri is an author here, of vanleeuwen2023 and of Pieri 2010; a flag only, not held. Shares no equation with the engine's wetness pieces.

## Bearing (2026-10-27)

- **Canopy transpiration for the truth:** gbs by variety from Rc, Dc and predawn potential, then Eq. 1 for latent heat, gives vine transpiration with a published form and coefficients for five varieties in Bordeaux, VSP, 1.8 m by 1.0 m. It needs a soil water state to supply predawn potential, which the paper takes from a water balance model. Kind of result: a regression on one season, two vines per variety, checked only against another model.
- **Canopy humidity:** Dc is an input here, not an output; the paper gives no equation that returns canopy VPD or humidity from transpiration. Agrarium would have to close the loop itself, and the paper notes that different transpiration changes FTSW and Psi (l. 802-806, grep). Not shown: leaf wetness, dew, or any disease link.
- **Limits:** one summer, one dry-farmed plot, two vines per variety; no variety result outside Bordeaux; Eq. 1 with n = 2 and the Riou Rc are for open row canopies. The variety differences are small (Rc coefficient 0.161 to 0.303 standardized) and the authors say further study may be needed to separate them.

## From the Pieri collection (2026-10-30)

Lines to add to the note gowdy2022:

- **Method paper:** the method gowdy2022 uses (Shuttleworth-Wallace big-leaf inversion on sap flow, in-canopy T and RH at 1.15 m, Riou 1989 absorbed radiation, rbl = 25 s per m) is set out in gowdy2022b (Frontiers in Plant Science 13:839378). It prints the constants (lambda 2257 J per g, gamma 65.8 Pa per C, Delta 145 Pa per C, rho Cp 1212 Pa per C) and the in-canopy sensor placement.
- **Equation sign:** Eq. 2 of the method paper prints rbh (Delta/gamma - n); inverting its Eq. 1 gives (Delta/gamma + n) (arithmetic, not printed). Check this against the page image (gowdy2022b) before coding the gowdy2022 conductance.

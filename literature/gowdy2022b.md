---
id: gowdy2022b
citation: Gowdy, M., Pieri, P., Suter, B., Marguerit, E., Destrac-Irvine, A., Gambetta, G. & van Leeuwen, C. 2022. Estimating Bulk Stomatal Conductance in Grapevine Canopies. Frontiers in Plant Science 13:839378
doi: 10.3389/fpls.2022.839378
read: 2026-10-30, in full; Eqs. 1-3 read in the page image; Figures 2-4 by caption; by a reading agent and note writer (claude-sonnet-5-5); 20 of 20 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Pessac-Leognan]
processes: [bulk stomatal conductance, Shuttleworth-Wallace, two-source energy balance, sap flow, vapour pressure deficit, in-canopy temperature and humidity, net radiation absorbed by the canopy, sensitivity analysis]
records: []
datasets: []
files: [dr1030_gowdy2022b.pdf (from Chris's Pieri collection, the inbound folder: 2022-gowdy-10-3389-fpls-2022-839378.pdf)]
---

# Gowdy et al. 2022: a two-source method for whole-vine stomatal conductance from sap flow and in-canopy air

The method behind the held gowdy2022 (OENO One): Shuttleworth-Wallace for an open vine canopy, driven by sap flow, in-canopy temperature and humidity at 1.15 m, and radiation absorbed by the canopy by the Riou 1989 model.

**Read this first.** Same vineyard, vines and season as gowdy2022 (VitAdapt, 10 vines, 30 June to 15 September 2020); this paper holds the method, gowdy2022 holds the variety-specific response. One season. Eq. 2 as printed has the term rbh (Delta/gamma - n); inverting Eq. 1 as printed gives (Delta/gamma + n) (arithmetic, not printed), so use Eq. 1 to derive it.

## What it holds

- **Site and vines (l. 335-345):** VitAdapt common garden, 0.6 ha, Bordeaux (44 47 N, 0 34 W), 52 varieties; VSP double Guyot, canopy from 0.5 to 1.5 m above ground, 0.4 m wide, hedged twice; rows N-S, 1.8 m by 1.0 m; SO4; clay-gravel soil. Climate 1991-2020: rain 902 mm, ET0 929 mm, radiation 4790 MJ per m2 per year, May-June mean maximum 25.5 C (l. 288-293). Leaf area measured in July, August and September from length and width of leaves on about 25 % of shoots; porosity by phone camera (CANAPEO).
- **Eq. 1 (page image):** lambda Ec = [Delta Rc + rho Cp Dc / rbh] / [Delta + gamma (n + rbs / rbh)], W per m2 of ground; Ec evaporative flux per ground area; Dc VPD at mean canopy height (Pa); Rc net radiation absorbed by the canopy per unit ground area; n = 2 (stomata on one side).
- **Eq. 2-4:** rbs = (Delta Rc rbh + rho Cp Dc) / (lambda Ec gamma) - rbh (Delta/gamma - n) as printed; gbs = 1/rbs; rbs = n rs / (2 LAI) links bulk and leaf resistance.
- **Constants (l. 186-200):** lambda 2257 J per g; gamma 65.8 Pa per C; Delta 145 Pa per C; rho Cp 1212 Pa per C (air at 20 C); molar volume 41.04 mol per m3 (gbs in mmol per m2 per s).
- **Boundary layer:** rbh = rbl / (2 LAI) with one-sided leaf resistance rbl = 25 s per m assumed (Shuttleworth & Wallace 1985), which avoids wind measurement; rbh is the least important predictor (Table 1). Canopy mean height zc = 1.15 m: d = 1 m, zo = 0.15 m (from d 0.62 to 0.75 h and zo 0.08 to 0.14 h of Chahine et al. 2014 for h = 1.5 m).
- **Transpiration (l. 315-333):** Dynamax SGEX heat-balance sap flow on one of two canes at 50 cm, on 10 vines, scaled by leaf area of the vine to the shoots downstream, divided by ground area per vine.
- **In-canopy air (l. 335-353):** TinyTag Plus 2 TGP-4505 temperature and RH probes in RS3 radiation shields hung on a trellis wire at mean canopy height 1.15 m; VPD via Tetens saturation vapour pressure. This is the in-canopy air state the method needs; the authors argue that placement at zc matters.
- **Absorbed radiation (l. 355-411):** shortwave by the Riou et al. 1989 model (direct, diffuse, soil-reflected minus re-reflected; inputs canopy size, row and vine spacing, porosity; Liu & Jordan 1960 for the diffuse fraction; global radiation from a CMP6 pyranometer at the vineyard, hourly interpolated to 15 min). Longwave from a pyrgeometer 1.5 m above the canopy, ground temperature by IR radiometer (emissivity 0.98 dry grass) and canopy emissivity 0.98, view factors to sky, ground and adjacent rows; then dropped from the final Rc because net longwave averaged near zero on most days (up to 30 % of total net radiation when shortwave is low, in cloud). Records with Rc below 50 W per m2 are dropped.
- **Results:** per-vine maximum gbs about 5 to 10 mm per s, peaks to 10 to 15 (literature: Sultana 7.0, Merlot 8.5, Thompson Seedless 16 and 12). Lowest gbs at the most negative predawn potential (0.0 to -1.0 MPa); a rise after 36 mm of rain on 11-13 August. Random forest minimum depths: for gbs, Ec 0.00, Dc 1.00, Rc 6.20, rbh 6.80; for Ec, gbs 0.00, Dc 1.62, Rc 3.00, rbh 5.37.
- **Claim on open canopies:** soil evaporation can exceed half of evapotranspiration, the reason for the two-source form.

## Dependence

- Shuttleworth & Wallace 1985; Lhomme et al. 2012; riou1989 (held) for radiation; Chahine et al. 2014 for roughness; shares authors, site and data with gowdy2022 (held), from which it differs by being the method note.

## Bearing (2026-10-30)

- **Vine transpiration for Agrarium:** a worked, parameterised Penman-Monteith form for a vine row in terms of ground area, with constants and the boundary-layer simplification (rbl = 25 s per m), usable as a canopy transpiration kernel once gbs is given (from gowdy2022's regression); needs in-canopy T and RH at 1.15 m, which Agrarium's microclimate already carries.
- **In-canopy sensing:** a measured design for in-canopy T and RH logging (shielded probe at mean canopy height) that Agrarium's simulated station can mimic.
- **Not shown:** the leaf wetness or humidity time series themselves, or any in-canopy wind.

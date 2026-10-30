---
id: bois2008c
citation: Bois, B., Van Leeuwen, C., Pieri, P., Gaudillere, J.-P., Saur, E., Joly, D., Wald, L. & Grimal, D. 2008. Viticultural agroclimatic cartography and zoning at mesoscale level using terrain information, remotely sensed data and weather station measurements. Case study of Bordeaux winegrowing area. VIIth International Terroir Congress (Agroscope Changins-Wadenswil)
doi: hal-00719903 (HAL id; no DOI printed)
read: 2026-10-30, in full (HAL manuscript, 8 pages); Eq. 1 checked in the page image; by a reading agent and note writer (claude-sonnet-5-5); 14 of 14 quotes found by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Gironde]
processes: [agroclimatic zoning, temperature interpolation, residual kriging, rainfall kriging, growing degree days, reference evapotranspiration, Turc, satellite radiation]
records: []
datasets: []
files: [dr1030_bois2008c.pdf (from Chris's Pieri collection, the inbound folder: 2008-bois-url-pieri-hal-00719903.pdf)]
---

# Bois et al. 2008: mesoscale climate maps of Bordeaux (rain, temperature, radiation, ET0) and their errors

Daily Tmin and Tmax, rainfall, satellite radiation with terrain, and a Bordeaux-adjusted Turc ET0 are spatialised over the vineyard region, with cross-validated errors and a thermal and rainfall zoning.

**Read this first.** A congress paper. The new content is the interpolation recipe and the error table (Table 1); the radiation part repeats bois2008b. The authors drop radiation and ET0 zoning because their errors (16 to 21 %) are too large.

## What it holds

- **Stations:** 91 stations, Cimel automatic (daily rain, Tmin, Tmax) and Meteo-France rain gauges; 601 aberrant series removed; 36 (T, 2001) to 85 (rain, 2005) stations in use. Villenave d'Ornon (44.79 N, 0.58 W; class 2 pyranometer, humidity, cup anemometer at 2 m) is the validation site for radiation and ET0. Rain 1994-2005, other variables 2001-2005.
- **Temperature recipe:** ten co-variables from a 50 m DEM and CORINE (elevation, slope, aspect, rugosity, distances to the ocean and to the Gironde estuary, urban proximity, vegetation index, forest proximity, potential solar radiation). Each day, forward stepwise multiple regression on the co-variables significant at 1 %, then ordinary kriging of the residuals added back. Done for Tmin and Tmax; mean T is their mean. Rain: ordinary kriging of period totals.
- **Radiation:** HelioClim-1 kriged to 1 km, r.sun to 50 m (see bois2008b).
- **Eq. 1 (page image), Turc re-adjusted to Bordeaux:** ET0 = 0.014 (23.88 Rs + 70) T / (T + 15), Rs in MJ per m2 per day, T daily mean in C. The unadjusted form in bois2008 has 0.013 and 50. No fit data is printed.
- **Heat sum ST10:** daily mean above 10 C, 1 January to 30 September.
- **Table 1 (cross-validation, stations left out):**
  - Rain: bias +2.6 mm (year), RMSE 75.5 mm year (9 %), 39.1 mm April-September (11 %), 26.1 mm July-September (15 %); means 807, 363, 178 mm.
  - Temperature: Tmin bias +0.1 C, RMSE 0.9 C; Tmax bias 0.0, RMSE 0.6 C (means 8.7 and 18.9 C); ST10 bias +4.4 GDD, RMSE 56.3 GDD (mean 1644).
  - Radiation at Villenave d'Ornon: bias -1.5 / -2.0 / -1.8 MJ per m2 (year, April-September, July-September), RMSE 2.7 / 3.3 / 3.2 (20, 17, 17 %), means 13.4, 19.6, 19.1.
  - ET0 (Turc with interpolated T and spatialised Rs against PM): bias -0.1 / -0.2 / 0.0 mm, RMSE 0.6 mm (21, 16, 16 %), means 2.6, 4.0, 4.0 mm per day.
- **Spatial structure:** thermal classes 2001-2005 differ by 42 to 79 GDD per class (6 to 11 days of ripening; 30 to 55 days between coolest and warmest); 64 % of the area medium, 21 % early (valley slopes, estuary), 12 % late (northwest, near the ocean), 1 % very late. Thermal pattern is highly redundant between years. April-September rain: Medoc recurrently drier, Pessac-Leognan wetter; the July-September rain pattern changes every year.

## Dependence

- Same data and pipeline as bois2008b, FAO-56 PM as reference (as in bois2008), Turc 1961. Shares authors with bois2008, bois2008b, pieri2003.

## Bearing (2026-10-30)

- **Weather generator and sensor error:** gives interpolation error sizes for a regional network in a flat to gently hilly area: Tmin RMSE 0.9 C and Tmax 0.6 C daily, rain RMSE 15 % in summer, radiation RMSE 17 to 20 %. Useful as realistic error scales for a simulated station that is not at the site.
- **Terrain:** Tmin is the hard variable to interpolate; its spatial pattern is governed by local topography (not quantified here).
- **Not shown:** humidity, wind, leaf wetness, in-canopy values, hourly data.

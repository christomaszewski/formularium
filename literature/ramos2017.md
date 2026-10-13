---
id: ramos2017
citation: Ramos, M. C. 2017. Projection of phenology response to climate change in rainfed vineyards in north-east Spain. Agricultural and Forest Meteorology 247:104-115
doi: 10.1016/j.agrformet.2017.07.022
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 60 of 63 quotes found at their lines by scripts/verify_quotes.py, three table and text fragments checked by hand; held since 2026-10-07 as the source of the catalogue's Penedès phenology record, read then by Agrarium without a note
status: read
diseases: []
crops: [grapevine]
regions: [Penedès, Catalonia, Els Hostalets de Pierola]
processes: [phenology, budburst, degree-days, climate projection, runoff]
records: [ramos2017.budburst]
datasets: [ramos2017.penedes]
files: [2017-ramos-10-1016-j-agrformet-2017-07-022.pdf]
---

# Ramos 2017: Penedès phenology fitted by degree-days, and projected

The source of the catalogue's `ramos2017.budburst` (Table 2) and dataset
`ramos2017.penedes`, the only Penedès phenology the catalogue holds. Held since 2026-10-07;
this is its note. No disease appears anywhere in the paper.

## What it holds

- **Data:** one rainfed vineyard planted in 1989 in the Penedès Depression, Lyre trellis,
  3.1 × 1.3 m, rootstock R110, ten nodes a vine (l. 94-99, 135); phenology of Chardonnay
  1998-2012 and Macabeo and Parellada 1998-2009 (Table 1's caption says 1996-2012; l.
  33-34, 106, 222) as the day about 50 % of vines reached BBCH 5, 57, 81 and harvest by
  acidity and sugar, grapes grown for cava (l. 103-112); soil water at four depths every
  15 days (l. 87-89); hourly weather from the Els Hostalets de Pierola station of the
  Catalan meteorological service, "about 6 km" from the field (l. 117-119), though the
  printed coordinates (field 41.84 N, station 41.46 N, both at −1.81) are about 42 km
  apart and the longitude is not the Penedès's: a misprint. Annual rain 396 mm (2006) to
  903 mm (1996) (l. 210).
- **Mean dates** (Table 1, l. 227-230): Chardonnay budbreak 18 March, bloom 16 May,
  veraison 14 July, harvest 17 August; Macabeo 6 April, 26 May, 5 August, 30 August;
  Parellada 9 April, 1 June, 9 August, 14 September. Growing degree-days base 10 from
  budbreak to harvest 1,438 (Chardonnay) to 1,725 (Parellada) (l. 244-245).
- **The model** (eqs 1-2, l. 150-168): GDD = Σ max((Tmax + Tmin)/2 − Tb, 0) from a start
  date (22 February for Chardonnay, 25 February for the others; l. 291-292) to each
  stage, with Tb found per variety and stage by minimising the standard deviation of the
  sum across years (Excel Solver, after Zapata et al. 2017; l. 162-171). Chill portions
  (Dynamic Model) and growing degree hours (base 4 °C, optimum 26 °C) were used for a PLS
  analysis of budbreak (l. 131-139).
- **Table 2** (text layer, l. 321-334): fitted Tb for budbreak 7.0 (Chardonnay), 6.3
  (Macabeo), 5.6 °C (Parellada); bloom 8.2, 9.2, 8.4; veraison 10.5, 10.0, 9.6; harvest
  12.3, 12.0, 5.0 °C; GDD to budbreak 77, 182, 247; to bloom 353, 382, 441; to veraison
  635, 891, 905; RMSE in days 5.2, 7.3, 5.7 (budbreak), 7.6, 4.9, 3.8 (bloom), 8.0, 5.1,
  5.5 (veraison), 5.7, 8.9, 10.3 (harvest), against 11.6-18.7 d for budbreak at a fixed
  Tb of 10 °C. The text's veraison range "5.1 to 7" omits Chardonnay's 8.0 (l. 302, 322).
- **Water:** bloom advanced 0.22-0.60 d per 10 mm of water available from budbreak
  (l. 366); the veraison figure is printed in mm per 10 mm (l. 368), a slip. Runoff by
  WEPP, calibrated on 52 events of 2001-2003 (NSE 0.73) and validated on 17 of 2004 (NSE
  0.78), 8-36 % of rain a year (l. 246-270).
- **Projections** (eight CMIP5 models, RCP4.5 and 8.5, 2030, 2050, 2070 against
  1998-2012; l. 166, 179): budbreak up to 10 d earlier by 2050 and 12 by 2070 under
  RCP4.5, veraison and harvest 16 and 20 d, and 23-28 d by 2070 under RCP8.5, with the
  intervals between stages shortening by more than 10 d (l. 38-40, 380-381); growing-season
  warming to 2070 of 3.3 °C (RCP4.5) and 4.5 °C (RCP8.5) for Parellada (Table 4, l. 419;
  the text says 3.2 and 4.4, l. 393-394).

## Dependence

- **Fitted to** the vineyard's own observed dates (`ramos2017.penedes`); no model dated
  them. Tb's search procedure is Zapata et al. 2017's (`zapata2015`'s group); chill portions
  from Fishman et al. 1987, degree hours from Anderson et al. 1986 (both cited methods).
- **Engine piece:** `ramos2017.budburst` is Table 2's GDD with fitted Tb (degree-day
  phenology), as recorded.
- **Authors:** none shared with engine models.

## Bearing (2026-10-12)

- The record and dataset stand, with the station-distance misprint noted. For Agrarium:
  the Penedès dates and the 1998-2012 weather window are the region's own phenology
  reference; a truth that needs budbreak in the Penedès should not reuse these fitted Tb
  and sums (D27) but may be checked against Table 1's mean dates.

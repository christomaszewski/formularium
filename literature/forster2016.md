---
id: forster2016
citation: Förster, K., Hanzer, F., Winter, B., Marke, T. & Strasser, U. 2016. An open-source MEteoroLOgical observation time series DISaggregation Tool (MELODIST v0.1.1). Geoscientific Model Development 9:2315-2333
doi: 10.5194/gmd-9-2315-2016
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 48 of 48 quotes found at their lines by scripts/verify_quotes.py; no page image checked (equations read in the text layer)
status: read
diseases: []
crops: []
regions: [Netherlands, Svalbard, Austria, Rio de Janeiro, Arizona]
processes: [disaggregation, hourly weather, relative humidity, wind, radiation]
records: [forster2016.melodist]
datasets: [forster2016.five_sites]
files: [kristian_2016.pdf (the 2026-10-18 drop)]
---

# Förster et al. 2016: MELODIST, a daily-to-hourly disaggregation tool

An open Python tool that turns daily temperature, precipitation, humidity, wind speed and
shortwave radiation into hourly values, a variable and a site at a time, with no spatial
dependence (l. 30). Validated at five sites against their own observations.

## What it holds

- **Methods** (Table 2, l. 263-281, Eqs 1-13): temperature T1, a cosine between Tmin and
  Tmax (Eq. 1, l. 184), the hour of maximum set a priori (2 h after solar noon as a rule of
  thumb, l. 193) or fitted; humidity H1 (Tdew = Tmin, a = 1, b = 0, l. 269, 319), H2
  (Tdew = a Tmin + b fitted on hourly T and H by inverting Magnus, l. 270, 358-360), H3
  (Tdew linear between days with a sine term, kr = 6 above 100 W m-2 monthly radiation, else
  12, l. 271, 392, 409), H4 (daily Hmin and Hmax, linear on T; best when available, l. 272,
  359, 378); wind W1-W3 (W2 a cosine, W3 random); radiation R1 (scaling of potential
  radiation), R2 (Ångström a = 0.25, b = 0.75 by default, l. 277, 471), R3 (Bristow-
  Campbell); precipitation P1 (equal split), P2 (Olsson cascade, l. 281). Humidity for
  H1-H3 is 100 es(Tdew)/es(T) of the disaggregated temperature (l. 293, 313-316).
- **Sites** (Table 1, l. 256-260): De Bilt 1961-1990 / 1991-2014; Ny-Ålesund 1993-2004 /
  2006-2011; Obergurgl 2000-2007 / 2008-2014 (not free data, l. 208); Rio de Janeiro
  2003-2008 / 2009-2014; Tucson 1973-1993 / 1994-2014.
- **Results for humidity (H3, Table 4, l. 856-860):** observed vs generated mean RH: De Bilt
  81.82 / 81.63 %, RMSE 12.67 %, r 0.66; Ny-Ålesund 74.96 / 74.82, RMSE 17.41, r 0.02, NSE
  -0.91; Obergurgl 70.83 / 66.42, RMSE 16.43, r 0.51; Rio 70.95 / 67.45, RMSE 10.39, r 0.72;
  Tucson 35.31 / 33.31, RMSE 18.52, r 0.55. Means within ±5 % (l. 920). The text says
  "RMSE 20 %" (l. 925), which Table 4 does not show (10.39 to 18.52). Hmin and Hmax are
  not kept (l. 943). Temperature T1: RMSE 1.63 to 2.69 K, r 0.96-0.97 (Table 3, l. 839-842).
  Results for H1, H2 and H4 are not in the tables read.
- **Code:** GPL-3, Python 2.7 and 3.5, pandas, numpy, scipy (l. 1335); Zenodo
  10.5281/zenodo.54676 (l. 1276); github.com/kristianfoerster/melodist (l. 1278).
- **Not printed:** fitted a and b per station, the R2 constants (regression, l. 476), any
  cap of RH at 100 %, any statistic near saturation or on wet hours.

## Dependence

- Methods credited to Bregaglio et al. 2010, Waichler & Wigmosta 2003, Debele et al. 2007,
  Liston & Elder 2006, Ångström 1924, Olsson 1998 (Table 2). Credited, not read here.
- Fitted on each site's own observations; no other model's output is the data.
- Used by Pidoto & Haberlandt 2023 for the hourly step (`pidoto2023`), and compared with
  Görner et al. 2021 on De Bilt 1991-2014 (`gorner2021`: same observed series, same RH mean
  81.82 %, sigma 15.12).

## Bearing (2026-10-18)

For Agrarium's sweep (thousands of seasons of hourly weather driving a leaf-wetness model
whose engine counterpart is RH ≥ 90 %):

- **Variables and co-variation:** hourly temperature, humidity, wind speed, radiation and
  precipitation, each alone: no co-variation between wind and rain or humidity, and no wind
  direction. It is a disaggregator, not a generator: daily series come from elsewhere.
- **Near saturation or wet hours:** not validated on humidity near saturation; no wet-hour
  statistic. H3 humidity is checked as whole-series mean, RMSE, r and NSE; r is 0.02 at one
  site. H1 (Tdew = Tmin all day) is the rule the engine-side hours would feel most.
- **Where fitted and tested:** five sites (Netherlands, Svalbard, Austria, Rio, Tucson), a
  calibration and a validation period each.
- **Code and licence:** GPL-3, public.
- **Can it run:** yes, from the repository.

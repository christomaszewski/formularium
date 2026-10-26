---
id: kraus2018
citation: Kraus, C., Pennington, T., Herzog, K., Hecht, A., Fischer, M., Voegele, R.T., Hoffmann, C., Töpfer, R. & Kicherer, A. 2018. Effects of canopy architecture and microclimate on grapevine health in two training systems. Vitis 57:53-60
doi: 10.5073/vitis.2018.57.53-60
read: "2026-10-25, lightly: the methods, the microclimate results, Table 1 (canopy architecture) and the discussion sentence on drying (the disease and Drosophila sections skimmed; two columns share lines in the text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: [downy mildew, powdery mildew, Botrytis bunch rot]
crops: [grapevine]
regions: [Germany, Pfalz, Siebeldingen]
processes: [canopy architecture, canopy density, leaf area index, microclimate, relative humidity, drying, leaf wetness, training system, minimal pruning]
records: []
datasets: []
files: [dr1025_kraus2018.pdf (the 2026-10-25 drop)]
---

# Kraus et al. 2018: a minimal-pruned hedge (6 to 15 times the shoots, LAI 2.6 to 4.7 against 0.8 to 2.6 in VSP) held humidity up to 20 percentage points higher after rain

A two-year comparison of a dense semi-minimal-pruned hedge (SMPH) and vertical shoot positioning (VSP) on two cultivars, with in-canopy temperature and humidity and a measured LAI.

**Read this first.** Drying was not measured. The in-canopy loggers record only temperature and relative humidity (hourly, three per system and variety, 150 cm above ground, l. 140-143); leaf wetness came from the institute's weather station (l. 150-152). The "several hours longer" for a dense canopy to reach the humidity of VSP (l. 377, 399) is a statement about humidity, and the number of hours is not given. LAI is measured and tabulated (Table 1), but it is not matched to the humidity records by date in the lines read. The reading JSON said that no LAI is given; that is wrong, the LAI rows are in Table 1 (l. 206-208, 229-231). The text is two columns sharing lines.

## What it holds

- **Site and density:** Chardonnay (planted 2008) and Reberger (2001) at Geilweilerhof, Siebeldingen (Pfalz); half the rows of each pruned mechanically since 2013 as SMPH; inter-row distance 2 m, vine spacing 1 m; seasons 2016 and 2017 (l. 127-128, 81). SMPH panels carried eight to 15 times (Chardonnay) and six to eleven times (Reberger) the shoots per 0.5 m of VSP panels in both years (l. 144).
- **LAI:** from all leaves of four random 50 cm wide canopy sections, removed and measured with a leaf area meter (l. 93-96); read at flowering (BBCH 65), pea size (75) and veraison (81). SMPH against VSP at BBCH 65 / 75 / 81 (Table 1): 2016 Chardonnay 4.7 / 2.8 / 3.1 against 1.0 / 1.7 / 1.8; Reberger 2.6 / 2.6 / 3.2 against 1.2 / 1.9 / 1.9 (l. 206-208). 2017 Chardonnay 3.5 / 3.0 / 3.5 against 1.1 / 2.6 / 2.1; Reberger 3.7 / 2.6 / 4.0 against 0.8 / 1.5 / 2.1 (l. 229-231). Across the table SMPH runs 2.6 to 4.7 and VSP 0.8 to 2.6 (arithmetic, not printed); several differences are not significant, mostly at pea size. Chardonnay LAI was at least 1.5 times higher in SMPH through both seasons, except at BBCH 75 in 2017 (l. 162-165).
- **Microclimate:** 3 percentage points higher humidity and 0.9 degC lower mean temperature in the SMPH canopy than in VSP (abstract, l. 26-27). After a rain event relative humidity in SMPH was up to 20 percentage points higher than in VSP, while temperature differed by up to 3 degC (l. 251-253); similar in the morning dew, in both vineyards (l. 254-256).
- **Authors' conclusion:** SMPH canopies "dry much slower" and need several hours longer after rain or morning dew to reach a similar humidity level as VSP canopies (l. 377, 399).
- **Disease side (not used here):** SMPH vines could be more susceptible to downy and powdery mildew and VSP to Botrytis bunch rot (abstract, l. 36-38).

## Dependence

- Own measurements; nothing borrowed for the microclimate.

## Bearing (2026-10-25)

- **micro.density_drying_slowdown (0.4, a divisor added per unit LAI above 1):** the direction is supported: the canopy with the higher LAI (SMPH, 2.6 to 4.7) stayed humid hours longer after rain and dew than the canopy with the lower LAI (VSP, 0.8 to 2.6). The registry's divisor 1 + 0.4 (LAI - 1) puts LAI 3.5 against 1.8 at divisors of 2.0 and 1.32, a canopy about 1.5 times slower (arithmetic, not printed; the form is read from the registry's unit text). The paper gives no hours and no wetness duration, so it cannot confirm 0.4 or its range 0 to 1. The SMPH hedge is also a different structure (many hanging shoots), not simply more LAI.
- **micro.evap_mm_h_per_hpa, micro.wet_threshold_mm, micro.interception, micro.storage_mm_per_lai:** not addressed.
- **Kind of result:** measurement (two cultivars, one site, two seasons) of humidity with a measured LAI, not of leaf wetness or evaporation; a hedge system, so an analogue for a row-trellised vineyard.

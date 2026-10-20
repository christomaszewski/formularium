---
id: furushopercot2025
citation: Furusho-Percot, C., Maury, O., Minet, V., De Decker, T., Roux, D., Beauvois, C., Le Roux, R., Décome, J., Launay, M. & García de Cortázar-Atauri, I. 2025. French agroclimatic research network dataset. Data in Brief 61:111809
doi: 10.1016/j.dib.2025.111809
read: 2026-10-20, in full (a short data paper), by the main session in the PubMed Central JATS copy (PMC12266558); the dataset's README, variables file and station list (10.57745/BQ0BWB, version 4.0) and two station sheets (10.57745/PXJBH4) read beside it; three stations' hourly files checked
status: read
diseases: []
crops: []
regions: [France, Bordeaux, Alsace, Languedoc, Corsica, Guadeloupe, French Guiana]
processes: [leaf wetness duration, weather station network, solar radiation, measurement methods]
records: []
datasets: []
files: [paper.xml (PMC JATS copy, open access, fetched 2026-10-19 for the W1 dataset search)]
---

# Furusho-Percot et al. 2025: the INRAE AgroClim network's hourly and daily data

Read for Agrarium's check W1 (PLAN 15, D45), which needs measured leaf wetness beside hourly
weather. The data paper describes the dataset 10.57745/BQ0BWB; it is not a formulation.

## What it holds

- **The network:** 54 stations "located in research fields" in mainland France, Corsica,
  Guadeloupe and French Guiana; "47 stations are located at INRAE and 7 at partner experimental
  sites" (l. 50). All have the same hardware (Table 2, l. 57-65). The dataset runs 1983-2025.
- **Leaf wetness:** "leaf wetness duration at 50 cm" (l. 53), Cimel HU 1871, "Weekly check,
  bi-annual replacement" (Table 2). It is "measured with the same type of sensor in diverse climatic
  regions" (l. 25). The variables file defines hourly H as "Durée d'humectation cumulée sur l'heure
  précédente, mesurée par un capteur de mouillage", in hours and tenths. No wet threshold, angle or
  surface is stated.
- **Other sensors:** Vaisala HMP110 humidity; Kipp & Zonen CMP6 pyranometer; PAR Lite; a 0.5 mm
  tipping gauge; Cimel CE 155 N cup anemometer; PT100 temperatures at 2 m, 50 cm and 10 cm. Heights:
  "reference height of 2 m for measurements (3, 4, and 5) and 1.5 m for measurements (1, 2)" (l. 53).
- **Siting:** stations follow Météo-France's rule of a "minimum distance of 20 m from any building,
  tree or irrigation that could influence the measurements" (l. 95). The wetness sensor therefore
  sits in an open enclosure, not in a crop canopy (inferred).
- **Quality:** the daily data are filtered for outliers with biweight estimators (l. 96-101).
  The hourly data are "raw and not yet filtered or validated" (README). Sensor changes and
  malfunctions "may have introduced undetected" inconsistencies (l. 102).
- **Licence:** the paper is CC BY 4.0; the dataset and the station sheets are Etalab 2.0 (Licence
  Ouverte; the repository records, read).

## Dependence

- A measurement network; no model shapes the data. Wetness is a sensor's reading, not an RH rule.

## Bearing (2026-10-20)

Own checks, Apr-Sep, scripts in the W1 drop:
- **Time zone.** Hourly values are cumulative over the preceding hour. In July 2023, Couhins'
  mean radiation peaks in hours 12-13, so the timestamps are UTC (inferred; not stated).
- **Stuck spells.** On sunny (> 200 J cm⁻² h⁻¹), rainless hours from 11 to 15 h, Bergheim reads
  wet 0.00-0.03 of the time every year from 2008 to 2025. Couhins reads wet 0.39 of the time in
  2011, 0.23 in 2021 and 0.17 in 2023, and Toulenne up to 0.06. The raw hourly wetness needs
  screening before use.
- **The engine's RH ≥ 90 % rule** against measured daily wet hours: Bergheim MAE 1.94 h (2022)
  and 2.08 h (2023), the rule low by about 1.8 h; Couhins 1.49 h (2022) and 2.50 h (2025).
- **Vineyards.** Couhins is an INRA vineyard estate ("Château Couhins, cru classé des Graves, un
  domaine de l'INRA", a title found by search, not read). Grande Ferrade carries vineyard trials;
  Toulenne (Domaine des Jarres) is a fruit-tree unit. The station sheets (10.57745/PXJBH4) are
  climate summaries and do not show what surrounds a station.
- **For W1:** ranked third, behind ARPAV Veneto and MeteoGalicia
  (Agrarium research_notes/pilot-equations, section 6). It is open and complete, but its sensor
  is at 50 cm in a station enclosure, not in the vines.

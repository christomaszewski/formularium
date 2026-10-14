---
id: fernandezgomez2013
citation: Fernández Gómez, O. 2013. Análisis de las diferencias en el crecimiento vegetativo, en los componentes del rendimiento y en la composición de las uvas y vinos del cv. Cabernet Sauvignon (Vitis vinifera L.), producidos por el déficit hídrico durante pre-envero y post-envero. PhD thesis, Universidad Politécnica de Madrid
doi:
read: 2026-10-14, a targeted reading (not the whole thesis) of the cover and title pages (l. 1-60), Ch. II §3 site and stage method (l. 3253-3257, 3376-3650), Ch. II §6.1 shoot length, LAI equations and SA (l. 3780-3930), Ch. III Tabla 3.1 and text (l. 5536-5590, 5836-5902), Tabla 3.2 (l. 5966-6069), Tabla 3.3 (l. 6144-6172) and six cited references, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; Tabla 2.6 and Tablas 3.1-3.2 read in the text by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Madrid, Chinchón]
processes: [phenology, shoot growth, leaf area index, deficit irrigation]
records: []
datasets: [fernandezgomez2013.chinchon]
files: [olga_2013.pdf]
---

# Fernández Gómez 2013: Cabernet Sauvignon under deficit irrigation at Chinchón

A Spanish doctoral thesis on four water-deficit regimes (before and after veraison) in
Cabernet Sauvignon near Madrid, 2010 and 2011. Read for its observed stage dates, shoot
lengths and leaf area, not for the deficit effects on wine.

## What it holds

- **Site** (l. 3253-3257): Chinchón (Madrid), 550 m; Cabernet Sauvignon on 41 B planted
  2005, 3 m by 1 m, vertical shoot positioning. The nearest long-term station, Getafe,
  is 40.6 km away (l. 3383).
- **Stage days of the year** (Tabla 2.6, l. 3627-3630; E-L stages 4, 23, 27, 35, 38
  after Eichhorn & Lorenz 1977 as modified by Coombe 1995; a stage is the day over
  50 % of buds or shoots reached it, l. 3592):

  | | budburst | flowering | fruit set | veraison | maturity |
  |---|---|---|---|---|---|
  | 2010 | 111 (21 Apr) | 153 (2 Jun) | 165 (14 Jun) | 214 (2 Aug) | 280 (7 Oct) |
  | 2011 | 98 (8 Apr) | 143 (23 May) | 152 (1 Jun) | 203 (22 Jul) | 258 (15 Sep) |

- **Heat sum Ite** (base 10 °C, from 1 April, l. 3504, 3518; daily formula not printed):
  at budburst 48.0 and 54.2 °Cd, at flowering 328.0 and 339.8 °Cd, at fruit set 438.4 and
  430.2, at veraison 1146.7 and 1079.3, at maturity 1900.3 and 1845.6 (2010, 2011).
  Annual Ite 1951.8 °Cd in 2010 and 2168.5 in 2011 (l. 3465, 3486). Rain 478.0 and 332.2
  mm.
- **Shoot length** (Tabla 3.1, l. 5879-5880; measured weekly on 6 shoots a replicate from
  about 15 cm to growth stop, l. 3786-3798): year means 110 cm (2010) and 103 cm (2011) at
  fruit set, 166 and 160 cm at growth stop (day 218 and day 187). Treatments run 99-121 cm
  at fruit set and 124-210 cm at growth stop (l. 5855-5867).
- **Leaf area** (Tabla 3.2, l. 6067-6068): year-mean LAI 1.2 m²/m² in both years, external
  leaf area (SA) 0.8 m²/m², LAI/SA 1.5; LAI per canopy volume 8.1 and 13.6 m²/m³. Two-year
  means: LAI 1.0 with a pre-veraison deficit against 1.4 without (l. 5990). LAI is
  computed from leaf counts, not measured by area meter; the date is not printed.
- **Bunches** (Tabla 3.3, l. 6167-6171): 1.9 to 2.0 per shoot, two-year means; yield
  0.67-0.87 kg/m².
- **Text against tables:** the text says bloom was 12 days apart (l. 3602), Tabla 2.6 gives
  10; fruit set to growth stop is 54 and 36 days in the text (l. 5830-5832), 53 and 35 in
  the table days. The table values are used.
- **Not printed in what was read:** the LAI date, the log base in AF1 and AF2, shoot length
  by date, canopy height and width, leaf area a vine, bunches a vine, leaf appearance and
  shoot elongation rates. Tabla 2.7 and the rest of Chapter III were not read.

## Dependence

- **Method, not model:** LAI follows Sánchez-de-Miguel et al. 2011 (l. 3810), with
  AF1 = 10 [0.012 + 0.996 log(AFM1)] (R² 0.98) for the main shoot and AF2 = 10 [0.036 +
  0.982 log(AFM2)] (R² 0.99) for laterals (l. 3845-3847): the coefficients printed there are
  those in `sanchezdemiguel2011.shoot_leaf_area`, so they are copied or refitted to the same
  value. The thesis does not say which. Carbonneau 1976, Lopes & Pinto 2000 and Schneider
  1989 (SA formula, l. 3900) are cited methods. The authors belong to the Lissarrague
  group, like Sánchez-de-Miguel: a flag only.
- **No model shaped the dates;** the stage days are field scores.

## Bearing (2026-10-14)

- **Observed seasons free of any engine fitting:** stage dates for two Madrid seasons
  (budburst to maturity) and shoot lengths at fruit set and growth stop: a test set for a
  truth phenology. It prints no fitted curve, so it gives no record.
- **A deficit-irrigated vine:** LAI 1.2 and external leaf area 0.8 m²/m² under deficit
  (1.0 with a pre-veraison deficit, 1.4 without). Reported, not judged against any
  assumption.

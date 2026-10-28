# Answer to pom-limits.md

2026-10-27, by an `ingest` session. Sources:
- Tran Manh Sung et al. 1990 and Ronzon 1987, both in the library, read in the page images
  where it mattered.
- Bordeaux-Mérignac's daily rain, Météo-France station 33281001, from "données climatologiques
  de base quotidiennes" (Licence Ouverte 2.0). Kept outside the repository.

## The short answer

**Hm is printed as RM over the rainy days, but the printed indices need Hm = the month's mean
daily rain** (RM over the days in the month, 2.3-3.5 mm at Bordeaux), with every day below it
lacking and HM a constant near 9 mm. On the station's own rain, that reading reproduces:
- Table 1 within MAE 17 index units, January r = 0.98;
- Ronzon's Tableau 25 within MAE 17.

Hm = RM / rainy days, at either threshold, gives Cooptera's problem: January from -37 to -668,
MAE 228-416. `scripts/pom_limits_check.py` makes every number here.

## The four questions

1. **Hm and HM, as printed:**
   - Both sources: Hm = RM / the monthly mean number of rainy days (paper p. 122). In Ronzon,
     ESPm is the monthly mean rain over at least 20 years (1951-1985) divided by "nombre de
     jours de pluie" (p. 93, page image).
   - Neither defines a rainy day. Ronzon's NJM is "the mean number of rainy days of the month
     over at least 20 years" (p. 31).
   - RM is the month's mean total.
   - HM's bracketing is not printed. Ronzon's "18 / NJM = 9" comes from the EPI model (its
     equations use a = 18 / (NJM x 1.5)). In practice it is a constant 9 mm.
   - **What reproduces the tables:** Hm = RM / days in the month, and HM = 9 mm.
     - Hm. A wholly dry 21-30 September prints -24 and -26 (September 1980, 1983 and 1985 at
       the station). Ten days at RM / 30 = 2.57 mm give -25.7. RM over rainy days (6.1 mm, or
       8.1 at 1 mm) would give -61 or -81.
     - HM. A constant of 8-9 mm fits best (MAE 12-21). (RM + SD) / rainy days at 0.1 mm gives
       MAE 22 for Table 1 and 32 for Tableau 25.
     - No upper limit gives MAE 67-76.
2. **Printed limits or normals:** none in either source.
3. **Worked examples:** two tables of monthly indices.
   - Table 1 (paper p. 123): Im for each month, September to March, 1977-1988, and the
     observed severity. In `literature/tranmanhsung1990_table1.csv`.
   - Tableau 25 (Ronzon p. 150, printed sideways): the same for 1977-1986, with 1951-1985
     normals. In `literature/ronzon1987_tableau25.csv`.
   - Neither prints POS, NEG or a day's terms.
4. **The rules, as printed** (Ronzon p. 94):
   - MAN(J) = ESPm - PL(J) whenever PL(J) < ESPm, so a dry day lacks the whole minimum. The
     station test confirms it: rainy days alone would give 0 for a dry September, not -26.
   - The count starts on 21 September of the previous year, every year, from an index of 0.
   - Ronzon ran it daily to 31 March.

## Delivered

- `literature/tranmanhsung1990_table1.csv` and `literature/ronzon1987_tableau25.csv`.
- `tranmanhsung1990.pom`: two flags, the limits as they reproduce the tables and where the
  tables are.
- `equations/tranmanhsung1990.py`: the rules were right. Its docstring now says to pass the
  days in the month as `rainy_days` to reproduce the paper.
- `tests/test_tranmanhsung1990.py`: the station's 1983-84 season, with 1946-1987 normals:
  - the reading above gives -26, -77, -129, -77, 39 against the printed -26, -75, -126,
    -79, 33;
  - Hm over rainy days gives -61 for September and below -250 for January.
- `scripts/pom_limits_check.py`, and a section in each of the two notes.

## For Cooptera

Use Hm = the month's mean daily rain and HM = 9 mm. At Changins, build the normals from the
same daily series the index is run on. The match is not exact to the unit, perhaps because the
station series has been revised since 1987. ERA5 at Bordeaux gave the same ranking of the
readings, but it is less close: MAE 38 for the reading above.

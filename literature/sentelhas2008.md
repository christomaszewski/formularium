---
id: sentelhas2008
citation: Sentelhas, Paulo C., Dalla Marta, Anna, Orlandini, Simone, Santos, Eduardo A., Gillespie, Terry J. & Gleason, Mark L. 2008. Suitability of relative humidity as an estimator of leaf wetness duration. Agricultural and Forest Meteorology 148:392-400
doi: 10.1016/j.agrformet.2007.09.011
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 52 of 52 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 as the engine's wetness source and read then by Agrarium without a note
status: read
diseases: []
crops: [turfgrass]
regions: [Ames Iowa, Elora Ontario, Florence Tuscany, Piracicaba São Paulo]
processes: [leaf wetness, sensors, humidity threshold, dew point depression]
records: [sentelhas2008.wetness]
datasets: []
files: [2008-sentelhas-10-1016-j-agrformet-2007-09-011.pdf]
---

# Sentelhas et al. 2008: RH at 90 % as a stand-in for leaf wetness, at four sites

The source of the engine's wetness stand-in (`sentelhas2008.wetness`, an hourly RH
threshold). Held since 2026-10-07 and cited in the catalogue; this is its note.

## What it holds

- **Sites and data:** mowed turfgrass at Ames (USA, 2003, 72 d), Elora (Canada, 2003 and
  2004, 118 d), Florence (Italy, 2003 and 2004, 120 d) and Piracicaba (Brazil, 2005-2006,
  183 d) (l. 43-44, 136-153); two wetness sensors a site, flat-plate (Campbell 237) or
  electronic transducer, averaged, at 30 cm (120 cm at Florence), logged every 10 to 60
  min (l. 137-163). Table 1 gives Ames as 23/07-07/10 where the text says 27 July (l. 138,
  203). Validation data from the same sites: Ames 1998/99 (218 d), Elora and Ridgetown
  2006 (101 d), Piracicaba 2002/03 (108 d) (l. 254-257).
- **Three models:** (1) constant RH: daily wetness = hours with RH at or above a
  threshold, 90 % at first (l. 178-179, 187), the idea traced to Monteith 1957's dew at
  91-99 % RH (l. 181-182); (2) dew-point depression (DPD): wet while DPD stays between
  1.8 °C (onset) and 2.2 °C (dry-off), from Rao et al. 1998 (l. 213-216); (3) extended RH
  (Wichink Kruit et al. 2004): wet above 87 %, and between 70 and 87 % when RH rises more
  than 3 % in 30 min, dry when it falls more than 2 % (l. 223-236). Days run 12:01 to noon
  (l. 241-242).
- **Results at 90 %:** MAE 2.61, 1.93, 1.74 and 1.89 h a day at Ames, Elora, Florence and
  Piracicaba (Table 2, l. 299-302); DPD 2.43, 1.74, 1.84, 2.09 h; extended RH 2.90, 2.33,
  4.44, 2.89 h (l. 304-312). RH 90 % and DPD underestimated wetness at Ames, Elora and
  Piracicaba and overestimated it at Florence (l. 47-48, 481-483). Fraction correct
  0.87-0.92, false-alarm rate 0.02-0.31 for RH 90 % (l. 51-52, 326-329).
- **Calibrated thresholds** by iterative search on R², D, C and MAE (l. 245-250): 83 %
  Ames, 85 % Elora, 92 % Florence, 90 % Piracicaba (l. 342-344, 406-407), MAE 1.54, 1.55,
  1.23, 1.89 h in sample (Table 4, l. 377-380; pooled 1.60 h, l. 381) and 1.78, 1.60, 1.71,
  1.29 h on the independent sets (Table 5, l. 395-398). The text calls Piracicaba's
  threshold higher than the default, though Table 4 prints 90 (l. 476, 380).
- **Recommendation:** the RH model, locally calibrated, is accurate enough for disease
  warning schemes (l. 368, 454); physical models are cited at about 1 h error and other
  empirical ones at 1.5-2.3 h (l. 444-448).
- **Garbled:** the comparison signs are control glyphs in the text layer (≥ and ≤ read from
  the wording, l. 178-179); the sensor inclinations print as 458 and 308 (45° and 30°).

## Dependence

- **Its own data,** turf wetness at four sites; no disease, no grapevine. The DPD limits are
  Rao et al. 1998's and the extended-RH rules Wichink Kruit et al. 2004's (borrowed rules,
  not engine models). Magarey et al. 2006 (the surface-wetness energy balance) is cited for
  context only (l. 78, 126).
- **The engine's piece:** `sentelhas2008.wetness` is this paper's constant-RH model at 90 %.
  The paper itself ends by recommending a calibrated threshold (83 to 92 %) rather than
  90 % everywhere.
- **Authors:** Dalla Marta and Orlandini (PLASMO), Gleason (`gleason2008`, `gleason1994`),
  Gillespie: flags that other notes already record.

## Bearing (2026-10-12)

- The catalogue record's one-line description stands. For Agrarium's truth: the RH ≥ 90 %
  rule is an engine piece and must not be the truth's wetness; this paper gives its
  error (about 1.7 to 2.6 h a day on turf, biased low at three of four sites) and shows
  the threshold is site-specific, which argues for a physical wetness model with a
  different form, as decision D27's structure rule already requires.

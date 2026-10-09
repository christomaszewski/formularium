---
id: sentelhas2004
citation: Sentelhas, Paulo Cesar. 2004. Duração do período de molhamento foliar: aspectos operacionais da sua medida, variabilidade espacial em diferentes culturas e sua estimativa a partir do modelo de Penman-Monteith. Livre-docência thesis, Escola Superior de Agricultura "Luiz de Queiroz", Universidade de São Paulo, Piracicaba (October 2004)
read: 2026-10-08, by a reading agent (claude-sonnet-5-5): summaries, the methods and results of chapters 3-7, chapter 7 in full, the conclusions; 60 quotes checked by scripts/verify_quotes.py, dependence by the main session. Earlier read on 2026-10-07 (Agrarium's read-wetness.md)
status: read
diseases: []
crops: [grapevine, turf, maize, coffee, cotton]
regions: [Ontario, Sao Paulo, Iowa]
processes: [leaf wetness, sensors]
records: [sentelhas2004.penman_monteith]
datasets: []
files: [related-sentelhas-2004-thesis.pdf]
---

# Sentelhas 2004: leaf wetness by Penman-Monteith (thesis)

One author, ESALQ/USP; written partly during a post-doctoral stay at the University of
Guelph. Chapters 3 to 6 are his 2004 papers on wetness sensors and their spatial
variability.

## What it holds

- **The model:** Penman-Monteith latent heat on a wet sensor, in the "RES" form of Rao et
  al. 1998 (l. 2245): LE = -{s·Rn + 1200·(es - ea)/(ra + rb)}/(s + γ*) (l. 6327), with the
  wet-period rule of Pedro & Gillespie 1982 (l. 2381): wetness begins when LE > 0 or rain
  falls, and ends when the stored water has evaporated.
- **Parameters are taken, not fitted:** γ* = 0.64 for dew and 1.28 for rain (l. 2330,
  2332), sensor size 0.07 m (l. 2350), a store of 0.8 mm for dew (l. 2354) and up to 0.6 mm
  for rain (l. 2364). The aerodynamic resistances at 30 and 110 cm are derived by
  difference from that at 190 cm: ra = 68.75/U2m and 19.79/U2m (l. 6401, 6405). Night net
  radiation is cut by 20%, a choice the thesis calls arbitrary (l. 6740).
- **Net radiation:** four schemes (eqs. 10-23) after Pedro Jr. 1980, Madeira et al. 2002 and
  Iziomon et al. 2000 (l. 6506, 6674), tested at Elora only (l. 6490).
- **Data:** wetness sensors (painted, heat-treated Campbell 237 plates; l. 1437) at Elora
  (maize and turf, 71 days from 28 July 2003; l. 3516), Piracicaba (coffee) and Jundiaí
  (grape, cv. Niagara Rosada, 68 days, 24 October 2003 to 14 January 2004; l. 5051).
- **Grape canopy:** top 8.48 h and lower canopy 8.33 h of wetness a day, no difference
  (l. 5209); turf at 30 cm reads about 6% more than the grape canopy (l. 5551).
- **Skill:** over turf at 30 cm, mean absolute error 1.05 h a day (l. 7020); across three
  reference sites 1.46 h (l. 7082); on crop tops, with night net radiation × 0.8, grape
  1.50 h (l. 7452).
- **Humidity rules:** hours above 90% RH are used as a stand-in, not fitted (l. 2163),
  and tested on Piracicaba cotton, 70 days, error 1.27 h (l. 2604, 2608). Dew-point
  depression limits of 2.0 and 3.8 °C were chosen for that study (l. 2183, 2753). The CART
  model is Gleason et al. 1994's, adapted to 15-minute data (l. 2191).

## Dependence

- It computes Penman-Monteith (Monteith & Unsworth 1990), Rao et al.'s resistance and
  Pedro & Gillespie's wet-period rule; none of these is a model the engine runs.
- **No parameter of the wetness model was fitted** to the thesis's data, so it shares no
  calibration data with anything; the engine's `sentelhas2008.wetness` (RH and dew-point
  thresholds) has another form.
- Sentelhas is an author of `sentelhas2008.wetness`; Gleason lent sensors and data (l. 83);
  Gillespie co-wrote the chapter papers. All flags (D27).

## Bearing (2026-10-08)

- **The wetness candidate D27 frees.** Under D19 it was kin through its author; under D27
  it shares no equation, code, data or form with an engine model. Its author list is read
  and complete. Formularium records it as `sentelhas2004.penman_monteith`.
- It needs net radiation, wind and humidity at sensor height, which Agrarium's
  microclimate has. Its errors (about 1-1.5 h a day) bound how far a truth built on it
  can be trusted, and a truth using it should still sweep the stores and γ*, which are
  taken, not measured.
- In a trellised grape canopy the top and lower canopy agreed, so one wetness per vine is
  defensible.

---
id: orlandini1993
citation: Orlandini, S., Gozzini, B., Rosa, M., Egger, E., Storchi, P., Maracchi, G. & Miglietta, F. 1993. PLASMO: a simulation model for control of Plasmopara viticola on grapevine. Bulletin OEPP/EPPO Bulletin 23:619-626
doi: 10.1111/j.1365-2338.1993.tb00559.x
read: 2026-10-09, in full by the main session; equations read in the page images
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Tuscany]
processes: [primary infection, infection, incubation, sporangia survival, spray timing, validation]
records: [orlandini1993.plasmo, orlandini1993.incubation, orlandini1993.infection, orlandini1993.survival, orlandini1993.trigger]
datasets: [orlandini1993.emergences, blaeser1979, goidanich1957]
files: [EPPO Bulletin - December 1993 - ORLANDINI - PLASMO  a simulation model for control of Plasmopara viticola on grapevine1.pdf]
---

# Orlandini et al. 1993: PLASMO, with fitted parameters and three years of validation

Presented at the EPPO conference on computerized advisory systems, Eslöv, November 1992.
The publisher's PDF carries a download stamp on every page; it is not copied here.

## What it holds

- **Primary infection (p. 620):** rain ≥ 8 mm "within any 24-h period after the minimum
  temperature is consistently higher than 10°C (Goidanich, 1959)"; infection only on shoots
  of 100 mm.
- **Infection (p. 620):** wet hours needed f1(T) = n/T for 6 ≤ T ≤ 26 °C, otherwise 0;
  progress f2 = 100/f1. "This function has been derived on the basis of data from Blaeser &
  Weltzien (1979) ... found by the least squares method."
- **Incubation (pp. 620-621):** hourly increments summed to 100 %: d = f3(T)·f4(RH), f3 =
  4(T - Tmin)(Tmax - T)/(Tmax - Tmin)², f4 = m(RH - RHmin). Null below RH 30 % or outside
  Tmin-Tmax. Optimum "about 22°C", maximum "about 34°C" (Goidanich 1959), minimum "about
  10°C" (Goidanich 1959; Magarey et al. 1991). Incubation lasts 4-25 days.
- **Survival (p. 621):** f6 = 100/f7; f7 = (f8(T) - 12)·RH/100 + 12 hours; f8 = 235.8 (T <
  10 °C), 1.8T + 217.8 (10-15 °C), 15.52T + 12 (15-30 °C), 12 (T > 30 °C); "a simple model
  ... on the basis of temperature and humidity (Blaeser & Weltzien, 1979)".
- **Fitted values (p. 621):** "Optimal model parameters (m=0.097 and n = 75.69) were chosen
  when the difference in time between observed and calculated sporangia emergences reached
  a minimum."
- **Validation (pp. 622-624):** Mondeggi-Lappeggi farm (Firenze), vineyards Pulizzano
  (1990-1992) and Paretaio (1990), 140-150 m, slopes 14-18 %, Sangiovese, Canaiolo nero,
  Malvasia, Trebbiano; weather in each vineyard; untreated 1500 m² plots observed weekly
  on Sangiovese. Table 2: of 7, 7, 4 and 10 simulated infection periods, 4, 3, 2 and 4
  coincided with observed ones; every observed one was simulated; errors up to 5 days.
  Table 3: sprays 5, 5, 3, 6 by PLASMO against 8, 8, 8, 9 by calendar; disease intensity
  (classes of Table 1, 200 leaves a plot) not significantly different in most cases.

## Garbled or inconsistent

- With m = 0.097 the increment is 6.8 % an hour at 22 °C and 100 % RH, ending incubation in
  under 15 h, against the stated 4-25 days. Not corrected.
- f8's 15-30 °C piece rises to 477.6 h at 30 °C, then drops to 12 h: probably 15.52(30 - T)
  + 12, which meets both neighbours. Not corrected.

## Dependence

- **Infection:** fitted to Blaeser & Weltzien 1979's data (`blaeser1979`), the data behind
  part of Brischetto 2021's Magarey parameters, and of the same wet degree-hour form as the
  engine's `rossi2008.primary` infection and `blaeser1979.survival`. Kin.
- **Incubation:** cardinal temperatures from Goidanich's 1959 manual (taken here as the
  1957 table's data, inferred); m fitted to Tuscan emergences. Kin by the strict reading.
- **Survival:** Blaeser & Weltzien's data in PLASMO's own form (inferred). Kin by shared data.
- **Trigger:** a rain-temperature trigger, the 3-10 rule's form. Kin by structure.
- **Authors:** Orlandini also wrote Sentelhas et al. 2008: a flag only.

## Bearing (2026-10-09)

- Agrarium asked whether a PLASMO truth family would be independent of the engine. Process
  by process it is not: data or form link every piece. Recommended to the Agrarium session
  as development only. Agrarium recorded it (2026-10-09, branch `free-papers`).
- Franche 2012's form (2.616, with RHmax) is not in this paper; it comes from a later
  version, not held.
- Found 2026-10-09 through scite.ai: Rosa, Gozzini, Orlandini & Seghi 1995 is
  doi:10.1016/0168-1699(95)00007-q, and the later PLASMO is Orlandini, Massetti & Dalla
  Marta 2008, An agrometeorological approach for the simulation of Plasmopara viticola,
  Comput. Electron. Agric. 64:149-161, doi:10.1016/j.compag.2008.04.004. Both are closed
  access and not held; the 2008 paper is the likeliest source of Franche's 2.616 form and of
  the survival equation Brischetto et al. 2020 say has no printed parameters (snippet: its
  citing papers). Brischetto et al. 2021 counted latent infections with its incubation
  equation when scoring their model (read in their paper).

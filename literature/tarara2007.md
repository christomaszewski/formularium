---
id: tarara2007
citation: Tarara, Julie M. & Hoheisel, Gwen-Alyn. 2007. Low-cost shielding to minimize radiation errors of temperature sensors in the field. HortScience 42(6):1372-1379
doi:
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 57 of 57 quotes found at their lines by scripts/verify_quotes.py; text layer only (Table 1 legible; Figs 5-9 are figures and their values are not in the text); no page images rendered
status: read
diseases: []
crops: [grapevine]
regions: [Prosser, Washington]
processes: [air temperature, radiation shield, radiative error, sensor error, humidity sensor]
records: []
datasets: []
files: [julie_2007.pdf (the 2026-10-18 drop)]
---

# Tarara & Hoheisel 2007: cheap shields against a standard Gill shield

Home-made radiation shields for temperature sensors, each tested against the commercial
Gill shield (R.M. Young 41002) on bare ground near Prosser, Washington. The acceptance
rule was a daytime air temperature within 1 °C of the Gill's (l. 66). The dates as printed
disagree (received 6 December 2007, accepted 18 March 2007, l. 60).

## What it holds

- **Setup** (l. 86-132, 182-192): sensors 2 m above bare dry soil (midday albedo 0.21), each
  shield type in three replicates; type T thermocouples (Omega PR-T-24-SLE) and Vaisala
  HMP45C temperature and humidity sensors; scanned every 5 s, averaged over 15 min.
  Short 2-4 day tests, then an 11-day run from day of year 235, 2005, without rainy or overcast
  days. Buried reference thermocouples agreed within ±0.15 C (l. 143).
- **Difference from the Gill, DT** (l. 252-345): the handmade Gill (six stacked plates, US$4,
  45 min to make) -0.7 to +2.2 °C, 93 % at or below 1.5 °C, two thirds at or below 1.0 °C,
  89 % of daytime and 87 % of midday values at or below 1.5 °C; never above +1.8 °C in
  similar conditions. Open-bottomed cone -1.2 to +5.4 °C (5 % of midday values within
  1.5 °C); double cone -1.2 to +2.6 °C (23 % of midday); pagoda +2.4 to +7.2 °C, rocket +1.4
  to +3.4 °C, hanging tube +2.0 to +7.4 °C.
- **Aspirated shields** (l. 163-171, 307-342): the aspirated thermocouple shield (1.8 m s-1)
  -1.3 to +0.8 °C, 95 % within 0.5 °C; the low-speed aspirated temperature and humidity
  shield (1.2 m s-1) +0.05 to +1.5 °C at midday; the super-aspirated one (4.4 m s-1) -1.6 to
  +1.24 °C.
- **What drives the error** (l. 39, 263, 268): largest at wind under 1 m s-1 and irradiance
  above 600 W m-2; a logarithmic rise with irradiance to an asymptote near 200 W m-2; night
  errors inconsequential (l. 43). The response surfaces (Figs 7, 9) are figures only.
- **Cited** (l. 384, 402, 479): Lin et al. 2001a (radiation loading, up to 1.4 °C daytime
  error for a +5 °C inner-surface difference); Gill 1983 (over snow, above +5 °C).
- **Not printed:** any humidity error, bias or RMSE (the humidity sensors sit only in the
  aspirated shields and the results give temperature only, l. 166-171, 221-223); the mean
  difference by hour; a DOI; a data statement.

## Dependence

- No equation or model; the handmade Gill copies the geometry of the commercial one
  (l. 35-37), a shared form. Radiation principles are cited to Lin et al. 2001a, Fuchs &
  Tanner 1965, Gill 1979, 1983 and Hubbard et al. 2001.
- The `tarara2009` canopy work is from the same laboratory; a shared author is a flag.

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take.

- **Bias:** the shield is the dominant error of an air-temperature sensor. A shield-specific
  daytime bias, from the range printed: a good passive shield a few tenths of a degree to
  +2 °C above an aspirated one, a poor one up to +7 °C; aspirated within ±0.5 °C. It grows
  with irradiance and falls with wind; no formula is printed (compare `nakamura2005`).
- **Noise, drift, failure:** none. The reference thermocouple agreement ±0.15 °C is the
  only noise figure.
- **Threshold:** none, and no relative-humidity or wetness error although humidity sensors
  were mounted. A warm bias of 1-2 °C would lower a computed relative humidity.
- **Kind of result:** a field comparison of shields at one site, 11 days of clear weather
  in late summer 2005 (day of year 235 onward), not a datasheet or a lab test.
- **Can it run:** not as a model; only ranges.

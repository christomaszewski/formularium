---
id: nakamura2005
citation: Nakamura, R. & Mahrt, L. 2005. Air temperature measurement errors in naturally ventilated radiation shields. Journal of Atmospheric and Oceanic Technology 22:1046-1058
doi:
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 56 of 56 quotes found at their lines by scripts/verify_quotes.py; Eqs 11-12 checked in the page image (journal p. 1054) and Table 3 (p. 1055) on the page and in the text by the main session; Eqs 1-10 are garbled in the text layer and not verified
status: read
diseases: []
crops: []
regions: [Oregon, Corvallis]
processes: [air temperature, radiation shield, radiative error, sensor error, wind]
records: [nakamura2005.radiative_error]
datasets: [nakamura2005.corvallis]
files: [reina_2005.pdf (the 2026-10-18 drop)]
---

# Nakamura & Mahrt 2005: radiative error of a naturally ventilated shield

How far a thermistor in a multiplate shield reads above (by day) or below (by night) an
aspirated reference, and a correction from the wind and radiation measured outside the
shield. No DOI is printed (manuscript JTECH1762).

## What it holds

- **Setup** (l. 22-24, 222-224, 294-298): an Onset HOBO Pro thermistor in a Davis 7714
  naturally ventilated multiplate shield, against a platinum RTD in an aspirated shield (RM
  Young 43408), both at 1 m, 1.5 m apart, over flat grassland at Hyslop Experimental Station,
  Corvallis (44°38' N, 123°12' W). Dataset A 14 March-30 August 2002; dataset B 15 July-30
  August 2003 (Table 2). Individual offsets under 0.1 °C were removed after an intercomparison
  at 0 °C and room temperature (l. 256).
- **Error** (l. 508-514): daytime mean 0.39 °C; above 0.5 °C in 22.9 % and above 1.0 °C in
  2.6 % of daytime 30-min periods. Nocturnal mean -0.002 °C, below -0.5 °C in 4.6 % of
  nocturnal periods; it grows with radiative forcing at night too.
- **Correction** (Eqs 11-12, p. 1054; l. 516-536): RE = C0 + C1 X, X = Rad / (rho Cp T_HB U),
  Rad the shortwave outside the shield by day and the net radiation at night, rho 1.2 kg m-3,
  Cp 1004 J K-1 kg-1, T_HB in kelvin, U the 30-min scalar wind (m s-1). Table 3 (l. 547-549):
  day C0 0.13, C1 373.40; night C0 0.047, C1 355.84. R² 0.98 day and 0.94 night against 95 %
  critical values 0.21 and 0.19 (l. 557-565). Higher-order terms were not significant by an F
  test (l. 536, 553); the fit is on bin averages of X (l. 518-521). The daytime fit breaks
  down below X = 1.0e-4 and is neglected there (3.1 % of daytime data, l. 581-584).
- **Effect** (Tables 4-5, l. 634, 690): 2002, day mean 0.39 to 0.008 °C and RMSE 0.39 to
  0.11 °C; night RMSE 0.054 to 0.047 °C. 2003 test with the 2002 coefficients: day mean 0.29
  to -0.08 °C, RMSE 0.29 to 0.13 °C; night 0.05 to 0.04 °C.
- **Inside the shield** (l. 363, 391-394): albedos black 0.08, grass 0.23, white 0.56; midday
  shortwave inside the shield 1.4 %, 2.3 % and 3.1 % of the outside value; the error is
  larger over a bright ground. The coefficients may not hold for other surfaces (l. 568).
- **Instrument specifications** (Table 1, l. 232-242): HOBO accuracy ±0.2 °C, time constant
  270 s (manufacturer; 180 s in still air measured, about 26 s aspirated at 3-7 m s-1,
  l. 205-211), 300 s sampling (l. 220); aspirated RTD accuracy ±0.1 °C, shield radiation error
  under 0.2 °C at 1100 W m-2.
- **Also in the paper** (Eqs 1-7): a Monin-Obukhov argument for standardising a sensor height
  over a displacement height; a 0.15 m height error changes the reading by up to 0.2 °C in
  stable air (l. 174). Not used here.
- **Not printed:** the data's availability; error against wind in numbers (Fig. 8 only; the
  text says the error falls quickly with wind, l. 658); humidity.

## Dependence

- **Fitted** to the paper's own dataset A and tested on its own B at the same site and
  instrument: no other model. The reference's radiative error is assumed small (l. 470-472).
- **Shared calibration:** the pyranometer spectral correction is Hubbard et al. 2001's
  (l. 339-341). Radiative-error models by Tanner 1979, Anderson & Baumgartner 1998 and Erell
  et al. 2005 are cited, not used. "Lin et al. 2001a" here is the airflow paper in this
  journal, not the radiation-loading paper of the same label in `tarara2007`.

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take.

- **Bias:** a signed air-temperature bias that depends on weather, not a constant: +0.39 °C
  on average by day, about 0 at night, up to the 1.0 °C or more in 2.6 % of daytime periods
  (22.9 % above 0.5 °C). It can be generated from shortwave, wind and temperature through
  the Table 3 line, or drawn from these distributions. At night it is negative and small
  (below -0.5 °C in 4.6 % of periods).
- **Noise and drift:** not given. The paper gives the specification ±0.2 °C for the HOBO and
  ±0.1 °C for the RTD (datasheet), and the 2003 residual RMSE of 0.13 °C by day and 0.04 °C
  by night after correction (field).
- **Failure, threshold:** nothing; an air-temperature sensor only. It does not touch a
  relative-humidity or wetness threshold, although a temperature bias moves a computed
  relative humidity.
- **Kind of result:** a field result (the shield against an aspirated sensor in the open for
  two summers), with datasheet figures beside it. One shield and sensor type, one grassland
  site, in the Oregon summer.
- **Can it run:** yes; the equation and four coefficients are printed.

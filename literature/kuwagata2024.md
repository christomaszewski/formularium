---
id: kuwagata2024
citation: Kuwagata, T., Maruyama, A., Kondo, J. & Watanabe, T. 2024. Theoretical study on dew formation in plant canopies based on a one-layer energy-balance model. Agricultural and Forest Meteorology 354:109911
doi: 10.1016/j.agrformet.2024.109911
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-7 and 21-24 checked in the page images by the main session, Eqs 8-20, 22-23, 27b and 28 from the text layer
status: read
diseases: []
crops: [rice]
regions: [Japan, Kumamoto]
processes: [dew, canopy energy balance, leaf wetness duration, critical relative humidity]
records: [kuwagata2024.canopy_dew]
datasets: [kuwagata2024.kumamoto]
files: [tsuneo_2024.pdf (the 2026-10-18 drop)]
---

# Kuwagata et al. 2024: dew in a plant canopy from a one-layer energy balance

A theory paper: when and how fast dew forms on a canopy, from the energy balance of one
canopy layer, then a check against a rice paddy.

## What it holds

- **Model** (l. 285-572): Eq 1 energy balance of the layer (net radiation and longwave
  exchange against sensible and latent heat); Eq 2 absorbed radiation; Eqs 4-5 bulk fluxes with
  an exchange velocity kL (m/s) and a surface moisture availability β; Eq 6 surface temperature
  equal to canopy temperature; Eq 7 dW/dt = -E_L / ρ_w. It is "essentially similar to" Kondo
  (1996) (l. 411). Eq 10 is the maximum condensation rate (Monteith 1961). No aerodynamic or
  boundary-layer resistances: kL from the Watanabe & Mizutani (1996) convection formula.
- **Critical relative humidity** (Eq 8, approximated by Eq 24): dew forms only when rh exceeds
  rh_cr, which falls with more negative effective radiation and at lower air temperature
  (l. 834). For an effective radiation below -100 W m-2 condensation can occur at rh under
  0.4 (l. 1576-1578). At -100 W m-2 and 20 °C the maximum rate is 1.42 mm per day at rh 0.9,
  0.37 mm per day at 0.6 and 0.058 mm per day at 0.4 (l. 1582-1589). Condensation rate falls
  rapidly with rh. Eqs 12-14 hold only for |T_L - T| under 5 °C, so for rh above 0.82 at
  -50 W m-2 and above 0.87 at -100 W m-2 (l. 968-972).
- **Dew amounts** (Eqs 25-27): reference W0 uses kL from wind; potential Wp uses the maximum
  rate; when rh < rh_cr the rate is set at kL = chL u_min (Eq 27b). Leaf wetness duration is the
  time dew exceeds 0.01 mm, afternoon to 07:30 local time (l. 1374).
- **Constants** (as printed): σ 5.67e-8 W m-2 K-4; ε = 1 and β = 1 (assumed; l. 309, 403);
  ρ_w 1000 kg m-3; p 1013 hPa (l. 409); Δt 1800 s and u_min 0.05 m/s (l. 613); chL 0.05
  (l. 615); r 0.3 and τ 0.2 for paddy rice (l. 617); D_L 0.1 m (l. 629). Not printed: c_p, λ and
  ρ values, the solver, the MLC parameters.
- **Check** (l. 643-723, 1209-1401): rice 'Hinohikari', transplanted 11 June 2003, Kumamoto,
  76 m; dew measured on four nights; MLC simulated 18-27 August (LAI 6.2) and
  24 September-3 October 2003 (LAI 3.7). Measured and MLC "fairly consistent", W0 "roughly
  consistent", Wp "slightly larger"; LWD from Wp longer than from MLC. No RMSE, bias or r is
  printed. Fig. 7 (read by eye, approximate): Wp about 0.6 mm and MLC about 0.37 mm on DOY 270.
- **Not independent:** MLC (a MINCER derivative) was itself confirmed against the same field
  data (l. 725), and D_L = 0.1 m was set "for comparison with the measured data" (l. 629).
- **Garbles:** Fig. 8 panel (b) legend labels the 21 August observation 8/21-8/22 where panels
  (a) and (c) say 8/20-8/21; Fig. 7 shows more than four leaf sets (DOY 230-237) against four
  nights in the text.
- **Data:** DOI 10.17632/fmvr43csy3.3 (Mendeley Data); licence not printed.

## Dependence

- **Borrowed:** the one-layer structure from Kondo (1996); Eq 10 from Monteith (1961); bulk
  fluxes from Kondo & Ishida (1997) and Kuwagata et al. (2008); TS = TL from Jacobs et al.
  (1990), Wilson et al. (1999) and Maruyama et al. (2023); kL from Watanabe & Mizutani (1996).
- **Data:** the Kumamoto observations are those of Maruyama et al. 2023
  (`maruyama2023`), the same group (Kuwagata, Maruyama, Watanabe shared); MLC was checked on them
  too. Shared authors are a flag, and here the data and the reference model are shared.

## Bearing (2026-10-18)

For strand 3, what Agrarium's truth can take, and how it compares with the engine's RH ≥ 90 %
wetness stand-in:

- **The stand-in is not this model's rule.** Dew here needs no humidity threshold: rh_cr is an
  output that runs from near 1 at no radiative cooling to below 0.4 under strong cooling (below
  -100 W m-2). Under strong clear-night cooling the model has dew where RH ≥ 90 % would say dry,
  but at those rh the amount is small (0.058 mm per day at 0.4 against 1.42 at 0.9). With a
  weak effective radiation (cloud, wind) it is close to the stand-in. The paper itself quotes
  empirical rules near 0.9 (l. 1566).
- **Inputs a truth would need:** effective radiation (downward longwave), air temperature,
  humidity, wind and canopy radiation properties, at 30 min. A weather generator with no
  longwave or radiation-cooling variable, or one that holds Tdew = Tmin, cannot feed it.
- **Limits:** a rice paddy, one site, four measured nights, no error statistics; vineyard
  canopy constants (D_L, albedo, transmittance, LAI) are not given. Wetness here is dew
  amount over 0.01 mm, not rain wetness.
- **Can it run:** the equations are printed; the solver and several constants are not.

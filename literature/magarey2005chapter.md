---
id: magarey2005chapter
citation: Magarey, R. D., Seem, R. C., Weiss, A., Gillespie, T. & Huber, L. 2005. Estimating surface wetness on plants. In Micrometeorology in Agricultural Systems, Agronomy Monograph 47, chapter 10, pp. 199-226. American Society of Agronomy, Crop Science Society of America and Soil Science Society of America, Madison WI (editors not printed in the copy read)
doi: 10.2134/agronmonogr47.c10
read: 2026-10-19, targeted (the SWEB section pp. 205-208, the simulation passages pp. 209-211, standardization and Table 10-2 pp. 218-219) by the main session, from the University of Nebraska repository copy (agronomyfacpub 696, fetched through a headless browser); Eqs 1-3 (p. 206) and Table 10-2 (p. 219) read on the page images
status: read
diseases: []
crops: [grapevine]
regions: []
processes: [leaf wetness, energy balance, canopy water budget, sensor standards]
records: []
datasets: []
files: [unl_chapter_pw.pdf (the 2026-10-19 SWEB drop)]
---

# Magarey et al. 2005: estimating surface wetness on plants (review chapter)

A review of wetness sensors, empirical and physical models and standards, by SWEB's authors
and others; it prints SWEB's water budget and combination equation with the units of every
symbol, a year before the 2006 papers.

## What it holds

- **SWEB** is named as "a big leaf model … (Magarey, 1999)", calibrated to drying drops and
  films in a wind tunnel and laboratory (l. 347-354). Canopy water budget S = I + D − E,
  with S, C, I, D and E all in cm (Eq 1, l. 357, p. 206); interception
  I = (1 − exp(−0.5 LAI)) P after Norman & Campbell 1983, P in cm (Eq 2, l. 373).
- **Combination equation** (Eq 3, l. 384-397, p. 206 image): E = Ep W = Δ/[λ(Δ + δ)]
  {Rn + ρ Cp (h/Δ)(ea* − ea)} W, with Ep "potential latent heat flux density (evaporation),
  cm min–1", Δ and δ in mb C–1, λ in J g–1, Rn in J min–1 cm–2, ρ in g cm–3, Cp in
  J g–1 C–1, h in cm min–1, ea and ea* in mb, W dimensionless. These are the units the 2006
  paper prints in its Table 2. Worked through, the right side is g cm–2 min–1, which is
  cm min–1 of water at 1 g cm–3 (own working, from the printed units).
- **Time step:** "Models to predict surface wetness are usually run using hourly weather
  data" (l. 421); a preliminary SWEB version was run from microclimate data in Seem et al.
  2000 (l. 531, Fig. 10-2 caption l. 566). No SWEB time step is stated.
- **Crop parameters:** physical wetness models "typically" have four: crop height, LAI,
  maximum water storage and leaf wettability (l. 442-443).
- **Standard sensor** (Table 10-2, p. 219 image): water storage 0.20 cm, credited to Noilhan
  & Planton 1989 (l. 940); contact angle > 90°; short-wave absorption 0.50, long-wave 0.95.
  The 2006 papers give 0.02 cm per leaf area, credited to the same source.
- **Implementation:** SWEB "has been incorporated into Metbroker, a web-based server"
  (Laurenson 2002, l. 927).
- **Not printed:** Wd, Wf, p or Wmax; the dew term; the transfer coefficient; any time step
  for SWEB itself.

## Dependence

- Restates SWEB (Magarey 1999, thesis, not held) and its drop-and-film calibration (Magarey
  et al. 2004, held as `magarey2005b`). Interception from Norman & Campbell 1983; energy
  balance from Tanner & Fuchs 1968; storage value from Noilhan & Planton 1989 (all cited).

## Bearing (2026-10-19)

- For completing `magarey2006.sweb`: it confirms the units of Eqs 9-10 at a second source
  by the same authors, and that hourly data are the usual input. It does not print Wd, Wf
  or p. Its 0.20 cm storage (for a standard sensor) disagrees tenfold with the 2006 papers'
  0.02 cm per leaf area for the same citation; both are recorded on the record.

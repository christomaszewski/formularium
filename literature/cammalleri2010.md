---
id: cammalleri2010
citation: Cammalleri, C., Anderson, M.C., Ciraolo, G., D'Urso, G., Kustas, W.P., La Loggia, G. & Minacapilli, M. 2010. The impact of in-canopy wind profile formulations on heat flux estimation in an open orchard using the remote sensing-based two-source model. Hydrology and Earth System Sciences 14:2643-2659
doi: 10.5194/hess-14-2643-2010
read: "2026-10-25, lightly: Section 2 (the in-canopy wind formulas) and the site description; results skimmed; Eq. 18 checked on the page image, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [olive]
regions: [Italy, Sicily]
processes: [canopy flow, wind, in-canopy wind profile, wind attenuation, two-source energy balance, sensible heat flux]
records: []
datasets: []
files: [dr1025_cammalleri2010.pdf (the 2026-10-25 drop)]
---

# Cammalleri et al. 2010: three in-canopy wind profiles for a two-source energy balance, tested on an olive orchard

The paper that prints Goudriaan's exponential in-canopy wind with its attenuation coefficient computed from leaf area index, canopy height and leaf size, beside Massman's hyperbolic-cosine form.

**Read this first.** An analogue: an olive orchard (trees on an 8 x 5 m grid, canopy about 3.3 m, cover about 0.35), not a vine hedgerow (l. 391-393). The equations are for a uniform-foliage canopy. Eq. 18's exponents are garbled in the text layer; the page image prints a = 0.28 LAI^(2/3) h_c^(1/3) s^(-1/3). The vine numbers below are the reading agent's own arithmetic on assumed inputs, not data.

## What it holds

- **Eq. 17 (Goudriaan approach):** U_s = U_c exp[-a (1 - z_s / h_c)]. U_s is the wind just above the soil at height z_s (0.1 m for tall vegetation here), U_c the wind at canopy top from a logarithmic profile with a stability correction, and a the extinction factor (l. 266).
- **Eq. 18:** a = 0.28 LAI^(2/3) h_c^(1/3) s^(-1/3), with s four times the leaf area divided by the leaf perimeter (l. 299, 303-304). Cited from Goudriaan (1977).
- **Eqs. 19-20 (Massman approach):** U(z) = U_c [cosh(beta z / h_c) / cosh(beta)]^(1/2), with beta = 4 C_d LAI / (0.16 alpha*^2). C_d is typically 0.2 (l. 334); alpha* is 1.5 after Massman (1987), in a range 1.0 to 2.0 (l. 304). Table 1 adopts C_d 0.2, alpha* 1.5 and z_d = h_c/3.
- **Arithmetic for a vine (not printed):** LAI 3, h_c 2 m and s 0.1 m, chosen by the reading agent, give a = 1.6, so the wind at mid-canopy is exp(-0.8) = 0.45 of the canopy-top wind (l. 299). I re-ran the sum and it holds.
- **Site and result:** an olive field of about 13 ha in western Sicily with a flux tower (l. 385; found by grep). The abstract reports that Massman and Goudriaan profiles agree closely with measured fluxes on 7 image dates and Lalic et al. does poorly, and that profile differences matter only for sparse canopies of moderate cover (abstract, l. 38-43; found by grep).

## Dependence

Goudriaan (1977, a book, Eqs. 17-18), Massman (1987, Eqs. 19-20) and Lalic et al. (2003), all cited, not re-derived. The model is TSEB (Norman et al. 1995; Kustas and Norman 1999). Authors (Kustas, Anderson) are shared with the GRAPEX notes `nieto2019` and `alfieri2018roughness` (a flag).

## Bearing (2026-10-25)

- **Canopy wind (SWEB Eq 15):** a candidate replacement for the mid-canopy factor that does close. For assumed vine inputs it gives 0.45 of the canopy-top wind at mid-canopy. That is relative to the canopy top, not to a wind at 200 cm above a 150 cm canopy, so it cannot be compared with SWEB's 0.3 U_Z without a canopy-top to U_Z factor (not computed here).
- Not tested on vines or on a hedgerow in this paper; the vineyard test is `nieto2019` (abstract only).
- Kind of result: analogue (olive orchard); formulas cited from Goudriaan and Massman.

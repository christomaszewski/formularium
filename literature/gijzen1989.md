---
id: gijzen1989
citation: Gijzen, H. & Goudriaan, J. 1989. A flexible and explanatory model of light distribution and photosynthesis in row crops. Agricultural and Forest Meteorology 48:1-20
doi: not printed
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: [maize]
regions: [not stated]
processes: [row-crop light model, diffuse and direct light, canopy light interception, photosynthesis]
records: []
datasets: []
files: [huub_1989.pdf (the 2026-10-18 drop)]
---

# Gijzen & Goudriaan 1989: light distribution and photosynthesis in row crops

A model of diffuse and direct light absorption, with scattering and reflection, for hedgerow crops of any row geometry and leaf-area profile, with photosynthesis integrated over the row (l. 26-30). No record.

## What it holds

- **Model:** row geometry, vertical leaf-area density and leaf-angle distributions are inputs (l. 28-30); leaf photosynthesis from absorbed light is integrated over the row (l. 27-28).
- **Result:** for path widths under 30 % of the row height, light absorption and photosynthesis under diffuse light are little reduced against a closed canopy (l. 30-32); the vertical leaf-area distribution matters little (l. 32).
- **Validation:** diffuse interception checked on a young maize crop with distinct rows, LAI 2.0, row spacing 0.75 m (l. 386-390); the simulation overestimated measured light on the soil beneath it, and the interception curve shape was well simulated (l. 700-704). The percentage is garbled in the text.

## Read again in full (2026-10-28, for Agrarium D61)

- **Geometry** (Eqs 1-9, pp. 3-4): rectangular hedgerow of width Wr and height Hr, path Wp, rows of infinite length; sin(beta) = cos(alpha_c) cos(beta_c), sin(beta_c) = cos(alpha) cos(beta) (alpha the difference between row azimuth and beam azimuth, beta the beam elevation); x_hor = z tan(alpha_c); Xr = |((x_hor + x)/(Wp + Wr))| remainder; Nu = (x_hor + x - Xr)/(Wp + Wr); path through foliage P'r = (Nu Wr - x + Xr)/sin(alpha_c) for Xr <= Wr, [(Nu + 1) Wr - x]/sin(alpha_c) for Xr > Wr; Pr = P'r/cos(beta_c); leaf area crossed Lt = Pr Ld (Ld m²/m³; summed over layers for a non-uniform profile).
- **Attenuation** (Eqs 10-14, p. 5): black leaves I = I0 exp(-Oav Lt)/sin(beta); Oav the mean leaf projection on the beam (0.5 for spherical leaves, sin(beta) for horizontal ones; for other distributions from the leaf-angle frequencies in classes 0-30, 30-60, 60-90°, after Goudriaan 1988, formulae not printed), no azimuth preference (l. 216). Scattering leaves: K multiplied by (1 - sigma)^(1/2); sigma 0.2 (l. 224-225); reflection of a closed canopy (1 - sqrt(1-sigma))/(1 + sqrt(1-sigma)) (Eq. 15), spherical leaves times 2/(1 + 2 sin beta) (Eq. 16); about 6 % of light reflected (l. 263).
- **Diffuse absorbed** (Eq. 19, p. 7): Idif = I0,dif (1/pi) double integral over beta_c, alpha_c of (1 - rho) Oav (1 - sigma)^(1/2) exp[-Oav Lt (1 - sigma)^(1/2)] cos beta_c d beta_c d alpha_c; 3-point Gaussian integration in segments cut at the row corners.
- **Direct light:** "followed the same lines" as Goudriaan 1977 and Spitters 1986 (l. 314-316): not printed. Sunlit fraction Fsl and the A = Ash(1 - Fsl) + As Fsl split (Eq. 21) are named, Fsl's formula is not.
- **Row integration** (Eqs 22-23): 5 x 5 Gauss points, offsets -0.453090, -0.269235, 0, 0.269235, 0.453090, weights 0.118463, 0.239314, 0.284444; under 0.5 % from a 40 x 40 grid.
- **Check:** diffuse light on the soil under a young maize row crop (triangular rows, base 0.65 m, height 0.8 m, spacing 0.75 m, LAI 2.0) overestimated by about 5 % (the text layer prints "_,5%"; read as ~5 %, Fig. 9 not read); curve shape well simulated. Photosynthesis part (Am 0.91 mg CO2/m²/s, efficiency 0.011 mg/J PAR) not vine.
- **Bearing (2026-10-28):** a complete turbid-medium row model for any leaf-angle class set, but the direct beam sunlit fraction is left to Goudriaan 1977. Code from print: diffuse and direct attenuation along a ray (Eqs 1-10), with Fsl = exp(-K Lt) at a point as my reading of Beer's law, not printed for the row.

## Dependence

- Builds on Goudriaan-style canopy light schemes; the paper is from the Wageningen theoretical production ecology school.

## Bearing (2026-10-18)

- **Strand s3 (terrain and canopy physics):** a published row-crop light-interception model with a diffuse-light result that a vine row (hedgerow) could use. A simulator could take the geometry-to-light step for vine rows; the validation is a young maize crop, not a vine.
- Triage-grade: not read in full.

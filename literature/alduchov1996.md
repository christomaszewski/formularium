---
id: alduchov1996
citation: Alduchov, O. A. & Eskridge, R. E. 1996. Improved Magnus form approximation of saturation vapor pressure. Journal of Applied Meteorology 35(4):601-609
doi: 10.1175/1520-0450(1996)035<0601:IMFAOS>2.0.CO;2
read: 2026-11-03, in full (a scan read by OCR; page image of p. 608 checked), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [saturation vapour pressure, Magnus formula, vapour pressure deficit, dew point]
records: [alduchov1996.magnus]
datasets: []
files: [dr1103_alduchov1996.pdf (the 2026-11-03 drop)]
---

# Alduchov & Eskridge 1996: the improved Magnus coefficients (AERK)

A NOAA note that refits the Magnus form to the Goff-Gratch, Wexler and Sonntag formulations and recommends one set of coefficients for -40 to 50 °C.

**Read this first.** The text is an OCR of a scan. The exponent layout of Eq. 21 and Table 1 is garbled in the OCR; the values were read from the page image of p. 608.

## What it holds

- **Authors (l. 7):** Oleg A. Alduchov and Robert E. Eskridge, National Climatic Data Center, NOAA, Asheville.
- **Recommended form AERK (l. 779, Eq. 21, p. 608):** e_w(t) = 6.1094 exp(17.625 t / (243.04 + t)), t in °C, e in hPa (l. 781; the appendix gives pressures in hPa, l. 871). Table 1 lists the same coefficients (l. 293, garbled in OCR).
- **Range (l. 777):** -40 to 50 °C over a plane water surface.
- **Error (l. 784):** maximum relative error under 0.384 % and a maximum measure of accuracy under 0.868, against the three basic formulations GG46 (Goff-Gratch 1946), WE76 (Wexler 1976) and SO90 (Sonntag 1990).
- **Table 2 row for AERK (l. 473):** relative errors and accuracy measures against each basic formulation, with the temperature of the maximum in brackets (e.g. 0.384 at -30 °C, 0.868 at 27 °C; OCR dashes garbled).

## Dependence

- Coefficients fitted by the authors by minimising the maximum deviation from Goff-Gratch 1946, Wexler 1976 and Sonntag 1990. No observations are used. It is the Magnus (1844) form.

## Bearing (2026-11-03)

- **Record alduchov1996.magnus (engine's Magnus coefficients):** confirmed with no difference: 6.1094 hPa, 17.625 and 243.04 °C as printed (Eq. 21, p. 608), range -40 to 50 °C, authors Alduchov and Eskridge. The record's "not held" is now obtained.
- **Limit:** error figures are against other formulations, not against measurements; over ice or outside -40 to 50 °C the fit is not claimed. Kind: peer-reviewed fit to reference formulas.

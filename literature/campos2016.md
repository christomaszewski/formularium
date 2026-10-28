---
id: campos2016
citation: Campos, I., Neale, C.M.U., Gonzalez-Piqueras, J., Calera, A., Samani, Z. & Bleiweiss, M. 2017 (online 2016). Is row orientation a determinant factor for radiation interception in row vineyards? Australian Journal of Grape and Wine Research 23(1):77-86
doi: 10.1111/ajgw.12246
read: 2026-10-28, leaf angle, extinction, porosity and light measurements; by a reading agent and note writer (claude-sonnet-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Albacete, Spain]
processes: [PAR absorption, row orientation, canopy porosity, fraction of intercepted PAR]
records: []
datasets: []
files: [dr1028_campos2016.pdf (the 2026-10-28 requests drop)]
---

# Campos et al. 2017: row direction and PAR absorption in VSP vineyards, with the Oyarzun fIPAR model

Measured and modelled fPAR and APAR for VSP vineyards at three Spanish sites with different row directions, and simulated PAR absorption by row direction for 30-50 N.

## What it holds

- **Measurements** (l. 181): incoming and reflected PAR at 3.5 m (Skye SKP215 and Li-Cor 190SB); transmitted PAR hourly with a SunScan 15 cm above ground at three positions across the row under three rows.
- **Model** (l. 163-164, 238): the row-crop model of Oyarzun et al. 2007: fIPAR_h = f_B fIPAR_B + f_D fIPAR_D (Eq. 4), fIPAR_B = FGS (1 - C*p) (Eq. 5), absorptivity 0.85 (Eq. 6), fIPAR_D = 1 - t_D,d (Eq. 7). Inputs are canopy height, base height, widths, row and vine spacings, sun zenith and sun-row azimuth. The text layer garbles Eqs 4-6.
- **Fitted porosity** (l. 416-424, Table 3): effective canopy porosity by inversion: 0.32, 0.54, 0.36 (Alcocer 2008, 2010), 0.44, 0.23, 0.15 (Las Tiesas 2011), 0.44 (Los Llanos 2008).
- **Simulation canopy** (l. 220-221): width 0.90 m, height 1.8 m, base 0.4 m, rows 3.0 m, vines 1.5 m.
- **Accuracy** (l. 412, 426): RRMSE below 17 % of mean daily value; Riou 1989's RRMSE 0.09-0.14 for N-S rows (cited).
- **Not printed:** the data as a file; Table 2 canopy dimensions and fPAR are in the paper but not quoted here.

## Dependence

- **Computes** Oyarzun et al. 2007 (not read in this batch) and borrows Campbell & Norman 1998 for diffuse transmittance, Schultz 1996 for absorptivity. Compares with Mabrouk 1997 and Riou 1989. No engine overlap.

## Bearing

- A usable porous-hedgerow interception model with a fitted C*p that changes with the season (0.15-0.54).

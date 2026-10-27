---
id: mariani2007
citation: Mariani, L., Failla, O. & Capece, P. 2007. Possible synergies between phenological and crop protection models: an example for Lobesia botrana. Italian Journal of Agrometeorology 2007(3):39-44
doi:
read: 2026-10-26, in full, by a reading agent (claude-haiku-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py; Eq. 1 and Fig. 1 (p. 40) and Tables 1-4 (p. 41) read in the page images by the agent and the main session
status: read
diseases: []
crops: [grapevine]
regions: [Alghero]
processes: [phenology, grape berry moth, heat units, temperature response]
records: [mariani2007.bbch_nhh, mariani2007.lobesia_flights]
datasets: [mariani2007.alghero]
files: [mariani2007.pdf (the 2026-10-25 other-sources drop; a ResearchGate copy with a cover page)]
---

# Mariani et al. 2007: vine stages and Lobesia flights on heat hours at Alghero

Grapevine BBCH stage as a power or log of Normal Heat Hours (NHH), hourly beta-weighted
heat summed from 1 January, fitted for Cabernet Sauvignon and Chardonnay on one year at
Olmedo; and the Lobesia botrana flight model (LBfm) of Arca et al. 1993, thermal units above
8 °C to printed thresholds. Both run on Alghero's 1951-2006 temperatures to show when the
flights meet the stages.

## What it holds

- **Site and data** (l. 59, 116-128): Alghero (Santa Maria La Palma, north-west Sardinia);
  daily Tmax and Tmin 1951-2006 from the Air Force station; BBCH records from Sardinia's
  agrometeorological database and the Olmedo vineyard; Lobesia observations from Arca et al.
  1993.
- **Hours** (l. 116-117): hourly temperatures by the Parton and Logan algorithm, cited to
  Mariani 2002, not printed.
- **NHH** (Eq. 1, page image p. 40; l. 102-107, 156): fvn(T) = [2 (T - Tmin)^α (Topt -
  Tmin)^α - (T - Tmin)^2α] / (Topt - Tmin)^2α for Tmin ≤ T ≤ Tmax, else 0, a beta after
  Wang & Engel 1998 with Tmin 7, Topt 26, Tmax 35 °C; one hour at 15 °C gives 0.55 NHH. The
  printed α = ln[2 / ln((Tmax - Tmin)/(Topt - Tmin))] misplaces a bracket against Wang &
  Engel's ln 2 / ln(...); Fig. 1 labels the optimum 22-28 °C.
- **Stage equations** (Table 1, p. 41; Olmedo 2006): Cabernet Sauvignon vegetative BBCH =
  1e-24 NHH^9.5639 (r² 0.9167), reproductive BBCH = 27.28 ln NHH - 123.27 (0.9707);
  Chardonnay 8e-15 NHH^5.9521 (0.8111) and 29.77 ln NHH - 138.03 (0.9614). n not printed.
- **Validation** (Table 2; stages 71 and 77, 2000-2004): Cabernet MAE 7.35, RMSE 5.80 d,
  EF 0.60, r² 0.73; Chardonnay MAE 6.59, RMSE 5.60 d, EF 0.52, r² 0.54.
- **Flights** (Table 3, l. 188-230): thermal units above 8 °C; first flight 270-470,
  second 825-1070, third 1510-1990, fourth 2035-2530, from Arca et al. 1993 adjusted on
  1993 observations (not printed); the caption says four flights, the text three.
- **Results** (l. 269-285, Table 5): Bai-Perron breaks in the simulated flights, the second
  starting earlier from 1991 and the third from 1991; Alghero is Mediterranean by two
  criteria (Table 4).
- **Not printed:** the Table 1 sample sizes, Table 2's significance column, the 1993
  adjustment data, the hourly method, any DOI.

## Dependence

- **Stage equations fitted to** Olmedo 2006 (`mariani2007.alghero`), observed stages and
  station temperatures; validated 2000-2004. **Flight thresholds** taken from Arca et al.
  1993 and adjusted on 1993 data: fitted to that paper's observations, inferred.
- **Borrows** Wang & Engel 1998's beta and the IPHEN NHH framework (Mariani et al. 2007);
  national equations from Calò et al. 1997 are cited, not printed.

## Bearing (2026-10-26)

- For Agrarium's phenology truth (the 10-14 search): a stage-on-heat-sum form with an
  hourly beta weighting, one year's fit, printed; kin by form to the engine's degree-day
  phenology records. For Cooptera's berry moth work: the LBfm thresholds, a plain heat-sum
  flight model beside `castex2020.lgm`, which it does not share data or equations with.

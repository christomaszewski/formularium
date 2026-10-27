---
id: leolini2022
citation: Leolini, L., Moriondo, M., Rossi, R., Bellini, E., Brilli, L., López-Bernal, Á., Santos, J. A., Fraga, H., Bindi, M., Dibari, C. & Costafreda-Aumedes, S. 2023 (online 2022). Use of remote sensing-derived fPAR data in a grapevine simulation model for estimating vine biomass accumulation and yield variability at sub-field level. Precision Agriculture 24:705-726
doi: 10.1007/s11119-022-09970-8
read: 2026-10-26, a light reading (methods, results and conclusions) by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Eq. 2 and Eqs 4-6 (printed pp. 711, 714) read in the page images by the agent
status: read
diseases: []
crops: [grapevine]
regions: [Tuscany]
processes: [whole-vine model, leaf area index, fPAR, NDVI, yield]
records: []
datasets: []
files: [leolini2022.pdf (the 2026-10-25 other-sources drop, from CNR IRIS)]
---

# Leolini et al. 2023: a radiation-use-efficiency vine model forced with measured or satellite fPAR

UNIFI.GrapeML, whose equations sit in Leolini et al. 2018 and 2019 (not held), is run on two
Sangiovese vineyards with the fraction of absorbed radiation forced from measured LAI or from
Sentinel-2 NDVI, so that biomass and yield follow the vigour zones. A method paper for a
whole-vine model, not a formulation printed here.

## What it holds

- **Sites** (l. 139-177): Site A, 0.5 ha at Suvereto, 2015; Site B, 1.4 ha at Fonterutoli,
  2018; both Sangiovese.
- **Measurements** (l. 198-228): Site A LAI with a LAI-2000 on DOY 162 and 190 in three
  vigour areas (75 vines), pruning weight in February 2016 at 50 % dry matter from
  unpublished data; Site B fPAR and LAI by ceptometer on DOY 177, 220 and 268, 39 Sentinel-2A
  pixels, fruit fresh weight on 208 plants; radiation by Hargreaves-Samani (l. 245).
- **fPAR from LAI** (l. 371): fPAR = 0.149 LAI + 0.0585, r² 0.94, from Site B's ceptometer
  pairs, used also to force Site A (l. 353-356).
- **fPAR from NDVI** (l. 387): fPAR = 1.1638 NDVI - 0.1426 after Myneni & Williams 1994, on
  NDVI rescaled by canopy cover with coefficients not printed (l. 378-383).
- **Model** (l. 124, 293, 300-330): daily biomass by radiation-use efficiency (Bindi et al.
  1997) and transpiration efficiency, the green LAI in three stages with senescence after
  veraison; SLAE, HI and HIcutoff adjusted here, the Sangiovese set from earlier work
  (l. 399-403); HI 51 % from measurements (l. 570).
- **Fit** (l. 486-490, 569): Site A LAI r² 0.96 and RMSE 0.09, shoot biomass r² 0.61 and RMSE
  19.86 g m⁻²; Site B yield r² 0.47, RMSE 75.52 g m⁻². Site A LAI on DOY 149 and 224 comes
  from a Caruso et al. 2017 relation, not measured (l. 350-351).
- **Inconsistencies:** yield "even without a specific model calibration" (l. 685) against
  the HI set from measurements (l. 570); three day-of-year mismatches (l. 259/655, 218/531,
  561).

## Dependence

- **Computes** UNIFI.GrapeML (Leolini et al. 2018a, 2019) with the Bindi et al. 1997 RUE
  approach and the UNIMI.SoilW water balance; **calibrated** on Sangiovese data of Bindi
  et al. 1997-2005 and Leolini 2019, not named here, with HI adjusted on Site B.
- The fPAR-LAI line is fitted to Site B's own ceptometer pairs (observed); Site A's LAI
  series is partly a model's (Caruso 2017).

## Bearing (2026-10-26)

- For Agrarium's growth truth (the 10-14 search): a whole-vine model's validation numbers
  and a printed fPAR-LAI line (0.149 per unit LAI) for Sangiovese canopies. No record: the
  model's equations are not in this paper, and the tools run no whole-vine model.

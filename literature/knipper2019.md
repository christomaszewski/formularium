---
id: knipper2019
citation: Knipper, Kyle R., Kustas, William P., Anderson, Martha C., Alsina, Maria Mar, Hain, Christopher R., Alfieri, Joseph G., Prueger, John H., Gao, Feng, McKee, Lynn G. & Sanchez, Luis A. 2019. Using High-Spatiotemporal Thermal Satellite ET Retrievals for Operational Water Use and Stress Monitoring in a California Vineyard. Remote Sensing 11 (issue 18):2124
doi: 10.3390/rs11182124
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 31 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [California]
processes: [evapotranspiration, remote sensing]
records: []
datasets: []
files: [10-3390-rs11182124.pdf]
---

# Knipper et al. 2019: satellite ET for water use and stress in a California vineyard

From USDA-ARS and E&J Gallo.

## What it holds

- Vineyard test of an operational thermal-satellite ET product: merlot, 16 ha, 25 km west of Fresno, California, May-October 2018 (l. 159, l. 158). Four blocks with variable-rate drip and one tower each (l. 171); precipitation only 12 mm (l. 169).
- Blocks 1 and 2 had irrigation withheld 14 June-23 July (l. 491).
- The product is ALEXI + DisALEXI + STARFM (GOES, MODIS, Landsat) at 30 m, weekly, with no equations given (l. 273). Fused ET is two days behind (l. 329); the last two days are scaled by CIMIS ETo (l. 331).
- Landsat 8 T1 latency averaged 21.6 days (l. 315).
- Daily MAE 0.61-0.85 mm/day retrospective and 0.71-0.82 operational, against a 0.80 target (l. 439). Block 4 operational MBE is -0.61 mm/day (l. 476).
- Operational weekly ET fell from 45 to 35 mm/week on 19-26 July in the stressed blocks (l. 511); NDVI-based ETc stayed near 40 (l. 513). The stress signal reached users two weeks late (l. 601).
- ETc = Kc x ETo, Kc = 1.2 NDVI, Ko fitted to block 4 tower ET (l. 381, l. 385). Observed ET is closure-corrected by the residual method (l. 236), so the check is not fully independent.
- No leaf wetness, interception or wet-canopy evaporation; a dry, irrigated site.

## Dependence

- It computes ALEXI and DisALEXI with STARFM data fusion, and FAO-56 crop coefficients from NDVI (its Ko fitted to one block's tower ET).
- No author of an engine model.

## Bearing (2026-10-08)

- Clear. Weekly 30 m vineyard ET against towers, and the latency of the Landsat scenes it needs: the error and delay of a satellite ET operator in a vineyard.

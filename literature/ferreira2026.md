---
id: ferreira2026
citation: Ferreira, L., Marques, P., Portela, F., Sousa, J.J., Peres, E., Morais, R. & Pádua, L. 2026. TLS-grapevine2024: A terrestrial laser scanner point cloud dataset of grapevines at different phenological stages. Data in Brief 65:112614
doi: 10.1016/j.dib.2026.112614
read: 2026-10-27, lightly: abstract, value of the data, specification table, the site, methods and limitations (Europe PMC full text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Portugal, Douro, Vila Real]
processes: [dataset, point cloud, terrestrial laser scanning, leaf area index, phenology, canopy structure, UAV photogrammetry]
records: []
datasets: [ferreira2026.vilareal]
files: [syn1027_ferreira2026tls.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Ferreira et al. 2026: TLS-grapevine2024, laser-scanned vines at nine growth stages with LAI, yield and pruning weight

A data paper for terrestrial laser scanner (TLS) point clouds of two vine rows through one season, with a UAV survey before harvest and per-vine ground truth. No record: a dataset.

**Read this first.** The paper is CC BY-NC (l. 10); the 2026-10-22 catalogue gives CC BY 4.0 for the Zenodo record and that was not re-checked, so the data licence is unconfirmed. Leaf area index and the UAV survey were taken once only, at BBCH 89 (l. 263, 269, 274).

## What it holds

- **Where to get it** (l. 26): Zenodo 10.5281/zenodo.16751663. Formats: .las clouds, .tif rasters, .shp shapefiles and .csv ground truth, organised in one folder per BBCH stage (l. 20, 84).
- **Licence** (l. 10): the article is open access under CC BY-NC. The Zenodo record's licence is not in the paper; the earlier catalogue's CC BY 4.0 is cited from it, unchecked.
- **Site** (l. 24, 159): one 0.10 ha vineyard at Arroios, Vila Real, Portugal, 435 m. A 117 m2 area with two rows holds 52 vines of Touriga Nacional, Viosinho and Cardinal; 38 of them (29 Touriga Nacional, 9 Viosinho) were analysed (l. 159).
- **Years and time step** (l. 32, 204, 259): nine field campaigns, 2024-04-09 to 2025-01-29, one per BBCH stage; one season only. The abstract gives 15 TLS scans along the two rows at nine stages (l. 11); the text does not say whether 15 is per stage or in all.
- **Variables** (l. 11, 263): Leica BLK360 TLS clouds; UAV multispectral (five bands) and RGB photogrammetric clouds and orthomosaics at BBCH 89; per vine, leaf area index (LI-COR LAI-2200C), grape production and pruning wood biomass.
- **How labels were made** (l. 263): ground truth observed by instruments and standard field protocols (LAI with a canopy analyser, corrected in the maker's software, l. 263-266; grape production and pruning biomass by field protocol, l. 11, 34-36); point clouds registered and filtered in software. No plant model computes a label.
- **Authors' limits** (l. 273-275): no senescence (BBCH 91-99) and some flowering stages missing (placeholder folders); LAI and UAV data at one date only; no phytosanitary records; no multi-year data.

## Dependence

- Registration and filtering by Cyclone REGISTER 360 PLUS and CloudCompare, photogrammetry by Pix4Dmapper (l. 22). The same group wrote the Portela 2026 leaf-image set (a shared-author flag) and a related TLS-versus-UAV paper (Sensors 2024, not read). None recorded otherwise.

## Bearing (2026-10-27)

- **D60 tier 4 (research only: a terrestrial laser scanner), with the UAV imagery at tier 3; a check of rendered output.** Real canopy geometry through a season gives the viewer's two-level vine models something to be measured against (height, depth, row spacing 2.1 m and plant spacing about 1.1 m, l. 159), and per-vine LAI at harvest to test a canopy model's leaf area.
- **For D58, no disease.** No phytosanitary data and no weather in what was read, so it cannot judge a disease variable; it could judge a canopy or phenology variable if the weather were taken from a nearby station.
- **Limits:** two rows, 52 vines (38 analysed), one season, LAI once, a non-commercial paper licence, 15 scans with the per-stage split not stated.

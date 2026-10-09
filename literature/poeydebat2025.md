---
id: poeydebat2025
citation: Poeydebat, C., Courchinoux, E., Mazet, I. D., Rodriguez, M., Chataigner, A., Lelièvre, M., Goutouly, J.-P., Rossi, J.-P., Raynal, M., Delière, L. & Delmotte, F. 2025. Digital droplet PCR quantification and field-scale spatial distribution of Plasmopara viticola oospores in vineyard soil. Applied and Environmental Microbiology 91(12):e0166725
doi: 10.1128/aem.01667-25
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5) in Europe PMC's full-text XML (PMC12724222, open access); the spatial numbers, the site and the row contrast checked in that text by the main session; authors from Europe PMC's record
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [oospores, inoculum spatial structure]
records: []
datasets: [poeydebat2025.villenave]
files: []
---

# Poeydebat et al. 2025: oospores in a vineyard's soil, mapped

The first field-scale map of P. viticola oospores: soil sampled on a grid, oospore DNA
counted by digital droplet PCR, a variogram fitted. It settles the patch size that search
summaries reported as 15 or 25 m.

## What it holds

- **Site:** INRAE Bordeaux, Villenave d'Ornon (sandy-gravel soil).
  - Merlot planted 2011, 18 rows of 68 vines, 0.22 ha (70 × 32 m), 1.6 m between rows and
    0.95 m along them.
  - Organic, copper only. The soil is ridged under the row in autumn and reopened in
    spring.
- **Sampling, March 2022:**
  - **Regular grid:** 198 samples at 2.85 × 3.2 m nodes, 0-15 cm.
  - **Nested plots:** five more, 120 samples, at about 3, 0.8 and 0.2 m.
  - **Depth profiles:** 24 samples in six holes, 0-40 cm.
  - **Soil only;** leaf litter was not assayed as such.
- **ddPCR:**
  - 215 ± 37 ITS copies per genome (175-281 across seven strains).
  - Detection between 1 and 50 oospores per 2 g of soil, by criterion.
  - Oospores 0 to 1,858 per g, 303 ± 308. Present at every sampled location.
- **Spatial structure** (regular grid, 2 m lags to 60 m, no clear anisotropy):
  - **Variogram:** a Matérn model with smoothness fixed at 0.2, on log data. Range 15.83 m;
    nugget 0.156, structural variance 0.354, sill 0.510, so the nugget is about 31 % of the
    sill.
  - **Patches:** "15-m diameter patches of concentrically increasing oospore
    concentration", from the kriged map. "25 m" appears nowhere in the paper.
  - **The large nugget:** sub-grid variation, or measurement error.
- **Row against inter-row:** "five to six times more concentrated in the ridge of soil
  below the vine stocks" (9.32 against 1.72 ITS copies per µL). The text also gives "4-5
  times" and "five times". The contrast holds everywhere in the field.
- **Depth:** less below 20 cm than in the top 10 cm.
- **Infectivity:** density predicted a leaf-disc bioassay, though weakly (R² 0.19 for
  infected discs, 0.33 for infected area; 40 samples).
- **No link to the previous season:** the disease "we unfortunately did not assess the
  year before our soil survey".

## Dependence

- **No formulation;** the variogram is a description.
- **Author flags:** J.-P. Rossi (CBGP, Montferrier) is not Vittorio Rossi. Raynal (IFV) is
  a co-author of Chen 2019's chapters on IFV's data. Delmotte co-wrote Maddalena et al.
  2020 on population genetics. None computes or fits an engine model here.

## Bearing (2026-10-09)

- **For Agrarium's truth:** its oospore field (`fields.inoculum_length_m`, assumed 25 m) is
  white noise smoothed by a Gaussian.
  - **Too smooth:** Gaussian covariance is far smoother than Matérn with smoothness 0.2.
  - **Too large:** 25 m smoothing gives patches much larger than 15 m.
  - **No nugget,** where the measured one is a third of the sill.
  - **No row contrast,** where the measured one is fivefold.
- **A field-scale pattern for history matching:** sample the truth's field as the paper
  did, on a 2.85 × 3.2 m grid, and compare the variogram's range, nugget share and
  isotropy.
- **Caveat:** the paper maps soil, and the truth's field is oospores in the litter.

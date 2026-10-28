---
id: brown2024
citation: Brown, L.A., Morris, H., MacLachlan, A., D'Adamo, F., Adams, J., Lopez-Baeza, E., Albero, E., Martínez, B., Sánchez-Ruiz, S., Campos-Taberner, M., Lidón, A., Lull, C., Bautista, I., Clewley, D., Llewellyn, G., Xie, Q., Camacho, F., Pastor-Guzman, J., Morrone, R., Sinclair, M., Williams, O., Hunt, M., Hueni, A., Boccia, V., Dransfeld, S. & Dash, J. 2024. Hyperspectral Leaf Area Index and Chlorophyll Retrieval over Forest and Row-Structured Vineyard Canopies. Remote Sensing 16(12):2066
doi: 10.3390/rs16122066
read: 2026-10-27, lightly: abstract, the look-up-table and validation methods, results 3.2 to 3.4 (Tables 6 and 7) and discussion 4.1 to 4.2 (open-access MDPI PDF), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 18 of 18 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine, forest]
regions: [Spain, Valencia, UK, Wytham Woods]
processes: [radiative transfer, synthetic training data, look-up table, canopy reflectance, leaf area index, chlorophyll, row geometry, hyperspectral imagery]
records: []
datasets: []
files: [syn1027_brown2024.pdf (the 2026-10-27 drop)]
---

# Brown et al. 2024: look-up-table retrieval of LAI and chlorophyll from airborne hyperspectral images, with a vineyard row-structure model

Simulates 100,000 canopy spectra per site with PROSPECT leaf optics and a canopy model (SAIL as a turbid medium; rowSAIL for the vineyard, INFORM for the forest) and retrieves leaf area index (LAI) and canopy chlorophyll (CCC) by nearest simulated spectra. No record: a method with a small field test.

**Read this first.** "Hybrid" here means a hybrid radiative-transfer model (turbid medium plus row or crown geometry), not machine learning on simulations. The vineyard result is near zero correlation: the authors read rowSAIL as an improvement (l. 707) because its bias fell, although r2 stayed at 0.02. Only the vineyard rows of Table 7 are used below; the forest results are in the paper.

## What it holds

- **Generator** (l. 358, 360, 431): for each site two look-up tables of 100,000 simulated reflectances each (turbid SAIL, and the geometric hybrid model), inputs drawn at random from fixed, uniform or truncated Gaussian distributions (Tables 2 and 3). The retrieval is the mean of the 100 closest simulated spectra by root mean square difference over bands. Nothing is trained: the table is the model.
- **Real samples** (l. 180, 473): the Valencia Anchor Station area, dominated by vineyards (Vitis vinifera); campaign 14 to 16 June 2017, 45 LAI units and 40 chlorophyll units, each 40 m x 40 m, 10 to 20 locations per unit. An airborne image (AisaFENIX, 17 June 2017, per the reading agent) is compared with in-situ LAI.
- **Test** (l. 473, 547): the same 45 units used for the comparison; no split, because no parameter is fitted to them. The in-situ vineyard LAI is narrow and sparse: mean 1.37, SD 0.68 (l. 547).
- **SAIL (turbid) at the vineyard** (Table 7, l. 634, 635, 638): LAI r2 0.05, RMSD 0.92, bias -0.64; canopy chlorophyll r2 0.00, RMSD 0.27 g/m2. Almost all retrievals were LAI about 1 (l. 582), "a failure of SAIL to adequately simulate" the canopy. Column order is the reading agent's reading of the table text.
- **rowSAIL at the vineyard** (Table 7, l. 639, 640, 643): LAI r2 0.02, RMSD 0.88, bias -0.13; canopy chlorophyll r2 0.01, RMSD 0.30 g/m2. Row geometry cut the LAI bias and left the correlation at zero.
- **All sites pooled** (l. 580, 588): SAIL r2 0.58, RMSD 1.61; the geometric hybrid (rowSAIL or INFORM) r2 0.75, RMSD 1.21, bias -0.30. The pooled figures are driven by the forest sites.
- **Authors' reading** (l. 67, 624): SAIL is known to perform poorly over heterogeneous canopies, including row crops; the near-zero vineyard r2 is "likely a result of the very limited" LAI range.
- **Without synthetic data:** none. There is no empirical (index or regression) baseline on the same units.

## Dependence

- PROSPECT, SAIL, rowSAIL (row geometry; the reading agent notes its relation to the rowMCRM vineyard work of Zarco-Tejada and colleagues) and INFORM; ATCOR-4 and FLAASH atmospheric correction. In-situ LAI from the authors' earlier campaign paper (cited as ref. 37, per the reading agent). `zarcotejada2013` is a separate study of the same row-structure family; no shared author appears in Brown's list.

## Bearing (2026-10-27)

- **D60 (several physical models per gap):** a direct test of a one-dimensional against a row-structured model for vine LAI, with 45 field units: geometry moves the bias (-0.64 to -0.13) and not the scatter (r2 0.05 to 0.02). It gives Agrarium's tier-3 canopy imagery sensor a measured error scale: an RT retrieval of vine LAI may be biased low (-0.64 against a mean of 1.37 is 47 %; arithmetic, not printed) and uncorrelated with the field value.
- **Rendered canopies:** a 3-D vine canopy that Agrarium's viewer could render is the geometry rowSAIL idealises; this paper gives no test of a rendered or voxel canopy.
- **Not shown:** an empirical baseline, a sample beyond one campaign and one June day, a training of any model on the simulations, disease or water status.

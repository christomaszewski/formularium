---
id: hugalde2020
citation: Hugalde, I. P., Agüero, C. B., Barrios-Masias, F. H., Romero, N., Nguyen, A. V., Riaz, S., Piccoli, P., McElrone, A. J., Walker, M. A. & Vila, H. F. 2020. Modeling vegetative vigour in grapevine - unraveling underlying mechanisms. Heliyon 6:e05708
doi: 10.1016/j.heliyon.2020.e05708
read: 2026-10-14, in full by a reading agent (claude-haiku-5-5); 54 of 54 quotes found at their lines by scripts/verify_quotes.py; the equations lose their symbols in the text layer, so Figure 1 (eqs 1-18), eqs 4-7, Table 4, eq 19 and the GA fit were checked on page images by the agent; Table 3 and the count of its Lpr values above 0.454 read in the text by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Davis, California]
processes: [vigour, carbon balance, hydraulics, growth model]
records: []
datasets: []
files: [in_s_2020.pdf]
---

# Hugalde et al. 2020: a hydraulic and carbon model of grapevine vigour

A daily model of the canopy dry weight of a potted, single-stem rootstock seedling, built in
Vensim from a water side (root hydraulics, stomata) and a carbon side (photosynthesis,
respiration, partitioning). It is run for 90 days at a fixed 25 °C and checked on 28 grafted
genotypes. Read in full, for its structure and for whether anything in it can run a
vineyard vine.

## What it holds

- **Structure** (Figure 1, eqs 1-18; l. 134-137, 197-226, 284-305). The model "integrates a
  number of already existing models" (l. 138-139):
  - Root hydraulic conductance Lp = Lpr x root biomass (eq 1); plant conductance kH = Lp
    (eq 2); leaf-specific kL = kH / LA (eq 3, printed with an approximate sign).
  - Atmospheric deficit q' = (es(TL) - ea) / Pa (eq 4); guard-cell osmotic potential held
    at -3 MPa (eq 5).
  - Stomatal conductance by the Buckley form (eq 6, l. 140, 197): gs = X (-Ψπg + Ψπe -
    M Ψsoil + M Ψπe) / (1 - X (M kL^-1 - fg rg) q'), with X = 105 and M = 0.98.
  - Photosynthesis by diffusion (eq 7): A = (gs / 1.6)(Ca - Ci); whole plant Aplant = A x
    LA (eq 8).
  - Daily carbon balance (eq 9): Biomass = (Aplant - Respiration) x 0.648 x i x GAs, with
    respiration = 0.45 x Aplant (eq 10). The 0.648 g carbohydrate a day per m² of leaf
    comes from 1 µmol CO2 per m² per s, 15 h of sun and glucose at 180.156 g/mol (l. 222-224).
    Neither it nor the 0.45 is cited.
  - Growth factor i = f(Lpr) (eq 11); fitted i = -2.04 Lpr + 0.926 (eq 19, Pearson 0.73,
    p = 0.016, l. 440-444), on group means of Lpr and vigour (l. 435-441).
  - Partitioning (eqs 12-14): canopy = biomass x partition factor, root = biomass x
    (1 - factor), factor = j x GAs with j = 0.05, "inferred" from residuals of observed
    against predicted biomass versus SLA (data not shown, l. 446-450).
  - Leaf area LA = canopy biomass x SLA (eq 15), SLA a genotype input (l. 301-303); leaf
    water potential ΨPL = Ψsoil - E / kL - Ψπl (eq 17); E = gs q' (eq 18).
  - GAs = a^((time - b)² / c), a = 22.27, b = 27.44, c = -1901, time in days of the growing
    season (l. 478-484); an empirical fit to "purported" gibberellin dynamics of other
    species and grape leaves. It is a function of days, not a heat sum.
- **Constants** (Table 4, l. 455-462): Ca 375 ppm, Ci 0.7 x 375 ppm, Ψsoil 0.01 MPa (sign
  unclear, below), Ψπg -3 MPa, TL 25 °C, ea 3 hPa, j 0.05, i variable, X 105, M 0.98. Run
  for 90 days from 0.5 g initial biomass, Ψsoil -0.01 MPa, q' 0.03 (l. 347-348, 455).
  Inputs: Lpr and SLA per genotype; output: canopy dry weight. Feedback loops: LA to Aplant
  to biomass to LA, and Lp to kH to gs to biomass to Lp (l. 296-304).
- **Data** (l. 36-41, 318-345, 434-444):
  - Progeny of Ramsey (Vitis champinii) x Riparia Gloire, multiplied by green cuttings in
    spring 2014, one shoot in 4 L pots, three replicates, greenhouse at 25 °C (l. 321-324);
    summers 2014 and 2015; 125 genotypes (Figure 2); dry weights after 60 days (l. 434),
    leaf area by LI-3100C (l. 437).
  - gs on 40 genotypes (2014) and 50 (2015) (l. 322); Lpr by pressure-flow on 50 (l. 334).
  - Pruning weights of 2-year-old field vines at UC Davis, 108 genotypes, year not stated
    (l. 442-443); pot canopy against pruning weight R 0.91 (Figure 3, l. 471).
  - Validation (l. 338-345): 30 woody cuttings from the 2015 set, bench-grafted to
    Cabernet Sauvignon, 28 used, in nine vigour groups; group-mean inputs (Table 3). R 0.85,
    mean squared prediction error 5 g, RMSE 2.2 g, observed range 0.65 to 13.47 g
    (l. 498-500); mean bias share 0.89, line bias share 0.003, random share 0.10
    (l. 476, 503, 512). Predictions run low: "consistently lower than the observed ones".
  - A plant with the Lpr of a small plant would be 42 % larger (l. 538-539, Figure 6a).
- **Unsettled points** (the reading agent's "garbled" field, with the main session's
  checks):
  - **Eq 19 sign.** i = -2.04 Lpr + 0.926 is negative above Lpr = 0.454 (0.926 / 2.04). Table
    3 runs from 0.129 to 1.776. Of its 28 genotypes, 11 are above 0.454 (the main
    session's count), so eq 9 would give negative biomass for them. The paper prints no
    unit or sign rule for eq 19.
  - **Lpr units differ.** l. 331 gives "m3 g DW-1 s-1 M-1 Pa"; Table 1 (l. 255) "mmol H2O
    m2 s-1 MPa-1 g-1"; Table 3 (l. 393-395) "mmol m-2 s-1 MPa-1"; the simulation text
    (l. 538-540) uses mmol H2O m-1 s-1 MPa-1 g-1 with values 0.005 and 0.6. The range
    behind eq 19 cannot be fixed from the text.
  - **GA units.** Table 1 gives GAs in ng g-1 (l. 275), but the fit with the printed a, b, c
    runs from about 0.002 to 1 over days 0 to 90, with 1 at day 27.44 (the reading agent's
    calculation).
  - **Soil potential sign.** Table 4 prints Ψsoil as 0.01; the text says -0.01 MPa
    (l. 347-348).
  - **Eq 7 is called Farquhar** (l. 213) but is a diffusion form; the biochemical model is
    not in the paper.
  - Also not printed: Ψπe, fg and rg values (Table 4 omits them); the units of q' (Table 1,
    l. 249); the piecewise growth-rate fits (l. 318-320); the year of the field pruning data.

## Dependence

- **Borrowed structure,** as the paper says (l. 138-143): stomatal conductance from Buckley
  et al. 2003 (eq 6 follows the Buckley 2005 form, l. 197; X from Buckley 2003, l. 462); leaf
  temperature from Campbell & Norman 2012; guard-cell osmotic potential after Taiz et al.
  2015 and Tardieu & Simonneau 1998; photosynthesis said to follow Farquhar et al. 1980.
  Shared equations, borrowed and not fitted.
- **Own:** the 0.648 and 0.45 constants (assumed, no source), i (eq 19) and j, fitted to
  this progeny's group means.
- **Shared calibration data:** the genotypes come from the Ramsey x Riparia population of
  Hugalde et al. 2017 (l. 321), and Figure 4 is "adapted from" it (l. 510): the same
  population and data as that paper. Shared authors (Walker, Barrios-Masias) are a flag only.
- **The GA course** is a fit to other species' seasonal data (Kopcewicz 1968; Yörük et al.
  2004; Acheampong et al. 2015), not to this progeny.

## Bearing (2026-10-14)

- **Not the engine's form, and nothing the truth can run:** a carbon-and-water balance of
  potted rootstock seedlings at a fixed 25 °C for 90 days. It has no heat sum, no vineyard
  vine, no phenology and no leaf-area-in-time curve (SLA is an input and leaf expansion is
  not modelled). Its growth factor as printed goes negative for 11 of the 28 genotypes of
  its own validation table. No record.
- **Reported, not used:** the hydraulic and stomatal structure is a reference for how a
  water-limited growth piece could look. The sub-estimation of vigour (mean bias 0.89 of the
  error) is the paper's own caveat.

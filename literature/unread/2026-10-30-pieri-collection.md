# Philippe Pieri's papers (2026-10-30): what was read, and leads not obtained

A collection of 33 PDFs by or with Philippe Pieri (INRAE Bordeaux) was gathered at Chris's
request on 2026-10-27, into the library's `inbound/pieri-2026-10-27/`. Its `metadata/records.json`
holds the HAL, OpenAlex and Crossref inventory, 139 records.

Four were held already: `riou1989`, `pieri2003`, `gowdy2022`, `vanleeuwen2023`. The other 29 were
read on 2026-10-30 by three reading agents (claude-sonnet-5-5). Every quote, 436 in all, was
rechecked by the main session with `scripts/verify_quotes.py`.

## What the collection gives Agrarium

- **In-canopy temperature, measured:** air at 30, 60, 90 and 120 cm in a Saint-Émilion row,
  2016-2020, cover crop against tillage (`deresseguier2023`). The nearest paper to Agrarium's
  canopy temperature.
- **Transpiration:** vine transpiration as a fraction of Penman's ETP, k = Rg,v / (0.8 Rg),
  about 0.5 for the Bordeaux trellis (`riou1994`, `riou1995`).
- **Radiation and reference ET:**
  - satellite radiation and ET0 at Bordeaux (`bois2008`, `bois2008b`, `bois2008c`);
  - a Bordeaux-adjusted Turc formula;
  - a daily diffuse fraction, the same fit as `pieri2003`'s Eq. 3.
- **Whole-vine conductance:** the two-source method in full (`gowdy2022b`). Its Eq. 2's sign
  is flagged.
- **Berry temperature:** modelled exposed berries up to 10 °C above bunch air (`pieri2016`); a
  field warming of the bunch zone by 1.5 °C (`wu2019`); heated cuttings (`pillet2012`,
  `ouakedlecourieux2017`, `lecourieux2020`).
- **Climate change:** CLIMATOR ran no downy mildew model (`brisson2010`, `gouache2010`,
  `gouache2011`). Its one vine disease model is Fermaud's Botrytis model, and its wetness model
  is for wheat leaves. Sgubin et al. 2023 use a seasonal rain-by-temperature index for disease.
- **Botrytis:** light and cluster compactness change the spread in clusters, in growth-chamber
  trials (`fermaud2001`).
- **Phenology:** a GFV maturity zoning of Bordeaux (`bois2018`). GFV is not among the engine's
  models (it runs `cortazar2009.brin` and a GDD5 budburst sum). Being a degree-day sum, its kinship
  is for Agrarium to judge.
- **Not useful to Agrarium:** `itier2010` (aquifer recharge), `lecomte2012` (esca), the reviews
  `dai2011`, `vanleeuwen2019b` and `torregrosa2017`.

Candidate formulations, with their equations and pages, are in the drop
(`2026-10-30-pieri/*/reading/ANSWER.md`). None was added to the catalogue in this pass.

## Leads not obtained

From the inventory's Crossref, OpenAlex or HAL records. None is in the collection.

**Microclimate and wetness** (the two Pieri 2010 papers were obtained on 2026-10-30, from Chris: notes `pieri2010`, `pieri2010b`)
- Pieri, P. 2010. Modelling radiative balance in a row-crop canopy: Row–soil surface net
  radiation partition. Ecol. Model. 221(5):791-801. doi:10.1016/j.ecolmodel.2009.11.019
- Pieri, P. 2010. Modelling radiative balance in a row-crop canopy: Cross-row distribution of
  net radiation at the soil surface and energy available to clusters in a vineyard. Ecol. Model.
  221(5):802-811. doi:10.1016/j.ecolmodel.2009.07.028
- Pieri, P. & Fermaud, M. 2005. Effects of defoliation on temperature and wetness of grapevine
  berries. Acta Hortic. 689:109-116. doi:10.17660/actahortic.2005.689.9 (the field source the
  heating papers cite)
- Riou, C., Pieri, P. & Valancogne, C. 1987. Variation de la vitesse du vent à l'intérieur et
  au-dessus d'une vigne. Agric. For. Meteorol. 39(2-3):143-154. doi:10.1016/0168-1923(87)90033-5
- Pieri, P. 1989. Étude expérimentale et modélisation des écoulements aérodynamiques au voisinage
  de cultures en rangs. Thesis. HAL tel-02853871
- Pieri, P. & Fuchs, M. 1990. Comparison of Bowen ratio and aerodynamic estimates of
  evapotranspiration. Agric. For. Meteorol. 49(3):243-256. doi:10.1016/0168-1923(90)90035-5
- Pradel, E. & Pieri, P. 2000. Influence of a grass layer on vineyard soil temperature. Aust. J.
  Grape Wine Res. 6(1):59-67. doi:10.1111/j.1755-0238.2000.tb00163.x
- de Rességuier, L., Pieri, P., Petitjean, T., Mary, S. & van Leeuwen, C. 2023. Temperature
  variation linked to trellis height: an opportunity for adaptation to climate change? IVES
  Technical Reviews. doi:10.20870/ives-tr.2023.7672
- Cola, G. et al. 2009. A berry temperature model, Agric. For. Meteorol. 149:1215, cited by the
  physiology papers. Not in the inventory, and its reference is unchecked.

**Botrytis**
- Fermaud, M., Pieri, P. & Liminana, J.M. 2001. Botrytis et microclimat. HAL hal-02672777
- Fermaud, M., Pieri, P., Dubos, B., Roudet, J. & Mimiague, F. 2004. Development of a statistical
  model for predicting grey mould epidemics on grapevine based on weather data. HAL hal-02758636
- Fermaud, M., Martínez, F., Pieri, P. et al. 2003. Pourriture grise de la vigne : prévision du
  risque épidémique et protection fongicide. HAL hal-02672678. The model CLIMATOR ran is cited
  as Fermaud, Pieri & Mimiague 2003.
- Pieri, P. & Fermaud, M. 2000. Modeling temperature of ripening grape berries: calibration in
  controlled conditions. HAL hal-02770157

**Water**
- Lebon, E., Dumas, V., Pieri, P. & Schultz, H.R. 2003. Modelling the seasonal dynamics of the
  soil water balance of vineyards. Funct. Plant Biol. 30(6):699-710. doi:10.1071/fp02222
- Valancogne, C. et al. 2000. Influence of orchard and vineyard characteristics on maximal plant
  transpiration. Acta Hortic. 537:61-68. doi:10.17660/actahortic.2000.537.4
- Pieri, P. & Gaudillère, J.P. 2005. Vines water stress derived from a soil water balance
  model. pp. 457-463, venue not recorded. OpenAlex W1557532871
- Bois, B., Pieri, P., van Leeuwen, C. & Gaudillère, J.P. 2005. Sensitivity analysis of the
  Penman-Monteith evapotranspiration formula. pp. 187-193, venue not recorded. OpenAlex
  W173352905

**Climate change**
- Pieri, P., Lebon, E. & Brisson, N. 2012. Climate change impact on French vineyards as
  predicted by models. Acta Hortic. 931:29-37. doi:10.17660/actahortic.2012.931.2

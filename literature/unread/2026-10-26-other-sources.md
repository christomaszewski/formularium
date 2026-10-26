# Other sources (2026-10-26): leads from the unread lists found elsewhere

The five unread lists (2026-10-14 Table 1, 2026-10-18, 2026-10-20, 2026-10-20 vine leaf area,
2026-10-21) held 371 rows of leads this VM could not fetch from the publisher. On 2026-10-25/26
every one was tried again through sources the earlier searches had not used. Nothing here was
read: each file was checked against its lead by its first page (title, authors, venue) and no
further. A paper worth reading still gets a note of its own (INGESTING.md).

- **Rows removed first:** 23 rows whose paper already had a note, found by DOI or by first
  author and year (Nita 2005, Erincik 2002, Oriolani 2015, Vercesi 1999, Taylor 2018, Smith
  2023, Krause 2008 and the DOI matches). The older lists are not rewritten; each gets a pointer
  to this file instead.
- **What was asked, per DOI (295 DOIs):** Europe PMC's REST search (PMC id and open-access
  flag), OpenAIRE's API (repository copies), CORE's API v3 (repository copies and CORE's own
  copy) and HAL's API (deposited files). Cached in the drop's `search/probe/`.
- **For leads without a DOI:** Crossref by title, OpenAlex by exact title
  (`filter=display_name.search:`), theses.fr's API for French theses, and the repositories
  themselves: OhioLINK, RiuNet, SUNScholar, ULisboa, UPCommons, UNESP, MIT, eScholarship,
  Purdue e-Pubs, UNCuyo, UTAS figshare, CSU, TU Delft, Open PRAIRIE, TopSCHOLAR, the Giornate
  Fitopatologiche archive, J-STAGE, Vitis on OpenAgrar, SciELO, SAJEV, Boletín Micológico,
  agrometeorologia.it, NZ Plant Protection, Zenodo. Web search for seven grey items.
- **How the files were fetched:** curl first; a landing page's `citation_pdf_url` or PDF link
  next; DSpace 7's REST API where the HTML site shows a bot check; the Wayback Machine's raw
  captures (`id_`) for HAL deposits and for bepress sites behind Cloudflare; Europe PMC's
  full-text XML (REST at ebi.ac.uk) where the publisher's PDF is unreachable. A headless browser
  (home page first) only where a site served HTML to curl; never against a bot check.
- **What refused this VM** is recorded in INGESTING.md ("Routes that worked on 2026-10-26").
  Scite's tools still need a paid plan; Semantic Scholar answers 429 to every call without an
  API key (a free key would give its `openAccessPdf` for the rest).
- **Copies:** `/srv/papers/drop/2026-10-25-other-sources/fetch/<key>/paper.pdf` (or
  `paper.xml`, Europe PMC's JATS full text), with text in `text/<key>/paper.txt` (OCR for the
  two scanned SAJEV papers). Seven fetched files turned out to be papers that already had notes
  (brink2006 twice, brink2016, erincik2002, nita2005, hamada2008, fernandezgonzalez2009, the
  franceschi2020 preprint); they are set aside in `fetch/_already_noted/`.
- **Obtained: 57 (48 PDFs, 9 full-text XML).** Table 1. **Seen but not reachable from
  here: 53.** Table 2 gives the link for Chris's browser.

## Table 1: obtained (not read; first page checked against the lead)

| Drop key | List | Year | First author | Title | DOI | Where it came from | File |
|---|---|---|---|---|---|---|---|
| albasha2019 | 10-14 | 2019 | Rami Albasha | HydroShoot: a functional-structural plant model for simulating hydraulic structure, gas and ene | 10.1093/insilicoplants/diz007 | Wayback Machine capture of inria.hal.science | paper.pdf, 3856 kB |
| alimad2016 | 10-20 | 2016 | Nujoud Alimad | Initiation and development of Erysiphe necator chasmothecia and their role in the epidemiology  | 10.5586/am.1088 | Biblioteka Nauki (via CORE) | paper.pdf, 847 kB |
| atauri2017 | 10-14 | 2017 | Iñaki García de Cortázar Ata | Grapevine phenology in France: from past observations to future evolutions in the context of cl | 10.20870/oeno-one.2016.0.0.1622 | Wayback Machine capture of hal.science | paper.pdf, 1433 kB |
| binks2021 | 10-18, 10-21 | 2021 | Oliver J. Binks | Measuring the vertical profile of leaf wetness in a forest canopy | 10.1016/j.mex.2021.101332 | Europe PMC full-text XML (PMC8374337), REST at ebi.ac.uk | paper.xml, 30 kB |
| bourgeon2015 | 10-14 | 2015 | Marie-Aure Bourgeon | Conception et évaluation d'un dispositif d'imagerie multispectrale de proxidétection embarqué p | 10.70675/1802c03dz6c6cz4302zace2z18ba40b87e17 | Wayback Machine capture of theses.hal.science | paper.pdf, 7007 kB |
| brink2005thesis | 10-20 | 2005 | Jan-Cor Brink | Quantification of spray coverage on grape bunch parts and the incidence of Botrytis cinerea |  | SUNScholar (DSpace REST API) | paper.pdf, 500 kB |
| buesa2018thesis | 10-14 | 2018 | IGNACIO BUESA PUEYO | Field practices for adapting Mediterranean viticulture to climate change (doi 10.4995/thesis/10 | 10.4995/thesis/10251/107365 | RiuNet (DSpace REST API) | paper.pdf, 4876 kB |
| camposarguedas2026 | 10-14 | 2026 | Francisco Campos‐Arguedas | Cold hardiness dynamics predict budbreak and associated low‐temperature threats in grapevine (N | 10.1111/nph.71074 | Europe PMC full-text XML (PMC13103416), REST at ebi.ac.uk | paper.xml, 193 kB |
| castex2020 | 10-20 | 2020 | Victorine Castex | Assembling and testing a generic phenological model to predict Lobesia botrana voltinism for im | 10.1016/j.ecolmodel.2020.108946 | Wayback Machine capture of hal.science | paper.pdf, 985 kB |
| chalfant2012 | 10-14 | 2012 | Patricia Chalfant | Responses of Grapevines to Timing and Method of Leaf Removal (OhioLink ETD Center (Ohio Library |  | OhioLINK ETD Center | paper.pdf, 2196 kB |
| cheraiet2021 | 10-20 | 2021 | Anice Cheraïet | Predicting the site-specific distribution of agrochemical spray deposition in vineyards at mult | 10.1016/j.compag.2021.106402 | Wayback Machine capture of hal.inrae.fr | paper.pdf, 1569 kB |
| dasilva2024 | 10-14 | 2024 | Thais Gabrielle Ferreira de  | Climatic influence on the development and yield of grapevine (Vitis vinifera L.) described by m |  | UNESP repository (DSpace REST API) | paper.pdf, 6994 kB |
| djuikem2024 | 10-20 | 2024 | Clotilde Djuikem | Impact of ontogenic changes on the dynamics of a fungal crop disease model motivated by coffee  | 10.1007/s00285-024-02053-4 | Wayback Machine capture of inria.hal.science | paper.pdf, 1381 kB |
| dunne2014 | 10-20 | 2014 | KJ Dunne | Novel application of methods to investigate epidemiology and management of botrytis bunch rot i | 10.25959/23236418 | UTAS figshare (API) | paper.pdf, 6868 kB |
| fernandezgonzalez2012 | 10-20 | 2012 | María Fernández-González | Forecasting ARIMA models for atmospheric vineyard pathogens in Galicia and Northern Portugal: B |  | Minerva USC (DSpace) | paper.pdf, 588 kB |
| garin2015 | 10-14 | 2015 | Guillaume Garin | Vers la compréhension des épidémies fongiques foliaires par modélisation multi-échelle dans les | 10.70675/61dad2bez5e93z4c75z9d83z7bc747ff193d | Wayback Machine capture of hal.inrae.fr | paper.pdf, 9038 kB |
| gegoutpetit2019 | 10-20 | 2019 | Anne Gégout‐Petit | A new centered spatio-temporal autologistic regression model with an application to local sprea | 10.1016/j.spasta.2019.100361 | Wayback Machine capture of inria.hal.science | paper.pdf, 740 kB |
| gil2014 | 10-20 | 2014 | Emilio Gil Moya | Spray adjustments based on LWA concept in vineyard. Relationship between canopy and coverage fo |  | UPCommons (DSpace REST API) | paper.pdf, 975 kB |
| gladstone2003 | 10-14 | 2003 | E. A. Gladstone | Influence of leaf area density and trellis/training system on the light microclimate within gra | 10.5073/vitis.2003.42.123-131 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 614 kB |
| herzog2022 | 10-20 | 2022 | Katja Herzog | Towards Sensor-Based Phenotyping of Physical Barriers of Grapes to Improve Resilience to Botryt | 10.3389/fpls.2021.808365 | Europe PMC full-text XML (PMC8866247), REST at ebi.ac.uk | paper.xml, 221 kB |
| jin2026 | 10-18 | 2026 | Wei Jin | Optimized Design and Radiation Error Correction of a Naturally Ventilated Air Temperature Senso | 10.3390/s26123853 | Europe PMC full-text XML (PMC13306756), REST at ebi.ac.uk | paper.xml, 103 kB |
| jofre2016 | 10-14 | 2016 | María Florencia Jofré | Efecto de la calidad de la luz percibida por fitocromos sobre la morfología y la fisiología de  |  | UNCuyo digital library | paper.pdf, 2021 kB |
| kalt2026 | 10-18 | 2026 | Sebastian Kalt | Detection of Airborne Pathogenic Wheat Rust Spores Using Machine-Learning-Assisted Optical Imag | 10.1021/acsagscitech.5c00836 | KITopen (via OpenAIRE) | paper.pdf, 9069 kB |
| kovaleski2018 | 10-14 | 2018 | Alisson P. Kovaleski | Deacclimation kinetics as a quantitative phenotype for delineating the dormancy transition and  | 10.1093/aobpla/ply066 | Europe PMC full-text XML (PMC6207836), REST at ebi.ac.uk | paper.xml, 98 kB |
| koyama2022 | 10-14 | 2022 | Kohei Koyama | Scaling the leaf length-times-width equation to predict total leaf area of shoots (Annals of Bo | 10.1093/aob/mcac043 | Europe PMC full-text XML (PMC9445601), REST at ebi.ac.uk | paper.xml, 240 kB |
| kraus2018 | 10-20 | 2018 | Christian Kraus | Effects of canopy architecture and microclimate on grapevine health in two training systems | 10.5073/vitis.2018.57.53-60 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 603 kB |
| krause2008jmlr | 10-21 | 2008 | Andreas Krause | Robust submodular observation selection (JMLR journal version; the long technical report is rea |  | jmlr.org | paper.pdf, 426 kB |
| kuwagata1990 | 10-18 | 1990 | T. Kuwagata | The daytime PBL heating process over complex terrain in central Japan (J. Meteorol. Soc. Jpn 68:625; cited by Kuwagata 2024 for a longwave formula) | 10.2151/jmsj1965.68.6_625 | J-STAGE | paper.pdf, 1856 kB |
| kuwagata2011 | 10-18 | 2011 | T. Kuwagata | MeteoCrop DB: an agro-meteorological database coupled with crop models (J. Agric. Meteorol. 67:297-306) | 10.2480/agrmet.67.4.9 | J-STAGE | paper.pdf, 1600 kB |
| laurenson2002 | 10-18 | 2002 | M. Laurenson | Developing agricultural models using MetBroker mediation software (J. Agric. Meteorol. 58:1-9) | 10.2480/agrmet.58.1 | J-STAGE | paper.pdf, 7979 kB |
| leolini2022 | 10-14 | 2022 | Luisa Leolini | Use of remote sensing-derived fPAR data in a grapevine simulation model for estimating vine bio | 10.1007/s11119-022-09970-8 | CNR IRIS (via CORE) | paper.pdf, 2477 kB |
| liu2017 | 10-20 | 2017 | Yangxuan Liu | Economic Benefit Analysis of the Late Blight Forecasting Systems |  | Purdue e-Pubs | paper.pdf, 478 kB |
| lopes2005 | 10-14 | 2005 | Carlos Manuel Lopes | Easy and accurate estimation of grapevine leaf area with simple mathematical models (Vitis, doi | 10.5073/vitis.2005.44.55-61 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 591 kB |
| mainini2017 | 10-21 | 2017 | Laura Mainini | Sensor placement strategy to inform decisions | 10.2514/6.2017-3820 | MIT DSpace (REST API) | paper.pdf, 1024 kB |
| mairs2018 | 10-20 | 2018 | Ryan Alan Mairs | Effects of Bacillus Mycoides Supplement in a Reduced Frequency Fungicide Program on Chambourcin |  | Wayback Machine capture of digitalcommons.wku.edu | paper.pdf, 779 kB |
| mariani2007 | 10-14 | 2007 | Luigi Mariani | POSSIBLE SYNERGIES BETWEEN PHENOLOGICAL AND CROP PROTECTION MODELS: AN EXAMPLE FOR LOBESIA BOTR |  | agrometeorologia.it (Italian Journal of Agrometeorology) | paper.pdf, 299 kB |
| mondet2023 | 10-18 | 2023 | Cécilia Mondet | Vine leaf decomposition: Feeding preferences and effects of physico-chemical traits of litter o | 10.1016/j.apsoil.2023.104928 | Wayback Machine capture of hal.science | paper.pdf, 612 kB |
| nonnecke1980 | 10-14 | 1980 | Gail R. Nonnecke | The influence of cluster-thinning and shoot-tip removal on 'Seyval' grapevines / (OhioLink ETD  |  | OhioLINK ETD Center | paper.pdf, 4315 kB |
| phinopoulos2014 | 10-14 | 2014 | Victoras Georgios Phinopoulo | Estimation of leaf area in grapevine cv. Syrah using empirical models (Portuguese National Fund |  | Repositório ULisboa (DSpace REST API) | paper.pdf, 362 kB |
| pieri2003 | 10-18 | 2003 | Philippe Pieri | Sensitivity to training system parameters and soil surface albedo of solar radiation intercepte | 10.5073/vitis.2003.42.77-82 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 203 kB |
| poitou2021 | 10-20 | 2021 | Xavier Poitou | Methyl salicylate, a grape and wine chemical marker and sensory contributor in wines elaborated | 10.1016/j.foodchem.2021.130120 | Wayback Machine capture of hal.inrae.fr | paper.pdf, 379 kB |
| ramanathan2006 | 10-21 | 2006 | Nithya Ramanathan | Rapid deployment with confidence: calibration and fault detection in environmental sensor netwo |  | eScholarship | paper.pdf, 1126 kB |
| ramos2022 | 10-14 | 2022 | M.C. Ramos | Macabeo (Viura) grape response to climate variability in areas located at different elevations  | 10.1002/jsfa.11914 | Europe PMC full-text XML (PMC9544767), REST at ebi.ac.uk | paper.xml, 97 kB |
| rossouw2016 | 10-20 | 2016 | Cornelis Johannes Rossouw | Mancozeb rainfastness and residue thresholds for control of Venturia inaequalis |  | SUNScholar (DSpace REST API) | paper.pdf, 2633 kB |
| schultz1993 | 10-14 | 1993 | Hans R. Schultz | Photosynthesis of sun and shade leaves of field-grown grapevine (Vitis vinifera L.) in relation | 10.5073/vitis.1993.32.197 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 645 kB |
| shiraishi2007 | 10-20 | 2007 | Shiraishi, M. | Screening for resistance to ripe rot caused by Colletotrichum acutatum in grape germplasm | 10.5073/vitis.2007.46.196-200 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 321 kB |
| steinkellner1998 | 10-20 | 1998 | Siegrid Steinkellner | Overwintering of Uncinula necator in Austrian vineyards | 10.5073/vitis.1998.37.193-194 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 77 kB |
| steyn2016 | 10-14 | 2016 | J. T. Steyn | Grapevine vigour and within vineyard variability: a review (RiuNet (Universitat Politècnica de  |  | RiuNet (DSpace REST API) | paper.pdf, 2311 kB |
| vanrooi2002 | 10-20 | 2002 | C. van Rooi | Infection by dry, airborne Botrytis cinerea conidia and fungicide efficacy on different parts o |  | SUNScholar (DSpace REST API) | paper.pdf, 22782 kB |
| vanrooi2002sajev | 10-20 | 2002 | C. van Rooi | Epidemiology of Botrytis cinerea on grape: wound infection by dry, airborne conidia (S. Afr. J. Enol. Vitic. 23; the thesis's first paper) | 10.21548/23-2-2157 | SAJEV (OJS galley) | paper.pdf, 8015 kB |
| vanrooi2003sajev | 10-20 | 2003 | C. van Rooi | Fungicide efficacy against Botrytis cinerea at different positions on grape shoots (S. Afr. J. Enol. Vitic. 24; the thesis's second paper, not a listed lead) | 10.21548/24-1-2145 | SAJEV (OJS galley) | paper.pdf, 1688 kB |
| vialetchabrand2019 | 10-18 | 2019 | Silvère Vialet‐Chabrand | Dynamic leaf energy balance: deriving stomatal conductance from thermal imaging in a dynamic en | 10.1093/jxb/erz068 | Europe PMC full-text XML (PMC6506762), REST at ebi.ac.uk | paper.xml, 213 kB |
| vivin2017 | 10-14 | 2017 | P Vivin | Combining ecophysiological models and genetic analysis: a promising way to dissect complex adap | 10.20870/oeno-one.2016.0.0.1588 | Wayback Machine capture of hal.science | paper.pdf, 1148 kB |
| wermelinger1990 | 10-14 | 1990 | Beat Wermelinger | Seasonal growth and nitrogen distribution in grapevine leaves, shoots and grapes (Vitis, doi 10 | 10.5073/vitis.1990.29.15-26 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 292 kB |
| weyand2006 | 10-14 | 2006 | Karsten M. Weyand | Light interception, gas exchange and carbon balance of different canopy zones of minimally and  | 10.5073/vitis.2006.45.105-114 | Vitis on OpenAgrar (OJS galley) | paper.pdf, 2267 kB |
| yang2021 | 10-14 | 2021 | Chenyao Yang | Assessing the grapevine crop water stress indicator over the flowering-veraison phase and the p | 10.1016/j.agwat.2021.107349 | Wayback Machine capture of hal.inrae.fr | paper.pdf, 9056 kB |
| yang2023 | 10-14, 10-20 | 2023 | Weiwei Yang | GrapevineXL reliably predicts multi-annual dynamics of vine water status, berry growth, and sug | 10.1093/hr/uhad071 | Europe PMC full-text XML (PMC10244804), REST at ebi.ac.uk | paper.xml, 161 kB |

Notes on Table 1:
- `vanrooi2002` is the thesis; `vanrooi2002sajev` and `vanrooi2003sajev` are its two S. Afr. J.
  Enol. Vitic. papers (scans, OCR'd). `brink2005thesis` is the thesis behind the held brink2006.
- `kuwagata1990`, `kuwagata2011` and `laurenson2002` are the J-STAGE items the 10-18 SWEB and
  pilot-equation notes asked for (bullets in that list). Kuwagata 1990 is the PBL-heating paper
  Kuwagata 2024 cites at l. 562-563; whether it prints the longwave formula is for the reader.
- `steyn2016` is the published review (Int. J. Sci. Eng. Res. 7(2)), the RiuNet copy.
- `mariani2007` is the Italian Journal of Agrometeorology paper (2007(3):39-44), from the
  journal's site; the file carries a ResearchGate cover page.
- `krause2008jmlr` is the JMLR journal version; the technical report is `krause2008c`.
- The XML files are Europe PMC's JATS full text (open-access subset): the whole article with
  tables, no page images. Equations and figures that matter must be read in the publisher's
  PDF, which Chris can open at the DOI.
- Vitis rows carry the DOI's year; the 10-18 and 10-20 lists gave 2015 or 2017 for several.

## Table 2: open copies seen from here that this VM could not download

CORE's `download` host, HAL's files, PMC's PDF interstitial, NZ Plant Protection and the
Cloudflare-fronted repositories answer a browser but not this machine. Each row names the copy
the aggregators point to, so a click from Chris's browser should do.

| List | Year | First author | Title | DOI | Open copy seen from here |
|---|---|---|---|---|---|
| 10-14 | 2010 | Markus Keller | Warm spring temperatures induce persistent season-long changes in shoot developm | 10.1093/aob/mcq091 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC2889799/ (PDF behind an interstitial; no XML in Europe PMC) |
| 10-14 | 2024 | Alaa Haj-Yahya | Bimodal pattern of allometric scaling along grapevine shoots (Annals of Botany,  | 10.1093/aob/mcae146 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11688528/ (PDF behind an interstitial; no XML in Europe PMC) ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11688528/ |
| 10-14 | 2024 | Magali Poupard | Source–sink manipulations through shading, crop load and water deficit affect pl | 10.1093/aob/mcae203 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12401888/ (PDF behind an interstitial; no XML in Europe PMC) ; https://pubmed.ncbi.nlm.nih.gov/39656901/ |
| 10-18 | 2007 | Richard Essery | Scaling and parametrization of clear‐sky solar radiation over complex topography | 10.1029/2006jd007650 | CORE: https://core.ac.uk/download/28970998.pdf |
| 10-18 | 2007 | V. Y. Ivanov | A weather generator for hydrological, ecological, and agricultural applications | 10.1029/2006wr005364 | CORE: https://core.ac.uk/download/16416513.pdf |
| 10-18 | 2009 | Keir Colbo | Accuracy of the IMET Sensor Package in the Subtropics | 10.1175/2009jtecho667.1 | CORE: https://core.ac.uk/download/4168472.pdf |
| 10-18 | 2010 | Nora Helbig | Explicit validation of a surface shortwave radiation balance model over snow‐cov | 10.1029/2010jd013970 | CORE: https://core.ac.uk/download/30992447.pdf |
| 10-18 | 2014 | Dazhi Yang | Bidirectional irradiance transposition based on the Perez model | 10.1016/j.solener.2014.10.006 | CORE: https://core.ac.uk/download/42357967.pdf |
| 10-18 | 2014 | Julie Bessac | On the construction of stochastic generators of wind conditions offshore Brittan | 10.70675/1398fcf8za868z4d8az93a0zfec2f0a9e939 |  |
| 10-18 | 2017 | Gemma Hornero | A novel low-cost smart leaf wetness sensor | 10.1016/j.compag.2017.11.001 | CORE: https://core.ac.uk/download/195706624.pdf |
| 10-18 | 2017 | Nadav Peleg | An advanced stochastic weather generator for simulating 2‐D high‐resolution clim | 10.1002/2016ms000854 | CORE: https://core.ac.uk/download/146486347.pdf |
| 10-18 | 2019 | Edgar F.M. Abreu | Prediction of diffuse horizontal irradiance using a new climate zone model | 10.1016/j.rser.2019.04.055 | CORE: https://core.ac.uk/download/199448456.pdf |
| 10-18 | 2022 | Hanene Mairech | ClimaSG: A weather generator for crop modelling and water requirements studies | 10.1016/j.agwat.2022.107817 | CORE: https://core.ac.uk/download/533901181.pdf |
| 10-18 | 2023 | Anna Pelosi | Performance of the Copernicus European Regional Reanalysis (CERRA) dataset as pr | 10.1016/j.agwat.2023.108556 | CORE: https://core.ac.uk/download/599396618.pdf ; https://doaj.org/article/2e5c3c5bb60349b0be7a4950dddaf599 |
| 10-18 | 2024 | Jose Antonio Ruiz-Arias | Solar irradiance component separation benchmarking: The critical role of dynamic | 10.1016/j.rser.2024.114678 | CORE: https://core.ac.uk/download/614637081.pdf |
| 10-18 | 2025 | Said Obakrim | A multivariate and space-time stochastic weather generator using a latent Gaussi | 10.1007/s00477-024-02897-8 | HAL: https://hal.inrae.fr/hal-05489887/file/s00477-024-02897-8.pdf |
| 10-18 | 2026 | Saima Munawwar | Modelling hourly and daily diffuse solar radiation using world-wide database | 10.17869/enu.246487 | CORE: https://core.ac.uk/download/520507018.pdf ; https://napier-repository.worktribe.com/246487/1/Munawwar.pdf |
| 10-20 | 2005 | P. Cortesi | Genetic Similarity of Flag Shoot and Ascospore Subpopulations of Erysiphe necato | 10.1128/aem.71.12.7788-7791.2005 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC1317322/ (PDF behind an interstitial; no XML in Europe PMC) |
| 10-20 | 2010 | Gareth N. Hill | Tools for accurate assessment of botrytis bunch rot (Botrytis cinerea) on wine g | 10.30843/nzpp.2010.63.6560 | https://nzpps.org/_journal/index.php/nzpp/article/download/6560/6388 |
| 10-20 | 2010 | Jean‐Baptiste Burie | Switching from a mechanistic model to a continuous model to study at different s | 10.1093/aob/mcq233 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC3077982/ (PDF behind an interstitial; no XML in Europe PMC) |
| 10-20 | 2010 | Travis J. Lybbert | POWDERY MILDEW RISK AND FORECASTING IN WINE GRAPES: DO GROWERS CHANGE RISK MANAG | 10.22004/ag.econ.61745 | CORE: https://core.ac.uk/download/352992949.pdf |
| 10-20 | 2011 | David M. Gadoury | Grapevine powdery mildew ( Erysiphe necator ): a fascinating system for the stud | 10.1111/j.1364-3703.2011.00728.x | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6638670/ (PDF behind an interstitial; no XML in Europe PMC) |
| 10-20 | 2012 | D.C. Mundy | Tendrils as a source of seasonal carryover of Botrytis cinerea in vineyards | 10.30843/nzpp.2012.65.5375 | https://nzpps.org/_journal/index.php/nzpp/article/download/5375/5203 |
| 10-20 | 2012 | Travis J. Lybbert | Multi-Dimensional Responses to Risk Information: How do Winegrape Growers Respon | 10.22004/ag.econ.162521 | CORE: https://core.ac.uk/download/353023759.pdf |
| 10-20 | 2014 | Gareth N. Hill | Use of nitrate non-utilizing (nit) mutants to determine phenological stages at w | 10.1111/ppa.12225 | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/ppa.12225 |
| 10-20 | 2017 | Emerson M. Del Ponte | Standard Area Diagrams for Aiding Severity Estimation: Scientometrics, Pathosyst | 10.1094/phyto-02-17-0069-fi | CORE: https://core.ac.uk/download/324126789.pdf |
| 10-20 | 2017 | Gareth N. Hill | Manipulating rainfall to study symptom expression of Botrytis cinerea infection  | 10.30843/nzpp.2017.70.64 | https://journal.nzpps.org/index.php/nzpp/article/download/64/43 |
| 10-20 | 2018 | Serge Savary | Concepts, approaches, and avenues for modelling crop health and crop losses | 10.1016/j.eja.2018.04.003 | CORE: https://core.ac.uk/download/572203899.pdf |
| 10-20 | 2019 | Marika Rossi | Genetic Diversity of Flavescence Dorée Phytoplasmas at the Vineyard Scale | 10.1128/aem.03123-18 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6498159/ (PDF behind an interstitial; no XML in Europe PMC) ; CORE: https://core.ac.uk/download/302330057.pdf |
| 10-20 | 2020 | Estefanía González-Fernández | Identification and evaluation of the main risk periods of Botrytis cinerea infec | 10.1017/s0021859620000362 | CORE: https://core.ac.uk/download/516408356.pdf |
| 10-20 | 2020 | Marco Grella | Field assessment of a newly‐designed pneumatic spout to contain spray drift in v | 10.1002/ps.5975 | CORE: https://core.ac.uk/download/552451319.pdf |
| 10-20 | 2021 | Samuel Reis | European grapevine moth in the Douro region: voltinism and climatic scenarios | 10.20870/oeno-one.2021.55.2.4595 | CORE: https://core.ac.uk/download/429743495.pdf |
| 10-20 | 2022 | Jurrian Wilmink | Effects of grape phylloxera leaf infestation on grapevine growth and yield param | 10.20870/oeno-one.2022.56.1.4803 | https://doaj.org/article/6fba3239d31944bd98955095e84b3edc |
| 10-20 | 2022 | Lu Xun | Pesticide dose based on canopy characteristics in apple trees: Reducing environm | 10.1016/j.scitotenv.2022.154204 | CORE: https://core.ac.uk/download/512035838.pdf |
| 10-20 | 2022 | Pou, A. | How rootstocks impact the scion vigour and vine performance of Tempranillo (Aust | 10.1155/2022/9871347 | CORE: https://core.ac.uk/download/599681289.pdf |
| 10-20 | 2023 | Francisco García-Ruíz | Assessment of map based variable rate strategies for copper reduction in hedge v | 10.1016/j.compag.2023.107753 | CORE: https://core.ac.uk/download/565928851.pdf |
| 10-20 | 2024 | Jelena Plavec | Genetically divergent 'Candidatus Phytoplasma solani' isolates in Croatian viney | 10.1186/s42483-024-00261-w | HAL: https://hal.science/hal-04683658/file/2024-Plavec-Phytopathology%20Research.pdf |
| 10-20 | 2024 | Othmane Taibi | A qPCR Assay for the Quantification of the Overwintering Chasmothecia of Erysiph | 10.1094/phyto-04-24-0126-r | https://riunet.upv.es/handle/10251/221197 |
| 10-20 | 2026 | Raphaël Métral | Agroecological performances of low pesticide used grapevine systems adapted to s | 10.1016/j.agsy.2026.104690 | HAL: https://hal.inrae.fr/hal-05542610/file/1-s2.0-S0308521X26000582-main.pdf |
| 10-21 | 2014 | Powell | The spatial variation of minimum near-surface temperature in complex terrain (th | 10.26021/9174 | CORE: https://core.ac.uk/download/35471487.pdf |
| 10-21 | 2020 | Javier López-Lorente | Worldwide evaluation and correction of irradiance measurements from personal wea | 10.1016/j.solener.2020.06.073 | CORE: https://core.ac.uk/download/326422773.pdf |
| 10-21 | 2024 | Sébastien Dandrifosse | Automatic quality control of weather data for timely decisions in agriculture | 10.1016/j.atech.2024.100445 | https://doaj.org/article/8660460883154d7b9e4e3fd626b09554 |
| 10-21 | 2025 | Hamed Mokhtarzadeh | Design, development and evaluation of a low-cost smart solar-powered weather sta | 10.1016/j.rineng.2025.104848 | https://doaj.org/article/f6c38fd4d6554c13a1644edc571b23ac |
| 10-14 | 2020 | Dilmini Alahakoon | Exploring Phenotypic Diversity and Quantitative Trait Loci Mapping ... in Grapevine Populations (thesis) | none | Open PRAIRIE, behind Cloudflare: https://openprairie.sdstate.edu/etd/4855 (both Wayback captures of its PDF are truncated at 1 MB) |
| 10-14 | 2015 | Hans R. Schultz | An empirical model for the simulation of leaf appearance and leaf area development of primary shoots (Scientia Horticulturae) | 10.1016/0304-4238(92)90020-d | no open copy anywhere (Europe PMC, OpenAIRE, CORE, HAL, Semantic Scholar not asked); Article Galaxy about 42 USD, see the 10-14 list |
| 10-18 | 2016 | Navideh Sadoughi | Effect of Ripe Rot of Grapes (Colletotrichum spp.) on the Chemical Composition and Off-Flavour Compounds (thesis) | none | CSU Research Output, behind Cloudflare: https://researchoutput.csu.edu.au/files/88605092/Sadoughi_Navideh_thesis.pdf |
| 10-18, 10-20 | 2024 | Othmane Taibi | A qPCR Assay for the Quantification of the Overwintering Chasmothecia of Erysiphe necator in Grapevine Bark | 10.1094/phyto-04-24-0126-r | RiuNet holds the accepted manuscript (handle 10251/221197) but its bitstream refused this VM (embargo or login) |
| 10-20 | 2010 | Craig N. Austin | Sunlight's influence on grapevine powdery mildew (thesis, Cornell) | none | eCommons, behind a human-verification page: https://ecommons.cornell.edu/bitstreams/854483a3-331c-4777-b8d3-b181143dc8fe/download |
| 10-20 | 2002 | E. Egger | New experiences with grapevine powdery mildew epidemic simulation models in Tuscany | none | not found: not in Crossref, OpenAlex (title only) or the Giornate Fitopatologiche archive's search; probably a 2002 workshop paper (4th GDPM workshop, Napa, or IOBC/WPRS) |
| 10-20 | 2019 | Nicolas Navarre | Development of a quantitative tool for environmentally sustainable copper fungicide application and tracking within vineyards (MSc thesis, TU Delft and Leiden) | none | TU Delft repository, unreachable from this VM: https://repository.tudelft.nl/file/File_35d0f2dc-67aa-41b4-97d8-08a2aee6922e |
| 10-21 | 2004 | Jenna Burrell | Vineyard computing: sensor networks in agricultural production | 10.1109/mprv.2004.1269130 | IEEE only; no repository copy found (Crossref, OpenAlex, CORE, web search) |
| 10-21 | 2006 | Koen Langendoen | Murphy loves potatoes: experiences from a pilot sensor network deployment in precision agriculture | 10.1109/ipdps.2006.1639412 | IEEE; TU Delft's repository is unreachable from this VM |
| 10-18 | 2026 | Guimarães | Emulating STICS grapevine yield across Europe with machine learning; and the benchmarking companion | 10.5281/zenodo.23105284, 10.5281/zenodo.21874220 | the Zenodo records hold code and data archives only (zenodo_v2.zip, zenodo_NG.zip: scripts, a README, no manuscript); the paper itself is not deposited there |

## Rows of the older lists that already had notes

| List | Year | First author | Note |
|---|---|---|---|
| 10-18 | 1999 | Annamaria Vercesi | vercesi1999 |
| 10-18 | 2018 | Andrew S. Taylor | taylor2018 |
| 10-18 | 2023 | Michael Thomas Smith | smith2022 |
| 10-20 | 2002 | Ömer Erincik | erincik2002 |
| 10-20 | 2005 | Mizuho Nita | nita2005 |
| 10-20 | 2015 | Enrique J. A. Oriolani | oriolani2015 |
| 10-21 | 2008 | Andreas Krause | krause2008c |

Also matched by DOI (not listed again): Lebon 2004, Pellegrino 2005, Louarn 2007a and 2007b,
Pallas 2008 (as the 2009 thesis), Keller 2010 (AJGWR), Caffarra 2011, Arnó 2012, Cola 2014,
Gladstone 2003 (now also fetched from Vitis), Magarey 2005, Sentelhas 2005, Pérez Rodríguez 2013,
Gil 2019 (DOSAVIÑA), Moyer 2015.

## Still not obtained, no open copy seen

Everything else in the five lists: the closed Wiley (Australian Journal of Grape and Wine
Research above all), Elsevier, APS, Springer, AMS and IOP items, the old literature (Laviola
1964, Arens 1929, Capus 1918), Magarey 1999 (thesis, not online), Rao 1989, Ji 2012 (Guoshu
Xuebao), Sawalha 2012, Ribeiro 2013, du Sautoy 2007, Potratz 1994, Streck 2006 (UFSM's
repository timed out), Douillet 2023 (HAL tel-04970525, no Wayback capture), Bessac 2014
(HAL tel-01079520, no capture), Campos-Arguedas 2026 (obtained as XML), Fernández-González
2012 (obtained). For the closed journal articles the remaining routes are a library, Article
Galaxy through Scite, or the authors.

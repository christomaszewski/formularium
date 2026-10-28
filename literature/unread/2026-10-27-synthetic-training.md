# Training on real, synthetic and augmented data (2026-10-27): leads not obtained

The pass of 2026-10-27/28 searched six questions for training plant models (vineyards first) on
real, synthetic and synthetically augmented data: models pretrained on simulators and fine-tuned
on real data (`hybrid`), the method of synthetic-truth experiments behind Agrarium's TRUTH-METHOD
(`osse`), open vineyard datasets (`datasets`), disease forecasting from data (`diseaseml`),
synthetic weather (`weather`) and synthetic or augmented images (`imagery`): 131 OpenAlex
calls in all (19, 17, 24, 24, 24 and 23). Nothing below was read beyond an abstract where one
is said. Titles and DOIs are from the strands' reference lists, OpenAlex or Crossref, unchecked
unless said. Each strand's `search.md` in the drop lists every route tried.

- **Refusals:** Elsevier (a captcha), Wiley, Taylor & Francis and ingentaconnect (Cloudflare,
  in curl and the headless browser), Springer and Nature (paywalls). Some Wayback requests were
  refused by the session's own permission rules and not retried.
- **Routes that worked this time:** Europe PMC full-text XML for open Elsevier, Wiley and
  Springer articles (read as XML, filed as `.xml`); the headless browser with the publisher's
  home page first for Wiley open access, Springer and HAL `/document` PDFs, and AMS through its
  DOI landing page; NASA's NTRS; a thesis in place of a paywalled article (Zurell 2010).

## Simulator-trained models (hybrid)

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2022 | Xie | Combining CERES-Wheat model, Sentinel-2 data, and deep learning method for winter wheat yield estimation. Int. J. Remote Sens. 43(2):630-648 | 10.1080/01431161.2022.2026521 | an LSTM pretrained on a crop model, then real yields | WebSearch abstract; Wayback (HTML) |
| 2022 | Droutsas | Integration of machine learning into process-based modelling to improve simulation of complex crop responses. in silico Plants 4(2):diac017 | 10.1093/insilicoplants/diac017 | ML inside a crop model | OUP (two URLs), Wayback, headless browser, Europe PMC |
| 2019 | Reichstein | Deep learning and process understanding for data-driven Earth system science. Nature 566:195-204 | 10.1038/s41586-019-0912-1 | review | nature.com, Wayback |
| 2019 | Jia | Physics guided RNNs for modeling dynamical systems (SIAM SDM; arXiv 1810.13075) | — | the energy loss apart from pretraining | not attempted |

## Synthetic-truth method (osse)

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2017 | Parnell | Annu. Rev. Phytopathol. 55:591-610 (simulation-based surveillance design) | 10.1146/annurev-phyto-080516-035334 | TRUTH-METHOD's plant-health reference | OpenAlex, Rothamsted (restricted), Salford |
| 2007 | Kaipio | J. Comput. Appl. Math. 198:493-504 (the inverse crime) | 10.1016/j.cam.2005.09.027 | whether the inverse crime "gives overconfident results" | ScienceDirect, Aalto portal |
| 2013 | Meynard | J. Biogeogr. 40:1-8 (virtual species; abstract read: `meynard2013`) | 10.1111/jbi.12006 | how a virtual species' design biases methods | Wiley, HAL notice |
| 2012 | Meynard | Ecography 35:499-509 | 10.1111/j.1600-0587.2011.07157.x | the same, measured | HAL notice, Wiley |
| 2013 | Errico | Q. J. R. Meteorol. Soc. 139:1162-1178 (validating GMAO's OSSE; 2015 slides read: `errico2015ntrs`) | 10.1002/qj.2027 | OSSE validation against real data | Wiley, NTRS |
| 2015 | Atlas | Mar. Technol. Soc. J. 49(6):140-148 | 10.4031/MTSJ.49.6.3 | which "Atlas et al. 2015" TRUTH-METHOD meant | ingentaconnect |
| 2021 | Privé | Tellus A 73:1886795 | 10.1080/16000870.2021.1886795 | identical against fraternal twins in the atmosphere | Taylor & Francis |
| 1985 | Atlas | conference preprint (the over/under-estimation rule Halliwell 2014 cites) | — | the rule's source | not searched |

## Datasets

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2018 | Templ | Pan European Phenological database (PEP725). Int. J. Biometeorol. 62:1109-1113 | 10.1007/s00484-018-1512-8 | how many Vitis records PEP725 holds | Springer, Europe PMC, Wayback (refused by the permission check) |
| 2025 | Lacueva Pérez | Comput. Electron. Agric. 231:110018 (models on the Aragon phenology set) | 10.1016/j.compag.2025.110018 | scores on `lacuevaperez2026.aragon_phenology` | Europe PMC |
| 2024 | Hughes | CropLife Europe Crop Development Database (C2D2). Integr. Environ. Assess. Manag. | 10.1002/ieam.4870 | whether C2D2 holds vine BBCH observations | Europe PMC |
| 2025 | Londo | J. Exp. Bot. (cold hardiness, deacclimation, budbreak data) | 10.1093/jxb/eraf045 | the Dryad set's design | Europe PMC |
| 2024 | Gastou | OENO One (46 vineyards' esca monitoring) | 10.20870/oeno-one.2024.58.2.8043 | whether the series is deposited | not fetched |
| 2023 | Daviet | Plant Methods 19 (ripening dynamics) | 10.1186/s13007-023-01125-8 | automated berry-ripening data | not fetched |

Open datasets seen on landing pages only (no paper read), in the strand's LEADS: BASF's 36 downy
mildew trials 2012-2019 (Zenodo 10.5281/zenodo.6520937, CC BY 4.0, no weather), Western
Switzerland's esca monitoring 2001-2022 (Zenodo 10.5281/zenodo.21704548), the Aragon powdery
mildew registry (Zenodo 10.5281/zenodo.20734058), Bergheim's Riesling stages (RDG 10.15454/GYSGNR),
a Tempranillo berry ripeness set (Zenodo 10.5281/zenodo.14177889), and several grape image sets.

## Disease forecasting (diseaseml)

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2026 | Temfack | A Hybrid Mechanistic-Data-Driven Approach for Grapevine Downy Mildew Risk Prediction. MSc thesis, Pisa (abstract read: `temfack2026`) | — | the only vine hybrid found | closed until 2096; ask the repository |
| 2026 | Sinha | Evaluation of Yield Quality and Grape Disease Prediction Using Machine Learning and Climatic Data. J. Phytopathol. | 10.1111/jph.70263 | a grape mildew ML model on sensor data | Wiley, headless browser |
| 2020 | Fenu | Artificial Intelligence Technique in Crop Disease Forecasting: potato late blight (Springer chapter) | 10.1007/978-981-15-5925-9_7 | full version of `fenu2019` | Crossref |
| 2021 | Cavanagh | approximate Bayesian computation on Asian soybean rust | — | simulation-based inference for a disease | Crossref rate limit |
| 2021 | Hamer | a powdery mildew ML forecast (Kiel thesis?) | 10.38071/2021-00113-4 | cited by Skelsey | not fetched |

## Synthetic weather (weather)

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2026 | Kim | Impact-oriented evaluation of stochastic weather generators for rice blast risk modeling. Climate Services (CC BY 4.0) | 10.1016/j.cliser.2026.100725 | **the check D45 found missing**: a generator judged by a wetness-driven disease's output | ScienceDirect (captcha), Wayback, HAL, DOAJ |
| 2011 | Fatichi | Simulation of future climate scenarios with a weather generator (AWE-GEN). Adv. Water Resour. 34:448-467 | 10.1016/j.advwatres.2010.12.013 | AWE-GEN's humidity validation | FLORE, ISTA, HAL |
| 2014 | Launay | Climatic indicators for crop infection risk. Agric. Ecosyst. Environ. | 10.1016/j.agee.2014.07.020 | the hourly chain `launay2020` reuses | ScienceDirect, HAL notice |
| 2007 | Debele | Accuracy evaluation of weather data generation and disaggregation methods at finer timescales. Adv. Water Resour. | 10.1016/j.advwatres.2006.11.009 | hourly humidity disaggregation | ScienceDirect, Wayback |
| 2006 | Salinari | Downy mildew epidemics on grapevine under climate change. Glob. Change Biol. | 10.1111/j.1365-2486.2006.01175.x | GCM weather into a downy mildew model | Wiley |
| 2010 | Bregaglio | Theor. Appl. Climatol. 102:429-438 (read as chapter 3 of `bregaglio2012`) | 10.1007/s00704-010-0274-y | — | Springer |
| 2021 | Asadi | Estimating leaf wetness duration with machine learning and climate reanalysis data. Agric. For. Meteorol. | 10.1016/j.agrformet.2021.108548 | wetness from reanalysis | Elsevier (an earlier pass's lead) |

## Images (imagery)

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2018 | Ferentinos | Comput. Electron. Agric. (deep learning on field against lab plant images) | 10.1016/j.compag.2018.01.009 | the lab-to-field drop | ScienceDirect, headless browser |
| 2018 | Barbedo | Comput. Electron. Agric. (factors in plant-disease image recognition) | 10.1016/j.compag.2018.08.013 | the same | WebSearch only |
| 2020 | Barth | the published version of the CycleGAN study on rendered pepper images (its preprint read: `barth2018`) | — | — | not obtained |

# Placement methods (2026-10-21): leads not obtained or not read

The 2026-10-21 search for Agrarium's D48 (where weather nodes go and which sensors they carry)
ran 74 OpenAlex queries in four strands: information-theoretic and decision-focused placement,
representative sites by clustering, vineyard and orchard microclimate networks, and node
sensors. A title screen by claude-haiku-5-5 kept 143 of 520 results as A; about 55 were obtained
and read or noted. Nothing below was read; titles come from OpenAlex, unchecked.

- **How they were tried:** the open-access link once; then every OpenAlex location and any PDF
  link on a landing page (`fetch_locations.py`); MIT DSpace and UBC cIRcle in headless Chromium
  (both refused: HTTP error and a browser-verification page). The Wayback Machine was offline
  during this search (night of 2026-10-20 to 21, EDT), so no Wayback capture was tried: retry those first.
  Elsevier, IEEE, ACM and APS pages refuse this VM; list them for Chris rather than retrying.
- **Scite's MCP tools need a paid plan** on this account (2026-10-21), so no Scite excerpts
  were used.

## Decision-focused and value-of-information placement (7)

| Year | First author | Title | DOI | Why it matters | Open copy listed |
|---|---|---|---|---|---|
| 2016 | Carl Malings | Value of information for spatially distributed systems: application to sensor placement | 10.1016/j.ress.2016.05.010 | spatial VoI placement on a Gaussian field: the decision-focused method D48 asks for | closed |
| 2017 | Carl Malings | Value-of-information in spatio-temporal systems: sensor placement and scheduling | 10.1016/j.ress.2017.11.019 | VoI over time: the re-plan | closed |
| 2019 | Carl Malings | Submodularity issues in value-of-information-based sensor placement | 10.1016/j.ress.2018.11.010 | when greedy VoI fails | closed |
| 2016 | Carl Malings | Conditional entropy and value of information metrics for optimal sensing in infrastructure systems | 10.1016/j.strusafe.2015.10.003 | entropy against VoI | closed |
| 2015 | Carl Malings | Sensor network optimization using Bayesian networks, decision graphs, and value of information (thesis, UBC) | 10.14288/1.0076269 | the same, open in principle | UBC cIRcle (browser check refused) |
| 2026 | Qian Sun | Decision-focused sensor network placement for rapid disaster response | 10.1145/3849814 | decision-focused learning with placement (abstract read from OpenAlex only) | closed |
| 2017 | Laura Mainini | Sensor placement strategy to inform decisions | 10.2514/6.2017-3820 | decision-informed placement | MIT DSpace (HTTP error) |

## Representative sites and network design (7)

| Year | First author | Title | DOI | Open copy listed |
|---|---|---|---|---|
| 2005 | Michael H. Cosh | Temporal stability of surface soil moisture in the Little Washita River watershed | 10.1016/j.jhydrol.2005.08.020 | closed |
| 2008 | Luca Brocca | Soil moisture temporal stability over experimental areas in Central Italy | 10.1016/j.geoderma.2008.11.004 | closed |
| 2016 | Mei Sun Yee | On the identification of representative in situ soil moisture monitoring stations | 10.1016/j.jhydrol.2016.03.060 | closed |
| 2011 | Manuel Zarzo | Modeling the variability of solar radiation data among weather stations by means of PCA | 10.1016/j.apenergy.2011.01.070 | closed |
| 2022 | Daniel Dooyum Uyeh | An online machine learning-based sensors clustering system | 10.1016/j.compag.2022.107139 | closed |
| 2019 | Sang-Yeon Lee | Optimal sensor placement for monitoring and controlling greenhouse internal environments | 10.1016/j.biosystemseng.2019.10.005 | closed |
| 2008 | Andreas Krause | Robust submodular observation selection (JMLR journal version; the long technical report is read as `krause2008c`) | — | jmlr.org, not tried |

## Vineyard and orchard networks (6)

| Year | First author | Title | DOI | Open copy listed |
|---|---|---|---|---|
| 2004 | Jenna Burrell | Vineyard computing: sensor networks in agricultural production | (IEEE Pervasive Computing 3(1)) | closed |
| 2006 | Koen Langendoen | Murphy loves potatoes: experiences from a pilot sensor network deployment in precision agriculture | — | closed (its 2007 follow-up is read: `kleinhaneveld2007`) |
| 2008 | Jean Carlson Batzer | Spatial heterogeneity of leaf wetness duration in apple trees and its influence on performance of a warning system | 10.1094/PDIS-92-1-0164 | APS, closed here; Wayback offline |
| 2008 | Emília Hamada | Spatial and temporal variability of leaf wetness duration in the State of São Paulo | (Sci. Agric. 65) | SciELO, fetch failed |
| 2014 | Powell | The spatial variation of minimum near-surface temperature in complex terrain (thesis, Canterbury) | 10.26021/9174 | not fetched |
| 2021 | Oliver J. Binks | Measuring the vertical profile of leaf wetness in a forest canopy | 10.1016/j.mex.2021.101332 | closed |

## Node sensors (8)

| Year | First author | Title | DOI | Open copy listed |
|---|---|---|---|---|
| 1994 | Gert J. W. Visscher | Long-term tests of capacitive humidity sensors | 10.1088/0957-0233/5/10/015 | closed |
| 2013 | Zachary A. Holden | Design and evaluation of an inexpensive radiation shield for monitoring surface air temperatures | 10.1016/j.agrformet.2013.06.011 | closed |
| 2020 | Javier López-Lorente | Worldwide evaluation and correction of irradiance measurements from personal weather stations | 10.1016/j.solener.2020.06.073 | closed |
| 2024 | Nikolaos A. Dervos | Development of experimental low-cost rain gauges and their evaluation during a high-intensity storm | 10.1007/s40710-024-00686-7 | closed |
| 2024 | Sébastien Dandrifosse | Automatic quality control of weather data for timely decisions in agriculture | 10.1016/j.atech.2024.100445 | closed |
| 2025 | Hamed Mokhtarzadeh | Design, development and evaluation of a low-cost smart solar-powered weather station | 10.1016/j.rineng.2025.104848 | closed |
| 2006 | Nithya Ramanathan | Rapid deployment with confidence: calibration and fault detection in environmental sensor networks | — | not fetched |
| 2026 | Abel Quevedo-Nolasco | One-year field evaluation of a low-cost Arduino-based tipping-bucket rain gauge | 10.38032/jea.2026.02.004 | **obtained, not read** (drop `text/quevedonolasco2026/`) |

## Obtained since (2026-10-26, other sources)

Fetched through sources the search had not used (`2026-10-26-other-sources.md`, Table 1), not yet read; their rows above no longer apply: binks2021 (Binks 2021), krause2008jmlr (Krause 2008), mainini2017 (Mainini 2017), ramanathan2006 (Ramanathan 2006).
Rows that already had notes when this pass ran: Andreas Krause 2008 (krause2008c).
Open copies this VM could not download are in that file's Table 2.

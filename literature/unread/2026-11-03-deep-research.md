# Deep research (2026-11-03): leads not obtained

The night pass of 2026-11-03 searched the gaps no earlier pass had touched: the truth's late
start outside Italy (Agrarium D67), F3's made-up values, cold nights in hollows and on the leaf,
the simulated station's errors, spray timing for Cooptera (E6, E7), open datasets, the catalogue's
own unheld sources, and regional bulletins with first-symptom dates. Strand agents
(claude-sonnet-5-5) searched with OpenAlex (about 200 calls in all), Crossref, Europe PMC,
DataCite, Zenodo, web search and the Wayback Machine; each strand's `search.md` and `LEADS.md` in
the drop (`2026-11-03-deep-research/reading/<strand>/`) lists every route tried.

Nothing below was read beyond an abstract where one is said. Titles and DOIs are from the strands'
reference lists, OpenAlex or Crossref, unchecked unless said.

- **Refusals this time:** Wiley, Elsevier, AMS (a human-verification page), APS for some PDFs,
  journals.ashs.org (a bot gate), OpenAgrar (a bot check), oeno-one.eu (unreachable; Wayback
  captures worked, some truncated at 1 MB). Scite's tools need a paid plan.
- **For a person's browser:** the OpenAgrar reports and the AMS papers below open in an ordinary
  browser; Pollock et al. 2018 is open access on Wiley.

## Primary infection outside Italy (Agrarium D67)

| Year | Author | Title / venue | DOI or URL | Settles | Tried |
|---|---|---|---|---|---|
| 2000 | G. K. Hill | Simulation of P. viticola oospore-maturation with the model SIMPO. IOBC/WPRS Bull. 23(4):7-8 | - | Geisenheim's oospore model | web search; IOBC sells its bulletins |
| 1998 | G. K. Hill | Studies on the germination of P. viticola oospores with a floating disc test. IOBC/WPRS Bull. 21(2):1-2 | - | German germination dates | same |
| 2001 | G. K. Hill | The survival of P. viticola macrosporangia under field conditions (cited by Si Ammour 2020) | - | primary sporangia | same |
| 1997 | G. K. Hill, B. Spies, O. Löhnertz | Die Weinwissenschaft 52 (Rheinhessen, severe primary infections); also Hill & Breth 1997 | - | German first infections | no online copy |
| 1987 | W. K. Gehmann | Hohenheim dissertation, body text (contents held: `gehmann1987`) | - | the 160 degree-day rule's data | KIM Hohenheim holds the scan |
| 2006 | Geisenheim, BBA, DWD | Primary-infection model reports, OpenAgrar derivates 00027004 (2006-580.pdf) and 00025764 (2006-168.pdf) | openagrar.de | a German primary-infection model | bot check; no Wayback copy |
| 2005 | B. X. Killigrew et al. | Plant Disease 89:777 (abstract) | 10.1094/PD-89-0777C | WA oospores | `killigrew2006` is the fuller report |
| - | P. Magarey | Managing downy mildew in NSW vineyards (DPIRD NSW) | - | the 10:10:24 rule's caveats | Cloudflare check |
| 2002 | O. Viret, B. Bloesch | Observation of oospore germination (Revue suisse) | - | Swiss germination dates | not found |

## The catalogue's own sources (engine models)

| Year | Author | Title / venue | DOI | Record | Tried |
|---|---|---|---|---|---|
| 2004 | W. Siegfried, O. Viret, B. Bloesch, G. Bleyer, H.-H. Kassemeyer | Vitimeteo Plasmopara - Ein neues Prognosemodell für den Falschen Rebenmehltau. Schweiz. Z. Obst- Weinbau 140(23):10 | - | `vitimeteo.oospores` | Crossref, e-periodica, Agroscope IRA, web search |
| 1974 | E. A. Richardson, S. D. Seeley, D. R. Walker | HortScience 9(4):331-332 | 10.21273/HORTSCI.9.4.331 | `richardson1974.forcing_hours` | journals.ashs.org bot gate |
| 2000 | I. Chuine | A unified model for budburst of trees. J. Theor. Biol. 207:337-347 | 10.1006/jtbi.2000.2178 | `chuine2000.unified` | OpenAlex, HAL, OpenAIRE; Caffarra, Donnelly & Chuine 2011 (Clim. Res. 46, OA) restates it |
| 1982 | D. G. Erbs, S. A. Klein, J. A. Duffie | Solar Energy 28(4):293-302 | 10.1016/0038-092X(82)90302-4 | `erbs1982.partition` | Elsevier |
| 1965 | J. Bidabe | C. R. Acad. Agric. Fr. 49:934-945 | - | `bidabe1965.cold_action` | Gallica, HAL |
| 1983 | P. Strizyk | EPI (ACTA) | - | `epi1983.corrected` | HAL, web search |
| 1997 | H. L. Ypema, W. D. Gubler | Plant Dis. 81:1187-1192 | - | the temperature work behind `gubler1999.powdery_index` | APS |
| 2013 | Peduto, Backup, Hand, Janousek, Gubler | Plant Dis. 97 (the index's high-temperature part revised) | 10.1094/PDIS-01-13-0039-RE | `gubler1999.powdery_index` | not tried |

## Cold nights, the leaf and budburst spread

| Year | Author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2004 | C. D. Whiteman et al. | Minimum temperatures ... in limestone sinkholes of different sizes and shapes. J. Appl. Meteorol. 43:1224 | 10.1175/1520-0450(2004)043<1224:MTDTRA>2.0.CO;2 | deficit by hollow depth (`micro.coldpool_c_per_m`) | AMS verification page |
| 2007 | C. D. Whiteman, S. F. J. De Wekker, T. Haiden | Effect of dewfall and frostfall on nighttime cooling in a small, closed basin. JAMC 46 | 10.1175/JAM2453.1 | humidity in hollows | AMS |
| 2011 | M. Dorninger et al. | Meteorological events affecting cold-air pools in a small basin. JAMC 50 | 10.1175/2011JAMC2681.1 | wind and cloud thresholds | AMS |
| 2007 | R. Steinacker et al. | BAMS 88:701 | 10.1175/BAMS-88-5-701 | sinkhole pools | AMS |
| 2023 | J. Boekee et al. | Agric. For. Meteorol. | 10.1016/j.agrformet.2023.109312 | leaf cooling | Elsevier |
| 2008 | H. Quénol, G. Beltrando | Meteorol. Appl. | 10.1002/met.81 | vineyard topoclimate | Wiley |
| 2022 | Moreno et al. | Agriculture 12:798 (RGB-D vine training systems) | 10.3390/agriculture12060798 | canopy dimensions | `fetch_locations` only |
| 2024 | Perna et al. | Sensors 24:7894 (LiDAR canopy) | 10.3390/s24247894 | canopy dimensions | `fetch_locations` only |
| 2019 | N. Verdugo-Vásquez et al. | Precision Agric. (within-field phenology model) | - | within-block budburst spread | not obtained |
| 2022 | A. Pellegrino et al. | Comparison of methods for determining budburst date in grapevine. OENO One 56(1) | 10.20870/oeno-one.2022.56.1.4751 | per-bud timing | Wayback capture truncated at 1 MB |
| 1996 | R. A. Hamman et al. | grape bud temperature | - | leaf and bud cooling | not found online |

## The simulated station

| Year | Author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2018 | M. D. Pollock et al. | Quantifying and mitigating wind-induced undercatch in rainfall measurements. WRR 54 | 10.1029/2017WR022421 | liquid undercatch, measured | Wiley (OA) |
| 2025 | Dunn et al. | Tipping-bucket rain gauges: a review of the undercatch phenomenon. Weather | 10.1002/wea.7736 | gauge errors | Wiley |
| 2011 | M. Lacombe et al. | WMO IOM Report 106 (the Ghardaïa intercomparison of shields and humidity sensors) | - | shield and humidity errors | WMO library, not tried |
| 2014 | A. Tokay et al.; Mandapaka & Qin 2013 | hourly rain correlation against distance | - | station-to-vineyard rain | AMS |
| 2026 | Jang | Flow Meas. Instrum. | 10.1016/j.flowmeasinst.2026.103578 | intensity-dependent gauge error | Elsevier |
| - | Meteocat | technical notes on XEMA's sensors, heights and quality control | - | the station's sensors | not located |

## Spray timing (Cooptera E6, E7)

| Year | Author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 1997 | J.-L. Genet, Y. Bugaret, G. Jaworska, R. Hamlen | Études de l'action curative du cymoxanil sur le mildiou de la vigne | - | cymoxanil's window by temperature | not searched in a repository |
| 1980, 1982 | T. Wicks | Aust. Plant Pathol. (fungicides applied after infection); Plant Dis. 66:839 | 10.1094/PD-66-839 | curative windows, field | 403 |
| 1991 | P. A. Magarey, M. F. Wachtel, M. R. Newton | Aust. Plant Pathol. 20:34 | 10.1071/APP9910034 | phosphonate curative use | not obtained |
| 2011 | S. L. Toffolatti, D. Maffi, L. Serrati | J. Phytopathol. 159:201 | 10.1111/j.1439-0434.2010.01748.x | mandipropamid's curative histology | Wiley |
| 2014 | Pirondi et al. | GDPM7 proceedings pp. 108-109 | - | CAA and cyazofamid at 24-36 h | abstract only |
| 2015 | D. H. Gent et al. | Plant Dis. (hop downy mildew pre- and post-infection activity) | 10.1094/PDIS-10-14-1004-RE | curative hours by class, another crop | APS |
| 2007 | Y. Cohen, U. Gisi | Phytopathology 97:1274 | - | CAA activity by stage | APS |
| 2020 | González-Domínguez, Legler, Reyes-Aybar, Giralt, do Val, Rossi | IOBC-WPRS Bull. 154:88-92 (vite.net in Penedès) | - | a DSS against growers in Penedès | abstract only |
| 2026 | M. Furiosi et al. | Pest Manag. Sci. (meta-analysis of decision tools) | 10.1002/ps.71434 | sprays saved | Wiley; abstract on PubMed |
| 2009 | Kuflik et al. | copper parameters of vite.net's protection model | - | E6 | still not obtained (also 2026-10-25) |

## Penedès and Catalonia

| Year | Author | Title / venue | DOI or URL | Settles | Tried |
|---|---|---|---|---|---|
| 2020 | E. González-Domínguez, S. E. Legler, J. Reyes-Aybar, L. Giralt, C. Val, C. Fregoni, V. Rossi | IOBC-WPRS Bull. 154:88-92 (vite.net's Penedès pilot) | iobc-wprs.org | dates and sprays per vineyard, 2016-17 | sold by IOBC; abstract held as `gonzalezdominguez2019` |
| 2022 | M. Otero et al. | FAIA 356:164-167 (machine-learning risk at L'Aranyó) | 10.3233/FAIA220333 | the sites and models of `otero2023` | IOS Press returns HTML |
| 2025 and earlier | M. Galimany Vives | "Balanç fitosanitari" season reviews of the Estació d'Avisos del Penedès (December technical days, Escola Mercè Rossell, Sant Sadurní) | - | first spots and spray counts by season | programme leaflet only (`escolamerce2025`) |
| 2012-2016 | Sanitat Vegetal, Tarragona | avisos for Alt Camp and Baix Penedès (laselvadelcamp.cat) | - | Baix Penedès first spots | 404; no Wayback captures |
| 1997 | E. Giralt | Míldiu: 1960-1995 (ICEA) | - | Penedès first spots over 35 years | print only |
| 2014 | S. Boso et al. | Crop Prot. 63 (field susceptibility of Vitis varieties) | - | cultivar susceptibility | Elsevier |
| 2004 | - | Horticultura 178:36-41 (the Catalan warning networks) | mapa.gob.es | how the networks work | the server did not answer |

## Bulletins and season reviews not reached

The bulletin strands' `ARCHIVES.md` files in the drop give URL patterns and every route tried.

| Source | Years | Settles | Tried |
|---|---|---|---|
| Regione Piemonte, Settore Fitosanitario, "Bollettino vite" | 2010-2026 | Italian laboratory oospore tests (the one Italian series said to run them) | regione.piemonte.it, sistemapiemonte.it time out; Wayback offline |
| Emilia-Romagna, "Bollettino modelli previsionali patogeni" | 2021-2026 | daily model oospore maturity by area | 14 of 2021's files fetched; the rest listed |
| Emilia-Romagna bulletins 2012-2020; Trentino FEM; Alto Adige Beratungsring; ERSA 2008-2009 | - | Italian first spots | not reached |
| BSV Champagne, Alsace, Lorraine 2010-2015; Bourgogne 2010; Aquitaine before 2019; Pays de la Loire; Limousin; Occitanie 2024; Centre-Val de Loire 2019, 2021-2024 | - | French laboratory maturity and first spots | old regional sites gone; Wayback captures truncated at 1 MiB or missing |
| DLR Rheinhessen-Nahe-Hunsrück 2019-2025; DLR Pfalz 2022-2024; Mosel 2023 | - | German first spots | dead links, no captures |
| Ticino's Bolfito; Valais and Neuchâtel annual reports; Wädenswil Winzerinfo 2024 Nr. 6 | - | Swiss first spots | www4.ti.ch refuses this VM; PDFs gone |
| Austria (LK Steiermark, Burgenland), Luxembourg (IVV) | - | first spots | logins, bot checks |
| La Rioja's bulletin PDFs 2008-2016; INTIA Navarra; DRAP Norte Entre Douro e Minho 2022, 2025 | - | Iberian first spots | larioja.org unreachable; INTIA for subscribers |
| Grapegrower & Winemaker 659 (Dec 2018) and 660 (Jan 2019); Magarey, Wachtel, Emmett & Magarey 1993, "Downy mildew season 1992/93", Aust. NZ Wine Ind. J. 8(3):234 | - | Australian seasons | paywalled |
| NSW DPI, Agriculture Victoria, SARDI, Bragato, NZ Winegrowers alerts | - | Australian and New Zealand first detections | bot checks or nothing dated |

## The newest literature (2025-07 to 2026-11) not obtained

| Year | First author | Title / venue | DOI | Tried |
|---|---|---|---|---|
| 2026 | H. Wang | A user-friendly decision support system for supporting grape downy mildew control. Smart Agric. Technol. | 10.1016/j.atech.2026.102109 | Elsevier |
| 2026 | M. Kotaidou | Grapevine disease risk assessment through multi-modal data analysis. Smart Agric. Technol. | 10.1016/j.atech.2026.102040 | Elsevier |
| 2026 | Hjelkrem et al. | A mathematical model for estimation of leaf wetness for use in European agricultural DSSs. Smart Agric. Technol. | 10.1016/j.atech.2025.101723 | Elsevier |
| 2026 | S. Leoni | Quadruplex real-time PCR targeting airborne spores of grapevine pathogens. Crop Prot. | 10.1016/j.cropro.2026.107925 | Elsevier |
| 2025 | C. Poblete-Echeverría | AI detection of downy mildew. Eur. J. Agron. | 10.1016/j.eja.2025.127755 | Elsevier |
| 2026 | D. Kapetas | Multispectral imaging for downy mildew and grey mould. Smart Agric. Technol. | 10.1016/j.atech.2026.101990 | Elsevier |
| 2026 | H. Huitu | Crop protection models for decision support: web infrastructure. in silico Plants | 10.1093/insilicoplants/diag006 | OUP |
| 2026 | Pippi et al. | Hyperspectral early detection of grapevine downy mildew. Plant Dis. (AgriRxiv 10.31220/agrirxiv.2026.00411, free) | 10.1094/pdis-03-26-0540-sr | AgriRxiv hung in the headless browser: try by hand |
| 2026 | Mendes et al. | High spring rainfall, downy mildew and yield in France. SSRN | 10.2139/ssrn.7346698 | SSRN |
| 2026 | Yang et al. | Stage-aware early warning of grapevine downy mildew, qPCR-constrained. SSRN | 10.2139/ssrn.7328849 | SSRN |
| 2026 | Xu et al. | Temperature, wetness duration and wetness interruption on grapevine infection. Plant Dis. | 10.1094/pdis-03-26-0456-re | APS |
| 2025 | de Rességuier et al. | Modeling grapevine phenology at local scale. Agric. For. Meteorol. | 10.1016/j.agrformet.2025.110831 | Elsevier |

## Closed by this pass

Leads of earlier lists now held: Bonnardot et al. 2012 (`bonnardot2012`; 2026-10-18 list),
Powell 2014 (`powell2014`; 2026-10-21 and 2026-10-26 lists). Chris's drop `2026-10-30-missing`:
all three files without a note are held papers (`pieri2003`, `riou1994`, the journal's PDF of
`bois2008b`); two of their names carry commas, which a note's `files` cannot list.

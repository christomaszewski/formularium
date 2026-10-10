# Literature notes

One note per paper read for Formularium or for the tools that use it: what the paper
holds, how it was read, and what was concluded, dated. The notes outlive the question
that prompted them, so they are written for a reader working on another disease, crop or
region.

The repository is public. A note holds facts, numbers and short quotes, never the paper.
It says where a copy is held only as "held by Chris" or "open access", never a path;
`files` records only the names a copy was dropped under.

Documents a search found but triage judged off the point are listed, unread, in
[unread/2026-10-09-deep-research-C.md](unread/2026-10-09-deep-research-C.md), so that
nobody fetches or triages them again.

## A note's header

Each note starts with a header between two `---` lines, one `key: value` per line; lists
are written `[a, b]`. `tests/test_literature.py` checks it.

| Key | What it holds |
|---|---|
| `id` | the file's name without `.md`: `<first author's surname><year>` and, if needed, a word |
| `citation` | authors, year, title, journal, volume and pages, as read |
| `doi` | where one exists |
| `read` | when, how much, and by whom: "2026-10-08, in full", "sections 2.5 and 3.4", "by a reading agent, key figures checked" |
| `status` | how the note's facts were obtained: `read`, `trail` (from another record that says how it was read), `snippet` (a search summary or a tool's summary of a page) |
| `diseases`, `crops`, `regions`, `processes` | lists, for finding notes later |
| `records` | catalogue ids the paper supports (`catalogue.py`); each must exist |
| `datasets` | dataset ids it describes (`datasets.py`); each must exist |
| `files` | the names the paper was dropped under, so `scripts/coverage.py` can tell which papers in a drop have notes; never a path |

## A note's body

- **What it holds:** data (sites, years, cultivars, conditions, counts) and formulations
  (equations and values, with the table or page).
- **Dependence:** which other models it computes, which data it was fitted to, which
  models shaped its data, and whose authors it shares (Agrarium decisions D27 to D29).
- **Bearing:** what was concluded for Agrarium and Cooptera, with the date. Conclusions
  age; the facts above them should not.

Numbers garbled by text extraction are marked as such, never guessed.

## Index

| Note | Disease | Process | Region | Bearing, in a line |
|---|---|---|---|---|
| [actahort1999](actahort1999.md) | downy mildew | epidemic progress, berry growth | Switzerland | Vinemild is clear of the engine, but these papers print too little to run it |
| [agoston2020](agoston2020.md) | downy mildew | infection, primary infection, season severity, spray timing… | Hungary, Bács-Kiskun County | A two-season record of fruit-bunch severity by class in one Hungarian county (2009 and 2010, two dated counts… |
| [aichiprefecture2019](aichiprefecture2019.md) | downy mildew | disease survey, incidence, season severity, forecast adviso… | Aichi prefecture, Japan, Nagoya | Offers a qualitative Japanese check: a June 2019 field incidence series with averages and a forecast-linked s… |
| [akcali2020](akcali2020.md) | downy mildew | fungicide efficacy, dose reduction, spray timing, disease s… | Turkey (Mediterranean region Tarsus Mersin) | None for the truth or the engine's models; it is a fungicide dose-efficacy trial, though its observed severit… |
| [albelda2005](albelda2005.md) | downy mildew, powdery mildew, grey mould | aerobiology | Galicia | Airborne spores at Cenlle, 2004 |
| [albetis2017](albetis2017.md) | flavescence dorée | remote sensing, detection | Gaillac AOC, southwest France | Detection by UAV multispectral images is good on red cultivars and poor on white ones |
| [alexi2011web](alexi2011web.md) | none | evapotranspiration | United States | Typical ALEXI flux errors (about 15%) |
| [alfonso2025](alfonso2025.md) | downy mildew, grey mould | sporulation, zoospores, infection, biostimulants, fungicide… | Switzerland (greenhouse and climate-chamber exper… | A dose-response assay of a biostimulant against P. viticola sporulation and zoospore release (0 to 51 % reduc… |
| [allegre2007](allegre2007.md) | downy mildew | host physiology, detection | Dijon | Thermal signature of infection before symptoms |
| [alves2015](alves2015.md) | downy mildew, grey mould, bunch rot (botrytis) | infection, leaf wetness, season severity, spray timing, inf… | Brazil, Rio Grande do Sul, Campanha Gaúcha, Santa… | It computes Lalancette et al. 1988a infection-efficiency equation, whose data the Formularium magarey2005 not… |
| [amey2006](amey2006.md) | pea downy mildew | detection | UK | Another crop |
| [amir2016](amir2016.md) | none | leaf wetness | New Zealand | Clear |
| [amirshekari2025](amirshekari2025.md) | none | evapotranspiration | Indoor plant factory, lettuce | Indoor lettuce under lamps |
| [ammour2020](ammour2020.md) | Botrytis bunch rot | detection | Italy | An observation method (latent infection by LAMP) |
| [ammour2020pcr](ammour2020pcr.md) | downy mildew | oospores, overwintering inoculum, leaf litter, germination,… | Italy, Piacenza | A molecular measurement of overwintering oospore density in leaves, which could serve the truth as an observa… |
| [anco2013](anco2013.md) | Phomopsis cane and leaf spot | sporulation, dispersal | Ohio | A flag now, not kin |
| [anderson2001](anderson2001.md) | potato late blight | leaf wetness, dew | Wisconsin | Clear of the engine |
| [anderson2007](anderson2007.md) | none | evapotranspiration, surface energy balance | United States | Clear |
| [anderson2018disalexi](anderson2018disalexi.md) | none | evapotranspiration | California Delta | Prose summary of DisALEXI's data fusion |
| [angeli2010](angeli2010.md) | powdery mildew | biocontrol, mycoparasitism, aggressiveness, sporulation, pa… | Trentino-Alto Adige (Northern Italy), Israel (AQ1… | None for the downy mildew truth: a powdery mildew biocontrol study. Its 2004 to 2007 parasitism survey is obs… |
| [angelottivsf](angelottivsf.md) | downy mildew | spray timing | Pernambuco | Míldio-VSF's rules not printed; a semi-arid spray trial |
| [aoki2021](aoki2021.md) | downy mildew | infection, host defence | Yamanashi | Warm nights weaken defence; chamber study |
| [armijo2016](armijo2016.md) | downy mildew, powdery mildew, grey mould, black rot | infection, oospores, sporulation, season severity | Chile, North America, Europe, China | None. Recorded so that it is not read again. |
| [armstrong2010](armstrong2010.md) | downy mildew, powdery mildew | primary infection, secondary infection, oospores, spray tim… | McLaren Vale, South Australia | A dated Australian case of an AWS-driven primary-infection model that diverged from field observations, with … |
| [arsac2023](arsac2023.md) | downy mildew | primary infection, secondary infection, incubation, leaf we… | Calabria, Italy, Europe | None for a truth's data; it states the 3-10 rule and a 4-5 to 14-15 day incubation range without source, so a… |
| [arvanitis2025](arvanitis2025.md) | downy mildew, powdery mildew | forecasting | Emilia-Romagna | Learns the spray log; not usable |
| [ashraf2026](ashraf2026.md) | downy mildew | oospores, overwintering, primary infection, inoculum, incub… | Kashmir, India | Overwintering oospore counts and viability by month and depth from one site in two seasons (l. 215-221): a da… |
| [aslanov2019](aslanov2019.md) | wheat yellow rust | season risk | Luxembourg | Another disease; a window-correlation method |
| [austin2010](austin2010.md) | powdery mildew | latent period, radiation | New York | UV and sunlight slow powdery mildew; no equation |
| [avesani2023](avesani2023.md) | downy mildew | induced resistance, volatiles, callose deposition, gene exp… | Italy (Trento Laimburg) | None for the truth's infection or weather models; the leaf-disk linalool study is a treatment-response result… |
| [avila2010](avila2010.md) | powdery mildew | overwintering | Michigan | Chasmothecia traps and eradicants |
| [bagnulo2025](bagnulo2025.md) | downy mildew, powdery mildew | season severity, infection, oospores, leaf wetness, spray t… | Montepulciano, Tuscany, Italy | A dated Tuscan 2025 record of day and night ranges with qualitative downy mildew status: at most a check that… |
| [bahmani2025](bahmani2025.md) | downy mildew | infection, induced resistance, biocontrol, biostimulant, sp… | Canada (greenhouse Dalhousie University) | None for the truth's weather or epidemic models; its greenhouse incidence and spore counts are controlled-con… |
| [baldamanzanos2026](baldamanzanos2026.md) | downy mildew, grey mould | primary infection, secondary infection, sporulation, leaf w… | La Rioja Spain, San Vicente de la Sonsierra | A teaching text that uses the engine's Goidanich and 3-10 rule and the RH-90 sporulation curve; the truth mus… |
| [balduquegil2024](balduquegil2024.md) | downy mildew, powdery mildew | airborne inoculum, spore detection, dna extraction, pcr dia… | Spain, Aragon, Zaragoza, Cariñena PDO | None. Recorded so that it is not read again. |
| [balduquegil2026](balduquegil2026.md) | downy mildew, powdery mildew, grey mould | airborne inoculum, spore trapping, molecular detection, pcr… | Spain, Europe | A review of methods; no model is computed, so its value for the truth is the list of sources (Chen 2020, Fern… |
| [balotti2018](balotti2018.md) | none | phenology | South Tyrol | Regression coefficients (its Table 3) are not in the text copy |
| [basso2020](basso2020.md) | downy mildew, powdery mildew | aerobiology | Geneva, Vaud | Real-time spore counters 400 m apart differ sharply |
| [basso2026](basso2026.md) | downy mildew, powdery mildew | airborne inoculum, spore detection, spray timing, fungicide… | Switzerland, Bordeaux, France, Changins, Chateau … | A real-time airborne spore record for downy mildew at one Bordeaux vineyard (2021-2022) that a truth could us… |
| [bellow2012](bellow2012.md) | downy mildew | detection | France | Background to fluorescence sensing |
| [bellow2013](bellow2013.md) | downy mildew | detection | France | Fluorescence sees infection from day 1 (abaxial) |
| [benninga2019](benninga2019.md) | none | sensor error | Netherlands | A generic radar error law |
| [berkett2010](berkett2010.md) | powdery mildew, downy mildew, black rot, anthracnose | fungicide use, spray timing, season severity, susceptibilit… | Vermont, United States, Burlington | A cold-site cultivar record of observed powdery and downy mildew incidence with five sprays in one season (Ta… |
| [berlese1898](berlese1898.md) | downy mildews | taxonomy, morphology | Italy | History and morphology |
| [biddulph1999](biddulph1999.md) | phoma leaf spot, stem canker (blackleg) | infection, incubation, leaf wetness, season severity, ascos… | UK, eastern England, Rothamsted, Boxworth, High M… | A controlled-environment and field dataset on temperature and leaf wetness for infection of leaves by ascospo… |
| [biggs1988](biggs1988.md) | brown rot (Monilinia) | infection, incubation | Ontario | Its infection models are held out by structure (Broome's form) |
| [biggs2016](biggs2016.md) | none | evapotranspiration | global | Clear, and of indirect use |
| [biomebgc2010](biomebgc2010.md) | none | evapotranspiration, interception | Generic global biomes | No hourly wetness |
| [bivolnd](bivolnd.md) | downy mildew, powdery mildew, grey mould, botrytis, pseudopeziza tracheiphila | fungicide efficacy, copper fungicide, spray timing, disease… | Moldova, central zone, Ialoveni | Little for the truth or the engine: a Moldovan copper and metiram efficacy trial with no weather series and a… |
| [blaeser1978](blaeser1978.md) | downy mildew | sporulation, sporangia survival, dispersal | Germany | The laboratory survival data behind the 1979 curves; sporulation needs 98 % RH and 4 h dark |
| [blaeser1978diss](blaeser1978diss.md) | downy mildew | sporangia survival, infection, leaf wetness | Germany | Contents only: survival data on pp. 47-60, the wetness rule on pp. 24-28 |
| [blaeser1979](blaeser1979.md) | downy mildew | infection, sporangia survival | Ahr, Germany | c2 is 0.01 for detached sporangia, and the index is E·(1 - RH/100), not T·(1 - RH/100) |
| [bleyer2008](bleyer2008.md) | downy mildew | primary infection, sporulation | Baden-Württemberg, Switzerland | The engine's 140 °C·day oospore rule is still sourced only through Leoni et al |
| [bleyer2010](bleyer2010.md) | downy mildew, powdery mildew | primary infection, sporulation, secondary infection, incuba… | Germany (Baden-Württemberg Freiburg), Switzerland… | For a downy mildew truth, it gives a description of the VitiMeteo Plasmopara stages and forecast set-up, with… |
| [bleyer2020](bleyer2020.md) | downy mildew | spray timing, fungicide efficacy | Baden-Württemberg | States VitiMeteo's rule that one spray protects until 300-400 cm2 of new leaf has grown |
| [bleyer2022](bleyer2022.md) | downy mildew | spray strategy, validation | Baden-Württemberg | Untreated severity at Freiburg and Ihringen (Table 1, mean 60.5%) is a severity… |
| [bojkov2022](bojkov2022.md) | downy mildew | incubation | North Macedonia | One season, ten points, started by the 3-10 rule: not usable |
| [bojkov2023](bojkov2023.md) | downy mildew | infection | North Macedonia | One season, inconsistent; not usable |
| [bojkov2023yield](bojkov2023yield.md) | downy mildew | season severity, yield loss, spray timing, infection, sporu… | North Macedonia | A small one-vineyard severity and incidence series (2022) with a usable record of bunch-stage severity, but i… |
| [bombelli2012](bombelli2012.md) | alternaria leaf spot, downy mildew, late blight | severity, epidemic rate, senescence, leaf wetness, degree-d… | Argentina, San Pedro, Concordia, Gualeguaychú | Not downy mildew: an Alternaria method paper. Its shared forms (a fixed-date degree-day onset and a rain-plus… |
| [bonanomi2025](bonanomi2025.md) | downy mildew, grey mould | infection, sporulation, season severity, spray timing, bioc… | Italy, Puglia, Cerignola | A field severity record from one vineyard in two years (l. 247-248, 410-414) is an observed dataset a truth c… |
| [borzini1950](borzini1950.md) | downy mildew | spray timing | Italy | The incubation calendar in practice, 1950 |
| [bosshard1983](bosshard1983.md) | downy mildew | fungicide resistance | Switzerland | Context for a spray module |
| [bouma2003](bouma2003.md) | potato late blight, apple scab | decision support | Netherlands | DSS history; no equations |
| [bove2020](bove2020.md) | downy mildew | epidemic simulation | Italy (generic) | Values borrowed from Goidanich, Caffi, Rossi 2008, Lalancette; no validation |
| [bove2020resistance](bove2020resistance.md) | downy mildew | latent period, host resistance | Emilia-Romagna, Veneto | Latent periods at 20 °C for 16 varieties and three leaf stages |
| [breen2026](breen2026.md) | downy mildew | oospores, management | Europe | A perspective |
| [bregaglio2013](bregaglio2013.md) | downy mildew, Botrytis bunch rot | infection | Europe | Kin by a borrowed equation, as before, and now for that reason rather than its authors… |
| [bregaglio2022](bregaglio2022.md) | downy mildew | primary infection, secondary infection | Italy | Kin by a borrowed equation, now recorded as such |
| [brink2016](brink2016.md) | grey mould, botrytis bunch rot | spray deposition, spray volume, fungicide efficacy, infecti… | Paarl Western Cape South Africa, South Africa | A detached-part dataset linking spray deposit to Botrytis control on grapevine, with deposition benchmarks, t… |
| [brischetto2020](brischetto2020.md) | downy mildew | sporangia survival, aerobiology | Emilia-Romagna | Source of brischetto2020.survival; its Table 1 computes VPD as the saturation deficit, not the printed T(1 - RH/100) |
| [brischetto2021](brischetto2021.md) | downy mildew | secondary infection | Italy | the engine's secondary infection; its Magarey parameters, read |
| [broome1995](broome1995.md) | Botrytis bunch rot | infection | California, Chile | The engine's Botrytis model is now held and read |
| [broussard2026](broussard2026.md) | downy mildew, plasmopara viticola | sporulation, sporangia, resistance induction, volatile orga… | Piacenza Italy, Northern Italy | A glasshouse proof of concept for sage-VOC resistance induction, with no field data and no model; its authors… |
| [bruisson2019](bruisson2019.md) | grey mould, downy mildew, oomycete disease | biocontrol, antagonism, endophytes, epiphytes, volatile com… | Switzerland | None. Recorded so that it is not read again: lab biocontrol assays with P. infestans as a surrogate for P. vi… |
| [buciumeanu2019](buciumeanu2019.md) | none | phenology | Romania | ANOVA of factors only |
| [buffara2014](buffara2014.md) | downy mildew | disease assessment, severity estimation, accuracy, precisio… | Southern Brazil, Santa Catarina, Lages | Offers the truth an observation-error reference for field scoring of downy mildew (rater R2 about 0.89 withou… |
| [burruano1989](burruano1989.md) | downy mildew | oospore germination | Sicily, Apulia, Latium | One spring's maturity at seven sites |
| [burruano1990](burruano1990.md) | downy mildew | oospore germination | Sicily | Cold storage kept oospores germinable into summer |
| [burruano1992nuclei](burruano1992nuclei.md) | downy mildew | oospore cytology | Sicily | Cytology only |
| [burruano1992soil](burruano1992soil.md) | downy mildew | oospore maturation | Sicily | Soil moisture changes maturation; preliminary |
| [burruano2006](burruano2006.md) | downy mildew | oospores, latency | Sicily | Summer latency up to 52 days in Sicily |
| [busato2022](busato2022.md) | downy mildew | sporulation, infection, biocontrol, biopesticide, secondary… | Italy, Veneto, Nervesa della Battaglia | None. Recorded so that it is not read again. |
| [caffi2006validation](caffi2006validation.md) | downy mildew | primary infection, validation | Italy | Validates the engine's Rossi model: no misses, 9.6 % false alarms |
| [caffi2006water](caffi2006water.md) | downy mildew | oospore germination, litter moisture | Emilia-Romagna | Litter moisture data behind Rossi's dormancy |
| [caffi2007](caffi2007.md) | downy mildew | primary infection, oospore maturation | Sardinia | Formularium records the Siniscola data as `caffi2007.siniscola`, with the dating |
| [caffi2009](caffi2009.md) | downy mildew | primary infection, season onset | Italy | Its observed onsets are data a truth could be matched to |
| [caffi2009thesis](caffi2009thesis.md) | downy mildew | oospores, primary infection | Italy | The thesis behind Rossi 2008's model; front matter only |
| [caffi2010](caffi2010.md) | downy mildew | warning system, spray decisions | Emilia-Romagna | It evaluates the engine's rossi2008.primary in practice (Emilia-Romagna, 2006-2008) |
| [caffi2010lesions](caffi2010lesions.md) | downy mildew | damage, incubation | Emilia-Romagna | Photosynthesis lost around lesions (virtual lesions) |
| [caffind](caffind.md) | downy mildew | primary infection, secondary infection, oospores, sporulati… | Italy, Piedmont, Piacenza | It names Rossi et al. 2008 as the primary-infection sub-model of a life-cycle frame, a dependence flag for th… |
| [calderone2022](calderone2022.md) | powdery mildew, grey mould, sour rot, downy mildew (mentioned not assessed) | fungicide alternatives, resistance induction, arbuscular my… | Sicily, Italy, Messina province, Rodi Milici | None for downy mildew: the trials score powdery mildew, gray mould and sour rot and never P. viticola, so the… |
| [calonnec2010](calonnec2010.md) | powdery mildew | host growth, epidemic dynamics | Bordeaux | Vine vigour drives powdery mildew |
| [calonnec2018](calonnec2018.md) | powdery mildew | ontogenic resistance | Bordeaux | Leaf susceptibility falls within two weeks, by a fitted curve |
| [calzarano2022](calzarano2022.md) | downy mildew, grey mould, sour rot, berry brown rot | infection, leaf wetness, spray timing, fungicide efficacy, … | Italy, Abruzzo, Ari (Chieti) | Two-year field data on downy mildew severity under a copper-reduced mineral product against a farm programme,… |
| [camargo2017](camargo2017.md) | downy mildew, grapevine rust | primary infection, oospores, sporangia, leaf wetness, seaso… | São Paulo State, Piracicaba | The richest downy mildew data in the set for a truth: three seasons of weekly incidence and severity with sen… |
| [cameron2021](cameron2021.md) | none | phenology | global | Clear |
| [cammalleri2012](cammalleri2012.md) | none | evapotranspiration | Southern Sicily, Italy | TSEB run without in-situ air temperature (scene calibration or DisALEXI), over a… |
| [cannon2001](cannon2001.md) | none | sampling, detection | Australia | The engine's observation piece, confirmed |
| [cano1942](cano1942.md) | downy mildew | fungicide efficacy | Italy | History of fungicides |
| [cappelletti2016](cappelletti2016.md) | downy mildew | resistance induction, defence gene expression, phyllosphere… | Italy | Little for the truth or the engine: a controlled lab and greenhouse efficacy result for a protein inducer, wi… |
| [carisse2005](carisse2005.md) | botrytis leaf blight (grey mould on onion) | airborne inoculum, conidia, sporulation, spray timing, inoc… | Quebec, eastern Canada, New York, Michigan | None for the downy mildew truth or the Cooptera engine: an onion Botrytis threshold study whose IPI is a diff… |
| [carisse2010](carisse2010.md) | powdery mildew | aerobiology, spray timing | Quebec | Airborne-conidia thresholds; Richards and Weibull models |
| [carisse2020](carisse2020.md) | anthracnose | infection, leaf wetness | Quebec | Its printed infection equation cannot reproduce its own figure |
| [carisse2021](carisse2021.md) | downy mildew | airborne inoculum, detection | Quebec | Clear |
| [carisse2024](carisse2024.md) | anthracnose | incubation, sporulation | Quebec | Anthracnose incubation by temperature and leaf age |
| [cartolaro2010](cartolaro2010.md) | powdery mildew | overwintering, flag shoots, sexual reproduction, season sev… | southern France, Languedoc-Roussillon | None for the truth or the engine: powdery mildew genetics, not downy mildew. Recorded so that it is not read … |
| [cartolaro2010b](cartolaro2010b.md) | powdery mildew | incidence, severity, decision rule, spray timing, early sym… | Bordeaux, Cadaujac, Latresne, France, national ne… | Little for the truth or the engine: an incidence-threshold spray rule for powdery mildew in French vineyards,… |
| [casanovagascon2019](casanovagascon2019.md) | downy mildew, powdery mildew | model evaluation, host resistance | Aragón | Goidanich's dates off by weeks in Somontano; the Gubler index accurate |
| [castellvi2021](castellvi2021.md) | none | evapotranspiration | Central Iowa, USA | Sensible heat from surface renewal and land surface temperature |
| [cavalcanti2025](cavalcanti2025.md) | downy mildew, mycosphaerella leaf spot | symptom classification, image classification, diagnosis, tr… | Brazil (Embrapa Uva e Vinho Bento Gonçalves RS) | None. Recorded so that it is not read again: a leaf-image classifier with no weather, incidence or model cont… |
| [cawsenicholson2021](cawsenicholson2021.md) | none | evapotranspiration | Contiguous United States | TSEB equations and inputs as an operational product |
| [celotti2023](celotti2023.md) | downy mildew | copper deposition, copper accumulation, copper application,… | Friuli-Venezia Giulia (North-East Italy) | Gives the truth an observed field record of copper deposition on leaves against downy mildew incidence on fiv… |
| [chauvin2025](chauvin2025.md) | virus yellows | risk prediction | France | Method only |
| [chavarria2009](chavarria2009.md) | downy mildew | aerobiology, microclimate | Rio Grande do Sul | Sporangia airborne under plastic, but leaves dry |
| [chen2019](chen2019.md) | downy mildew | season risk, regional data | Bordeaux | see the note |
| [chen2019onset](chen2019onset.md) | downy mildew | season onset | Bordeaux | A history-matching pattern made outside the engine's lineage |
| [chen2020delay](chen2020delay.md) | downy mildew | season onset, spray timing | Bordeaux | Thesis ch. 6 published; nothing beyond chen2019 |
| [chen2020ml](chen2020ml.md) | downy mildew | season severity, forecasting | Bordeaux | Thesis ch. 7 published; nothing beyond chen2019 |
| [chrelashvili1993](chrelashvili1993.md) | downy mildew | season onset, incubation | Kakheti | 16 years of first appearance; the Müller curve a month early every year |
| [christoforides2026](christoforides2026.md) | downy mildew | oospore maturation, primary infection | Greece | Kin, for borrowed equations and four shared forms (Agrarium's candidates) |
| [ciliberti2015berries](ciliberti2015berries.md) | Botrytis bunch rot | infection | Piacenza | A flag now, not kin |
| [ciliberti2015flowers](ciliberti2015flowers.md) | Botrytis bunch rot | infection | Piacenza | A flag now, not kin |
| [cingolani2020](cingolani2020.md) | downy mildew, copper residues | infection, primary infection, secondary infection, incubati… | Marche Italy, Castelplanio (AN), Angeli di Varano… | A 2020 field trial of a copper-sparing alternative in two vineyards, with plot-level leaf and cluster scores … |
| [claverie2010](claverie2010.md) | downy mildew, powdery mildew | spray deposit, leaf area index, dose adjustment, canopy vol… | south-eastern France, Rhône-Méditerranée, Vauclus… | Little for the truth or the engine: a spray-deposit and dose-reduction method for Mediterranean vines with no… |
| [claverie2018](claverie2018.md) | none | remote sensing, revisit | Global land | Revisit and surface-reflectance error of the satellite record a satellite operator… |
| [clippinger2024](clippinger2024.md) | downy mildew | management | global | Review |
| [cogato2020](cogato2020.md) | none | remote sensing | Veneto | Frost damage visible for about 40 days in Sentinel-2 indices |
| [cohen2015](cohen2015.md) | downy mildew (peronospora belbahrii basil), downy mildew (plasmopara viticola cited) | survival, heat tolerance, sporulation, sporangia, sporulati… | Israel | None. Recorded so that it is not read again (basil downy mildew, not Plasmopara on grapevine; its only link t… |
| [cohen2022](cohen2022.md) | downy mildew | infection, leaf wetness, season severity, fungicide efficacy | Israel | A thermal-imaging test of early downy mildew with a dataset of observed leaf temperature and severity that a … |
| [colombo2020](colombo2020.md) | downy mildew, late blight, powdery mildew | germ tube formation, sporulation, infection, fungicide effi… | Trentino, Italy | None. Recorded so that it is not read again: a peptide antifungal tested on leaf disks and greenhouse plants,… |
| [coronelli2025](coronelli2025.md) | downy mildew | detection | Apulia | A qPCR test's detection limits |
| [cortinas2020](cortinas2020.md) | downy mildew, powdery mildew, grey mould | aerobiology | Galicia | Two Galician vineyards' airborne spores, 2016-2018 |
| [cosseboom2024](cosseboom2024.md) | ripe rot | spray timing | Maryland | Two ripe rot models time sprays |
| [costa2013](costa2013.md) | none | thermal sensing | global | Sensor background |
| [costantini2022](costantini2022.md) | none | regulation | European Union | Regulatory context |
| [courchinoux2025](courchinoux2025.md) | downy mildew | oospores | Bordeaux | A month at 50 °C kills oospores; compost does too |
| [czermainski2004](czermainski2004.md) | downy mildew | season severity, fungicide efficacy | Rio Grande do Sul | Untreated incidence by date, Bento Gonçalves 1995-96 |
| [dagostin2010](dagostin2010.md) | downy mildew | spray efficacy, biocontrol, sporangia inoculation, incidenc… | Italy, Trentino, Switzerland | None. Recorded so that it is not read again. |
| [dallamarta2006](dallamarta2006.md) | downy mildew | leaf wetness | Tuscany | Modelled wetness serves PLASMO as well as sensors |
| [dallamarta2008](dallamarta2008.md) | downy mildew | sporulation, infection, resistance, leaf wetness, season se… | Tuscany, Chianti, Italy | A single-season field observation that more sunlight means more leaf polyphenols and less downy mildew, with … |
| [davy2010](davy2010.md) | downy mildew, powdery mildew | fungicide dose, decision rule, spray frequency, severity, d… | France, Bordeaux, Gironde, Dordogne, Charente | A dose-adjustment rule set and trial summary: a reference for how the simulator's spray decisions might scale… |
| [delafuente2021](delafuente2021.md) | downy mildew | copper use, soil copper accumulation, primary infection, fu… | Europe, EU, Germany, Austria, France, California,… | A review of the copper problem and the models used to time sprays; the truth could take its copper-limit and … |
| [demaneche2020](demaneche2020.md) | downy mildew | fungicide efficacy, biocontrol, sporulation, zoospore germi… | Gyékényes Hungary, Sulzfeld Bavaria Germany, Moul… | A company-run efficacy study of a biocontrol product with field severity data for downy mildew, useful as an … |
| [dey2020](dey2020.md) | none | wetness sensing | laboratory | A laboratory prototype with no field error |
| [dietz2019](dietz2019.md) | oat crown rust, leaf spot | yield loss | Argentina | Another crop: loss through healthy area duration |
| [diezn2010](diezn2010.md) | downy mildew, powdery mildew | aerobiology | Basque Country | Spore traps against station risk; no numbers |
| [digennaro2019](digennaro2019.md) | none | remote sensing | Orsogna Winery vineyards | Satellite NDVI agrees with UAV NDVI only so well on a tall trellis (R² 0.80 and 0.60) |
| [douillet2022](douillet2022.md) | downy mildew | airborne inoculum, detection | Bordeaux | Clear |
| [doutreloup2022](doutreloup2022.md) | downy mildew, powdery mildew | bud break, flowering, veraison, spray timing, season severi… | Belgium, Champagne, Alsace, Jura, Bourgogne, Arde… | A source of 2000-2020 daily station data for Belgium and north-east France (observed, l. 167-179) and a frost… |
| [dubuis2019](dubuis2019.md) | downy mildew, powdery mildew | oospore maturation, primary infection | Switzerland, Baden-Württemberg | Changins's oil-spot dates are risky to match a truth to |
| [dumitriu2021](dumitriu2021.md) | downy mildew | leaf infection, bunch infection, spray timing, fungicide pr… | Romania, Dolj County | Little for the truth: one site, two seasons of variety-level visual attack scores with no weather series and … |
| [dumitriu2021b](dumitriu2021b.md) | downy mildew | season severity, fungicide efficacy, spray timing, variety … | Segarcea Dolj County Romania, Romania | A one-site, one-season set of observed downy mildew F%, I% and DA% on five varieties under six sprays, usable… |
| [dussert2020](dussert2020.md) | downy mildew | population genomics | France | Off-topic for simulation |
| [efsa2020](efsa2020.md) | none | sampling, detection | European Union | Held out by structure if the truth's scouts used it (D26) |
| [eisenmann2023](eisenmann2023.md) | downy mildew, powdery mildew | season severity, host resistance | Palatinate | Two seasons without downy mildew, one severe |
| [elbailemur2016](elbailemur2016.md) | downy mildew, powdery mildew, grey mould | infection, incubation, sporulation, leaf wetness, spray tim… | Somontano Huesca Spain, Aragón | For a downy mildew truth, it is a 2016 Somontano weekly dataset with weather, and its Goidanich run (Table 28… |
| [elena2016](elena2016.md) | trunk diseases | wound susceptibility | Catalonia | Wound susceptibility falls to about 10% twelve weeks after pruning |
| [elhelaly1965](elhelaly1965.md) | berry rots | postharvest | Egypt | Off-topic |
| [elsharkawy2018](elsharkawy2018.md) | downy mildew | biocontrol | Egypt | Control efficacy only |
| [emmett2010](emmett2010.md) | powdery mildew, downy mildew | spray timing, spray programme, primary infection, secondary… | south eastern Australia, Victoria, Sunraysia, Riv… | A dated Australian record of spray practice and a named downy mildew simulation model (DModel, not in the tex… |
| [erincik2003](erincik2003.md) | Phomopsis cane and leaf spot | infection | Ohio | A flag now, not kin (D27) |
| [esteban2012](esteban2012.md) | none | climatology | Catalonia | Off-topic for the disease truth |
| [eswari2021](eswari2021.md) | downy mildew | forecasting | Tamil Nadu | A regression with one residual df: not usable |
| [eswari2022](eswari2022.md) | downy mildew | yield | Tamil Nadu | A mass-action model with no data fit; not usable |
| [fang2019](fang2019.md) | none | evapotranspiration | United States | An operational ET product |
| [faretra1991](faretra1991.md) | downy mildew | cultivar susceptibility | Apulia | Cultivar ranks in a severe year |
| [farina1976](farina1976.md) | downy mildew | infection anatomy | Italy | Anatomy only |
| [fedele2020](fedele2020.md) | Botrytis bunch rot | biocontrol, infection | Piacenza | A flag, not kin |
| [fedele2025](fedele2025.md) | downy mildew | oospore dose | Italy | the truth's dose; calibrated with Rossi 2008's model |
| [fedele2026](fedele2026.md) | downy mildew | host susceptibility, canopy microclimate | Italy | Denser canopies had more susceptible leaves and longer wetness, yet epidemics did not… |
| [fernandezgonzalez2009](fernandezgonzalez2009.md) | downy mildew, powdery mildew, grey mould | aerobiology | Galicia | Cenlle 2007, the thesis's first season |
| [fernandezgonzalez2011](fernandezgonzalez2011.md) | downy mildew | airborne sporangia, phenology | Galicia | Four seasons of daily airborne sporangia |
| [ferreira2023](ferreira2023.md) | downy mildew, powdery mildew, scab, blast, asian soybean rust | leaf wetness, season severity, infection, sporulation, fung… | Paraná State Brazil, Londrina, Paranavaí, Cascave… | The observed Paraná daily RH series (1975-2021) is a usable station record for a truth's climate; its RH abov… |
| [firanjsremac2018](firanjsremac2018.md) | downy mildew, fire blight | primary infection, season onset | Vojvodina | Seven seasons of first symptoms and 10 cm shoots at Vršac |
| [foister1935](foister1935.md) | many | weather and disease | general | History; no formulation |
| [foister1946](foister1946.md) | downy mildews, various | weather and disease | general | History; no formulation |
| [folkedal2003](folkedal2003.md) | apple scab, potato late blight | decision support | Norway | A web warning system's design |
| [fontaine2021](fontaine2021.md) | downy mildew | population genomics | global | Off-topic for simulation |
| [franche2012](franche2012.md) | downy mildew | whole cycle in a DSS | France | mostly Rossi's chain; a few independent pieces |
| [franzen2025](franzen2025.md) | downy mildew, powdery mildew, black rot, black wood | infection, incubation, infection risk forecast, leaf wetnes… | Germany (Baden-Württemberg Bavaria Rhineland-Pala… | Gives the truth only the descriptive shape of VitiMeteo's Plasmopara model and field-trial figures for PIWI v… |
| [frobel2019](frobel2019.md) | downy mildew | infection, colonization, sporulation, leaf wetness, season … | Germany, Palatinate | The field classes and dates from one unsprayed 2018 plot are observed data a truth could use to check where a… |
| [furiosi2022](furiosi2022.md) | powdery mildew, downy mildew | spray timing, fungicide use, resistance, season severity, s… | Veneto, Italy | Operational records of spray counts, copper dose and FRAC risk classes for 179 vineyards over six years, whic… |
| [gadoury1997](gadoury1997.md) | downy mildew | primary infection | New York, Pennsylvania | First printing of the engine's Kennelly trigger |
| [gadoury2003](gadoury2003.md) | powdery mildew | host susceptibility, ontogenic resistance | New York | Held out by structure, as the rule stands |
| [gadoury2006](gadoury2006.md) | downy mildew, powdery mildew, black rot | ontogenic resistance | New York, Germany, Australia | Shares Kennelly's berry data with the engine's bunch window |
| [gadoury2010](gadoury2010.md) | powdery mildew | sporulation, latent period, inoculum density, light, conidi… | Geneva New York, Adelaide Australia | None. Recorded so that it is not read again: powdery mildew conidiation on detached leaves, with no downy mil… |
| [galbiati1980](galbiati1980.md) | downy mildew | oospore formation | Lombardy | Timing of oospore formation, cited |
| [gan2023](gan2023.md) | none | wetness sensing | laboratory | About 88% accuracy on an indoor plant |
| [garcia2021](garcia2021.md) | downy mildew | sporangia germination, fungicide efficacy, induced resistan… | Guarapuava Paraná Brazil, Brazil | Small greenhouse and laboratory trial of cinnamon extract and catalase on downy mildew, usable as a catalase … |
| [garciaariza2024](garciaariza2024.md) | downy mildew | primary infection, secondary infection, oospores, leaf wetn… | Castilla y León, Spain | A regional extension sheet with unsourced qualitative thresholds; it offers the truth's grower-facing check o… |
| [garciagutierrez2023](garciagutierrez2023.md) | none | phenology | Chile | Held out by structure, as recorded |
| [gashu2020](gashu2020.md) | none | phenology, berry composition | Israel | Clear and observational |
| [gautam2013](gautam2013.md) | various | climate change | India, global | Context only |
| [gawande2024](gawande2024.md) | downy mildew, powdery mildew | sensors, leaf wetness | not stated | 12 h of sensor bursts, no disease labels: not a training set |
| [gdpm2010china](gdpm2010china.md) | downy mildew | season severity, aerobiology | Shandong | One Shandong season, 2009 |
| [gehmann1987](gehmann1987.md) | downy mildew | oospores, primary infection | Baden | Contents only: behind the 160 °C·day oospore rule (Gessler 2011); pp. 57-77 |
| [gent2007cones](gent2007cones.md) | powdery mildew | sampling, observation | Oregon, Washington | Held out by structure as Part I |
| [gent2007leaves](gent2007leaves.md) | powdery mildew | sampling, observation | Oregon, Washington | Held out by structure if the truth's scouts sampled this way (D26) |
| [gent2008](gent2008.md) | powdery mildew | risk index, management | Pacific Northwest | Context for the Gubler-Thomas index's hop use (gent2025 note) |
| [gent2013](gent2013.md) | none | decision support, adoption | general | Why growers seldom use warning systems |
| [gent2025](gent2025.md) | powdery mildew | risk index, spray timing | Washington | Kin, by a borrowed equation and form (Agrarium's candidates) |
| [geppert2024](geppert2024.md) | downy mildew, powdery mildew | season severity, spray timing, fungicide use, leaf wetness,… | Italy | None for a downy mildew truth or the Cooptera engine: a management and yield survey with no disease data, who… |
| [gessler2011](gessler2011.md) | downy mildew | review: oospores, incubation, warning models | Europe | Gehmann's 160 °C·days; Merjanian's 61/T incubation; the 3-10 as Goidanich |
| [ghiani2025](ghiani2025.md) | downy mildew, powdery mildew | detection, observation | Sardinia | Clear |
| [ghule2015](ghule2015.md) | anthracnose | forecasting | Maharashtra | An in-sample weekly regression |
| [gimenezromero2022](gimenezromero2022.md) | Pierce's disease | establishment risk | global | Outside Cooptera's diseases |
| [giosue2002](giosue2002.md) | downy mildew | primary infection, spatial analysis | Emilia-Romagna | Abstract only: onset zones keep their order from year to year |
| [giovannini2022](giovannini2022.md) | downy mildew, powdery mildew | spray timing, disease severity, audpc, sporulation, ferment… | Italy, San Michele all'Adige, Trentino | Field severity and AUDPC for a rare-sugar fungicide, with the spray timing set by the RIMpro-Plasmopara DSS, … |
| [gisi2002](gisi2002.md) | downy mildews | fungicides, warning models | Europe | Which country ran which model, 2002 |
| [gleason1994](gleason1994.md) | none | leaf wetness, dew | Iowa, Kansas | Held out by structure, not by its author (Agrarium's candidates) |
| [gleason2008](gleason2008.md) | sooty blotch, flyspeck | leaf wetness, spray timing, season severity, infection | Iowa, Wisconsin, São Paulo State, Ontario, Costa … | For the truth it is a secondary source on the RH>90% wetness surrogate that the engine's sentelhas2008.wetnes… |
| [gobbin2005](gobbin2005.md) | downy mildew | epidemic structure, dispersal | central Europe | 70 % of genotypes once, 14 % twice; under 20 m per cycle; colonization 1-2 m² a day |
| [gobbin2006](gobbin2006.md) | downy mildew | population genetics, epidemic structure | Europe | random-mating oospore populations; Greek ones less diverse; cites the epidemic-structure numbers |
| [gobbin2007](gobbin2007.md) | downy mildew | dispersal | Germany | 130 m in one event; 0 to 99 % incidence in three days |
| [godfrey2010](godfrey2010.md) | powdery mildew | spray timing, infection, sporulation, season severity | South Australia, Australia | None for the truth or the engine: powdery mildew and a milk biocontrol trial. Recorded so that it is not read… |
| [gonzalezdominguez2015](gonzalezdominguez2015.md) | grey mould | infection, sporulation | Italy | A mechanistic Botrytis model independent of Broome's; 21 epidemics |
| [gonzalezdominguez2022](gonzalezdominguez2022.md) | Phomopsis cane and leaf spot | infection, validation | Italy, Montenegro | A Phomopsis model, for Cooptera |
| [gonzalezdominguez2023](gonzalezdominguez2023.md) | none | modelling history | general | Review by the Piacenza group |
| [gonzalezfernandez2021](gonzalezfernandez2021.md) | grey mould | aerobiology | Galicia | Botrytis conidia viability by immunoassay |
| [gregory1915](gregory1915.md) | downy mildew | conidial germination, sporulation, oospores, oospore germin… | United States (Ithaca New York), Europe (cited) | Offers the truth a set of observed 1913 incubation and germination values for American varieties at Ithaca, b… |
| [groot2026](groot2026.md) | grey mould, apple scab, septoria leaf blotch, soybean rust, late blight, downy mildew (as a grapevine case in the literature only) | leaf wetness, infection, infection threshold, sensor placem… | Western Europe, Pacific Northwest, Central Europe… | None for the truth or the engine: it is a review with no data of its own, and its wetness thresholds for grap… |
| [grunzel1961](grunzel1961.md) | downy mildew | oospore formation | Germany | Oospores formed in few leaves; weather no clear driver |
| [guevaratorres2025](guevaratorres2025.md) | none | evapotranspiration, remote sensing | South Australia | Pixel (about 100 m2) against canopy (about 2 m2) mismatch, for irrigation |
| [gutierrez2017](gutierrez2017.md) | grapevine moth | pest demography | Europe | An insect pest model |
| [gutierrez2021](gutierrez2021.md) | downy mildew, spider mite | detection, observation | Basque Country | Clear, and optimistic |
| [gyeonggi2011](gyeonggi2011.md) | downy mildew | spray timing | Gyeonggi | A 25 °C and 40 mm first-spray rule, tested on its own year |
| [haasbroek2006](haasbroek2006.md) | downy mildew | warning model, leaf wetness | Western Cape | Refines METOS's 10:10:24 rules; weekly untreated-plot data 2002-03 |
| [hain2009](hain2009.md) | none | soil moisture | Oklahoma | Soil moisture proxy, not leaf wetness |
| [hain2018poster](hain2018poster.md) | none | evapotranspiration | United States | A poster |
| [halsted1900](halsted1900.md) | downy mildew | cluster infection | South Carolina | Historical field note |
| [hamada2008](hamada2008.md) | downy mildew | infection, climatic risk | São Paulo | Lalancette's equation mapped, intercept misprinted; no disease data |
| [hamada2012](hamada2012.md) | downy mildew | season severity, leaf wetness, climate favourability, spray… | Brazil | None. Recorded so that it is not read again. |
| [hamada2015](hamada2015.md) | powdery mildew | favourability, climate change scenario, season severity, te… | Brazil, Northeast Brazil, South Brazil, Southeast… | None for downy mildew, but recorded as the only powdery-mildew climate band study in this batch: its RH and t… |
| [hatmi2015](hatmi2015.md) | Botrytis bunch rot | host physiology | France, Tunisia | Off-topic |
| [heger2026](heger2026.md) | downy mildew, Botrytis bunch rot | airborne inoculum, detection | Michigan | Clear |
| [hegyikalo2019](hegyikalo2019.md) | Botrytis bunch rot | incidence, isolate growth | Hungary | Noble rot isolate phenotypes in Eger |
| [henshall2005](henshall2005.md) | grey mould | leaf wetness | Auckland | Canopy against outside wetness, rainy and dry days |
| [henshall2015](henshall2015.md) | grey mould | leaf wetness | New Zealand | Modelled wetness flips a Botrytis model's verdict |
| [hentosh2026](hentosh2026.md) | powdery mildew | forecasting, host resistance | Odesa | A temperature-sum forecast on the Black Sea steppe |
| [hernandez2022](hernandez2022.md) | downy mildew | sporulation, severity assessment, leaf disc bioassay, image… | La Rioja (Spain), Milan (Italy) | A severity-reading method for sporulation on leaf discs: a possible observation operator for the truth's lab … |
| [hernandez2024](hernandez2024.md) | downy mildew | symptom detection, image classification, disease localisati… | Spain (La Rioja) | Offers a field scouting observation method (symptom images classified with 91% accuracy) that a truth could u… |
| [hernandez2025](hernandez2025.md) | downy mildew | symptom detection, disease severity, canopy imaging, proxim… | northern Spain, La Rioja | Little for the truth or the engine: a symptom-detection vision method with no weather or epidemic component, … |
| [hill2019](hill2019.md) | Botrytis bunch rot | infection risk, season severity | New Zealand, south-east Australia | Bacchus is the Botrytis candidate, recorded in Formularium as `kim2007.bacchus` with |
| [holcman2014](holcman2014.md) | downy mildew, anthracnose (mentioned), powdery mildew (mentioned) | primary infection, sporulation, oospores, sporangia, leaf w… | Northwest São Paulo, Jales (SP), Brazil, Ohio (in… | Field evidence that a 3-10 rule and a Lalancette-type infection-efficiency warning can cut sprays by 60 to 80… |
| [hong2008](hong2008.md) | downy mildew, saenun-mounmuribyeong (not identified in this text), chili anthracnose, pear rust (붉은별무늬병), rice stripe virus | forecasting, weather data collection, disease incidence sur… | Gyeonggi Province Korea, Hwaseong, Anseong, Pyeon… | For a downy mildew truth, it is a 2008 plan with no data, equations or results, and its per-spray costs (350,… |
| [hoppmann1997](hoppmann1997.md) | downy mildew | oospores, infection, leaf wetness | Rheingau | VitiMeteo's oospore form at 170 °C·days; modelled wetness r² 0.91 |
| [hubbard2021](hubbard2021.md) | none | soil, vigour | Bordeaux | Soil and vigour mapping |
| [huber1956](huber1956.md) | none | plant physiology | Germany | Off-topic |
| [huerga2010](huerga2010.md) | downy mildew, powdery mildew, grey mould | airborne spores, spore monitoring, detection, sporulation, … | laboratory (Vitoria-Gasteiz Spain), vineyard air … | None for the truth or the engine: a laboratory spore-identification method with no field, weather or model co… |
| [hug2005](hug2005.md) | downy mildew | oospores, sporangia, primary infection, secondary infection… | Western Australia, Swan Valley, New South Wales, … | Offers the truth a WA oospore-timing check, the Caversham genotype and weather record, and a source for the 1… |
| [hughes2013](hughes2013.md) | none | warning scores, risk calibration | general | Clear and a method |
| [hughes2017](hughes2017.md) | none | warning scores, forecast evaluation | general | Clear and a method |
| [humphrey1891](humphrey1891.md) | cucurbit downy mildew, brown rot | taxonomy | Massachusetts | Off-topic |
| [ilari2023](ilari2023.md) | downy mildew, powdery mildew | spray timing, spray drift, season severity, infection, fung… | Italy, Marche Region, Arcevia | A one-season field trial of spray distribution with downy mildew incidence on bunches (l. 1149-1152): a possi… |
| [institutvitivinicole2015](institutvitivinicole2015.md) | downy mildew | infection, leaf wetness, oospores, incubation, sporulation,… | Germany (Freiburg Weinsberg) | Gives a second VitiMeteo figure (160 degree-days oospore readiness, a 50 degree-hour infection gate) to set b… |
| [istvanffi1913](istvanffi1913.md) | downy mildew | incubation | Hungary | Latent periods by half-month, 1911-12: older than Müller and Goidanich |
| [jacquin2003](jacquin2003.md) | downy mildew, others | warning systems | France | The French warning models in 2002; no equations |
| [janczewski1897](janczewski1897.md) | cereal smuts | survey | Lithuania | Off-topic |
| [jensen2025](jensen2025.md) | none | modelling review | global | Review of 146 models |
| [jermini2010](jermini2010.md) | downy mildew | damage, spray strategy | Ticino | A measured damage function for Merlot |
| [jermini2010yield](jermini2010yield.md) | downy mildew | compensation, carbohydrate reserves, reserve mobilisation, … | Switzerland, Cadenazzo (Ticino) | A measured site dataset of reserve starch and sugars and of severity under downy mildew defoliation, usable a… |
| [ji2021coniella](ji2021coniella.md) | white rot | infection, incubation | Emilia-Romagna | White rot infection; incubation by Magarey's f(T) |
| [ji2021ripe](ji2021ripe.md) | ripe rot | infection, sporulation | China, Japan, United States | A ripe rot model on 19 epidemics |
| [ji2024coniella](ji2024coniella.md) | white rot | latency, sporulation | Emilia-Romagna | White rot latency and sporulation |
| [juroszek2015](juroszek2015.md) | many, incl. downy mildew | climate change projections | global | Context for climate scenarios |
| [kabela2006](kabela2006.md) | none | dew, leaf wetness | Iowa | Clear |
| [kabela2009](kabela2009.md) | none | dew, leaf wetness | Iowa | Clear |
| [kanaley2024](kanaley2024.md) | downy mildew | remote sensing, detection | New York | Clear |
| [kandilli2022](kandilli2022.md) | downy mildew, powdery mildew | climate indices, winkler index, season severity, phenology,… | Yalova Turkey, Marmara region | A field scoring of downy and powdery mildew on 12 cultivars under natural infection and four sprays, useful a… |
| [kang2025](kang2025.md) | none | image analysis | greenhouse | Off-topic |
| [kast1993](kast1993.md) | downy mildew | sporangia survival, dispersal | Württemberg | Infective sporangia caught when Bläser-based devices said none survived |
| [kast2006](kast2006.md) | downy mildew, powdery mildew | season severity | Württemberg | 43 seasons of severity at one site |
| [kast2010](kast2010.md) | powdery mildew | spray timing | Württemberg | OiDiag-2.2's equations |
| [kast2010window](kast2010window.md) | powdery mildew | spray timing, fungicide efficacy, ontogenetic resistance, s… | Weinsberg, Württemberg, Germany | A ten-year field record that the spray-timing window around flowering matters more than the number of sprays,… |
| [keil2006](keil2006.md) | downy mildew | infection severity | Baden | Severity by temperature and wetness; algorithm not printed |
| [keil2007](keil2007.md) | downy mildew | infection, sporulation, survival | Baden-Württemberg | Infection by 5-30 °C x 1-23 h, independent of Blaeser & Weltzien; sun kills slowly |
| [kennelly2005](kennelly2005.md) | downy mildew | host susceptibility, ontogenic resistance | New York, South Australia | The engine's window is not what the paper found for berries |
| [kennelly2006](kennelly2006.md) | downy mildew | trigger, susceptibility, survival | New York, South Australia | The engine's trigger tuned on 15 Chancellor seasons |
| [kennelly2007](kennelly2007.md) | downy mildew | sporangia survival, lesion productivity, oospores, trigger | New York, South Australia | no sporangia viable after 6-8 h of clear dry days; the engine's trigger; lesion decline per event |
| [kennelly2007php](kennelly2007php.md) | downy mildew | trigger, lesions, sporangia, fruit | New York | the engine's trigger and bunch window; field sporangia survival |
| [kerkech2019](kerkech2019.md) | downy mildew, esca, flavescence doree | symptom detection, image registration, segmentation, diseas… | France, Centre-Val de Loire | A labelled UAV symptom map from one summer, two plots, with no weather or infection dates: it could check a t… |
| [khaliq2019](khaliq2019.md) | none | remote sensing | Serralunga d'Alba, Piedmont | Inter-row pixels bias satellite vigour maps |
| [kim2002](kim2002.md) | none | leaf wetness | Iowa, Nebraska | Held out by structure |
| [kim2006](kim2006.md) | none | leaf wetness, forecasting | Iowa, Illinois | Forecast-driven wetness was biased low for every model it ran (its error tables) |
| [kim2007nzpp](kim2007nzpp.md) | grey mould | infection risk, weather interpolation | New Zealand | Bacchus as first printed: c = 0.1856, no reciprocal |
| [kleb2026](kleb2026.md) | downy mildew | infection, microclimate | Württemberg | Canopy sensors beat a border station and a network station |
| [knipper2019](knipper2019.md) | none | evapotranspiration, remote sensing | California | Clear |
| [kolbl2023](kolbl2023.md) | downy mildew | inoculation, sporulation, detection, incubation, leaf wetne… | Germany, Geisenheim | A small greenhouse dataset (one cultivar, one 17-day campaign) that gives observed detection timing for downy… |
| [koledenkova2022](koledenkova2022.md) | downy mildew | review | global | Review; context |
| [kontogiannis2024](kontogiannis2024.md) | downy mildew | forecasting | Greece | Prints a variant of EPI and DMCast's maturity curve; labels simulated |
| [koopman2007](koopman2007.md) | downy mildew | epidemic structure, overwintering | Western Cape | new genotypes all season (12-74 %); one or two clones dominate; ten genotypes survive the winter |
| [kortekamp1998](kortekamp1998.md) | downy mildew | host resistance | Palatinate | Resistance acts 3-4 days after infection |
| [kortekamp2005](kortekamp2005.md) | downy mildew | staining, histochemistry, infection structures, haustoria, … | Germany, Stuttgart | None. Recorded so that it is not read again, except that its carboxyfluorescein viability method (Sergeeva et… |
| [kowalczyk2006](kowalczyk2006.md) | none | evapotranspiration, canopy microclimate | Offline sites: Tharandt | A two-leaf canopy with in-canopy temperature and humidity, but no printed wet-canopy… |
| [kraus2021](kraus2021.md) | downy mildew, powdery mildew, grey mould | infection, sporulation, zoospore behaviour, germination, le… | Germany (Rhineland-Palatinate Siebeldingen), Ugan… | For a downy mildew truth, it offers one observed 2021 season (two vineyards, infection and severity at three … |
| [kremheller1983](kremheller1983.md) | hop downy mildew | forecasting, airborne inoculum | Bavaria | A spore-count threshold forecast for hops |
| [krzyzaniak2018](krzyzaniak2018.md) | downy mildew | infection, sporulation, spray timing, season severity, leaf… | France | None. Recorded so that it is not read again. |
| [kudinha2014](kudinha2014.md) | none | leaf wetness, canopy microclimate | Western Cape | Clear |
| [kumasoglu2022](kumasoglu2022.md) | downy mildew | host resistance, sporulation | Turkey | Resistant genotypes' infection counts |
| [kunova2021](kunova2021.md) | powdery mildew | fungicide resistance | general | Context for a future spray module (M4) |
| [lafond2010](lafond2010.md) | downy mildew | season severity, infection, primary infection, spray timing… | France, Loire Valley, Anjou, Saumur | A field test of whether soil-based intrinsic sensitivity classes explain downy mildew severity, which the tru… |
| [lakatos2022](lakatos2022.md) | downy mildew, powdery mildew, black rot, grapevine trunk disease | season severity, drought, yield, climate projection, spray … | Hungary | None for the truth or the engine beyond a citable, uncomputed remark that downy mildew follows rainfall (l. 2… |
| [lalancette1988infection](lalancette1988infection.md) | downy mildew | infection | Ohio | No longer kin to the engine under D27 |
| [lalancette1988sporulation](lalancette1988sporulation.md) | downy mildew | sporulation | Ohio | Kin, and rightly so, under D27 too |
| [lan2003](lan2003.md) | peach scab | dispersal | Georgia (USA) | Splash and runoff, not dew or air, carried infection (rain shields cut severity most) |
| [langcake1980](langcake1980.md) | downy mildew | infection, zoospore release, germ tube, haustorium, sporula… | United Kingdom | A 1980 laboratory record of the infection stages, with a first haustorium at 3.5 h and sporulation at about 9… |
| [larochepinel2021](larochepinel2021.md) | none | water status, remote sensing | Occitanie | Water status, not disease |
| [latinovic2010](latinovic2010.md) | downy mildew | fungicide efficacy, spray timing, season severity, yield lo… | Podgorica Montenegro, Montenegro | Observed 2009 leaf severity and per-vine yield under seven fungicide sprays in Montenegro, usable as a datase… |
| [latorre2018](latorre2018.md) | oomycetes, various | fungicide regulation | European Union | Context for a spray module |
| [lau2000](lau2000.md) | none | wetness sensing, sensor error | Iowa | Clear |
| [laviola1986](laviola1986.md) | downy mildew | oospore germination | Sicily | Inferred data behind Rossi 2008's germination time |
| [laviola2006](laviola2006.md) | downy mildew | laboratory storage | Sicily | Laboratory method only |
| [law2012](law2012.md) | none | land surface model | Australia | Planning document |
| [lebeda1994](lebeda1994.md) | downy mildews | review | global | Review; context |
| [legler2010](legler2010.md) | powdery mildew | ascospore release, infection, conidia, sporulation, leaf we… | Italy, California, Germany, Chile, Quebec | A review of powdery mildew models that writes out the UC Davis index's rules (l. 196-215), which the truth mu… |
| [lehoczky1965](lehoczky1965.md) | downy mildew | oospores, sporulation, infection, incubation, leaf wetness | Hungary | Summer oospore formation in leaf-disc culture without a cold period is a counter-observation to the winter-ma… |
| [leoni2026](leoni2026.md) | downy mildew | oospore maturation | Switzerland | The engine's GLM; coefficients recorded; fitted and scored on the same data |
| [lepik1931](lepik1931.md) | downy mildew | host resistance | Estonia | Historical anatomy |
| [leroy2010](leroy2010.md) | downy mildew, powdery mildew | economics | Bordeaux | A bio-economic model of strategies |
| [lindau1908](lindau1908.md) | downy mildew | distribution | South Africa | Historical arrival at the Cape |
| [liu2026robot](liu2026robot.md) | downy mildew, grapevine leafroll | detection, scouting | New York, California | Clear, and the closest thing to a rover operator's numbers |
| [liu2026tarag](liu2026tarag.md) | none | decision support | China | Off-topic |
| [lixandru2021](lixandru2021.md) | downy mildew, grey mould | infection, primary infection, season severity, fertilisatio… | Romania, Giurgiu County (Hotarele), Muntenia | None. Recorded so that it is not read again: a single-season fertiliser trial with no spray schedule, conflic… |
| [locci1969](locci1969.md) | downy mildew | infection anatomy | Lombardy | Morphology only |
| [locci1974](locci1974.md) | powdery mildew | infection anatomy | Lombardy | Morphology only |
| [lopezfrias2009](lopezfrias2009.md) | downy mildew | incubation, validation | Canary Islands | Prints the engine's Goidanich table, identical row for row |
| [lu2020](lu2020.md) | powdery mildew | infection, latent period | Quebec | Clear by every recorded link, and a flag-free candidate for powdery mildew pieces, if… |
| [lukas2016](lukas2016.md) | downy mildew | fungicide efficacy | South Tyrol | Stop-spray efficacy |
| [lulu2008spatial](lulu2008spatial.md) | none | leaf wetness | São Paulo | Wetness across a canopy, against turf |
| [lulu2008thesis](lulu2008thesis.md) | downy mildew | leaf wetness, season severity | São Paulo | Wetness models and downy mildew under six pruning dates |
| [lulu2008turf](lulu2008turf.md) | none | leaf wetness | São Paulo | RH > 90 %, dew point, CART and Penman-Monteith in a vineyard |
| [luo2001](luo2001.md) | brown rot (Monilinia) | latent infection, host susceptibility | California | Clear |
| [maclean2021](maclean2021.md) | none | canopy microclimate, leaf temperature | global | Clear |
| [maddalena2020](maddalena2020.md) | downy mildew | population genetics | Italy | Population genetics |
| [maddalena2021](maddalena2021.md) | downy mildew | oospores | Veneto | Four seasons of field oospore germination with station weather |
| [maddalena2022](maddalena2022.md) | downy mildew | oospore germination, primary infection | Lombardy | Kin by calibration, not by its authors (Agrarium's candidates |
| [maddalena2023](maddalena2023.md) | downy mildew, powdery mildew | forecasting, validation | Tuscany | EPI in nine organic vineyards; infection dates counted back with Goidanich |
| [maddalena2024](maddalena2024.md) | downy mildew | oospore germination, forecasting | Lombardy | The Franciacorta study over 2021-2023 (abstract) |
| [madden2000](madden2000.md) | downy mildew | infection, sporulation | Ohio | Kin, now for substantive reasons |
| [madden2018](madden2018.md) | none | sampling, spatial heterogeneity | global | Field heterogeneity across about 40 pathosystems (slopes 0.87-2.00, 80% between 1.06… |
| [madden2024glmm](madden2024glmm.md) | none | statistics | general | A statistics tutorial |
| [magarey1991](magarey1991.md) | downy mildew | incubation and more | South Australia | incubation cubic fitted to Müller, Zachos and Rafaila |
| [magarey2001](magarey2001.md) | none | virtual weather stations, interpolation error | United States | Errors of virtual stations (daily mean temperature within 0.2 °C at best |
| [magarey2005](magarey2005.md) | many | infection | general | the generic infection model; its grape rows' data |
| [magarey2007](magarey2007.md) | none | risk mapping | United States | Templates for Magarey's generic infection model, described without equations |
| [magarey2010](magarey2010.md) | downy mildew, powdery mildew | primary infection, secondary infection, infection, incubati… | Australia, Hunter Valley, inland regions of Austr… | The source of the engine's magarey2010.rules (10:10:24, sporulation, infection), so a truth that holds those … |
| [magarey2010b](magarey2010b.md) | powdery mildew | season severity, spray timing, fungicide use, inoculum, ove… | South Australia, Riverland, Australia, New York | None. Recorded so that it is not read again. |
| [magarey2010c](magarey2010c.md) | powdery mildew | spray timing, spray number, disease rating, irrigation, spr… | Riverland South Australia, Australia | A powdery-mildew spray-diary study, not a downy-mildew source; its irrigation table and spray-count benchmark… |
| [magarey2010dispersal](magarey2010dispersal.md) | downy mildew | dispersal | South Australia | A measured gradient from one source: 43 % at 8 m, 12 % at 20 m |
| [magyar2017](magyar2017.md) | downy mildew, apple scab, powdery mildew, brown rot, tomato late blight, phoma leaf spot, fusarium, leaf spot of beet, grey mould | spore trapping, airborne inoculum, primary infection, secon… | Hungary, Poland, Spain, Italy, England (Rothamste… | The one useful pointer is ref 31: a spore-trap downy mildew predictor built on the Goidanich index, to be che… |
| [maillet2022](maillet2022.md) | downy mildew | detection, remote sensing | Loire | Labels are months; not usable |
| [malviya2022](malviya2022.md) | powdery mildew | biocontrol efficacy | India | Product efficacy trials |
| [marchal1897](marchal1897.md) | downy mildew | distribution | Belgium | Historical note |
| [marciano2023](marciano2023.md) | downy mildew | nitrogen nutrition, susceptibility, sporulation, leaf nitro… | Italy | A greenhouse and lab study of N effects on sporulation, with no field, weather or model content: a source for… |
| [marko2026](marko2026.md) | downy mildew, powdery mildew | disease occurrence | Hungary | Grower-survey effect sizes from Hungary |
| [maronefassolo2022](maronefassolo2022.md) | downy mildew | latent period, host resistance | northern Italy | Latent period about 6 days at 22 °C across 72 isolates |
| [martin2005](martin2005.md) | powdery mildew | fungicide efficacy | Spain | Control only |
| [martre2014](martre2014.md) | none | crop growth | global | Off-topic, though its finding (an ensemble mean beats single models) is the argument… |
| [massi2021](massi2021.md) | downy mildew | fungicide resistance | general | Review |
| [massi2022](massi2022.md) | downy mildew | infection efficiency | Italy | About 8% of single sporangia infected on leaf discs at 22 °C |
| [masson2011](masson2011.md) | none (climate models) | model dependence | global | why dependence is judged by components and behaviour |
| [matasci2010](matasci2010.md) | downy mildew | epidemic development, incidence, severity, cultivar mixture… | Switzerland, Ticino | A small observed incidence-and-severity dataset on cultivar mixtures that the truth could use as a cultivar-s… |
| [mecikalski2004alexi](mecikalski2004alexi.md) | none | evapotranspiration | United States | Methods in words |
| [meggio2008](meggio2008.md) | none | remote sensing | Ribera del Duero | Viewing geometry alters vineyard reflectance |
| [menesatti2013](menesatti2013.md) | downy mildew | forecasting, spray timing | Lazio | PLS-DA on a Goidanich predictor; targets cut from its own data |
| [menezes2024](menezes2024.md) | none | microclimate | Douro | Tree shade simulated, not validated |
| [metos2026](metos2026.md) | downy mildew, powdery mildew, black rot, grey mould | sporulation, risk index | general | iMETOS/FieldClimate rules: no data behind them; a comparator, not a truth |
| [mezei2022](mezei2022.md) | downy mildew | warning system, incubation | Serbia | 3-10 trigger; incubation fitted to Miller's table |
| [mijailovic2022](mijailovic2022.md) | downy mildew | spray timing, infection, sporulation, sporangia germination… | laboratory (in vitro France) | None for the engine or the truth's field processes: it is a laboratory efficacy test of a biocontrol product,… |
| [miles2018](miles2018.md) | downy mildews | detection | USA | Detection methods review |
| [miller1952](miller1952.md) | downy mildew, others | forecasting history | global | History of incubation calendars and rules |
| [molitor2009](molitor2009.md) | black rot | biology, control | northern German wine regions | None from this page; the dissertation body, which is not in the folder, would hold the Spotts-modified black-… |
| [molitor2014](molitor2014.md) | none | phenology | Germany, Austria | The engine's model |
| [molitor2016](molitor2016.md) | black rot | infection, incubation | Europe, United States | VitiMeteo black rot, documented |
| [molitor2020](molitor2020.md) | Botrytis bunch rot, downy mildew | phenology, season severity | Luxembourg, Germany | UniPhen and BotRisk are kin by a borrowed equation (the engine's degree-day function),… |
| [monteiro2012](monteiro2012.md) | downy mildew | infection, sporulation, climate change | Rio Grande do Sul | Lalancette copied with misprints; RH ≥ 90 % as wetness |
| [monteiro2015](monteiro2015.md) | downy mildew | infection, climatic risk | Brazil | Lalancette copied with misprints; model output only |
| [monteiro2015bol](monteiro2015bol.md) | downy mildew, grey mould | infection, climatic risk | Brazil | Prints Broome's coefficients as the engine has them |
| [monteiro2015podridao](monteiro2015podridao.md) | grey mould | infection, climatic risk | Brazil | Broome's coefficients again, as the engine has them |
| [moral2012infection](moral2012infection.md) | olive anthracnose | infection, latent period | Andalusia | Kin by a borrowed equation (Magarey's), for another host |
| [moral2012inoculum](moral2012inoculum.md) | olive anthracnose | sporulation, epidemic progress | Andalusia | Kin through the temperature function it shares with Magarey's model |
| [morelli2026](morelli2026.md) | downy mildew, powdery mildew, grapevine pests (european grapevine moth) | integrated pest management, decision support, forecasting, … | Italy, Europe, North America, Oceania, China, Sou… | None. Recorded so that it is not read again (a survey of apps, with no formulation, observed dataset or model… |
| [mouafo2022](mouafo2022.md) | downy mildew | clade competition | Quebec | little for Europe |
| [moyer2010](moyer2010.md) | powdery mildew | low temperature | New York | Leaves 4-8 °C below air on clear nights |
| [moyer2016](moyer2016.md) | powdery mildew | season severity | New York | A flag now, not kin |
| [muangprathub2019](muangprathub2019.md) | none | irrigation, sensing | Thailand | Off-topic |
| [mucalo2024](mucalo2024.md) | downy mildew, powdery mildew, botrytis, pests (phylloxera moths leafhoppers) | satellite monitoring, vegetation indices, prescription maps… | Europe, EU, France, Croatia, Italy, Spain | None. Recorded so that it is not read again (a satellite review; its only downy mildew content is background,… |
| [muth1916](muth1916.md) | downy mildew | infection, spray timing | Rheinhessen | History; qualitative |
| [naud2010](naud2010.md) | downy mildew, powdery mildew | spray timing, decision rule, plot survey, season severity, … | France, Bordeaux, South-West France, South-East F… | A field-tested decision workflow with observed farm records for 2008-2009 (severities, spray counts, grower j… |
| [negrel2018](negrel2018.md) | downy mildew | infection, early infection, lipid markers, sporulation, res… | France | Lipid markers rise by 24 h after inoculation, so they could serve as an early pathogen-biomass check for a tr… |
| [niimi2018](niimi2018.md) | none | wine quality | South Australia | Off-topic |
| [ninyerola2005](ninyerola2005.md) | none | climatology | Iberian Peninsula | Mean climate surfaces at about 200 m from regression and residual interpolation |
| [nityagovsky2025](nityagovsky2025.md) | downy mildew | detection | Russian Far East | A detection method from the Russian Far East |
| [nogueirajunior2016](nogueirajunior2016.md) | downy mildew, grapevine rust | photosynthesis, biomass allocation, yield loss, sporulation… | Brazil (Piracicaba São Paulo) | Offers the truth a field dataset of disease effects on vine biomass and gas exchange for a Brazilian cultivar… |
| [nogueirajunior2020](nogueirajunior2020.md) | downy mildew | photosynthesis, stomatal conductance, infection, sporulatio… | Brazil (authors' institutes), greenhouse Germany … | None for the truth or the engine's models: it is a greenhouse photosynthesis and induced-resistance study wit… |
| [oerke2016](oerke2016.md) | downy mildew | detection | Palatinate | Reflectance changes 1-2 days before sporulation |
| [oficiulfitosanitararges2023](oficiulfitosanitararges2023.md) | downy mildew, powdery mildew, grey mould, black rot, black spot | spray timing, treatment window, incubation, oil spot stage,… | Romania (Argeș county) | None. Recorded so that it is not read again: a regional warning bulletin with no model, weather input or infe… |
| [oficiulfitosanitarcalarasi2025](oficiulfitosanitarcalarasi2025.md) | downy mildew, powdery mildew, grey mould | spray timing, infection, berry wetness, overwintering | Călărași Romania, Romania | None. Recorded so that it is not read again. |
| [onofre2020](onofre2020.md) | none | wetness sensing | Florida | The usual faults of wetness sensors (height, angle, orientation, coating) |
| [orlandini1993](orlandini1993.md) | downy mildew | infection, incubation, survival, validation | Tuscany | PLASMO with fitted n and m; every piece kin to the engine by data or form |
| [orlandini1998](orlandini1998.md) | downy mildew | photosynthesis, gas exchange, stomatal conductance, transpi… | Italy, Tuscany, Mondeggi (Bagno a Ripoli) | A measured link between downy mildew disease share and leaf gas exchange in vines, which the truth could use … |
| [orlandini2003](orlandini2003.md) | downy mildew | disease severity, model evaluation | Tuscany | A fuzzy-logic PLASMO; prints no equations |
| [orlandini2008](orlandini2008.md) | downy mildew | survival, sporulation, infection, incubation | Tuscany | PLASMO's later form: bounds printed, coefficients not; kin in every process |
| [orth1937](orth1937.md) | potato late blight | sporangia survival | Germany | Another oomycete; humidity and sporangia |
| [padro2019](padro2019.md) | none | remote sensing | Catalonia | Positional error of UAV images by method (raw GNSS about 1 m |
| [pak2008cable](pak2008cable.md) | none | land surface model | Australia | Slides only (OCR) |
| [palfi2022](palfi2022.md) | powdery mildew, grape powdery mildew (gpm), downy mildew (mentioned only) | spray timing, season severity, gas exchange, yield, phytoto… | Hungary, Eger, Eger wine region | None. Recorded so that it is not read again. |
| [parker2011](parker2011.md) | none | phenology | France, Switzerland | Held out by structure (a degree-day forcing sum, the engine's form), as before |
| [pdmildew2006](pdmildew2006.md) | downy mildew, powdery mildew | proceedings: epidemiology, models, control | Europe, Australia, North America | Chapter notes for the epidemiology papers |
| [peddicord2025](peddicord2025.md) | northern leaf blight, gray leaf spot | risk prediction | US Midwest | Uses a CART-style wetness tree (after Kim et al.) and RH >= 90% disease units |
| [peng2024](peng2024.md) | downy mildew | review | global | Review; context |
| [peng2025](peng2025.md) | none | animal science | China | Off-topic |
| [perazzolli2020](perazzolli2020.md) | downy mildew, powdery mildew | phyllosphere microbiota, rare sugar treatment, tagatose, di… | Trentino, San Michele all'Adige, northern Italy | Offers a field downy mildew severity record for a biocontrol (tagatose, 8 g/l, two vineyards, 2014) that the … |
| [pereira2018](pereira2018.md) | downy mildew | season severity | Paraná | Double cropping: one crop escapes, one has an epidemic |
| [perezexposito2017](perezexposito2017.md) | downy mildew, powdery mildew, grey mould, black rot, phylloxera, excoriose | infection, spray timing, primary infection, secondary infec… | Spain, Galicia, Ribeira Sacra, Italy, France, New… | The truth must not share the Goidanich table or the 3-10 rule that this system runs (l. 204, l. 332), and its… |
| [perrone2017](perrone2017.md) | grapevine viruses | host-virus interaction | Mediterranean | Off-topic |
| [pertot2007](pertot2007.md) | downy mildew | oospores, primary infection, secondary infection, incubatio… | Trentino, Italy, Bommes (Bordeaux France), Navice… | It reproduces the engine-list Goidanich incubation table and the Blaeser wetness form, and gives observed gen… |
| [pertot2016](pertot2016.md) | downy mildew, powdery mildew, grey mould, black rot, esca, grapevine trunk diseases | oospores, primary infection, secondary infection, spray tim… | Italy, France, Switzerland, Quebec, Germany, Aust… | A review that reports the engine-list primary model (Rossi et al. 2008) and the 3-10 rule as used by other DS… |
| [pesquer2014](pesquer2014.md) | none | interpolation error | Catalonia, Spain | Interpolation error of Catalan precipitation by how stations are split |
| [pezzotti2020](pezzotti2020.md) | downy mildew, powdery mildew | sporangia, sporangia viability, zoospore release, infection… | Italy, Japan, USA | None. Recorded so that it is not read again. |
| [piemontemodelli](piemontemodelli.md) | downy mildew, powdery mildew, apple scab, black rot, grey mould, late blight, rice blast, grape berry moth, fruit moths, thrips, scaphoideus titanus | primary infection, secondary infection, oospores, sporulati… | Emilia-Romagna, Italy, Switzerland, Germany | A pointer list: it names the grapevine models a regional service uses (Rossi 2008, VitiMeteo, Magarey 2005, K… |
| [pii2024](pii2024.md) | downy mildew, powdery mildew | fungicide residues, leaf wetness, season severity, remote s… | Italy, France, Brazil | None for the truth's disease process; its one downy mildew item is an optical-sensing diagnosis (Calcante et … |
| [pobleteecheverria2025](pobleteecheverria2025.md) | downy mildew | symptom detection, canopy imaging, deep learning, leaf coun… | Spain, La Rioja, Basque Country | A vision-based symptom detector with a labelled canopy dataset from northern Spain; it offers an observation … |
| [poeydebat2025](poeydebat2025.md) | downy mildew | oospores in soil, spatial structure | Bordeaux | 15 m patches (Matérn range 15.8 m); fivefold row contrast |
| [pokovai2025](pokovai2025.md) | none | remote sensing | Hungary | Off-topic |
| [prillieux1883](prillieux1883.md) | downy mildew | oospores, germination, overwintering, primary infection | France (Nérac) | Offers the truth a dated 1883 observation that oospores germinate by a germ tube, which supports the spring-i… |
| [prillieux1887](prillieux1887.md) | downy mildew | oospores, soil infection, germination, primary infection, o… | France, Indre-et-Loire, Isère valley, Gard, Neufc… | None. Recorded so that it is not read again. |
| [prodorutti2006](prodorutti2006.md) | downy mildew | oospore germination | Trentino | Seven seasons of germination delay |
| [puelles2020](puelles2020.md) | downy mildew | spray timing | La Rioja | A bachelor's thesis with the UR model's first rules |
| [puelles2024](puelles2024.md) | downy mildew | oospores, infection, sporulation, validation | La Rioja | The engine's UR rules: Goidanich plus the 3-10 rule, Gehmann's oospores, 50 °C·h |
| [puopolo2014](puopolo2014.md) | downy mildew, late blight | sporangia viability, anti-oomycete activity, culture filtra… | Italy, Trentino | None for the truth or the engine: the paper reports lab and greenhouse efficacy of a bacterial metabolite on … |
| [puopolo2014b](puopolo2014b.md) | downy mildew | copper resistance, biocontrol, copper reduction, phyllosphe… | Italy (Trentino San Michele all'Adige), greenhouse | None for the truth or the engine: a bacterial biocontrol greenhouse study whose copper figures (375 to 93.75 … |
| [qiu2015](qiu2015.md) | powdery mildew | host resistance | general | Host genetics review |
| [rafaila1968](rafaila1968.md) | downy mildew | incubation | Romania | an incubation independent of Goidanich's data |
| [raynal2010](raynal2010.md) | downy mildew | rainfall | Bordeaux | Radar rain differs from stations by tens of mm |
| [raynal2010epicure](raynal2010epicure.md) | downy mildew, powdery mildew, hail damage | forecasting, rainfall, radar, hail detection, sample survey… | Bordeaux, Gironde, Dordogne, Blayais, Cognac | Offers the truth a fine-scale observed hail and damage dataset and a reason to vary rain within a region (rad… |
| [redeacores2024](redeacores2024.md) | downy mildew | infection, oospores, primary infection, spray timing, seaso… | Azores Portugal | A field-scouting protocol and a statement of the 3-10 rule; the rule is on the engine's listed set, so the tr… |
| [redeacores2025](redeacores2025.md) | downy mildew | primary infection, secondary infection, leaf wetness, spray… | Azores, Portugal | A field-scoring protocol (organ and plot scales, sampling design) for the observation operator of a downy mil… |
| [regionelazio2024](regionelazio2024.md) | downy mildew | primary infection, secondary infection, incubation, oospore… | Lazio Italy, Italy | A regional advisory: the 3-10 rule, called superseded, is on the engine's list, so the truth must not take it… |
| [reinehr2021](reinehr2021.md) | downy mildew, grey mould | season severity, host vigour | Santa Catarina | Less vigour, less downy mildew; no untreated plot |
| [reis2013](reis2013.md) | downy mildew | spray timing, validation | Rio Grande do Sul | A Lalancette-based trigger; three seasons of untreated AUDPC |
| [reis2020](reis2020.md) | none | phenology | Portugal | Held out by structure, read strictly (Agrarium's candidates) |
| [rienth2019](rienth2019.md) | downy mildew | infection, spray timing, leaf wetness | Switzerland | None. Recorded so that it is not read again. |
| [rienth2021](rienth2021.md) | downy mildew, powdery mildew, grey mould, grapevine fanleaf virus, grapevine leafroll virus, grapevine red blotch virus | season severity, infection, ontogenic resistance, sporulati… | Burgundy (cited model study), Europe, wine-growin… | None beyond leads: its cited Bove et al. 2020 DM simulation and Kennelly et al. 2005 ontogenic-resistance pap… |
| [roberts2017](roberts2017.md) | none | statistics | general | Block cross-validation for structured data |
| [rodrigues2019](rodrigues2019.md) | downy mildew, grey mould | infection, climatic risk | Espírito Santo | Lalancette and Broome copied with misprints |
| [rodrigues2026](rodrigues2026.md) | downy mildew | infection, spread, spray timing | Rio Grande do Sul | A compartment model on powdery mildew's parameters; no data |
| [rodriguezdeacunaypego2011](rodriguezdeacunaypego2011.md) | downy mildew | infection, oospores, incubation, spray timing, leaf wetness… | Tenerife, Canary Islands, Spain | It states the engine's 3-10 rule and a wetness threshold as local practice in Tenerife; a description, not a … |
| [romanazzi2024](romanazzi2024.md) | downy mildew | season severity, organic control | Marche | Seven vineyard-years of untreated incidence on the Adriatic |
| [ronzon1987](ronzon1987.md) | downy mildew | oospores, forecasting | Bordeaux | EPI printed in full; POM's thesis fit rests on 1985-86 |
| [rosa1993](rosa1993.md) | downy mildew | infection, incubation, survival | Tuscany | PLASMO's first equations; incubation fitted to Goidanich's table, so kin |
| [rosa1995](rosa1995.md) | downy mildew | incubation, spray timing | Tuscany | PLASMO 2.11's incubation, fully printed (m = 0.082); kin by Goidanich and Zachos |
| [rose2016](rose2016.md) | none | decision support | England and Wales | Why farmers use or ignore decision tools |
| [rossi2002](rossi2002.md) | downy mildew | incubation, primary infection | Emilia-Romagna | Rossi 2008's incubation regressions, fitted to Goidanich's data as stated |
| [rossi2005](rossi2005.md) | downy mildew | primary infection, incubation | northern Italy | Does not say what the incubation regressions were fitted to |
| [rossi2006](rossi2006.md) | downy mildew | primary infection model | Italy | No equations; does not settle the incubation's data |
| [rossi2008](rossi2008.md) | downy mildew | primary infection, incubation | Italy | incubation eqs 8-9 from Rossi et al. 2002, fitted to Goidanich's data |
| [rossi2010](rossi2010.md) | powdery mildew | ascospore maturation, ascospore release | Piacenza | A flag, not kin |
| [rossi2012](rossi2012.md) | downy mildew | splash dispersal, primary infection | Emilia-Romagna | Its splash data (4.4 drops/cm² at 40 cm, 0.03 at 80 cm, 0.003 at 140 cm |
| [rossi2013](rossi2013.md) | downy mildew | epidemic structure | Europe | Gobbin's genotype patterns, for history matching |
| [rossi2025](rossi2025.md) | downy mildew | host susceptibility, spray efficacy | Piacenza | Efficacy rises with cluster stage, interacting with ontogenic resistance |
| [rotem1969](rotem1969.md) | many | irrigation | Israel | drip adds no leaf wetness; sprinkling does |
| [roubal2013](roubal2013.md) | olive scab | infection, latent period | Provence | Held out by structure through its RH-threshold wetness (Agrarium's candidates) |
| [rouxel2014](rouxel2014.md) | downy mildew | population genetics | Eastern North America | Population genetics |
| [rouzet2003](rouzet2003.md) | downy mildew | oospore maturation, season severity | France | The 60 cold days start a correlation window, not maturation |
| [rowlandson2015](rowlandson2015.md) | none | leaf wetness, sensors | general | The review behind the wetness definitions Agrarium uses |
| [rumbou2004](rumbou2004.md) | downy mildew | epidemic structure, oospores, season severity | Greece | one clone 72-92 %; a drier 2002 worse after a heavier 2001: the previous year's inoculum |
| [ruralcatmildiu](ruralcatmildiu.md) | downy mildew | copper use, alternative fungicides, primary infection, seco… | Catalonia, Spain, Falset | Gives the truth a practitioner's rule set and timing (10:10:24, four stages, 10 mm wash-off) for Catalan orga… |
| [ryu2024](ryu2024.md) | none | interpolation error | Jeju Island, South Korea | Interpolation error of 10-min temperature with IoT stations (MAE about 0.7 °C) |
| [sagar2023](sagar2023.md) | powdery mildew | conidial germination | Karnataka | Inconsistent tables; not usable |
| [sajo1901](sajo1901.md) | downy mildew, powdery mildew | season severity | Hungary | Historical season comparison |
| [salazargutierrez2016](salazargutierrez2016.md) | none | phenology, dormancy | Washington | Held out by structure |
| [salcedo2021](salcedo2021.md) | downy mildews | detection | USA, global | Detection methods review |
| [salinari2007](salinari2007.md) | downy mildew | season onset | Italy | a statistical onset model at one site |
| [salotti2022](salotti2022.md) | downy mildew, powdery mildew, black rot | host resistance | Emilia-Romagna | 16 unsprayed varieties over four seasons |
| [salotti2023](salotti2023.md) | anthracnose, ripe rot | infection, incubation | several | A Colletotrichum model by clade; Magarey's f(T) for incubation |
| [salotti2026](salotti2026.md) | alternaria disease complex, alternaria leaf spot, mycotoxin contamination | infection, sporulation, wetness duration, relative humidity… | Italy, India, Canada, Foggia Italy | A tomato Alternaria process model with a temperature-times-wetness infection rate, of the form the brief list… |
| [sanna2014](sanna2014.md) | downy mildew | forecasting, measurement | Italy | Sensor calibration moves EPI's start by 7-12 days |
| [sanna2017](sanna2017.md) | downy mildew | incubation, sensor uncertainty | Piedmont | Says the Rossi-group regressions were adapted to Goidanich's table |
| [sanna2018](sanna2018.md) | downy mildew | sensor error | Piedmont | Calibration shifts the forecast by up to 4 days |
| [sanna2019](sanna2019.md) | downy mildew | primary infection, secondary infection, incubation, germina… | Monferrato Piedmont North Italy | Gives the truth an observation design for sensor calibration and station siting, and a 5-day sensitivity of f… |
| [sanzablanedo2018](sanzablanedo2018.md) | none | photogrammetry | León (Spain) | Off-topic |
| [sarejanni1950reports](sarejanni1950reports.md) | downy mildew | season severity, oospores | Greece | 1952: abundant oospores, late-winter drought, no mildew |
| [sarejanni1951](sarejanni1951.md) | downy mildew | season severity, oospores, overwintering | Greece | Capus's winter-by-spring rain rule; preparatory years; Greek mildew years |
| [sawant2013](sawant2013.md) | grape anthracnose | climate change, temperature trend, minimum temperature, lea… | India, Solapur, Ludhiana, Pune | None. Recorded so that it is not read again: it is about anthracnose in India, not downy mildew, and its mons… |
| [schilder2010](schilder2010.md) | downy mildew, powdery mildew | fungicide efficacy, organic fungicides, spray timing, spray… | Michigan, Fennville | A field record of organic fungicide control, with incidence and severity per treatment for two Michigan seaso… |
| [schmidt2003](schmidt2003.md) | grape berry moths | pest demography | Rheingau | An insect model; for Cooptera's pests |
| [schnee2010](schnee2010.md) | powdery mildew | ontogenic resistance, sporulation, leaf age, host growth, v… | Bordeaux, Couhins, Latresne, France | Observed leaf-age and vigour effects on powdery mildew sporulation and leaf glucose at two sites and years: a… |
| [schuepp1986](schuepp1986.md) | downy mildew | laboratory method | Switzerland | Method only |
| [schulte1907](schulte1907.md) | downy mildew (falsche meltau blattfallkrankheit) | infection, leaf wetness, spray timing, spray deposit, coppe… | Kreuznach Rhineland-Palatinate Germany, Germany | None. Recorded so that it is not read again. |
| [scott2014](scott2014.md) | downy mildew, powdery mildew, botrytis bunch rot, black rot | forecasting, decision support, primary infection, fungicide… | Spain, Basque Country, Rioja Alavesa, Gipuzkoa, C… | A pointer only: its secondhand summary of VitiMeteo-Plasmopara's 11-year primary-infection record at Changins… |
| [sebela2012](sebela2012.md) | downy mildew | leaf wetness, sporulation, detection, symptom appearance, p… | Czech Republic, Lednice | A one-day field snapshot of 15 infected and 15 healthy leaves with pigment and fluorescence changes, with inf… |
| [sebela2014](sebela2014.md) | downy mildew | detection | Moravia | Optical indices for infected leaves |
| [sekulic2020](sekulic2020.md) | none | interpolation error | Synthetic fields | Interpolation accuracy for daily precipitation in Catalonia and temperature in Croatia |
| [sendhilvel2020](sendhilvel2020.md) | downy mildew | forecasting, spray timing | Tamil Nadu | A logistic schedule tested on the curve it came from |
| [sentelhas2004](sentelhas2004.md) | none | leaf wetness, sensors | Ontario, Sao Paulo | The wetness candidate D27 frees |
| [serrano2010](serrano2010.md) | downy mildew | fungicide dose, spray water quality, adjuvant, phosphite, e… | France, Gaillac (AOP), Tarn | Field efficacy data for a half-dose and adjuvant strategy against downy mildew in France, with a ratio-to-unt… |
| [shin2020](shin2020.md) | none | leaf wetness, remote sensing | South Korea | Kin by calibration (Agrarium's candidates) |
| [shishkoff2019](shishkoff2019.md) | impatiens downy mildew | oospore germination | eastern USA | A cold requirement for oospore germination |
| [skahill2024](skahill2024.md) | none | frost risk | Oregon | Off-topic for the disease truth |
| [skakun2022](skakun2022.md) | none | remote sensing, cloud masking | Global | Cloud masks miss thin cloud, and the scores depend on the reference set |
| [smith1892](smith1892.md) | downy mildews | cytology | France | Off-topic |
| [smith2010](smith2010.md) | powdery mildew | ontogenic resistance | Tasmania | Severity peaks at the sink-to-source leaf |
| [solla1906](solla1906.md) | downy mildew | host physiology | Italy | Off-topic |
| [spencerphillips2002](spencerphillips2002.md) | downy mildews | book: control, host biology, epidemiology | global | Mostly control; Vercesi's oospore data noted apart |
| [spie2019](spie2019.md) | none | remote sensing | United States | Front matter only |
| [spotts1977](spotts1977.md) | black rot | infection, leaf wetness | Ohio | Black rot wetness hours by temperature; the source of later tables |
| [srinivasan1976](srinivasan1976.md) | downy mildew | sporangia viability | Tamil Nadu | Day-produced sporangia, above 30 °C in sun, did not germinate |
| [srinivasan1976india](srinivasan1976india.md) | downy mildew | incubation, infection, leaf age, stomata, berry susceptibil… | Tamil Nadu India | Observed incubation, leaf-age and berry-stage data for a warm-climate cultivar; no model is computed here, an… |
| [stambuk2021](stambuk2021.md) | downy mildew, powdery mildew | infection, sporulation, resistance, cultivar susceptibility… | Croatia | Little for the truth or the engine: a leaf-disc susceptibility ranking of Croatian cultivars that could set a… |
| [steel2011](steel2011.md) | bunch rots | berry infection by temperature | New South Wales | two temperatures; points to Nair & Allen 1993 |
| [stefanini2022](stefanini2022.md) | downy mildew | spray decision | Tuscany | An elicited causal graph; no data |
| [steffenel2023](steffenel2023.md) | downy mildew | forecasting | Champagne | Classifiers trained on the 3-10 rule's labels |
| [steiger2010](steiger2010.md) | downy mildew, powdery mildew | fungicide use, crop protection cost, resistance management,… | Europe, global (twelve major countries per diseas… | Offers the truth only a cost frame (22 €/ha average downy protection; 2008 treated hectares), which a spray-e… |
| [stein1985](stein1985.md) | downy mildew, powdery mildew | host resistance | Palatinate | A resistance test |
| [stille1965](stille1965.md) | potato late blight | germination | Germany | Another oomycete |
| [stobwasser1956](stobwasser1956.md) | apple scab, downy mildew | spray application | Württemberg | Spray technology |
| [stojanova2026](stojanova2026.md) | downy mildew, powdery mildew | spray timing, season severity, leaf wetness, infection, spr… | Slovenia, Podravska region | The paper offers only an operational spray count from one vineyard and an unvalidated proposal to run a powde… |
| [sun2026](sun2026.md) | none | dormancy, phenology | Shanghai | Held out by structure if it drove a truth |
| [sutherland2010](sutherland2010.md) | powdery mildew | volatile organic compounds, detection, infection, sensor, e… | California, USA | None. Recorded so that it is not read again. |
| [syobu2022](syobu2022.md) | downy mildew | infection, sporulation, season severity, leaf wetness, incu… | Japan, Saga Prefecture | A dataset for onion, not grapevine: observed disease in three seasons with station weather (2016-2018) that a… |
| [taibi2023](taibi2023.md) | downy mildew, powdery mildew | spray timing | Emilia-Romagna | Uses the engine's Rossi-group models to time sprays |
| [taibi2023inducers](taibi2023inducers.md) | downy mildew, powdery mildew | infection, incubation, latent period, sporulation, sporangi… | Emilia-Romagna, Italy | Field data on the monocycle after PRI treatment, with observed latency and lesion counts for 2020-2022 at one… |
| [thiessen2018](thiessen2018.md) | powdery mildew | ascospore release | Oregon | The engine's record can become `read`, with initials L |
| [thind1988](thind1988.md) | downy mildew | laboratory method | Punjab | Method only |
| [thomidis2021](thomidis2021.md) | olive leaf spot | conidial germination, infection, leaf wetness, temperature … | Northern Greece, Chalkidiki, Potidea | Gives a Magarey-type infection response run on field data with a stated validation rule (predicted day agains… |
| [ticomaluquer2013](ticomaluquer2013.md) | downy mildew | infection, incubation, spray timing, season severity, leaf … | Catalonia, Penedès, Spain, Vilafranca, Sant Jaume… | A historic warning service whose daily incubation step (Bologna study, probably Goidanich 1957) is an engine-… |
| [toffolatti2006](toffolatti2006.md) | downy mildew | oospore germination, primary infection | Veneto | Primary inoculum to late May or early June |
| [toffolatti2024](toffolatti2024.md) | downy mildew | fungicide resistance | northern Italy | Resistance-allele monitoring in Italy |
| [tonle2024](tonle2024.md) | none | decision support | Africa | Off-topic |
| [tor2023](tor2023.md) | downy mildews | host-pathogen biology | global | Molecular review; context |
| [tranmanhsung1990](tranmanhsung1990.md) | downy mildew | oospore maturation, season severity | Bordeaux | Clear of the engine by every substantive test, and its author list is read |
| [twomey2015](twomey2015.md) | powdery mildew | infection, season severity, spray timing, latent period, sp… | Oregon, United States | None. Recorded so that it is not read again. |
| [urbeztorres2010](urbeztorres2010.md) | Botryosphaeria dieback | spore release, observation | California | Clear, and of indirect use |
| [valdesgomez2017](valdesgomez2017.md) | powdery mildew | scouting, spray decisions | Chile | A costed scouting policy (2-3 sprays against 7-9 |
| [valleggi2023](valleggi2023.md) | downy mildew | spray strategy, season severity | Tuscany | Three Chianti seasons of control-plot incidence |
| [valsesia2005](valsesia2005.md) | downy mildew | detection, observation | Switzerland, Trentino | Clear |
| [vazquezabal2019](vazquezabal2019.md) | downy mildew, black rot | infection, incubation | Galicia | Extension rules, all engine forms; Spotts's black rot table |
| [velasquezcamacho2023](velasquezcamacho2023.md) | downy mildew, powdery mildew | infection, oospores, spray timing, season severity, leaf we… | Italy, Quebec, Douro, New York State | It gives a map of the models the truth must not share with the engine: the 3–10 rule, Goidanich's table, and … |
| [velez2020](velez2020.md) | none | remote sensing | Greenhouse at Stellenbosch University, South Africa | NDVI falls about 0.3 per unit of lost leaf area |
| [vercesi2002](vercesi2002.md) | downy mildew | oospore germination, fungicide | Lombardy | Untreated oospores germinated most in late March |
| [veverka2009](veverka2009.md) | downy mildews | general | global | A book review only; the book is not held |
| [viret2010](viret2010.md) | downy mildew, grape berry moth, powdery mildew | infection, oospores, leaf wetness, spray timing, forecastin… | Switzerland, Germany | Describes the VitiMeteo model that the engine partly runs, but gives no oospore equation, so it cannot settle… |
| [viruega2011](viruega2011.md) | olive scab | infection, incubation | Andalusia | Not held out today |
| [viruega2013](viruega2013.md) | olive scab | inoculum production, dispersal | Andalusia | Clear |
| [volpi2021](volpi2021.md) | downy mildew, powdery mildew, grey mould | forecasting | Tuscany | Tuscany's IPM network, 2006-2019, behind tree classifiers |
| [wakehamnd](wakehamnd.md) | grey mould | bio-aerosol, inoculum availability, wind speed, relative hu… | United Kingdom | None. Recorded so that it is not read again: Botrytis aerobiology in UK tomato glasshouses, with no downy mil… |
| [watson2002](watson2002.md) | brown rot (Monilinia) | sporulation | South Carolina | Clear and of little use to a grape truth |
| [williams2024](williams2024.md) | none | remote sensing | England | Cover crop dominates the Sentinel-2 signal of a vineyard |
| [winkler1949](winkler1949.md) | none | viticulture | California | Off-topic |
| [winter1940](winter1940.md) | take-all | infection | Germany | Another disease |
| [wober1920](wober1920.md) | downy mildew | fungicide efficacy | Austria | History of fungicides |
| [wurz2021](wurz2021.md) | downy mildew, anthracnose | season severity, canopy density, bud load, incidence, sever… | Brazil, Santa Catarina, São Joaquim | Field incidence and severity by canopy density in a humid highland site, which gives a truth scenario the can… |
| [wurz2023](wurz2023.md) | downy mildew | season severity, host vigour | Santa Catarina | More buds, more downy mildew; no untreated plot |
| [yang2023](yang2023.md) | downy mildew | primary inoculum, latent infection | Ningxia | Clear |
| [yang2026](yang2026.md) | none | evapotranspiration | Contiguous United States | Cropland monthly error about 17% |
| [yin2018](yin2018.md) | none | drought | United States | Off-topic |
| [yu2022metabolomics](yu2022metabolomics.md) | powdery mildew | fruit chemistry | Guangxi | Off-topic for simulation |
| [yu2022shelter](yu2022shelter.md) | downy mildew | epidemic progress, canopy microclimate | Liaoning | Rain shelters cut leaf wetness and slowed epidemics (Shenyang) |
| [yuen2002](yuen2002.md) | none | warning scores | England, Sweden | Clear and a method |
| [zachos1959](zachos1959.md) | downy mildew | incubation, oospores, conidia | Greece | an incubation independent of Goidanich's data |
| [zaffaroni2022](zaffaroni2022.md) | downy mildew | sexual reproduction, oospores, dormancy, dispersal, resista… | general | A model framework only: it gives the truth a structural note (sexual spores persist in soil and reach the can… |
| [zanzotto2010](zanzotto2010.md) | downy mildew | season onset, season severity | Veneto | Eleven untreated seasons of first symptoms |
| [zapata2015](zapata2015.md) | none | phenology, dormancy | Washington | Held out by structure, as before |
| [zarcotejada2018](zarcotejada2018.md) | Xylella fastidiosa | remote sensing, detection | Puglia | Pre-visual detection above 80% accuracy for another pathogen and host |
| [zendler2021](zendler2021.md) | downy mildew | sporulation, variety resistance, disease severity scoring, … | Siebeldingen Germany, Germany | An open, documented leaf-disc phenotyping method for downy mildew with labelled images and a percentage-of-ar… |
| [zhang2018](zhang2018.md) | none | remote sensing | Southern Africa, about 10° × 10° | Coefficients that make the two sensors consistent |
| [zhang2025review](zhang2025review.md) | downy mildew | biology | general | Review |
| [zhang2025unet](zhang2025unet.md) | none | image analysis | China | Off-topic |
| [zhang2026](zhang2026.md) | powdery mildew | season severity | Shaanxi | Powdery mildew under rain shelters |
| [zipse2010](zipse2010.md) | downy mildew | infection, incubation, sporulation, sporangia density, leaf… | Mosel, Bernkastel-Kues, Germany, Baden (WBI Freib… | Offers the truth a description of the VitiMeteo incubation and sporangia-density outputs, but no printed oosp… |
| [zorrilla2024](zorrilla2024.md) | downy mildew | biofungicide, allelopathy, leaf disc bioassay, disease seve… | Italy, Trentino, San Michele all'Adige | A lab leaf-disc record of an extract whose severity (11.4 %) the authors call similar to copper hydroxide (2.… |

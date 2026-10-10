# Literature notes

One note per paper read for Formularium or for the tools that use it: what the paper
holds, how it was read, and what was concluded, dated. The notes outlive the question
that prompted them, so they are written for a reader working on another disease, crop or
region.

The repository is public. A note holds facts, numbers and short quotes, never the paper.
It says where a copy is held only as "held by Chris" or "open access", never a path;
`files` records only the names a copy was dropped under.

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
| [albetis2017](albetis2017.md) | flavescence dorée | remote sensing, detection | Gaillac AOC, southwest France | Detection by UAV multispectral images is good on red cultivars and poor on white ones |
| [alexi2011web](alexi2011web.md) | none | evapotranspiration | United States | Typical ALEXI flux errors (about 15%) |
| [allegre2007](allegre2007.md) | downy mildew | host physiology, detection | Dijon | Thermal signature of infection before symptoms |
| [amey2006](amey2006.md) | pea downy mildew | detection | UK | Another crop |
| [amir2016](amir2016.md) | none | leaf wetness | New Zealand | Clear |
| [amirshekari2025](amirshekari2025.md) | none | evapotranspiration | Indoor plant factory, lettuce | Indoor lettuce under lamps |
| [ammour2020](ammour2020.md) | Botrytis bunch rot | detection | Italy | An observation method (latent infection by LAMP) |
| [anco2013](anco2013.md) | Phomopsis cane and leaf spot | sporulation, dispersal | Ohio | A flag now, not kin |
| [anderson2001](anderson2001.md) | potato late blight | leaf wetness, dew | Wisconsin | Clear of the engine |
| [anderson2007](anderson2007.md) | none | evapotranspiration, surface energy balance | United States | Clear |
| [anderson2018disalexi](anderson2018disalexi.md) | none | evapotranspiration | California Delta | Prose summary of DisALEXI's data fusion |
| [angelottivsf](angelottivsf.md) | downy mildew | spray timing | Pernambuco | Míldio-VSF's rules not printed; a semi-arid spray trial |
| [aslanov2019](aslanov2019.md) | wheat yellow rust | season risk | Luxembourg | Another disease; a window-correlation method |
| [balotti2018](balotti2018.md) | none | phenology | South Tyrol | Regression coefficients (its Table 3) are not in the text copy |
| [bellow2012](bellow2012.md) | downy mildew | detection | France | Background to fluorescence sensing |
| [bellow2013](bellow2013.md) | downy mildew | detection | France | Fluorescence sees infection from day 1 (abaxial) |
| [benninga2019](benninga2019.md) | none | sensor error | Netherlands | A generic radar error law |
| [berlese1898](berlese1898.md) | downy mildews | taxonomy, morphology | Italy | History and morphology |
| [biggs1988](biggs1988.md) | brown rot (Monilinia) | infection, incubation | Ontario | Its infection models are held out by structure (Broome's form) |
| [biggs2016](biggs2016.md) | none | evapotranspiration | global | Clear, and of indirect use |
| [biomebgc2010](biomebgc2010.md) | none | evapotranspiration, interception | Generic global biomes | No hourly wetness |
| [blaeser1978](blaeser1978.md) | downy mildew | sporulation, sporangia survival, dispersal | Germany | The laboratory survival data behind the 1979 curves; sporulation needs 98 % RH and 4 h dark |
| [blaeser1978diss](blaeser1978diss.md) | downy mildew | sporangia survival, infection, leaf wetness | Germany | Contents only: survival data on pp. 47-60, the wetness rule on pp. 24-28 |
| [blaeser1979](blaeser1979.md) | downy mildew | infection, sporangia survival | Ahr, Germany | c2 is 0.01 for detached sporangia, and the index is E·(1 - RH/100), not T·(1 - RH/100) |
| [bleyer2008](bleyer2008.md) | downy mildew | primary infection, sporulation | Baden-Württemberg, Switzerland | The engine's 140 °C·day oospore rule is still sourced only through Leoni et al |
| [bleyer2020](bleyer2020.md) | downy mildew | spray timing, fungicide efficacy | Baden-Württemberg | States VitiMeteo's rule that one spray protects until 300-400 cm2 of new leaf has grown |
| [bleyer2022](bleyer2022.md) | downy mildew | spray strategy, validation | Baden-Württemberg | Untreated severity at Freiburg and Ihringen (Table 1, mean 60.5%) is a severity… |
| [bojkov2022](bojkov2022.md) | downy mildew | incubation | North Macedonia | One season, ten points, started by the 3-10 rule: not usable |
| [bojkov2023](bojkov2023.md) | downy mildew | infection | North Macedonia | One season, inconsistent; not usable |
| [borzini1950](borzini1950.md) | downy mildew | spray timing | Italy | The incubation calendar in practice, 1950 |
| [bosshard1983](bosshard1983.md) | downy mildew | fungicide resistance | Switzerland | Context for a spray module |
| [bouma2003](bouma2003.md) | potato late blight, apple scab | decision support | Netherlands | DSS history; no equations |
| [bove2020](bove2020.md) | downy mildew | epidemic simulation | Italy (generic) | Values borrowed from Goidanich, Caffi, Rossi 2008, Lalancette; no validation |
| [breen2026](breen2026.md) | downy mildew | oospores, management | Europe | A perspective |
| [bregaglio2013](bregaglio2013.md) | downy mildew, Botrytis bunch rot | infection | Europe | Kin by a borrowed equation, as before, and now for that reason rather than its authors… |
| [bregaglio2022](bregaglio2022.md) | downy mildew | primary infection, secondary infection | Italy | Kin by a borrowed equation, now recorded as such |
| [brischetto2020](brischetto2020.md) | downy mildew | sporangia survival, aerobiology | Emilia-Romagna | Source of brischetto2020.survival; its Table 1 computes VPD as the saturation deficit, not the printed T(1 - RH/100) |
| [brischetto2021](brischetto2021.md) | downy mildew | secondary infection | Italy | the engine's secondary infection; its Magarey parameters, read |
| [broome1995](broome1995.md) | Botrytis bunch rot | infection | California, Chile | The engine's Botrytis model is now held and read |
| [buciumeanu2019](buciumeanu2019.md) | none | phenology | Romania | ANOVA of factors only |
| [burruano1989](burruano1989.md) | downy mildew | oospore germination | Sicily, Apulia, Latium | One spring's maturity at seven sites |
| [burruano1990](burruano1990.md) | downy mildew | oospore germination | Sicily | Cold storage kept oospores germinable into summer |
| [burruano1992nuclei](burruano1992nuclei.md) | downy mildew | oospore cytology | Sicily | Cytology only |
| [burruano1992soil](burruano1992soil.md) | downy mildew | oospore maturation | Sicily | Soil moisture changes maturation; preliminary |
| [burruano2006](burruano2006.md) | downy mildew | oospores, latency | Sicily | Summer latency up to 52 days in Sicily |
| [caffi2006validation](caffi2006validation.md) | downy mildew | primary infection, validation | Italy | Validates the engine's Rossi model: no misses, 9.6 % false alarms |
| [caffi2006water](caffi2006water.md) | downy mildew | oospore germination, litter moisture | Emilia-Romagna | Litter moisture data behind Rossi's dormancy |
| [caffi2007](caffi2007.md) | downy mildew | primary infection, oospore maturation | Sardinia | Formularium records the Siniscola data as `caffi2007.siniscola`, with the dating |
| [caffi2009](caffi2009.md) | downy mildew | primary infection, season onset | Italy | Its observed onsets are data a truth could be matched to |
| [caffi2010](caffi2010.md) | downy mildew | warning system, spray decisions | Emilia-Romagna | It evaluates the engine's rossi2008.primary in practice (Emilia-Romagna, 2006-2008) |
| [cameron2021](cameron2021.md) | none | phenology | global | Clear |
| [cammalleri2012](cammalleri2012.md) | none | evapotranspiration | Southern Sicily, Italy | TSEB run without in-situ air temperature (scene calibration or DisALEXI), over a… |
| [cannon2001](cannon2001.md) | none | sampling, detection | Australia | The engine's observation piece, confirmed |
| [cano1942](cano1942.md) | downy mildew | fungicide efficacy | Italy | History of fungicides |
| [carisse2021](carisse2021.md) | downy mildew | airborne inoculum, detection | Quebec | Clear |
| [castellvi2021](castellvi2021.md) | none | evapotranspiration | Central Iowa, USA | Sensible heat from surface renewal and land surface temperature |
| [cawsenicholson2021](cawsenicholson2021.md) | none | evapotranspiration | Contiguous United States | TSEB equations and inputs as an operational product |
| [chauvin2025](chauvin2025.md) | virus yellows | risk prediction | France | Method only |
| [chen2019](chen2019.md) | downy mildew | season risk, regional data | Bordeaux | see the note |
| [chen2019onset](chen2019onset.md) | downy mildew | season onset | Bordeaux | A history-matching pattern made outside the engine's lineage |
| [chen2020delay](chen2020delay.md) | downy mildew | season onset, spray timing | Bordeaux | Thesis ch. 6 published; nothing beyond chen2019 |
| [chen2020ml](chen2020ml.md) | downy mildew | season severity, forecasting | Bordeaux | Thesis ch. 7 published; nothing beyond chen2019 |
| [christoforides2026](christoforides2026.md) | downy mildew | oospore maturation, primary infection | Greece | Kin, for borrowed equations and four shared forms (Agrarium's candidates) |
| [ciliberti2015berries](ciliberti2015berries.md) | Botrytis bunch rot | infection | Piacenza | A flag now, not kin |
| [ciliberti2015flowers](ciliberti2015flowers.md) | Botrytis bunch rot | infection | Piacenza | A flag now, not kin |
| [claverie2018](claverie2018.md) | none | remote sensing, revisit | Global land | Revisit and surface-reflectance error of the satellite record a satellite operator… |
| [clippinger2024](clippinger2024.md) | downy mildew | management | global | Review |
| [cogato2020](cogato2020.md) | none | remote sensing | Veneto | Frost damage visible for about 40 days in Sentinel-2 indices |
| [coronelli2025](coronelli2025.md) | downy mildew | detection | Apulia | A qPCR test's detection limits |
| [costa2013](costa2013.md) | none | thermal sensing | global | Sensor background |
| [costantini2022](costantini2022.md) | none | regulation | European Union | Regulatory context |
| [dallamarta2006](dallamarta2006.md) | downy mildew | leaf wetness | Tuscany | Modelled wetness serves PLASMO as well as sensors |
| [dey2020](dey2020.md) | none | wetness sensing | laboratory | A laboratory prototype with no field error |
| [dietz2019](dietz2019.md) | oat crown rust, leaf spot | yield loss | Argentina | Another crop: loss through healthy area duration |
| [digennaro2019](digennaro2019.md) | none | remote sensing | Orsogna Winery vineyards | Satellite NDVI agrees with UAV NDVI only so well on a tall trellis (R² 0.80 and 0.60) |
| [douillet2022](douillet2022.md) | downy mildew | airborne inoculum, detection | Bordeaux | Clear |
| [dubuis2019](dubuis2019.md) | downy mildew, powdery mildew | oospore maturation, primary infection | Switzerland, Baden-Württemberg | Changins's oil-spot dates are risky to match a truth to |
| [dussert2020](dussert2020.md) | downy mildew | population genomics | France | Off-topic for simulation |
| [efsa2020](efsa2020.md) | none | sampling, detection | European Union | Held out by structure if the truth's scouts used it (D26) |
| [elena2016](elena2016.md) | trunk diseases | wound susceptibility | Catalonia | Wound susceptibility falls to about 10% twelve weeks after pruning |
| [elhelaly1965](elhelaly1965.md) | berry rots | postharvest | Egypt | Off-topic |
| [elsharkawy2018](elsharkawy2018.md) | downy mildew | biocontrol | Egypt | Control efficacy only |
| [erincik2003](erincik2003.md) | Phomopsis cane and leaf spot | infection | Ohio | A flag now, not kin (D27) |
| [esteban2012](esteban2012.md) | none | climatology | Catalonia | Off-topic for the disease truth |
| [eswari2021](eswari2021.md) | downy mildew | forecasting | Tamil Nadu | A regression with one residual df: not usable |
| [fang2019](fang2019.md) | none | evapotranspiration | United States | An operational ET product |
| [faretra1991](faretra1991.md) | downy mildew | cultivar susceptibility | Apulia | Cultivar ranks in a severe year |
| [farina1976](farina1976.md) | downy mildew | infection anatomy | Italy | Anatomy only |
| [fedele2020](fedele2020.md) | Botrytis bunch rot | biocontrol, infection | Piacenza | A flag, not kin |
| [fedele2025](fedele2025.md) | downy mildew | oospore dose | Italy | the truth's dose; calibrated with Rossi 2008's model |
| [fedele2026](fedele2026.md) | downy mildew | host susceptibility, canopy microclimate | Italy | Denser canopies had more susceptible leaves and longer wetness, yet epidemics did not… |
| [fernandezgonzalez2011](fernandezgonzalez2011.md) | downy mildew | airborne sporangia, phenology | Galicia | Four seasons of daily airborne sporangia |
| [firanjsremac2018](firanjsremac2018.md) | downy mildew, fire blight | primary infection, season onset | Vojvodina | Seven seasons of first symptoms and 10 cm shoots at Vršac |
| [foister1935](foister1935.md) | many | weather and disease | general | History; no formulation |
| [foister1946](foister1946.md) | downy mildews, various | weather and disease | general | History; no formulation |
| [folkedal2003](folkedal2003.md) | apple scab, potato late blight | decision support | Norway | A web warning system's design |
| [fontaine2021](fontaine2021.md) | downy mildew | population genomics | global | Off-topic for simulation |
| [franche2012](franche2012.md) | downy mildew | whole cycle in a DSS | France | mostly Rossi's chain; a few independent pieces |
| [gadoury1997](gadoury1997.md) | downy mildew | primary infection | New York, Pennsylvania | First printing of the engine's Kennelly trigger |
| [gadoury2003](gadoury2003.md) | powdery mildew | host susceptibility, ontogenic resistance | New York | Held out by structure, as the rule stands |
| [gadoury2006](gadoury2006.md) | downy mildew, powdery mildew, black rot | ontogenic resistance | New York, Germany, Australia | Shares Kennelly's berry data with the engine's bunch window |
| [galbiati1980](galbiati1980.md) | downy mildew | oospore formation | Lombardy | Timing of oospore formation, cited |
| [gan2023](gan2023.md) | none | wetness sensing | laboratory | About 88% accuracy on an indoor plant |
| [garciagutierrez2023](garciagutierrez2023.md) | none | phenology | Chile | Held out by structure, as recorded |
| [gashu2020](gashu2020.md) | none | phenology, berry composition | Israel | Clear and observational |
| [gautam2013](gautam2013.md) | various | climate change | India, global | Context only |
| [gehmann1987](gehmann1987.md) | downy mildew | oospores, primary infection | Baden | Contents only: behind the 160 °C·day oospore rule (Gessler 2011); pp. 57-77 |
| [gent2007cones](gent2007cones.md) | powdery mildew | sampling, observation | Oregon, Washington | Held out by structure as Part I |
| [gent2007leaves](gent2007leaves.md) | powdery mildew | sampling, observation | Oregon, Washington | Held out by structure if the truth's scouts sampled this way (D26) |
| [gent2008](gent2008.md) | powdery mildew | risk index, management | Pacific Northwest | Context for the Gubler-Thomas index's hop use (gent2025 note) |
| [gent2013](gent2013.md) | none | decision support, adoption | general | Why growers seldom use warning systems |
| [gent2025](gent2025.md) | powdery mildew | risk index, spray timing | Washington | Kin, by a borrowed equation and form (Agrarium's candidates) |
| [gessler2011](gessler2011.md) | downy mildew | review: oospores, incubation, warning models | Europe | Gehmann's 160 °C·days; Merjanian's 61/T incubation; the 3-10 as Goidanich |
| [ghiani2025](ghiani2025.md) | downy mildew, powdery mildew | detection, observation | Sardinia | Clear |
| [giosue2002](giosue2002.md) | downy mildew | primary infection, spatial analysis | Emilia-Romagna | Abstract only: onset zones keep their order from year to year |
| [gisi2002](gisi2002.md) | downy mildews | fungicides, warning models | Europe | Which country ran which model, 2002 |
| [gleason1994](gleason1994.md) | none | leaf wetness, dew | Iowa, Kansas | Held out by structure, not by its author (Agrarium's candidates) |
| [gobbin2005](gobbin2005.md) | downy mildew | epidemic structure, dispersal | central Europe | 70 % of genotypes once, 14 % twice; under 20 m per cycle; colonization 1-2 m² a day |
| [gobbin2006](gobbin2006.md) | downy mildew | population genetics, epidemic structure | Europe | random-mating oospore populations; Greek ones less diverse; cites the epidemic-structure numbers |
| [gobbin2007](gobbin2007.md) | downy mildew | dispersal | Germany | 130 m in one event; 0 to 99 % incidence in three days |
| [gonzalezdominguez2022](gonzalezdominguez2022.md) | Phomopsis cane and leaf spot | infection, validation | Italy, Montenegro | A Phomopsis model, for Cooptera |
| [gonzalezdominguez2023](gonzalezdominguez2023.md) | none | modelling history | general | Review by the Piacenza group |
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
| [hatmi2015](hatmi2015.md) | Botrytis bunch rot | host physiology | France, Tunisia | Off-topic |
| [heger2026](heger2026.md) | downy mildew, Botrytis bunch rot | airborne inoculum, detection | Michigan | Clear |
| [hegyikalo2019](hegyikalo2019.md) | Botrytis bunch rot | incidence, isolate growth | Hungary | Noble rot isolate phenotypes in Eger |
| [hill2019](hill2019.md) | Botrytis bunch rot | infection risk, season severity | New Zealand, south-east Australia | Bacchus is the Botrytis candidate, recorded in Formularium as `kim2007.bacchus` with |
| [hoppmann1997](hoppmann1997.md) | downy mildew | oospores, infection, leaf wetness | Rheingau | VitiMeteo's oospore form at 170 °C·days; modelled wetness r² 0.91 |
| [hubbard2021](hubbard2021.md) | none | soil, vigour | Bordeaux | Soil and vigour mapping |
| [huber1956](huber1956.md) | none | plant physiology | Germany | Off-topic |
| [hughes2013](hughes2013.md) | none | warning scores, risk calibration | general | Clear and a method |
| [hughes2017](hughes2017.md) | none | warning scores, forecast evaluation | general | Clear and a method |
| [humphrey1891](humphrey1891.md) | cucurbit downy mildew, brown rot | taxonomy | Massachusetts | Off-topic |
| [istvanffi1913](istvanffi1913.md) | downy mildew | incubation | Hungary | Latent periods by half-month, 1911-12: older than Müller and Goidanich |
| [jacquin2003](jacquin2003.md) | downy mildew, others | warning systems | France | The French warning models in 2002; no equations |
| [janczewski1897](janczewski1897.md) | cereal smuts | survey | Lithuania | Off-topic |
| [jensen2025](jensen2025.md) | none | modelling review | global | Review of 146 models |
| [juroszek2015](juroszek2015.md) | many, incl. downy mildew | climate change projections | global | Context for climate scenarios |
| [kabela2006](kabela2006.md) | none | dew, leaf wetness | Iowa | Clear |
| [kabela2009](kabela2009.md) | none | dew, leaf wetness | Iowa | Clear |
| [kanaley2024](kanaley2024.md) | downy mildew | remote sensing, detection | New York | Clear |
| [kang2025](kang2025.md) | none | image analysis | greenhouse | Off-topic |
| [kast1993](kast1993.md) | downy mildew | sporangia survival, dispersal | Württemberg | Infective sporangia caught when Bläser-based devices said none survived |
| [kast2006](kast2006.md) | downy mildew, powdery mildew | season severity | Württemberg | 43 seasons of severity at one site |
| [keil2006](keil2006.md) | downy mildew | infection severity | Baden | Severity by temperature and wetness; algorithm not printed |
| [keil2007](keil2007.md) | downy mildew | infection, sporulation, survival | Baden-Württemberg | Infection by 5-30 °C x 1-23 h, independent of Blaeser & Weltzien; sun kills slowly |
| [kennelly2005](kennelly2005.md) | downy mildew | host susceptibility, ontogenic resistance | New York, South Australia | The engine's window is not what the paper found for berries |
| [kennelly2006](kennelly2006.md) | downy mildew | trigger, susceptibility, survival | New York, South Australia | The engine's trigger tuned on 15 Chancellor seasons |
| [kennelly2007](kennelly2007.md) | downy mildew | sporangia survival, lesion productivity, oospores, trigger | New York, South Australia | no sporangia viable after 6-8 h of clear dry days; the engine's trigger; lesion decline per event |
| [kennelly2007php](kennelly2007php.md) | downy mildew | trigger, lesions, sporangia, fruit | New York | the engine's trigger and bunch window; field sporangia survival |
| [khaliq2019](khaliq2019.md) | none | remote sensing | Serralunga d'Alba, Piedmont | Inter-row pixels bias satellite vigour maps |
| [kim2002](kim2002.md) | none | leaf wetness | Iowa, Nebraska | Held out by structure |
| [kim2006](kim2006.md) | none | leaf wetness, forecasting | Iowa, Illinois | Forecast-driven wetness was biased low for every model it ran (its error tables) |
| [kleb2026](kleb2026.md) | downy mildew | infection, microclimate | Württemberg | Canopy sensors beat a border station and a network station |
| [knipper2019](knipper2019.md) | none | evapotranspiration, remote sensing | California | Clear |
| [koledenkova2022](koledenkova2022.md) | downy mildew | review | global | Review; context |
| [koopman2007](koopman2007.md) | downy mildew | epidemic structure, overwintering | Western Cape | new genotypes all season (12-74 %); one or two clones dominate; ten genotypes survive the winter |
| [kortekamp1998](kortekamp1998.md) | downy mildew | host resistance | Palatinate | Resistance acts 3-4 days after infection |
| [kowalczyk2006](kowalczyk2006.md) | none | evapotranspiration, canopy microclimate | Offline sites: Tharandt | A two-leaf canopy with in-canopy temperature and humidity, but no printed wet-canopy… |
| [kremheller1983](kremheller1983.md) | hop downy mildew | forecasting, airborne inoculum | Bavaria | A spore-count threshold forecast for hops |
| [kudinha2014](kudinha2014.md) | none | leaf wetness, canopy microclimate | Western Cape | Clear |
| [kumasoglu2022](kumasoglu2022.md) | downy mildew | host resistance, sporulation | Turkey | Resistant genotypes' infection counts |
| [kunova2021](kunova2021.md) | powdery mildew | fungicide resistance | general | Context for a future spray module (M4) |
| [lalancette1988infection](lalancette1988infection.md) | downy mildew | infection | Ohio | No longer kin to the engine under D27 |
| [lalancette1988sporulation](lalancette1988sporulation.md) | downy mildew | sporulation | Ohio | Kin, and rightly so, under D27 too |
| [lan2003](lan2003.md) | peach scab | dispersal | Georgia (USA) | Splash and runoff, not dew or air, carried infection (rain shields cut severity most) |
| [larochepinel2021](larochepinel2021.md) | none | water status, remote sensing | Occitanie | Water status, not disease |
| [latorre2018](latorre2018.md) | oomycetes, various | fungicide regulation | European Union | Context for a spray module |
| [lau2000](lau2000.md) | none | wetness sensing, sensor error | Iowa | Clear |
| [laviola1986](laviola1986.md) | downy mildew | oospore germination | Sicily | Inferred data behind Rossi 2008's germination time |
| [laviola2006](laviola2006.md) | downy mildew | laboratory storage | Sicily | Laboratory method only |
| [law2012](law2012.md) | none | land surface model | Australia | Planning document |
| [lebeda1994](lebeda1994.md) | downy mildews | review | global | Review; context |
| [leoni2026](leoni2026.md) | downy mildew | oospore maturation | Switzerland | The engine's GLM; coefficients recorded; fitted and scored on the same data |
| [lepik1931](lepik1931.md) | downy mildew | host resistance | Estonia | Historical anatomy |
| [lindau1908](lindau1908.md) | downy mildew | distribution | South Africa | Historical arrival at the Cape |
| [liu2026robot](liu2026robot.md) | downy mildew, grapevine leafroll | detection, scouting | New York, California | Clear, and the closest thing to a rover operator's numbers |
| [liu2026tarag](liu2026tarag.md) | none | decision support | China | Off-topic |
| [locci1969](locci1969.md) | downy mildew | infection anatomy | Lombardy | Morphology only |
| [locci1974](locci1974.md) | powdery mildew | infection anatomy | Lombardy | Morphology only |
| [lopezfrias2009](lopezfrias2009.md) | downy mildew | incubation, validation | Canary Islands | Prints the engine's Goidanich table, identical row for row |
| [lu2020](lu2020.md) | powdery mildew | infection, latent period | Quebec | Clear by every recorded link, and a flag-free candidate for powdery mildew pieces, if… |
| [lukas2016](lukas2016.md) | downy mildew | fungicide efficacy | South Tyrol | Stop-spray efficacy |
| [luo2001](luo2001.md) | brown rot (Monilinia) | latent infection, host susceptibility | California | Clear |
| [maclean2021](maclean2021.md) | none | canopy microclimate, leaf temperature | global | Clear |
| [maddalena2020](maddalena2020.md) | downy mildew | population genetics | Italy | Population genetics |
| [maddalena2021](maddalena2021.md) | downy mildew | oospores | Veneto | Four seasons of field oospore germination with station weather |
| [maddalena2022](maddalena2022.md) | downy mildew | oospore germination, primary infection | Lombardy | Kin by calibration, not by its authors (Agrarium's candidates |
| [maddalena2023](maddalena2023.md) | downy mildew, powdery mildew | forecasting, validation | Tuscany | EPI in nine organic vineyards; infection dates counted back with Goidanich |
| [madden2000](madden2000.md) | downy mildew | infection, sporulation | Ohio | Kin, now for substantive reasons |
| [madden2018](madden2018.md) | none | sampling, spatial heterogeneity | global | Field heterogeneity across about 40 pathosystems (slopes 0.87-2.00, 80% between 1.06… |
| [madden2024glmm](madden2024glmm.md) | none | statistics | general | A statistics tutorial |
| [magarey1991](magarey1991.md) | downy mildew | incubation and more | South Australia | incubation cubic fitted to Müller, Zachos and Rafaila |
| [magarey2001](magarey2001.md) | none | virtual weather stations, interpolation error | United States | Errors of virtual stations (daily mean temperature within 0.2 °C at best |
| [magarey2005](magarey2005.md) | many | infection | general | the generic infection model; its grape rows' data |
| [magarey2007](magarey2007.md) | none | risk mapping | United States | Templates for Magarey's generic infection model, described without equations |
| [malviya2022](malviya2022.md) | powdery mildew | biocontrol efficacy | India | Product efficacy trials |
| [marchal1897](marchal1897.md) | downy mildew | distribution | Belgium | Historical note |
| [marko2026](marko2026.md) | downy mildew, powdery mildew | disease occurrence | Hungary | Grower-survey effect sizes from Hungary |
| [martin2005](martin2005.md) | powdery mildew | fungicide efficacy | Spain | Control only |
| [martre2014](martre2014.md) | none | crop growth | global | Off-topic, though its finding (an ensemble mean beats single models) is the argument… |
| [massi2021](massi2021.md) | downy mildew | fungicide resistance | general | Review |
| [massi2022](massi2022.md) | downy mildew | infection efficiency | Italy | About 8% of single sporangia infected on leaf discs at 22 °C |
| [masson2011](masson2011.md) | none (climate models) | model dependence | global | why dependence is judged by components and behaviour |
| [mecikalski2004alexi](mecikalski2004alexi.md) | none | evapotranspiration | United States | Methods in words |
| [meggio2008](meggio2008.md) | none | remote sensing | Ribera del Duero | Viewing geometry alters vineyard reflectance |
| [menesatti2013](menesatti2013.md) | downy mildew | forecasting, spray timing | Lazio | PLS-DA on a Goidanich predictor; targets cut from its own data |
| [metos2026](metos2026.md) | downy mildew, powdery mildew, black rot, grey mould | sporulation, risk index | general | iMETOS/FieldClimate rules: no data behind them; a comparator, not a truth |
| [mezei2022](mezei2022.md) | downy mildew | warning system, incubation | Serbia | 3-10 trigger; incubation fitted to Miller's table |
| [miles2018](miles2018.md) | downy mildews | detection | USA | Detection methods review |
| [miller1952](miller1952.md) | downy mildew, others | forecasting history | global | History of incubation calendars and rules |
| [molitor2014](molitor2014.md) | none | phenology | Germany, Austria | The engine's model |
| [molitor2020](molitor2020.md) | Botrytis bunch rot, downy mildew | phenology, season severity | Luxembourg, Germany | UniPhen and BotRisk are kin by a borrowed equation (the engine's degree-day function),… |
| [monteiro2012](monteiro2012.md) | downy mildew | infection, sporulation, climate change | Rio Grande do Sul | Lalancette copied with misprints; RH ≥ 90 % as wetness |
| [monteiro2015](monteiro2015.md) | downy mildew | infection, climatic risk | Brazil | Lalancette copied with misprints; model output only |
| [monteiro2015bol](monteiro2015bol.md) | downy mildew, grey mould | infection, climatic risk | Brazil | Prints Broome's coefficients as the engine has them |
| [moral2012infection](moral2012infection.md) | olive anthracnose | infection, latent period | Andalusia | Kin by a borrowed equation (Magarey's), for another host |
| [moral2012inoculum](moral2012inoculum.md) | olive anthracnose | sporulation, epidemic progress | Andalusia | Kin through the temperature function it shares with Magarey's model |
| [mouafo2022](mouafo2022.md) | downy mildew | clade competition | Quebec | little for Europe |
| [moyer2016](moyer2016.md) | powdery mildew | season severity | New York | A flag now, not kin |
| [muangprathub2019](muangprathub2019.md) | none | irrigation, sensing | Thailand | Off-topic |
| [muth1916](muth1916.md) | downy mildew | infection, spray timing | Rheinhessen | History; qualitative |
| [niimi2018](niimi2018.md) | none | wine quality | South Australia | Off-topic |
| [ninyerola2005](ninyerola2005.md) | none | climatology | Iberian Peninsula | Mean climate surfaces at about 200 m from regression and residual interpolation |
| [nityagovsky2025](nityagovsky2025.md) | downy mildew | detection | Russian Far East | A detection method from the Russian Far East |
| [oerke2016](oerke2016.md) | downy mildew | detection | Palatinate | Reflectance changes 1-2 days before sporulation |
| [onofre2020](onofre2020.md) | none | wetness sensing | Florida | The usual faults of wetness sensors (height, angle, orientation, coating) |
| [orlandini1993](orlandini1993.md) | downy mildew | infection, incubation, survival, validation | Tuscany | PLASMO with fitted n and m; every piece kin to the engine by data or form |
| [orlandini2003](orlandini2003.md) | downy mildew | disease severity, model evaluation | Tuscany | A fuzzy-logic PLASMO; prints no equations |
| [orlandini2008](orlandini2008.md) | downy mildew | survival, sporulation, infection, incubation | Tuscany | PLASMO's later form: bounds printed, coefficients not; kin in every process |
| [orth1937](orth1937.md) | potato late blight | sporangia survival | Germany | Another oomycete; humidity and sporangia |
| [padro2019](padro2019.md) | none | remote sensing | Catalonia | Positional error of UAV images by method (raw GNSS about 1 m |
| [pak2008cable](pak2008cable.md) | none | land surface model | Australia | Slides only (OCR) |
| [parker2011](parker2011.md) | none | phenology | France, Switzerland | Held out by structure (a degree-day forcing sum, the engine's form), as before |
| [pdmildew2006](pdmildew2006.md) | downy mildew, powdery mildew | proceedings: epidemiology, models, control | Europe, Australia, North America | Chapter notes for the epidemiology papers |
| [peddicord2025](peddicord2025.md) | northern leaf blight, gray leaf spot | risk prediction | US Midwest | Uses a CART-style wetness tree (after Kim et al.) and RH >= 90% disease units |
| [peng2024](peng2024.md) | downy mildew | review | global | Review; context |
| [peng2025](peng2025.md) | none | animal science | China | Off-topic |
| [perrone2017](perrone2017.md) | grapevine viruses | host-virus interaction | Mediterranean | Off-topic |
| [pesquer2014](pesquer2014.md) | none | interpolation error | Catalonia, Spain | Interpolation error of Catalan precipitation by how stations are split |
| [poeydebat2025](poeydebat2025.md) | downy mildew | oospores in soil, spatial structure | Bordeaux | 15 m patches (Matérn range 15.8 m); fivefold row contrast |
| [pokovai2025](pokovai2025.md) | none | remote sensing | Hungary | Off-topic |
| [prodorutti2006](prodorutti2006.md) | downy mildew | oospore germination | Trentino | Seven seasons of germination delay |
| [puelles2020](puelles2020.md) | downy mildew | spray timing | La Rioja | A bachelor's thesis with the UR model's first rules |
| [puelles2024](puelles2024.md) | downy mildew | oospores, infection, sporulation, validation | La Rioja | The engine's UR rules: Goidanich plus the 3-10 rule, Gehmann's oospores, 50 °C·h |
| [qiu2015](qiu2015.md) | powdery mildew | host resistance | general | Host genetics review |
| [rafaila1968](rafaila1968.md) | downy mildew | incubation | Romania | an incubation independent of Goidanich's data |
| [reis2013](reis2013.md) | downy mildew | spray timing, validation | Rio Grande do Sul | A Lalancette-based trigger; three seasons of untreated AUDPC |
| [reis2020](reis2020.md) | none | phenology | Portugal | Held out by structure, read strictly (Agrarium's candidates) |
| [roberts2017](roberts2017.md) | none | statistics | general | Block cross-validation for structured data |
| [rodrigues2019](rodrigues2019.md) | downy mildew, grey mould | infection, climatic risk | Espírito Santo | Lalancette and Broome copied with misprints |
| [rodrigues2026](rodrigues2026.md) | downy mildew | infection, spread, spray timing | Rio Grande do Sul | A compartment model on powdery mildew's parameters; no data |
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
| [ryu2024](ryu2024.md) | none | interpolation error | Jeju Island, South Korea | Interpolation error of 10-min temperature with IoT stations (MAE about 0.7 °C) |
| [sajo1901](sajo1901.md) | downy mildew, powdery mildew | season severity | Hungary | Historical season comparison |
| [salazargutierrez2016](salazargutierrez2016.md) | none | phenology, dormancy | Washington | Held out by structure |
| [salcedo2021](salcedo2021.md) | downy mildews | detection | USA, global | Detection methods review |
| [salinari2007](salinari2007.md) | downy mildew | season onset | Italy | a statistical onset model at one site |
| [salotti2022](salotti2022.md) | downy mildew, powdery mildew, black rot | host resistance | Emilia-Romagna | 16 unsprayed varieties over four seasons |
| [sanna2014](sanna2014.md) | downy mildew | forecasting, measurement | Italy | Sensor calibration moves EPI's start by 7-12 days |
| [sanna2017](sanna2017.md) | downy mildew | incubation, sensor uncertainty | Piedmont | Says the Rossi-group regressions were adapted to Goidanich's table |
| [sanna2018](sanna2018.md) | downy mildew | sensor error | Piedmont | Calibration shifts the forecast by up to 4 days |
| [sanzablanedo2018](sanzablanedo2018.md) | none | photogrammetry | León (Spain) | Off-topic |
| [sarejanni1950reports](sarejanni1950reports.md) | downy mildew | season severity, oospores | Greece | 1952: abundant oospores, late-winter drought, no mildew |
| [sarejanni1951](sarejanni1951.md) | downy mildew | season severity, oospores, overwintering | Greece | Capus's winter-by-spring rain rule; preparatory years; Greek mildew years |
| [schmidt2003](schmidt2003.md) | grape berry moths | pest demography | Rheingau | An insect model; for Cooptera's pests |
| [schuepp1986](schuepp1986.md) | downy mildew | laboratory method | Switzerland | Method only |
| [sebela2014](sebela2014.md) | downy mildew | detection | Moravia | Optical indices for infected leaves |
| [sekulic2020](sekulic2020.md) | none | interpolation error | Synthetic fields | Interpolation accuracy for daily precipitation in Catalonia and temperature in Croatia |
| [sendhilvel2020](sendhilvel2020.md) | downy mildew | forecasting, spray timing | Tamil Nadu | A logistic schedule tested on the curve it came from |
| [sentelhas2004](sentelhas2004.md) | none | leaf wetness, sensors | Ontario, Sao Paulo | The wetness candidate D27 frees |
| [shin2020](shin2020.md) | none | leaf wetness, remote sensing | South Korea | Kin by calibration (Agrarium's candidates) |
| [shishkoff2019](shishkoff2019.md) | impatiens downy mildew | oospore germination | eastern USA | A cold requirement for oospore germination |
| [skahill2024](skahill2024.md) | none | frost risk | Oregon | Off-topic for the disease truth |
| [skakun2022](skakun2022.md) | none | remote sensing, cloud masking | Global | Cloud masks miss thin cloud, and the scores depend on the reference set |
| [smith1892](smith1892.md) | downy mildews | cytology | France | Off-topic |
| [solla1906](solla1906.md) | downy mildew | host physiology | Italy | Off-topic |
| [spencerphillips2002](spencerphillips2002.md) | downy mildews | book: control, host biology, epidemiology | global | Mostly control; Vercesi's oospore data noted apart |
| [spie2019](spie2019.md) | none | remote sensing | United States | Front matter only |
| [srinivasan1976](srinivasan1976.md) | downy mildew | sporangia viability | Tamil Nadu | Day-produced sporangia, above 30 °C in sun, did not germinate |
| [steel2011](steel2011.md) | bunch rots | berry infection by temperature | New South Wales | two temperatures; points to Nair & Allen 1993 |
| [stefanini2022](stefanini2022.md) | downy mildew | spray decision | Tuscany | An elicited causal graph; no data |
| [steffenel2023](steffenel2023.md) | downy mildew | forecasting | Champagne | Classifiers trained on the 3-10 rule's labels |
| [stein1985](stein1985.md) | downy mildew, powdery mildew | host resistance | Palatinate | A resistance test |
| [stille1965](stille1965.md) | potato late blight | germination | Germany | Another oomycete |
| [stobwasser1956](stobwasser1956.md) | apple scab, downy mildew | spray application | Württemberg | Spray technology |
| [sun2026](sun2026.md) | none | dormancy, phenology | Shanghai | Held out by structure if it drove a truth |
| [taibi2023](taibi2023.md) | downy mildew, powdery mildew | spray timing | Emilia-Romagna | Uses the engine's Rossi-group models to time sprays |
| [thiessen2018](thiessen2018.md) | powdery mildew | ascospore release | Oregon | The engine's record can become `read`, with initials L |
| [thind1988](thind1988.md) | downy mildew | laboratory method | Punjab | Method only |
| [toffolatti2006](toffolatti2006.md) | downy mildew | oospore germination, primary infection | Veneto | Primary inoculum to late May or early June |
| [toffolatti2024](toffolatti2024.md) | downy mildew | fungicide resistance | northern Italy | Resistance-allele monitoring in Italy |
| [tonle2024](tonle2024.md) | none | decision support | Africa | Off-topic |
| [tor2023](tor2023.md) | downy mildews | host-pathogen biology | global | Molecular review; context |
| [tranmanhsung1990](tranmanhsung1990.md) | downy mildew | oospore maturation, season severity | Bordeaux | Clear of the engine by every substantive test, and its author list is read |
| [urbeztorres2010](urbeztorres2010.md) | Botryosphaeria dieback | spore release, observation | California | Clear, and of indirect use |
| [valdesgomez2017](valdesgomez2017.md) | powdery mildew | scouting, spray decisions | Chile | A costed scouting policy (2-3 sprays against 7-9 |
| [valleggi2023](valleggi2023.md) | downy mildew | spray strategy, season severity | Tuscany | Three Chianti seasons of control-plot incidence |
| [valsesia2005](valsesia2005.md) | downy mildew | detection, observation | Switzerland, Trentino | Clear |
| [vazquezabal2019](vazquezabal2019.md) | downy mildew, black rot | infection, incubation | Galicia | Extension rules, all engine forms; Spotts's black rot table |
| [velez2020](velez2020.md) | none | remote sensing | Greenhouse at Stellenbosch University, South Africa | NDVI falls about 0.3 per unit of lost leaf area |
| [vercesi2002](vercesi2002.md) | downy mildew | oospore germination, fungicide | Lombardy | Untreated oospores germinated most in late March |
| [veverka2009](veverka2009.md) | downy mildews | general | global | A book review only; the book is not held |
| [viruega2011](viruega2011.md) | olive scab | infection, incubation | Andalusia | Not held out today |
| [viruega2013](viruega2013.md) | olive scab | inoculum production, dispersal | Andalusia | Clear |
| [volpi2021](volpi2021.md) | downy mildew, powdery mildew, grey mould | forecasting | Tuscany | Tuscany's IPM network, 2006-2019, behind tree classifiers |
| [watson2002](watson2002.md) | brown rot (Monilinia) | sporulation | South Carolina | Clear and of little use to a grape truth |
| [williams2024](williams2024.md) | none | remote sensing | England | Cover crop dominates the Sentinel-2 signal of a vineyard |
| [winkler1949](winkler1949.md) | none | viticulture | California | Off-topic |
| [winter1940](winter1940.md) | take-all | infection | Germany | Another disease |
| [wober1920](wober1920.md) | downy mildew | fungicide efficacy | Austria | History of fungicides |
| [yang2023](yang2023.md) | downy mildew | primary inoculum, latent infection | Ningxia | Clear |
| [yang2026](yang2026.md) | none | evapotranspiration | Contiguous United States | Cropland monthly error about 17% |
| [yin2018](yin2018.md) | none | drought | United States | Off-topic |
| [yu2022metabolomics](yu2022metabolomics.md) | powdery mildew | fruit chemistry | Guangxi | Off-topic for simulation |
| [yu2022shelter](yu2022shelter.md) | downy mildew | epidemic progress, canopy microclimate | Liaoning | Rain shelters cut leaf wetness and slowed epidemics (Shenyang) |
| [yuen2002](yuen2002.md) | none | warning scores | England, Sweden | Clear and a method |
| [zachos1959](zachos1959.md) | downy mildew | incubation, oospores, conidia | Greece | an incubation independent of Goidanich's data |
| [zapata2015](zapata2015.md) | none | phenology, dormancy | Washington | Held out by structure, as before |
| [zarcotejada2018](zarcotejada2018.md) | Xylella fastidiosa | remote sensing, detection | Puglia | Pre-visual detection above 80% accuracy for another pathogen and host |
| [zhang2018](zhang2018.md) | none | remote sensing | Southern Africa, about 10° × 10° | Coefficients that make the two sensors consistent |
| [zhang2025review](zhang2025review.md) | downy mildew | biology | general | Review |
| [zhang2025unet](zhang2025unet.md) | none | image analysis | China | Off-topic |

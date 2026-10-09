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
| [amir2016](amir2016.md) | none | leaf wetness | New Zealand | Clear |
| [amirshekari2025](amirshekari2025.md) | none | evapotranspiration | Indoor plant factory, lettuce | Indoor lettuce under lamps |
| [ammour2020](ammour2020.md) | Botrytis bunch rot | detection | Italy | An observation method (latent infection by LAMP) |
| [anco2013](anco2013.md) | Phomopsis cane and leaf spot | sporulation, dispersal | Ohio | A flag now, not kin |
| [anderson2001](anderson2001.md) | potato late blight | leaf wetness, dew | Wisconsin | Clear of the engine |
| [anderson2007](anderson2007.md) | none | evapotranspiration, surface energy balance | United States | Clear |
| [anderson2018disalexi](anderson2018disalexi.md) | none | evapotranspiration | California Delta | Prose summary of DisALEXI's data fusion |
| [balotti2018](balotti2018.md) | none | phenology | South Tyrol | Regression coefficients (its Table 3) are not in the text copy |
| [benninga2019](benninga2019.md) | none | sensor error | Netherlands | A generic radar error law |
| [biggs1988](biggs1988.md) | brown rot (Monilinia) | infection, incubation | Ontario | Its infection models are held out by structure (Broome's form) |
| [biggs2016](biggs2016.md) | none | evapotranspiration | global | Clear, and of indirect use |
| [biomebgc2010](biomebgc2010.md) | none | evapotranspiration, interception | Generic global biomes | No hourly wetness |
| [blaeser1978](blaeser1978.md) | downy mildew | sporulation, sporangia survival, dispersal | Germany | The laboratory survival data behind the 1979 curves; sporulation needs 98 % RH and 4 h dark |
| [blaeser1979](blaeser1979.md) | downy mildew | infection, sporangia survival | Ahr, Germany | c2 is 0.01 for detached sporangia, and the index is E·(1 - RH/100), not T·(1 - RH/100) |
| [bleyer2008](bleyer2008.md) | downy mildew | primary infection, sporulation | Baden-Württemberg, Switzerland | The engine's 140 °C·day oospore rule is still sourced only through Leoni et al |
| [bleyer2020](bleyer2020.md) | downy mildew | spray timing, fungicide efficacy | Baden-Württemberg | States VitiMeteo's rule that one spray protects until 300-400 cm2 of new leaf has grown |
| [bleyer2022](bleyer2022.md) | downy mildew | spray strategy, validation | Baden-Württemberg | Untreated severity at Freiburg and Ihringen (Table 1, mean 60.5%) is a severity… |
| [breen2026](breen2026.md) | downy mildew | oospores, management | Europe | A perspective |
| [bregaglio2013](bregaglio2013.md) | downy mildew, Botrytis bunch rot | infection | Europe | Kin by a borrowed equation, as before, and now for that reason rather than its authors… |
| [bregaglio2022](bregaglio2022.md) | downy mildew | primary infection, secondary infection | Italy | Kin by a borrowed equation, now recorded as such |
| [brischetto2021](brischetto2021.md) | downy mildew | secondary infection | Italy | the engine's secondary infection; its Magarey parameters, read |
| [broome1995](broome1995.md) | Botrytis bunch rot | infection | California, Chile | The engine's Botrytis model is now held and read |
| [buciumeanu2019](buciumeanu2019.md) | none | phenology | Romania | ANOVA of factors only |
| [caffi2007](caffi2007.md) | downy mildew | primary infection, oospore maturation | Sardinia | Formularium records the Siniscola data as `caffi2007.siniscola`, with the dating |
| [caffi2009](caffi2009.md) | downy mildew | primary infection, season onset | Italy | Its observed onsets are data a truth could be matched to |
| [caffi2010](caffi2010.md) | downy mildew | warning system, spray decisions | Emilia-Romagna | It evaluates the engine's rossi2008.primary in practice (Emilia-Romagna, 2006-2008) |
| [cameron2021](cameron2021.md) | none | phenology | global | Clear |
| [cammalleri2012](cammalleri2012.md) | none | evapotranspiration | Southern Sicily, Italy | TSEB run without in-situ air temperature (scene calibration or DisALEXI), over a… |
| [cannon2001](cannon2001.md) | none | sampling, detection | Australia | The engine's observation piece, confirmed |
| [carisse2021](carisse2021.md) | downy mildew | airborne inoculum, detection | Quebec | Clear |
| [castellvi2021](castellvi2021.md) | none | evapotranspiration | Central Iowa, USA | Sensible heat from surface renewal and land surface temperature |
| [cawsenicholson2021](cawsenicholson2021.md) | none | evapotranspiration | Contiguous United States | TSEB equations and inputs as an operational product |
| [chauvin2025](chauvin2025.md) | virus yellows | risk prediction | France | Method only |
| [chen2019](chen2019.md) | downy mildew | season risk, regional data | Bordeaux | see the note |
| [chen2019onset](chen2019onset.md) | downy mildew | season onset | Bordeaux | A history-matching pattern made outside the engine's lineage |
| [christoforides2026](christoforides2026.md) | downy mildew | oospore maturation, primary infection | Greece | Kin, for borrowed equations and four shared forms (Agrarium's candidates) |
| [ciliberti2015berries](ciliberti2015berries.md) | Botrytis bunch rot | infection | Piacenza | A flag now, not kin |
| [ciliberti2015flowers](ciliberti2015flowers.md) | Botrytis bunch rot | infection | Piacenza | A flag now, not kin |
| [claverie2018](claverie2018.md) | none | remote sensing, revisit | Global land | Revisit and surface-reflectance error of the satellite record a satellite operator… |
| [clippinger2024](clippinger2024.md) | downy mildew | management | global | Review |
| [cogato2020](cogato2020.md) | none | remote sensing | Veneto | Frost damage visible for about 40 days in Sentinel-2 indices |
| [dey2020](dey2020.md) | none | wetness sensing | laboratory | A laboratory prototype with no field error |
| [digennaro2019](digennaro2019.md) | none | remote sensing | Orsogna Winery vineyards | Satellite NDVI agrees with UAV NDVI only so well on a tall trellis (R² 0.80 and 0.60) |
| [douillet2022](douillet2022.md) | downy mildew | airborne inoculum, detection | Bordeaux | Clear |
| [dubuis2019](dubuis2019.md) | downy mildew, powdery mildew | oospore maturation, primary infection | Switzerland, Baden-Württemberg | Changins's oil-spot dates are risky to match a truth to |
| [dussert2020](dussert2020.md) | downy mildew | population genomics | France | Off-topic for simulation |
| [efsa2020](efsa2020.md) | none | sampling, detection | European Union | Held out by structure if the truth's scouts used it (D26) |
| [elena2016](elena2016.md) | trunk diseases | wound susceptibility | Catalonia | Wound susceptibility falls to about 10% twelve weeks after pruning |
| [erincik2003](erincik2003.md) | Phomopsis cane and leaf spot | infection | Ohio | A flag now, not kin (D27) |
| [esteban2012](esteban2012.md) | none | climatology | Catalonia | Off-topic for the disease truth |
| [fang2019](fang2019.md) | none | evapotranspiration | United States | An operational ET product |
| [fedele2020](fedele2020.md) | Botrytis bunch rot | biocontrol, infection | Piacenza | A flag, not kin |
| [fedele2025](fedele2025.md) | downy mildew | oospore dose | Italy | the truth's dose; calibrated with Rossi 2008's model |
| [fedele2026](fedele2026.md) | downy mildew | host susceptibility, canopy microclimate | Italy | Denser canopies had more susceptible leaves and longer wetness, yet epidemics did not… |
| [fontaine2021](fontaine2021.md) | downy mildew | population genomics | global | Off-topic for simulation |
| [franche2012](franche2012.md) | downy mildew | whole cycle in a DSS | France | mostly Rossi's chain; a few independent pieces |
| [gadoury2003](gadoury2003.md) | powdery mildew | host susceptibility, ontogenic resistance | New York | Held out by structure, as the rule stands |
| [gan2023](gan2023.md) | none | wetness sensing | laboratory | About 88% accuracy on an indoor plant |
| [garciagutierrez2023](garciagutierrez2023.md) | none | phenology | Chile | Held out by structure, as recorded |
| [gashu2020](gashu2020.md) | none | phenology, berry composition | Israel | Clear and observational |
| [gent2007cones](gent2007cones.md) | powdery mildew | sampling, observation | Oregon, Washington | Held out by structure as Part I |
| [gent2007leaves](gent2007leaves.md) | powdery mildew | sampling, observation | Oregon, Washington | Held out by structure if the truth's scouts sampled this way (D26) |
| [gent2008](gent2008.md) | powdery mildew | risk index, management | Pacific Northwest | Context for the Gubler-Thomas index's hop use (gent2025 note) |
| [gent2013](gent2013.md) | none | decision support, adoption | general | Why growers seldom use warning systems |
| [gent2025](gent2025.md) | powdery mildew | risk index, spray timing | Washington | Kin, by a borrowed equation and form (Agrarium's candidates) |
| [ghiani2025](ghiani2025.md) | downy mildew, powdery mildew | detection, observation | Sardinia | Clear |
| [gleason1994](gleason1994.md) | none | leaf wetness, dew | Iowa, Kansas | Held out by structure, not by its author (Agrarium's candidates) |
| [gobbin2005](gobbin2005.md) | downy mildew | epidemic structure, dispersal | central Europe | 70 % of genotypes once, 14 % twice; under 20 m per cycle; colonization 1-2 m² a day |
| [gobbin2006](gobbin2006.md) | downy mildew | population genetics, epidemic structure | Europe | random-mating oospore populations; Greek ones less diverse; cites the epidemic-structure numbers |
| [gobbin2007](gobbin2007.md) | downy mildew | dispersal | Germany | 130 m in one event; 0 to 99 % incidence in three days |
| [gonzalezdominguez2023](gonzalezdominguez2023.md) | none | modelling history | general | Review by the Piacenza group |
| [guevaratorres2025](guevaratorres2025.md) | none | evapotranspiration, remote sensing | South Australia | Pixel (about 100 m2) against canopy (about 2 m2) mismatch, for irrigation |
| [gutierrez2017](gutierrez2017.md) | grapevine moth | pest demography | Europe | An insect pest model |
| [gutierrez2021](gutierrez2021.md) | downy mildew, spider mite | detection, observation | Basque Country | Clear, and optimistic |
| [hain2009](hain2009.md) | none | soil moisture | Oklahoma | Soil moisture proxy, not leaf wetness |
| [hain2018poster](hain2018poster.md) | none | evapotranspiration | United States | A poster |
| [heger2026](heger2026.md) | downy mildew, Botrytis bunch rot | airborne inoculum, detection | Michigan | Clear |
| [hegyikalo2019](hegyikalo2019.md) | Botrytis bunch rot | incidence, isolate growth | Hungary | Noble rot isolate phenotypes in Eger |
| [hill2019](hill2019.md) | Botrytis bunch rot | infection risk, season severity | New Zealand, south-east Australia | Bacchus is the Botrytis candidate, recorded in Formularium as `kim2007.bacchus` with |
| [hubbard2021](hubbard2021.md) | none | soil, vigour | Bordeaux | Soil and vigour mapping |
| [hughes2013](hughes2013.md) | none | warning scores, risk calibration | general | Clear and a method |
| [hughes2017](hughes2017.md) | none | warning scores, forecast evaluation | general | Clear and a method |
| [jensen2025](jensen2025.md) | none | modelling review | global | Review of 146 models |
| [kabela2006](kabela2006.md) | none | dew, leaf wetness | Iowa | Clear |
| [kabela2009](kabela2009.md) | none | dew, leaf wetness | Iowa | Clear |
| [kanaley2024](kanaley2024.md) | downy mildew | remote sensing, detection | New York | Clear |
| [kang2025](kang2025.md) | none | image analysis | greenhouse | Off-topic |
| [kennelly2005](kennelly2005.md) | downy mildew | host susceptibility, ontogenic resistance | New York, South Australia | The engine's window is not what the paper found for berries |
| [kennelly2007](kennelly2007.md) | downy mildew | sporangia survival, lesion productivity, oospores, trigger | New York, South Australia | no sporangia viable after 6-8 h of clear dry days; the engine's trigger; lesion decline per event |
| [kennelly2007php](kennelly2007php.md) | downy mildew | trigger, lesions, sporangia, fruit | New York | the engine's trigger and bunch window; field sporangia survival |
| [khaliq2019](khaliq2019.md) | none | remote sensing | Serralunga d'Alba, Piedmont | Inter-row pixels bias satellite vigour maps |
| [kim2002](kim2002.md) | none | leaf wetness | Iowa, Nebraska | Held out by structure |
| [kim2006](kim2006.md) | none | leaf wetness, forecasting | Iowa, Illinois | Forecast-driven wetness was biased low for every model it ran (its error tables) |
| [knipper2019](knipper2019.md) | none | evapotranspiration, remote sensing | California | Clear |
| [koopman2007](koopman2007.md) | downy mildew | epidemic structure, overwintering | Western Cape | new genotypes all season (12-74 %); one or two clones dominate; ten genotypes survive the winter |
| [kowalczyk2006](kowalczyk2006.md) | none | evapotranspiration, canopy microclimate | Offline sites: Tharandt | A two-leaf canopy with in-canopy temperature and humidity, but no printed wet-canopy… |
| [kudinha2014](kudinha2014.md) | none | leaf wetness, canopy microclimate | Western Cape | Clear |
| [kunova2021](kunova2021.md) | powdery mildew | fungicide resistance | general | Context for a future spray module (M4) |
| [lalancette1988infection](lalancette1988infection.md) | downy mildew | infection | Ohio | No longer kin to the engine under D27 |
| [lalancette1988sporulation](lalancette1988sporulation.md) | downy mildew | sporulation | Ohio | Kin, and rightly so, under D27 too |
| [lan2003](lan2003.md) | peach scab | dispersal | Georgia (USA) | Splash and runoff, not dew or air, carried infection (rain shields cut severity most) |
| [larochepinel2021](larochepinel2021.md) | none | water status, remote sensing | Occitanie | Water status, not disease |
| [lau2000](lau2000.md) | none | wetness sensing, sensor error | Iowa | Clear |
| [law2012](law2012.md) | none | land surface model | Australia | Planning document |
| [liu2026robot](liu2026robot.md) | downy mildew, grapevine leafroll | detection, scouting | New York, California | Clear, and the closest thing to a rover operator's numbers |
| [liu2026tarag](liu2026tarag.md) | none | decision support | China | Off-topic |
| [lu2020](lu2020.md) | powdery mildew | infection, latent period | Quebec | Clear by every recorded link, and a flag-free candidate for powdery mildew pieces, if… |
| [luo2001](luo2001.md) | brown rot (Monilinia) | latent infection, host susceptibility | California | Clear |
| [maclean2021](maclean2021.md) | none | canopy microclimate, leaf temperature | global | Clear |
| [maddalena2020](maddalena2020.md) | downy mildew | population genetics | Italy | Population genetics |
| [maddalena2022](maddalena2022.md) | downy mildew | oospore germination, primary infection | Lombardy | Kin by calibration, not by its authors (Agrarium's candidates |
| [madden2000](madden2000.md) | downy mildew | infection, sporulation | Ohio | Kin, now for substantive reasons |
| [madden2018](madden2018.md) | none | sampling, spatial heterogeneity | global | Field heterogeneity across about 40 pathosystems (slopes 0.87-2.00, 80% between 1.06… |
| [madden2024glmm](madden2024glmm.md) | none | statistics | general | A statistics tutorial |
| [magarey1991](magarey1991.md) | downy mildew | incubation and more | South Australia | incubation cubic fitted to Müller, Zachos and Rafaila |
| [magarey2001](magarey2001.md) | none | virtual weather stations, interpolation error | United States | Errors of virtual stations (daily mean temperature within 0.2 °C at best |
| [magarey2005](magarey2005.md) | many | infection | general | the generic infection model; its grape rows' data |
| [magarey2007](magarey2007.md) | none | risk mapping | United States | Templates for Magarey's generic infection model, described without equations |
| [malviya2022](malviya2022.md) | powdery mildew | biocontrol efficacy | India | Product efficacy trials |
| [marko2026](marko2026.md) | downy mildew, powdery mildew | disease occurrence | Hungary | Grower-survey effect sizes from Hungary |
| [martre2014](martre2014.md) | none | crop growth | global | Off-topic, though its finding (an ensemble mean beats single models) is the argument… |
| [massi2021](massi2021.md) | downy mildew | fungicide resistance | general | Review |
| [massi2022](massi2022.md) | downy mildew | infection efficiency | Italy | About 8% of single sporangia infected on leaf discs at 22 °C |
| [masson2011](masson2011.md) | none (climate models) | model dependence | global | why dependence is judged by components and behaviour |
| [mecikalski2004alexi](mecikalski2004alexi.md) | none | evapotranspiration | United States | Methods in words |
| [meggio2008](meggio2008.md) | none | remote sensing | Ribera del Duero | Viewing geometry alters vineyard reflectance |
| [molitor2014](molitor2014.md) | none | phenology | Germany, Austria | The engine's model |
| [molitor2020](molitor2020.md) | Botrytis bunch rot, downy mildew | phenology, season severity | Luxembourg, Germany | UniPhen and BotRisk are kin by a borrowed equation (the engine's degree-day function),… |
| [moral2012infection](moral2012infection.md) | olive anthracnose | infection, latent period | Andalusia | Kin by a borrowed equation (Magarey's), for another host |
| [moral2012inoculum](moral2012inoculum.md) | olive anthracnose | sporulation, epidemic progress | Andalusia | Kin through the temperature function it shares with Magarey's model |
| [mouafo2022](mouafo2022.md) | downy mildew | clade competition | Quebec | little for Europe |
| [moyer2016](moyer2016.md) | powdery mildew | season severity | New York | A flag now, not kin |
| [ninyerola2005](ninyerola2005.md) | none | climatology | Iberian Peninsula | Mean climate surfaces at about 200 m from regression and residual interpolation |
| [nityagovsky2025](nityagovsky2025.md) | downy mildew | detection | Russian Far East | A detection method from the Russian Far East |
| [onofre2020](onofre2020.md) | none | wetness sensing | Florida | The usual faults of wetness sensors (height, angle, orientation, coating) |
| [orlandini1993](orlandini1993.md) | downy mildew | infection, incubation, survival, validation | Tuscany | PLASMO with fitted n and m; every piece kin to the engine by data or form |
| [orlandini2003](orlandini2003.md) | downy mildew | disease severity, model evaluation | Tuscany | A fuzzy-logic PLASMO; prints no equations |
| [padro2019](padro2019.md) | none | remote sensing | Catalonia | Positional error of UAV images by method (raw GNSS about 1 m |
| [pak2008cable](pak2008cable.md) | none | land surface model | Australia | Slides only (OCR) |
| [parker2011](parker2011.md) | none | phenology | France, Switzerland | Held out by structure (a degree-day forcing sum, the engine's form), as before |
| [peddicord2025](peddicord2025.md) | northern leaf blight, gray leaf spot | risk prediction | US Midwest | Uses a CART-style wetness tree (after Kim et al.) and RH >= 90% disease units |
| [peng2025](peng2025.md) | none | animal science | China | Off-topic |
| [pesquer2014](pesquer2014.md) | none | interpolation error | Catalonia, Spain | Interpolation error of Catalan precipitation by how stations are split |
| [poeydebat2025](poeydebat2025.md) | downy mildew | oospores in soil, spatial structure | Bordeaux | 15 m patches (Matérn range 15.8 m); fivefold row contrast |
| [pokovai2025](pokovai2025.md) | none | remote sensing | Hungary | Off-topic |
| [qiu2015](qiu2015.md) | powdery mildew | host resistance | general | Host genetics review |
| [rafaila1968](rafaila1968.md) | downy mildew | incubation | Romania | an incubation independent of Goidanich's data |
| [reis2020](reis2020.md) | none | phenology | Portugal | Held out by structure, read strictly (Agrarium's candidates) |
| [roberts2017](roberts2017.md) | none | statistics | general | Block cross-validation for structured data |
| [rosa1993](rosa1993.md) | downy mildew | infection, incubation, survival | Tuscany | PLASMO's first equations; incubation fitted to Goidanich's table, so kin |
| [rose2016](rose2016.md) | none | decision support | England and Wales | Why farmers use or ignore decision tools |
| [rossi2005](rossi2005.md) | downy mildew | primary infection, incubation | northern Italy | Does not say what the incubation regressions were fitted to |
| [rossi2008](rossi2008.md) | downy mildew | primary infection, incubation | Italy | incubation eqs 8-9 from Rossi et al. 2002, after Goidanich |
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
| [salazargutierrez2016](salazargutierrez2016.md) | none | phenology, dormancy | Washington | Held out by structure |
| [salinari2007](salinari2007.md) | downy mildew | season onset | Italy | a statistical onset model at one site |
| [sanzablanedo2018](sanzablanedo2018.md) | none | photogrammetry | León (Spain) | Off-topic |
| [sarejanni1950reports](sarejanni1950reports.md) | downy mildew | season severity, oospores | Greece | 1952: abundant oospores, late-winter drought, no mildew |
| [sarejanni1951](sarejanni1951.md) | downy mildew | season severity, oospores, overwintering | Greece | Capus's winter-by-spring rain rule; preparatory years; Greek mildew years |
| [sekulic2020](sekulic2020.md) | none | interpolation error | Synthetic fields | Interpolation accuracy for daily precipitation in Catalonia and temperature in Croatia |
| [sentelhas2004](sentelhas2004.md) | none | leaf wetness, sensors | Ontario, Sao Paulo | The wetness candidate D27 frees |
| [shin2020](shin2020.md) | none | leaf wetness, remote sensing | South Korea | Kin by calibration (Agrarium's candidates) |
| [skahill2024](skahill2024.md) | none | frost risk | Oregon | Off-topic for the disease truth |
| [skakun2022](skakun2022.md) | none | remote sensing, cloud masking | Global | Cloud masks miss thin cloud, and the scores depend on the reference set |
| [spie2019](spie2019.md) | none | remote sensing | United States | Front matter only |
| [steel2011](steel2011.md) | bunch rots | berry infection by temperature | New South Wales | two temperatures; points to Nair & Allen 1993 |
| [sun2026](sun2026.md) | none | dormancy, phenology | Shanghai | Held out by structure if it drove a truth |
| [taibi2023](taibi2023.md) | downy mildew, powdery mildew | spray timing | Emilia-Romagna | Uses the engine's Rossi-group models to time sprays |
| [thiessen2018](thiessen2018.md) | powdery mildew | ascospore release | Oregon | The engine's record can become `read`, with initials L |
| [toffolatti2024](toffolatti2024.md) | downy mildew | fungicide resistance | northern Italy | Resistance-allele monitoring in Italy |
| [tonle2024](tonle2024.md) | none | decision support | Africa | Off-topic |
| [tranmanhsung1990](tranmanhsung1990.md) | downy mildew | oospore maturation, season severity | Bordeaux | Clear of the engine by every substantive test, and its author list is read |
| [urbeztorres2010](urbeztorres2010.md) | Botryosphaeria dieback | spore release, observation | California | Clear, and of indirect use |
| [valdesgomez2017](valdesgomez2017.md) | powdery mildew | scouting, spray decisions | Chile | A costed scouting policy (2-3 sprays against 7-9 |
| [valsesia2005](valsesia2005.md) | downy mildew | detection, observation | Switzerland, Trentino | Clear |
| [velez2020](velez2020.md) | none | remote sensing | Greenhouse at Stellenbosch University, South Africa | NDVI falls about 0.3 per unit of lost leaf area |
| [viruega2011](viruega2011.md) | olive scab | infection, incubation | Andalusia | Not held out today |
| [viruega2013](viruega2013.md) | olive scab | inoculum production, dispersal | Andalusia | Clear |
| [watson2002](watson2002.md) | brown rot (Monilinia) | sporulation | South Carolina | Clear and of little use to a grape truth |
| [williams2024](williams2024.md) | none | remote sensing | England | Cover crop dominates the Sentinel-2 signal of a vineyard |
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

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
| [alexi2011web](alexi2011web.md) | none | evapotranspiration | United States | Typical ALEXI flux errors (about 15%) |
| [amir2016](amir2016.md) | none | leaf wetness | New Zealand | Clear |
| [amirshekari2025](amirshekari2025.md) | none | evapotranspiration | Indoor plant factory, lettuce | Indoor lettuce under lamps |
| [anco2013](anco2013.md) | Phomopsis cane and leaf spot | sporulation, dispersal | Ohio | A flag now, not kin |
| [anderson2001](anderson2001.md) | potato late blight | leaf wetness, dew | Wisconsin | Clear of the engine |
| [anderson2007](anderson2007.md) | none | evapotranspiration, surface energy balance | United States | Clear |
| [anderson2018disalexi](anderson2018disalexi.md) | none | evapotranspiration | California Delta | Prose summary of DisALEXI's data fusion |
| [balotti2018](balotti2018.md) | none | phenology | South Tyrol | Regression coefficients (its Table 3) are not in the text copy |
| [biggs1988](biggs1988.md) | brown rot (Monilinia) | infection, incubation | Ontario | Its infection models are held out by structure (Broome's form) |
| [biggs2016](biggs2016.md) | none | evapotranspiration | global | Clear, and of indirect use |
| [biomebgc2010](biomebgc2010.md) | none | evapotranspiration, interception | Generic global biomes | No hourly wetness |
| [bleyer2008](bleyer2008.md) | downy mildew | primary infection, sporulation | Baden-Württemberg, Switzerland | The engine's 140 °C·day oospore rule is still sourced only through Leoni et al |
| [bleyer2020](bleyer2020.md) | downy mildew | spray timing, fungicide efficacy | Baden-Württemberg | States VitiMeteo's rule that one spray protects until 300-400 cm2 of new leaf has grown |
| [bleyer2022](bleyer2022.md) | downy mildew | spray strategy, validation | Baden-Württemberg | Untreated severity at Freiburg and Ihringen (Table 1, mean 60.5%) is a severity… |
| [breen2026](breen2026.md) | downy mildew | oospores, management | Europe | A perspective |
| [bregaglio2013](bregaglio2013.md) | downy mildew, Botrytis bunch rot | infection | Europe | Kin by a borrowed equation, as before, and now for that reason rather than its authors… |
| [bregaglio2022](bregaglio2022.md) | downy mildew | primary infection, secondary infection | Italy | Kin by a borrowed equation, now recorded as such |
| [brischetto2021](brischetto2021.md) | downy mildew | secondary infection | Italy | the engine's secondary infection; its Magarey parameters, read |
| [buciumeanu2019](buciumeanu2019.md) | none | phenology | Romania | ANOVA of factors only |
| [caffi2007](caffi2007.md) | downy mildew | primary infection, oospore maturation | Sardinia | Formularium records the Siniscola data as `caffi2007.siniscola`, with the dating |
| [caffi2009](caffi2009.md) | downy mildew | primary infection, season onset | Italy | Its observed onsets are data a truth could be matched to |
| [caffi2010](caffi2010.md) | downy mildew | warning system, spray decisions | Emilia-Romagna | It evaluates the engine's rossi2008.primary in practice (Emilia-Romagna, 2006-2008) |
| [cameron2021](cameron2021.md) | none | phenology | global | Clear |
| [cammalleri2012](cammalleri2012.md) | none | evapotranspiration | Southern Sicily, Italy | TSEB run without in-situ air temperature (scene calibration or DisALEXI), over a… |
| [carisse2021](carisse2021.md) | downy mildew | airborne inoculum, detection | Quebec | Clear |
| [castellvi2021](castellvi2021.md) | none | evapotranspiration | Central Iowa, USA | Sensible heat from surface renewal and land surface temperature |
| [cawsenicholson2021](cawsenicholson2021.md) | none | evapotranspiration | Contiguous United States | TSEB equations and inputs as an operational product |
| [chen2019](chen2019.md) | downy mildew | season risk, regional data | Bordeaux | see the note |
| [chen2019onset](chen2019onset.md) | downy mildew | season onset | Bordeaux | A history-matching pattern made outside the engine's lineage |
| [christoforides2026](christoforides2026.md) | downy mildew | oospore maturation, primary infection | Greece | Kin, for borrowed equations and four shared forms (Agrarium's candidates) |
| [clippinger2024](clippinger2024.md) | downy mildew | management | global | Review |
| [dubuis2019](dubuis2019.md) | downy mildew, powdery mildew | oospore maturation, primary infection | Switzerland, Baden-Württemberg | Changins's oil-spot dates are risky to match a truth to |
| [dussert2020](dussert2020.md) | downy mildew | population genomics | France | Off-topic for simulation |
| [elena2016](elena2016.md) | trunk diseases | wound susceptibility | Catalonia | Wound susceptibility falls to about 10% twelve weeks after pruning |
| [erincik2003](erincik2003.md) | Phomopsis cane and leaf spot | infection | Ohio | A flag now, not kin (D27) |
| [esteban2012](esteban2012.md) | none | climatology | Catalonia | Off-topic for the disease truth |
| [fang2019](fang2019.md) | none | evapotranspiration | United States | An operational ET product |
| [fedele2025](fedele2025.md) | downy mildew | oospore dose | Italy | the truth's dose; calibrated with Rossi 2008's model |
| [fedele2026](fedele2026.md) | downy mildew | host susceptibility, canopy microclimate | Italy | Denser canopies had more susceptible leaves and longer wetness, yet epidemics did not… |
| [fontaine2021](fontaine2021.md) | downy mildew | population genomics | global | Off-topic for simulation |
| [franche2012](franche2012.md) | downy mildew | whole cycle in a DSS | France | mostly Rossi's chain; a few independent pieces |
| [garciagutierrez2023](garciagutierrez2023.md) | none | phenology | Chile | Held out by structure, as recorded |
| [gashu2020](gashu2020.md) | none | phenology, berry composition | Israel | Clear and observational |
| [gleason1994](gleason1994.md) | none | leaf wetness, dew | Iowa, Kansas | Held out by structure, not by its author (Agrarium's candidates) |
| [gutierrez2017](gutierrez2017.md) | grapevine moth | pest demography | Europe | An insect pest model |
| [hain2009](hain2009.md) | none | soil moisture | Oklahoma | Soil moisture proxy, not leaf wetness |
| [hain2018poster](hain2018poster.md) | none | evapotranspiration | United States | A poster |
| [jensen2025](jensen2025.md) | none | modelling review | global | Review of 146 models |
| [kabela2006](kabela2006.md) | none | dew, leaf wetness | Iowa | Clear |
| [kabela2009](kabela2009.md) | none | dew, leaf wetness | Iowa | Clear |
| [kang2025](kang2025.md) | none | image analysis | greenhouse | Off-topic |
| [kennelly2005](kennelly2005.md) | downy mildew | host susceptibility, ontogenic resistance | New York, South Australia | The engine's window is not what the paper found for berries |
| [kennelly2007php](kennelly2007php.md) | downy mildew | trigger, lesions, sporangia, fruit | New York | the engine's trigger and bunch window; field sporangia survival |
| [kim2002](kim2002.md) | none | leaf wetness | Iowa, Nebraska | Held out by structure |
| [kim2006](kim2006.md) | none | leaf wetness, forecasting | Iowa, Illinois | Forecast-driven wetness was biased low for every model it ran (its error tables) |
| [knipper2019](knipper2019.md) | none | evapotranspiration, remote sensing | California | Clear |
| [kowalczyk2006](kowalczyk2006.md) | none | evapotranspiration, canopy microclimate | Offline sites: Tharandt | A two-leaf canopy with in-canopy temperature and humidity, but no printed wet-canopy… |
| [kudinha2014](kudinha2014.md) | none | leaf wetness, canopy microclimate | Western Cape | Clear |
| [lalancette1988infection](lalancette1988infection.md) | downy mildew | infection | Ohio | No longer kin to the engine under D27 |
| [lalancette1988sporulation](lalancette1988sporulation.md) | downy mildew | sporulation | Ohio | Kin, and rightly so, under D27 too |
| [lan2003](lan2003.md) | peach scab | dispersal | Georgia (USA) | Splash and runoff, not dew or air, carried infection (rain shields cut severity most) |
| [law2012](law2012.md) | none | land surface model | Australia | Planning document |
| [liu2026tarag](liu2026tarag.md) | none | decision support | China | Off-topic |
| [luo2001](luo2001.md) | brown rot (Monilinia) | latent infection, host susceptibility | California | Clear |
| [maclean2021](maclean2021.md) | none | canopy microclimate, leaf temperature | global | Clear |
| [maddalena2020](maddalena2020.md) | downy mildew | population genetics | Italy | Population genetics |
| [maddalena2022](maddalena2022.md) | downy mildew | oospore germination, primary infection | Lombardy | Kin by calibration, not by its authors (Agrarium's candidates |
| [madden2000](madden2000.md) | downy mildew | infection, sporulation | Ohio | Kin, now for substantive reasons |
| [madden2024glmm](madden2024glmm.md) | none | statistics | general | A statistics tutorial |
| [magarey1991](magarey1991.md) | downy mildew | incubation and more | South Australia | incubation cubic fitted to Müller, Zachos and Rafaila |
| [magarey2005](magarey2005.md) | many | infection | general | the generic infection model; its grape rows' data |
| [magarey2007](magarey2007.md) | none | risk mapping | United States | Templates for Magarey's generic infection model, described without equations |
| [martre2014](martre2014.md) | none | crop growth | global | Off-topic, though its finding (an ensemble mean beats single models) is the argument… |
| [massi2021](massi2021.md) | downy mildew | fungicide resistance | general | Review |
| [masson2011](masson2011.md) | none (climate models) | model dependence | global | why dependence is judged by components and behaviour |
| [mecikalski2004alexi](mecikalski2004alexi.md) | none | evapotranspiration | United States | Methods in words |
| [molitor2014](molitor2014.md) | none | phenology | Germany, Austria | The engine's model |
| [molitor2020](molitor2020.md) | Botrytis bunch rot, downy mildew | phenology, season severity | Luxembourg, Germany | UniPhen and BotRisk are kin by a borrowed equation (the engine's degree-day function),… |
| [moral2012infection](moral2012infection.md) | olive anthracnose | infection, latent period | Andalusia | Kin by a borrowed equation (Magarey's), for another host |
| [moral2012inoculum](moral2012inoculum.md) | olive anthracnose | sporulation, epidemic progress | Andalusia | Kin through the temperature function it shares with Magarey's model |
| [mouafo2022](mouafo2022.md) | downy mildew | clade competition | Quebec | little for Europe |
| [ninyerola2005](ninyerola2005.md) | none | climatology | Iberian Peninsula | Mean climate surfaces at about 200 m from regression and residual interpolation |
| [nityagovsky2025](nityagovsky2025.md) | downy mildew | detection | Russian Far East | A detection method from the Russian Far East |
| [pak2008cable](pak2008cable.md) | none | land surface model | Australia | Slides only (OCR) |
| [parker2011](parker2011.md) | none | phenology | France, Switzerland | Held out by structure (a degree-day forcing sum, the engine's form), as before |
| [peddicord2025](peddicord2025.md) | northern leaf blight, gray leaf spot | risk prediction | US Midwest | Uses a CART-style wetness tree (after Kim et al.) and RH >= 90% disease units |
| [peng2025](peng2025.md) | none | animal science | China | Off-topic |
| [pokovai2025](pokovai2025.md) | none | remote sensing | Hungary | Off-topic |
| [rafaila1968](rafaila1968.md) | downy mildew | incubation | Romania | an incubation independent of Goidanich's data |
| [reis2020](reis2020.md) | none | phenology | Portugal | Held out by structure, read strictly (Agrarium's candidates) |
| [roberts2017](roberts2017.md) | none | statistics | general | Block cross-validation for structured data |
| [rose2016](rose2016.md) | none | decision support | England and Wales | Why farmers use or ignore decision tools |
| [rossi2008](rossi2008.md) | downy mildew | primary infection, incubation | Italy | incubation eqs 8-9 from Rossi et al. 2002, after Goidanich |
| [rossi2012](rossi2012.md) | downy mildew | splash dispersal, primary infection | Emilia-Romagna | Its splash data (4.4 drops/cm² at 40 cm, 0.03 at 80 cm, 0.003 at 140 cm |
| [rossi2013](rossi2013.md) | downy mildew | epidemic structure | Europe | Gobbin's genotype patterns, for history matching |
| [rossi2025](rossi2025.md) | downy mildew | host susceptibility, spray efficacy | Piacenza | Efficacy rises with cluster stage, interacting with ontogenic resistance |
| [rotem1969](rotem1969.md) | many | irrigation | Israel | drip adds no leaf wetness; sprinkling does |
| [roubal2013](roubal2013.md) | olive scab | infection, latent period | Provence | Held out by structure through its RH-threshold wetness (Agrarium's candidates) |
| [rouxel2014](rouxel2014.md) | downy mildew | population genetics | Eastern North America | Population genetics |
| [rowlandson2015](rowlandson2015.md) | none | leaf wetness, sensors | general | The review behind the wetness definitions Agrarium uses |
| [salazargutierrez2016](salazargutierrez2016.md) | none | phenology, dormancy | Washington | Held out by structure |
| [salinari2007](salinari2007.md) | downy mildew | season onset | Italy | a statistical onset model at one site |
| [sentelhas2004](sentelhas2004.md) | none | leaf wetness, sensors | Ontario, Sao Paulo | The wetness candidate D27 frees |
| [shin2020](shin2020.md) | none | leaf wetness, remote sensing | South Korea | Kin by calibration (Agrarium's candidates) |
| [skahill2024](skahill2024.md) | none | frost risk | Oregon | Off-topic for the disease truth |
| [steel2011](steel2011.md) | bunch rots | berry infection by temperature | New South Wales | two temperatures; points to Nair & Allen 1993 |
| [sun2026](sun2026.md) | none | dormancy, phenology | Shanghai | Held out by structure if it drove a truth |
| [taibi2023](taibi2023.md) | downy mildew, powdery mildew | spray timing | Emilia-Romagna | Uses the engine's Rossi-group models to time sprays |
| [toffolatti2024](toffolatti2024.md) | downy mildew | fungicide resistance | northern Italy | Resistance-allele monitoring in Italy |
| [tranmanhsung1990](tranmanhsung1990.md) | downy mildew | oospore maturation, season severity | Bordeaux | Clear of the engine by every substantive test, and its author list is read |
| [viruega2011](viruega2011.md) | olive scab | infection, incubation | Andalusia | Not held out today |
| [viruega2013](viruega2013.md) | olive scab | inoculum production, dispersal | Andalusia | Clear |
| [watson2002](watson2002.md) | brown rot (Monilinia) | sporulation | South Carolina | Clear and of little use to a grape truth |
| [yang2026](yang2026.md) | none | evapotranspiration | Contiguous United States | Cropland monthly error about 17% |
| [yin2018](yin2018.md) | none | drought | United States | Off-topic |
| [yu2022shelter](yu2022shelter.md) | downy mildew | epidemic progress, canopy microclimate | Liaoning | Rain shelters cut leaf wetness and slowed epidemics (Shenyang) |
| [zachos1959](zachos1959.md) | downy mildew | incubation, oospores, conidia | Greece | an incubation independent of Goidanich's data |
| [zapata2015](zapata2015.md) | none | phenology, dormancy | Washington | Held out by structure, as before |
| [zhang2025review](zhang2025review.md) | downy mildew | biology | general | Review |
| [zhang2025unet](zhang2025unet.md) | none | image analysis | China | Off-topic |

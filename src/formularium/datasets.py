"""The data formulations were calibrated on, so that shared calibration can be seen.

Two formulations fitted to the same observations err together however different their
equations look. That is one of the substantive dependencies that decide the hold-out
(Agrarium decision D27); shared authorship alone is not. A record names its data in
`calibrated_on`, by the ids below, only where a source says so. An empty `calibrated_on`
means not recorded, never "fitted to nothing".

Each dataset says where the calibration was read, and how it was checked
(records.AUTHOR_SOURCES).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Dataset:
    citation: str
    where: str  # where a source says a formulation was fitted to it
    checked: str  # one of records.AUTHOR_SOURCES


DATASETS: dict[str, Dataset] = {
    "goidanich1957": Dataset(
        "Goidanich, Casarini & Foschi 1957, Lotta antiparassitaria e calendario dei trattamenti"
        " in viticoltura, Giornale di Agricoltura (13 January): 11-14: incubation of"
        " P. viticola by temperature and humidity (reference line read in Rossi et al. 2005;"
        " Rossi et al. 2002 titles it 'Lotta antiperonosporica e calendario d'incubazione';"
        " the paper itself not read)",
        "Rossi, Giosuè, Girometta & Bugiani 2002 (Atti Giornate Fitopatologiche 2002, 2:263-"
        "270, p. 265; read 2026-10-09 in the conference archive's scan): incubation 'è stata"
        " calcolata in funzione della temperatura dell'aria, mediante due equazioni di"
        " regressione adattate ai dati di Goidanich et al. (1957)', for the periods those"
        " authors called of high and low humidity; Fig. 2 prints them, 45.1 - 3.45T + 0.073T²"
        " and 59.9 - 4.55T + 0.095T² days, Rossi 2008's eqs 8-9. Rossi et al. 2005 (Riv. Ital."
        " Agrometeorol. 3:7-13; read 2026-10-08 by the paper search session) says the same"
        " less exactly. The engine's Goidanich table is these data, as Porras Soriano 2006"
        " prints them."
        " Zachos 1959 (read 2026-10-08, p. 250) describes Casarini 1957's own curves for"
        " Emilia, at high and at low humidity, from artificial and natural inoculations;"
        " Casarini co-wrote the table, so its data are probably his (inferred, not stated)."
        " Sanna 2017 (PhD thesis, Univ. Torino, pp. 75-76; read 2026-10-09) states it of the"
        " regressions: 'two regression equations accounting for both low and high level of"
        " relative humidity, adapted to the evaluation table of the incubation period of"
        " Goidànich (1957)', citing Giosuè et al. 2002 (Atti II Giornate di studio, Pisa,"
        " 1:229-237, not held): a third party's statement, not the authors'. Rosa et al. 1993"
        " (p. 208, read 2026-10-09) fitted PLASMO's incubation to 'the Goidanich table"
        " (Goidanich et al., 1958)', the authors' book I nemici della vite",
        "read",
    ),
    "rossi2002.emilia": Dataset(
        "The date of the first oil spots in unsprayed plots of 127 vineyards in Emilia-Romagna"
        " (80 on the plain, 47 in the hills), 1993-2000, leaves inspected every 5-7 days; mean"
        " dates for the western, central and eastern plain by year (Tab. 1), with daily rain"
        " and temperature at Piacenza, Bologna and Ravenna",
        "Rossi, Giosuè, Girometta & Bugiani 2002, Atti Giornate Fitopatologiche 2002, 2:263-270,"
        " pp. 264-266 and Tab. 1 (read 2026-10-09 in the conference archive's scan): the onset"
        " regression (eq. 1) was fitted to the plain's probable infection periods, which were"
        " back-calculated from these dates with the incubation regressions",
        "read",
    ),
    "sarejanni1951.greece": Dataset(
        "Greek downy mildew seasons: the mildew years in currant production, 1885-1939 (1900,"
        " 1916, 1920 and 1931 marked), and twenty years of observations in Attica, Euboea, the"
        " Peloponnese and Macedonia, with the Benaki Institute's yearly reports for 1949-1953",
        "Sarejanni 1951, Ann. Inst. Phytopathol. Benaki 5(2):53-65, and the Institute's"
        " reports in vols 4-8 (read 2026-10-09 in the Internet Archive's OCR). No formulation"
        " is recorded as fitted to them. Agrarium plans to history-match its truth's"
        " season-level behaviour against them (its TRUTH-METHOD part 2)",
        "read",
    ),
    "zachos1959": Dataset(
        "Artificial inoculations every ten days, April to October, for two years, in vineyards"
        " at Vello (Coconi) and Patras, Greece, on Corinth, Sultanina, Rhazaki, Rhoditis,"
        " Phraoula and Sideritis, leaves 4-6 from the shoot tip, with temperature and humidity"
        " from a thermohygrograph beside the vines; after years of natural infections",
        "Zachos 1959, Ann. Inst. Phytopathol. Benaki N.S. 2(4):193-355, chapter II (read"
        " 2026-10-08 in the Internet Archive scan Chris supplied). The curves are his own: he"
        " compares them with Ravaz, Müller and Sleumer, Baldacci and Casarini, adopting none",
        "read",
    ),
    "zachos1959.conidia": Dataset(
        "Conidia taken 5-7 h old from oil spots, detached onto glass slides and held in the"
        " sun, in a weather screen (open, or saturated under a bell jar) or at a constant 23 or"
        " 25 °C, then wetted and scored for germination at 2 h and 24 h; Greece, May-June",
        "Zachos 1959, Ann. Inst. Phytopathol. Benaki N.S. 2(4):193-355, chapter III, pp."
        " 254-261, Tables XVI-XVIII (read 2026-10-09 in an OCR of the scan, checked against"
        " the text). His own experiments; separate from his incubation inoculations",
        "read",
    ),
    "poeydebat2025.villenave": Dataset(
        "P. viticola oospore DNA by ddPCR in 318 soil samples (198 on a 2.85 x 3.2 m grid,"
        " 0-15 cm) of a 0.22 ha organic Merlot vineyard at Villenave d'Ornon, Bordeaux, March"
        " 2022, with depth profiles and a leaf-disc bioassay",
        "Poeydebat et al. 2025, Appl. Environ. Microbiol. 91(12):e0166725 (read 2026-10-09"
        " in Europe PMC's full text). No formulation is recorded as fitted to them; Agrarium"
        " plans to check its oospore field's spatial structure against them",
        "read",
    ),
    "kennelly2007.loxton": Dataset(
        "Chardonnay shoots and potted vines in a vineyard at Loxton, South Australia, October"
        " to December 2003: lesion cohorts induced to sporulate repeatedly, sporangia counted"
        " per mm², and sporangia sampled at 1-4 h intervals after sunrise and scored for"
        " germination within 4 h, with canopy temperature, RH and wetness every 10 min",
        "Kennelly et al. 2007, Phytopathology 97:512-522, Materials and methods and Figs 3-7"
        " (read 2026-10-09 in an Internet Archive capture of the publisher's PDF)",
        "read",
    ),
    "rumbou2004.aghialos": Dataset(
        "Every oil spot in an untreated 100-vine Roditis plot at N. Aghialos, Thessaly, 0.5 km"
        " from the sea, 2001 (five samplings, 327 lesions) and 2002 (four, 426), genotyped"
        " with four microsatellites and mapped to the vine, with the season's rain, mean"
        " temperature and RH",
        "Rumbou & Gessler 2004, Eur. J. Plant Pathol. 110:379-392, Tables 1 and 4 (read"
        " 2026-10-09). No formulation is recorded as fitted to them; Agrarium plans to"
        " history-match its truth's epidemic structure against them",
        "read",
    ),
    "rafaila1968": Dataset(
        "Detached leaves in a polythermostat at 5-30 °C and 100% humidity, Bucharest"
        " 1963-1965; and incubation by leaf age in the Minis and Blaj vineyards",
        "Rafaila, Sevcenco & David 1968, Phytopathol. Z. 63:328-336, Tables 3 and 4 (read"
        " 2026-10-08 in the copy Chris supplied). They cite neither Müller nor Goidanich",
        "read",
    ),
    "blaeser1979": Dataset(
        "Blaeser & Weltzien 1979, Z. PflKrankh. PflSchutz 86:489-498, Tab. 1: the least wetness"
        " that infected at least half the inoculated leaves (potted Müller-Thurgau, sporangial"
        " suspension) at constant 6-25 °C, 2 to 9 h; Bonn",
        "Brischetto et al. 2021, Figure 2 caption (D): the Magarey response's parameters were"
        " estimated from Blaeser & Weltzien 1979 and Caffi et al. 2016. Orlandini et al. 1993"
        " (p. 620) fitted PLASMO's n/T to 'data from Blaeser & Weltzien (1979)' by least"
        " squares. The table itself read 2026-10-09 (literature/blaeser1979)",
        "read",
    ),
    "blaeser1978.survival": Dataset(
        "Blaeser & Weltzien 1978, Z. PflKrankh. PflSchutz 85:155-161, Abb. 2-3: the maximum"
        " lifetime of sporangia on the leaf and detached (on aluminium foil), at 10-30 °C and"
        " 30-100 % RH, germination scored after 23 h, each test three times; sporangia from"
        " potted Müller-Thurgau, Bonn",
        "Blaeser & Weltzien 1979, p. 493 (read 2026-10-09): the survival polynomials were"
        " computed 'aus den vorliegenden Daten' of the tests at those temperatures and"
        " humidities, cited to the 1978 paper; that they are the 1978 data is inferred. PLASMO's"
        " survival (Orlandini et al. 1993) is credited to the 1979 paper",
        "read",
    ),
    "caffi2016": Dataset(
        "Caffi et al. 2016 (P. viticola infection data)",
        "Brischetto et al. 2021, Figure 2 caption (D), as for blaeser1979",
        "read",
    ),
    "lalancette1988a": Dataset(
        "Lalancette, Ellis & Madden 1988, Phytopathology 78:794-800 (infection of"
        " V. labrusca 'Catawba' at 5-28 °C, 2-24 h wet)",
        "Magarey et al. 2005, Tables 1 and 2, ref. 43: its P. viticola row",
        "read",
    ),
    "nair1993": Dataset(
        "Nair & Allen 1993, Mycol. Res. 97:1012-1014 (Botrytis on grape flowers and berries)",
        "Magarey et al. 2005, Tables 1 and 2, ref. 56: its grape Botrytis rows",
        "read",
    ),
    "ramos2017.penedes": Dataset(
        "Phenology of Chardonnay (1998-2012), Macabeo and Parellada (1998-2009) in one Penedès"
        " vineyard grown for cava, with hourly weather from the Els Hostalets de Pierola"
        " station, about 6 km away",
        "Ramos 2017, Agric. For. Meteorol. 247:104-115, sections 2.2-2.3 (read 2026-10-08 in"
        " the copy Cooptera holds)",
        "read",
    ),
    "chen2019.ifv": Dataset(
        "IFV's untreated rows (témoins non traités) in Bordeaux vineyards, 2010-2018: weekly"
        " incidence on vines and bunches, and end-of-season incidence and severity on leaves"
        " and bunches, in a central untreated row (mean 53.1 vines) between two untreated"
        " guard rows inside treated vineyards. Onset is the first week with over 1 % of vines"
        " symptomatic. 156 plot-years are public (github.com/MathildeChen/"
        "PhD-Supplementary-Data, Supp_Data_Chap_7.xlsx, no licence stated): onset week,"
        " monthly March-June weather from SAFRAN, and each end-of-season measure as above or"
        " below its median",
        "Chen 2019, PhD thesis (read 2026-10-08): ch. 4 fitted survival models (Turnbull,"
        " Cox, log-normal, log-logistic) to 266 site-years of 2010-2017; ch. 7 fitted"
        " classifiers to the 156, whose 97 censored onsets were imputed with a survival model"
        " that has March-June rainfall as covariate. Agrarium plans to history-match its"
        " truth against the patterns (its TRUTH-METHOD part 2), which would make the truth"
        " calibrated on these data",
        "read",
    ),
    "gobbin2006.europe": Dataset(
        "Gobbin et al. 2005 and 2006: P. viticola genotyped with four microsatellites in 39"
        " vineyards (Germany 4, France 4, Italy 12, Greece 10, Switzerland 9), 2000-2002 and"
        " 2004; 155 samplings, about 10,000 oil spots, each vineyard sampled from its first"
        " lesions until the mosaic stage",
        "Rossi, Caffi & Gobbin 2013, Eur. J. Plant Pathol. 135:641-654, pp. 645-647 (read"
        " 2026-10-08), a review Gobbin co-wrote; Gobbin's papers not held. No formulation is"
        " recorded as fitted to these data. Agrarium plans to history-match its truth's"
        " epidemic structure against them (its TRUTH-METHOD part 2)",
        "trail",
    ),
    "phenoclim": Dataset(
        "INRA's PHENOCLIM database (Chuine & Seguin 2008): grapevine budburst dates, 1970-2002,"
        " ten cultivars in five French regions, with their stations' temperatures",
        "García de Cortázar-Atauri et al. 2009, Int. J. Biometeorol. 53:317-326, 'The"
        " database' (read 2026-10-08 in the copy Cooptera holds; Cooptera read it 2026-10-07)",
        "read",
    ),
    "molitor2014.mt60": Dataset(
        "Sixty phenology series of Müller-Thurgau, 1995-2012, at Eltville, Veitshöchheim and"
        " Kindel (Germany), Klosterneuburg (Austria), Cembra (Italy) and Remich (Luxembourg)",
        "Molitor et al. 2014, Am. J. Enol. Vitic. 65:72-80, abstract and Table 1 (read"
        " 2026-10-08 in the copy Cooptera holds): 'used for model calibration'",
        "read",
    ),
    "leoni2026.changins": Dataset(
        "Oospore germination observed at Changins, Switzerland (a Chasselas plot), 2022-2024",
        "Leoni et al. 2026, OENO One 60(3), abstract and section 1 (read 2026-10-08 in the copy"
        " Cooptera holds)",
        "read",
    ),
    "madden1995": Dataset(
        "Madden, Hughes & Ellis 1995, Phytopathology 85:269-275: incidence of grape downy"
        " mildew in Ohio, 18 plots at two times in three years (108 plot-dates), 15 shoots of"
        " about 15 leaves each",
        "Madden & Hughes 1999, Phytopathology 89:1088, Figs. 3-4 and text: the intracluster"
        " correlation 0.07 is the mean of those 108 values (read 2026-10-08 in the copy"
        " Cooptera holds). Agrarium's TRUTH-METHOD part 2 lists the same data as a pattern for"
        " the truth's spatial heterogeneity",
        "read",
    ),
    "rossi2008pp.discs": Dataset(
        "Oospore germination, 1999-2003, as infection of grape leaf discs by oospores sampled"
        " from a vineyard, March to July",
        "Rossi et al. 2008, Plant Pathol. 57:216-226, abstract (read 2026-10-08 in the copy"
        " Cooptera holds)",
        "read",
    ),
    "ferguson2014.prosser": Dataset(
        "Cold hardiness (differential thermal analysis) of primary buds of 23 Vitis genotypes"
        " at Prosser, Washington",
        "Ferguson et al. 2014, Am. J. Enol. Vitic. 65:59-71, abstract and methods (read"
        " 2026-10-08 in the copy Cooptera holds)",
        "read",
    ),
    "tranmanhsung1990.bordeaux": Dataset(
        "Oospore maturity dates from the authors' burial assay at an INRA Bordeaux vineyard"
        " (about 24 March 1985, 2 May 1986, 24 March 1988), and regional downy mildew"
        " severity on a 1-4 scale, 1977-1988, rated by the authors from the Plant Protection"
        " Service's bulletins (about 100,000 ha)",
        "Tran Manh Sung, Strizyk & Clerjeau 1990, Plant Dis. 74:120-124, Materials and"
        " methods and Results (read 2026-10-08): POM's A and B were fitted to the three dates,"
        " its severity regression and classes to the twelve years. Whether the bulletins"
        " leaned on EPI is not stated",
        "read",
    ),
    "caffi2007.siniscola": Dataset(
        "First downy mildew onsets on cv. Cannonau at Siniscola, Sardinia, 1996-2004, an"
        " unsprayed plot inspected weekly; and probable infection dates inferred from them",
        "Caffi, Rossi, Cossu & Fronteddu 2007, EPPO Bull. 37:261-271 (read 2026-10-08): the"
        " infection dates were found 'going backward through the incubation period starting"
        " from the observed onset of symptoms, as shown in Rossi et al. (2002)', and predicted"
        " onsets were dated with the UCSC model's incubation (Tables 3-4). A formulation"
        " fitted or scored on the infection dates is calibrated with rossi2008.primary; the"
        " observed onsets alone are not",
        "read",
    ),
    "maddalena2022.franciacorta": Dataset(
        "Ten Franciacorta vineyards (mostly Chardonnay), 2020-2021: oospore germination"
        " assays (minimum days to germinate) and downy mildew onsets in untreated plots, with"
        " probable infection dates",
        "Maddalena et al. 2022, BIO Web Conf. 50:04002 (read 2026-10-08, lines 166-177): 'the"
        " length of incubation period was calculated (Goidanich et al., 1957), to ... ascertain"
        " the most probable date of disease infection'. A formulation fitted or scored on those"
        " dates is calibrated with goidanich.incubation (the paper names the method, not each"
        " date's source; infections are not observed in the field)",
        "read",
    ),
    "orlandini1993.emergences": Dataset(
        "Observed dates of P. viticola sporangial emergence in Tuscan vineyards (cv."
        " Sangiovese); validation at Mondeggi-Lappeggi, Firenze (Paretaio 1990, Pulizzano"
        " 1990-1992), weekly observations in 1500 m2 untreated plots",
        "Orlandini et al. 1993, EPPO Bull. 23:619-626, p. 621 (read 2026-10-09): m and n 'were"
        " chosen when the difference in time between observed and calculated sporangia"
        " emergences reached a minimum'. Which observations is not stated; these validation"
        " data are the likely ones (inferred)",
        "read",
    ),
    "orlandini2008.mondeggi": Dataset(
        "Downy mildew severity every 10 days, budbreak to harvest, on 800 leaves and 400"
        " clusters of 200 Sangiovese vines in three untreated plots (about 1000 m² each) of the"
        " Paretaio vineyard, Mondeggi-Lappeggi (Chianti, 43°47' N, 180 m), 1995-2003, with"
        " hourly temperature, RH, rain and leaf wetness beside it; leaf area 1995-1996",
        "Orlandini, Massetti & Dalla Marta 2008, Comput. Electron. Agric. 64:149-161, pp. 158-"
        "160 (read 2026-10-09): PLASMO's C and D were tuned on 1995-1996 (C22 D18) and"
        " validated on 1998-2003 (Tables 2-4)",
        "read",
    ),
    "keil2007.freiburg": Dataset(
        "Leaf discs of Müller-Thurgau inoculated with 25,000 sporangia/ml at 5-30 °C and 1-23 h"
        " of wetness, 20 discs per cell, the percent of stomata infected (Anhang 7.1); sporangia"
        " per cm² of field lesions at 15-30 °C; sporangia under direct sun on glass, summer 2005;"
        " untreated epidemics at the WBI Freiburg, 2004-2006",
        "Keil 2007, dissertation, Univ. Hohenheim, pp. 41, 53, 63, 74 and Anhang 7.1 (read"
        " 2026-10-09): the sporulation quadratic and the sun-exposure line are fitted to these"
        " counts. The infection cells carry no fitted equation",
        "read",
    ),
    "istvanffi1913.hungary": Dataset(
        "Latent periods of downy mildew from natural infections dated by the institute"
        " vineyard's weather station and from artificial infections in the open, Hungary, 1911"
        " and 1912 combined, by half-month from early May to August",
        "Istvánffi 1913, Botanikai Közlemények 12 (read 2026-10-09). No formulation is recorded"
        " as fitted to them; an incubation calendar older than Müller & Sleumer's and"
        " Goidanich's, for history matching",
        "read",
    ),
    "haasbroek2006.westerncape": Dataset(
        "Weekly downy mildew in untreated plots at Nietvoorbij (Stellenbosch), 6 November 2002 to"
        " 19 February 2003 (100 leaves, visual); monthly disease classes 1998-2003; hourly"
        " weather and leaf-wetness sensor readings at Nietvoorbij, Môrewag (Paarl) and four"
        " Robertson stations, Western Cape",
        "Haasbroek 2006, M.Sc. Agric. thesis, Univ. Free State (read 2026-10-09): the DSVW"
        " leaf-wetness regression is fitted to the 2002 Nietvoorbij sensor data. A"
        " Mediterranean-climate pattern for the truth",
        "read",
    ),
    "puelles2024.rioja": Dataset(
        "First symptoms and later infection blocks in eight Rioja vineyards (Tempranillo,"
        " Graciano; 452-552 m), 2018-2019, visited every 5-7 days, at least 40 untreated vines a"
        " plot beside an agroclimatic station; oospores buried in mesh bags and germinated at"
        " 20 °C",
        "Puelles et al. 2024, Crop Prot. (read 2026-10-09 in the authors' manuscript): the UR"
        " model's 160 °C·day oospore threshold was chosen on these data ('data not shown'), and"
        " the UR adjustments were judged on the same plots. Visits rose when models signalled",
        "read",
    ),
    "maddalena2021.montorio": Dataset(
        "Germination of P. viticola oospores from an untreated Corvina vineyard at Montorio"
        " (Verona), four consecutive seasons, overwintered in the vineyard (MT) or at 5 °C on wet"
        " sand (MTc), counted twice a week for 35 weeks, mid-November to mid-July, with daily"
        " weather from a station in the vineyard",
        "Maddalena, Russo & Toffolatti 2021, Front. Microbiol. (read 2026-10-09): the paper's"
        " probit and logit models are fitted to them. Independent of Rossi 2008's leaf-disc"
        " data (rossi2008pp.discs)",
        "read",
    ),
    "maddalena2023.panzano": Dataset(
        "Downy and powdery mildew incidence and severity in nine organic vineyards at Panzano in"
        " Chianti, 2020-2021, untreated, EPI-timed and grower-timed plots, with first-symptom"
        " dates; infection dates counted back from symptoms with Goidanich et al. 1957's"
        " incubation",
        "Maddalena et al. 2023, Plants (read 2026-10-09): used to judge EPI (Epicure). The"
        " symptom dates are observed; the infection dates are computed with Goidanich's"
        " incubation (section 4.4, ref. 55), so anything scored on them is calibrated with it",
        "read",
    ),
    "ronzon1987.bordeaux": Dataset(
        "Oospore maturation and germination of Malbec (1984, 1985) and Muscadelle (1986) lesions,"
        " in chambers and buried in the vineyard (Bordeaux); downy mildew attack classes 1975-1986"
        " from the Plant Protection Service's bulletins",
        "Ronzon 1987, thesis, Univ. Bordeaux II (read 2026-10-09 in an OCR checked against the"
        " page images): POM's thesis version fitted its coefficients to 1985 and 1986; EPI was"
        " judged against the attack classes. The 1985 and 1986 maturity dates are among the"
        " three of tranmanhsung1990.bordeaux (inferred: same lab, same years)",
        "read",
    ),
    "rouzet2003.balma": Dataset(
        "Dates from which oospores stored 2 cm under sand at Balma (Midi-Pyrénées) germinated"
        " within 24 h at 20-22 °C, 1969-1998 (Table 2); leaves collected at the end of October;"
        " French Plant Protection Service ('code mildiou')",
        "Rouzet & Jacquin 2003, EPPO Bull. 33:437-442, Tables 2 and 7 (read 2026-10-09)",
        "read",
    ),
    "laviola1986": Dataset(
        "Germination of P. viticola oospores at constant 4-30 °C (percentages and minimum, mean"
        " and maximum days to germinate), 1980, 1981 and 1983, from Catarratto leaves collected"
        " in November in Palermo province and overwintered there; Laviola, Burruano &"
        " Strazzeri 1986, Phytopathol. Mediterr. 25:80-84",
        "Rossi et al. 2008 (Ecol. Model. 212:480-491, p. 482): germination duration is"
        " 'regulated by temperature (Laviola et al., 1986)'; Rossi et al. 2005 likewise. That"
        " eq. 5 (1330.1 - 116.19T + 2.6256T² hours) was fitted to these data is inferred, not"
        " stated: it gives 18 d at 10 °C against Laviola's minimum of 17 d (1983), and 1.9 d"
        " at 22 °C against 3 d (read 2026-10-09)",
        "trail",
    ),
    "kennelly2006.chancellor": Dataset(
        "Historical records of downy mildew's first outbreak on the highly susceptible"
        " cultivar Chancellor in a vineyard at Geneva, New York: fifteen years, by Kennelly et"
        " al. 2006",
        "Kennelly et al. 2007, Phytopathology 97:512-522, p. 513 (read 2026-10-09): 'Using the"
        " reported data, a set of criteria was developed (7,8)', and the criteria were evaluated"
        " 'in addition to the Chancellor vineyard in Geneva where the original data used to"
        " develop the criteria were collected'. Kennelly, Gadoury, Seem, Wilcox & Magarey 2006"
        " (5th Int. Workshop on Grapevine Downy and Powdery Mildew, read 2026-10-09): the"
        " threshold 'was consistent across 15 years of historical data on the highly"
        " susceptible cultivar Chancellor at one site'",
        "read",
    ),
    "brischetto2020.piacenza": Dataset(
        "Airborne sporangia of P. viticola caught daily by a volumetric sampler, and lesions on"
        " leaves sampled on 108 dates and incubated 24 h, beside artificially inoculated vines,"
        " Piacenza campus vineyard, 2015-2017, with the vineyard station's weather (figures"
        " only)",
        "Brischetto et al. 2020, Front. Plant Sci. 11:1187 (read 2026-10-09): the logistic"
        " regression of infection on viable sporangia, and its 2.52 sporangia/m³/day threshold,"
        " are fitted to them. The predictor is computed with Blaeser & Weltzien's survival"
        " equations (eqs 1-2); the lesions are observed",
        "read",
    ),
    "salotti2022.piacenza": Dataset(
        "Downy mildew, powdery mildew and black rot severity (EPPO classes; AUDPC) on leaves and"
        " bunches of 16 unsprayed varieties, Merlot the susceptible control, Piacenza campus"
        " vineyard, 2017, 2018, 2019 and 2021, with the vineyard station's weather",
        "Salotti, Bove, Ji & Rossi 2022, Front. Plant Sci. 13:1017658 (read 2026-10-09). No"
        " formulation is recorded as fitted to them; variety resistance patterns",
        "read",
    ),
    "volpi2021.tuscany": Dataset(
        "Weekly presence or absence of downy mildew, powdery mildew and grey mould symptoms on"
        " Sangiovese in 112-179 vineyards a year of Tuscany's area-wide IPM network"
        " (Agroambiente.info), 2006-2019 except 2011; 18,857 downy mildew records (not in the"
        " paper)",
        "Volpi, Guidotti, Mammini & Marchi 2021, Ital. J. Agrometeorol. 2:57-69 (read"
        " 2026-10-09): their random forest and C5.0 classifiers are fitted to them, with"
        " ERA5-Land weather",
        "read",
    ),
    "kleb2026.hohenheim": Dataset(
        "Air temperature, RH and leaf wetness at 100, 130 and 160 cm in 12 canopy sites, at a"
        " border station (200 cm) and at the Metzingen network station 23 km away, with expert"
        " estimates of infected leaf area every three days over three periods, Pinot Meunier,"
        " Hohenheim, 2021",
        "Kleb et al. 2026, Research Square preprint (read 2026-10-09). No formulation is"
        " recorded as fitted to them; VitiMeteo-Plasmopara was run on each weather source and"
        " compared with the scores",
        "read",
    ),
    "firanjsremac2018.vrsac": Dataset(
        "Dates shoots reached 10 cm and first downy mildew symptoms at the plant-protection"
        " service's Vršac vineyard (VV), Serbia, 2012-2018, mostly untreated Šasla (Table 2),"
        " with the service's station weather",
        "Firanj Sremac, Lalić, Marčić & Dekić 2018, Atmosphere 9:484 (read 2026-10-09). No"
        " formulation is recorded as fitted to them; BAHUS-P (the 3-10 rule at 12 °C) was"
        " compared with them",
        "read",
    ),
    "valleggi2023.chianti": Dataset(
        "Leaves infected (yes or no) out of 400 per strategy and year at BBCH 85-89, five"
        " control strategies in one Sangiovese vineyard in Chianti Classico, 2018-2020 (the"
        " LIFE Green Grapes trial, Perria et al. 2022); 386, 34 and 318 infected under the"
        " biostimulant-only control",
        "Valleggi et al. 2023, Front. Plant Sci. 14:1117498 (read 2026-10-09): their Bayesian"
        " GLMM is fitted to the counts (Table 1), with no weather",
        "read",
    ),
    "maronefassolo2022.isolates": Dataset(
        "Infection frequency, sporulating area (5-13 days) and latent period of 72 northern"
        " Italian P. viticola isolates (2019) on leaf discs of Pinot noir, Bianca (Rpv3-1) and"
        " Mgaloblishvili (Rpv29) at 22 °C; oospore density and viability of three crosses",
        "Marone Fassolo et al. 2022, Plants 11:2619 (read 2026-10-10): a log-logistic curve of"
        " sporulating area is fitted to them per cultivar",
        "read",
    ),
    "bove2020resistance.piacenza": Dataset(
        "Leaf-disc monocycles at 20 °C on 15 partially resistant varieties and Merlot from three"
        " unsprayed vineyards (Piacenza, Monte Baldo), 2014-2016, at three leaf stages: infection"
        " frequency, latent period in degree-days, lesion size, sporangia per lesion, infectious"
        " period and infectivity",
        "Bove & Rossi 2020, Sci. Rep. 10:585 (read 2026-10-10). No formulation is recorded as"
        " fitted to them",
        "read",
    ),
    "calonnec2018.bordeaux": Dataset(
        "Powdery mildew infection efficiency, sporulation and colony size on leaf discs of known"
        " age, Cabernet Sauvignon (2005) and Merlot (2009-2010), Bordeaux, with leaf sugars and"
        " water",
        "Calonnec et al. 2018, Front. Plant Sci. 9:1808 (read 2026-10-10): exponential, logistic"
        " and Gaussian curves against leaf age are fitted to them",
        "read",
    ),
    "cortinas2020.galicia": Dataset(
        "Daily airborne Botrytis, Erysiphe and P. viticola spores from Hirst-type traps at"
        " Cenlle (Ribeiro) and O Mato (Ribeira Sacra), 2016-2018, with MeteoGalicia weather",
        "Cortiñas Rodríguez et al. 2020, Agronomy 10:219 (read 2026-10-10): lagged regressions"
        " of spore counts on weather are fitted to them",
        "read",
    ),
    "albelda2005.cenlle": Dataset(
        "Daily airborne Botrytis, Uncinula and P. viticola spores from a Lanzoni trap at Cenlle"
        " (Ribeiro), 15 April to 22 September 2004, with a station a few metres away",
        "Albelda et al. 2005, Bol. Micol. 20:1-8 (read 2026-10-10): lagged regressions of spore"
        " counts on weather are fitted to them",
        "read",
    ),
    "fernandezgonzalez2009.cenlle": Dataset(
        "Daily airborne Botrytis, Uncinula and P. viticola spores from a Lanzoni trap at Cenlle"
        " (Ribeiro), April-September 2007, with on-site weather; the 2007 season of Fernández"
        " González's 2011 thesis",
        "Fernández-González et al. 2009, Ann. Agric. Environ. Med. 16:263-271 (read 2026-10-10):"
        " lagged regressions on dew point are fitted to them",
        "read",
    ),
    "basso2020.geneva": Dataset(
        "Real-time particle counts of P. viticola and E. necator spores, with leaf wetness and"
        " weather, at five stations 400 m apart on 50 ha at Dardagny (2018-) and two at Pully"
        " (2019-), one in an untreated plot",
        "Basso et al. 2020, Rev. suisse Vitic. Arboric. Hortic. 52:334-349 (read 2026-10-10). No"
        " formulation is recorded as fitted to them; compared with VitiMeteo's outputs",
        "read",
    ),
    "chrelashvili1993.kvarely": Dataset(
        "First appearance of downy mildew at Kvarely (Kakheti, east Georgia), 1971-1986, beside"
        " the Müller curve's date for each year (Table 1)",
        "Chrelashvili 1993, Phytologia 75:124-133 (read 2026-10-10). No formulation is recorded"
        " as fitted to them; the Müller curve was run on them",
        "read",
    ),
    "pereira2018.marialva": Dataset(
        "Downy mildew leaf severity in untreated and sprayed BRS Vitória at Marialva, northern"
        " Paraná (602 m), four crops 2013-2015 (two with epidemics), first symptoms, with an"
        " in-vineyard station",
        "Pereira et al. 2018, Semina Ciênc. Agrár. 39:19-28 (read 2026-10-10). No formulation is"
        " recorded as fitted to them",
        "read",
    ),
    "chavarria2009.floresdacunha": Dataset(
        "Hourly airborne P. viticola sporangia from Burkard traps under plastic cover and in the"
        " open, Moscato Giallo at Flores da Cunha (541 m), 2005/06 and 2006/07, with the"
        " microclimate of both",
        "Chavarria et al. 2009, Rev. Bras. Frutic. 31:710-717 (read 2026-10-10). No formulation"
        " is recorded as fitted to them",
        "read",
    ),
    "czermainski2004.bentogoncalves": Dataset(
        "Downy mildew incidence and index by date in untreated and sprayed Tannat at Bento"
        " Gonçalves, 1995 and 1996, with first symptoms",
        "Czermainski & Sônego 2004, Ciênc. Rural 34:5-11 (read 2026-10-10). No formulation is"
        " recorded as fitted to them",
        "read",
    ),
    "romanazzi2024.marche": Dataset(
        "Downy mildew incidence, severity and McKinney index in untreated controls and"
        " treatments at Angeli di Varano, Castelplanio and Matelica (Marche), 2019-2021, with"
        " first symptoms",
        "Romanazzi et al. 2024, J. Clean. Prod. 451:142131 (read 2026-10-10). No formulation is"
        " recorded as fitted to them",
        "read",
    ),
    "casanovagascon2019.somontano": Dataset(
        "Weekly downy and powdery mildew degree of attack on untreated and treated Sauvignon"
        " blanc and resistant varieties at Barbastro (Somontano), 2016-2018, mostly in figures,"
        " with in-plot and regional weather",
        "Casanova-Gascón et al. 2019, Agronomy 9:738 (read 2026-10-10). No formulation is"
        " recorded as fitted to them; Goidanich's incubation and the UC Davis powdery index were"
        " checked against them",
        "read",
    ),
    "eisenmann2023.neustadt": Dataset(
        "Downy and powdery mildew incidence and severity on unsprayed grapes and leaves of"
        " resistant and susceptible cultivars at Neustadt an der Weinstraße, 2019-2021, with a"
        " station within 1 km",
        "Eisenmann et al. 2023, Plants 12:3120 (read 2026-10-10). No formulation is recorded as"
        " fitted to them",
        "read",
    ),
    "zanzotto2010.treviso": Dataset(
        "First downy mildew symptoms on leaves and bunches and season severity classes in"
        " untreated Merlot at Susegana (1999-2002) and Spresiano (2003-2009), Treviso province,"
        " with station weather",
        "Zanzotto & Borgo 2010, GDPM 2010 proceedings pp. 128-130 (read 2026-10-10). No"
        " formulation is recorded as fitted to them",
        "read",
    ),
    "magarey2010dispersal.nuriootpa": Dataset(
        "Downy mildew incidence and oil spots per leaf at 4-34 m downwind of a single inoculated"
        " source after one secondary event (29 November 1989), unsprayed vineyard near Nuriootpa,"
        " South Australia",
        "Magarey & Wicks 2010, GDPM 2010 proceedings pp. 103-105 (read 2026-10-10). No"
        " formulation is recorded as fitted to them; a trend line is drawn without an equation",
        "read",
    ),
    "lulu2008.jundiai": Dataset(
        "Leaf wetness from Campbell 237 sensors at four canopy positions in a Niagara Rosada"
        " vineyard and over turf at IAC Jundiaí, 11 November 2005 to 5 March 2006, with weather;"
        " downy mildew severity under six pruning dates, 2006-2007 (figures only)",
        "Lulu 2008, thesis, ESALQ/USP, and Lulu et al. 2008 (Sci. Agric. 65; Eng. Agríc. 28)"
        " (read 2026-10-10): wetness regressions and in-sample disease regressions are fitted to"
        " them",
        "read",
    ),
    "spotts1977.ohio": Dataset(
        "Minimum leaf wetness for light black rot infection at 10-32 °C on four cultivars in"
        " chambers (Table 1), and vineyard observations at Chesterville, Ohio, 1975-1976",
        "Spotts 1977, Phytopathology 67:1378-1381 (read 2026-10-10): VitiMeteo black rot's"
        " infection thresholds come from it, through Ellis et al. 1986",
        "read",
    ),
    "gonzalezdominguez2015.epidemics": Dataset(
        "Incidence and severity of Botrytis bunch rot at harvest in 21 untreated epidemics in 12"
        " Italian vineyards, 2009-2014, with hourly on-site weather",
        "González-Domínguez et al. 2015, PLoS ONE 10:e0140444 (read 2026-10-10): its"
        " discriminant analysis of the model's outputs is fitted to them",
        "read",
    ),
}

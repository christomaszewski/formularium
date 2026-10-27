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
    "bindi1997.mondeggi": Dataset(
        "Shoot leaf number and leaf area, cluster counts and dry weights of leaves, stems,"
        " stalks and berries of 20-year-old Sangiovese on 420 A at Mondeggi-Lappeggi (Chianti),"
        " sampled every three weeks from May to September 1992, with daily temperature and"
        " radiation from sensors about 10 m away; the phenology indicators were tested on"
        " Conegliano's 1965-1970 observations of 123 cultivars (Calò & Costacurta 1973)",
        "Bindi, Miglietta, Gozzini, Orlandini & Seghi 1997, Vitis 36:67-71, 'Materials and"
        " methods' (l. 29-64; literature/bindi1997); observed; one season behind every fitted"
        " constant",
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
    "ramos2010.penedes": Dataset(
        "Budbreak, bloom, veraison and harvest dates of dry-farmed Xarel·lo in two Alt Penedès"
        " vineyards over 14 seasons (1996-2009; the dates themselves are not printed), with"
        " daily rain and temperature from four observatories (Vilafranca del Penedès from"
        " 1952; Sant Sadurní d'Anoia, La Granada and Els Hostalets de Pierola from 1996) and"
        " a stage-by-stage water balance (P minus FAO-56 crop ET) at Els Hostalets",
        "Ramos & Martínez-Casasnovas 2010, VIII International Terroir Congress, pp. 3-23 to"
        " 3-28, 'Materials and methods' (l. 88-106) and Table 2 (p. 3-27, read 2026-10-13 in"
        " the page image; literature/ramos2010); the ET is a model's, the dates are observed",
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
    "alleweldt1975.flein": Dataset(
        "Budburst (first leaflets out of the wool), flowering start (25 % of caps shed) and"
        " end, shoot length, inflorescence and flower counts and berry set of Riesling on"
        " Kober 5 BB at three Württemberg plots (Flein Steinboden 202 m, Flein Tonboden 208 m,"
        " Stetten 253 m), 1969-1972, with grape-zone air and 20 cm soil temperature from"
        " recording thermographs, light by photocell, rain and gravimetric soil water",
        "Alleweldt & Hofäcker 1975, Vitis 14:103-115, section 2 (l. 60-120; literature/"
        "alleweldt1975); observed; the methods say 1968-1972, the results 1969-1972",
        "read",
    ),
    "barrios2004.vilafranca": Dataset(
        "The spring outcome of downy mildew at Vilafranca del Penedès for each year 1984-2004,"
        " in words (scarce and late primary infections, or general ones from the first rains,"
        " with the rain in mm in some years), beside EPI's winter value and the Catalan plant"
        " health service's verdict on the forecast (17 right, 2 partly, 2 wrong); INCAVI's"
        " station weather",
        "Barrios & Reyes 2004, Phytoma 164, table p. 4 (read 2026-10-13 in the page image,"
        " literature/barrios2004); the outcomes are the service's observations, the EPI values"
        " a model's",
        "read",
    ),
    "brook1992.auckland": Dataset(
        "Dates downy mildew lesions were first seen in a Black Hamburgh vineyard at Mt Albert,"
        " Auckland, each season 1971/72 to 1981/82 (none in 1972/73), with the wet period the"
        " author postulates as the primary infection (its dates, net rain in mm and mean air"
        " temperature), and the share of leaves mildewed 50 days on in five seasons beside"
        " that period's rain and night minima",
        "Brook 1992, N. Z. J. Crop Hortic. Sci. 20:37-49, Tables 7 and 10 (pp. 44 and 47,"
        " read 2026-10-13 in the page images, literature/brook1992); the first-lesion dates"
        " are observed, the infection periods the author's reading of the rain record by"
        " Galet 1977's two-wet-days rule",
        "read",
    ),
    "daux2012.harvest_dates": Dataset(
        "An open database of 380 grape harvest-date series (16,921 dates, 93 % French, from"
        " 1354 in Burgundy), grouped into 27 regional composites; harvest dates are decisions"
        " of authorities and growers, not stage observations",
        "Daux et al. 2012, Clim. Past 8:1403-1418, sections 2-3 and Table 1 (literature/daux2012);"
        " held at the GDR2968 phenology database and NOAA's World Data Center for"
        " Paleoclimatology, free for research",
        "read",
    ),
    "chacon2021.lamancha": Dataset(
        "Bud break, flowering, veraison and maturity (50 % of sampled vines, lots of four) of"
        " Tempranillo and Chardonnay, two series 2000-2019 plus two or three plots in half the"
        " years, at 663 m in La Mancha DO, with the Argamasilla de Alba station's daily weather"
        " (gaps filled from Tomelloso) and grape composition at ripening",
        "Chacón-Vozmediano, Martínez-Gascueña & Ramos 2021, Agron. Sustain. Dev. 41:24,"
        " section 2.2 (l. 84-142, 180-182; literature/chacon2021); observed; the data are IRIAF's"
        " and the Ministry's, on request",
        "read",
    ),
    "caffarra2010.conegliano": Dataset(
        "Chardonnay budburst (BBCH 07), flowering (BBCH 65) and veraison (BBCH 85) at Conegliano"
        " (Susegana 1969-2000, Spresiano 2001-2007; 39 years, the calibration series) and at"
        " San Michele all'Adige, Mezzocorona, Cembra (Trentino) and Carpeneto (Piedmont),"
        " 1986-2007, with daily mean temperatures (gaps filled by regression on nearby stations)",
        "Caffarra & Eccel 2010, Int. J. Biometeorol. 54:255-267, 'Phenological and meteorological"
        " data' and Table 1 (l. 74-88, 154-158; literature/caffarra2010); observed, the filled"
        " temperatures computed",
        "read",
    ),
    "caffi2013.piedmont": Dataset(
        "Sporulating and non-sporulating downy mildew lesions counted every second or third day"
        " on unsprayed vines at Grugliasco (Moscato) and Neive (Barbera), Piedmont, 2008-2010:"
        " 100 assessments, 58 with new lesions, 61,921 lesions, with hourly weather from the"
        " regional service's stations at the vineyard edges",
        "Caffi et al. 2013, Phytopathology 103:64-73, Methods and Results (read 2026-10-12,"
        " literature/caffi2013); observed, no model dated the assessments",
        "read",
    ),
    "ramos2018.ribera": Dataset(
        "Budbreak, bloom, véraison and maturity dates (Baggiolini stages C, I, M, N) of"
        " Tempranillo and Cabernet Sauvignon in four Ribera del Duero plots, 2004-2015,"
        " from the Consejo Regulador (a stage's date is when it was the most frequent in"
        " the area), with daily and hourly weather from the Aranda de Duero station (798 m)",
        "Ramos, Jones & Yuste 2018, OENO One 52(1):31-44, 'Materials and methods' (l. 173-227;"
        " literature/ramos2018); the dates are the Consejo's observations, the P minus ETc"
        " balance a model's",
        "read",
    ),
    "pola2017.urussanga": Dataset(
        "Budburst (50 % green tips), full bloom and harvest (50 % picked) of Goethe on Paulsen"
        " 1103 at Epagri's Urussanga station, Santa Catarina (humid subtropical, 49 m), seven"
        " seasons (2007-2011, 2013, 2014; three plants a stage), with the station's daily"
        " readings about 100 m away (Ta = (Tmax + Tmin + T9 + 2 T21)/5; hourly values by"
        " interpolation)",
        "Pola et al. 2017, Rev. Ciênc. Agrár. 40(1):236-245, 'Materiais e métodos' (l. 68-138;"
        " literature/pola2017); observed, the hourly temperatures interpolated",
        "read",
    ),
    "nendel2010.coolwinter": Dataset(
        "Budbreak dates (BBCH 09; at four sites BBCH 07 plus two days) of Riesling and"
        " Müller-Thurgau at 13 vineyards in Germany, France, Luxembourg, Slovakia and Czechia,"
        " 20 site-variety series within 1967-2008 (Table 1), with each site's station"
        " temperatures (Trier's lapse-corrected)",
        "Nendel 2010, Int. J. Biometeorol. 54:231-241, 'Data' and Table 1 (l. 142-183, 245-267;"
        " literature/nendel2010); observed except the BBCH 07 conversions",
        "read",
    ),
    "parker2013.database": Dataset(
        "Parker et al. 2011's flowering and veraison database, updated: 81 varieties, 2,278"
        " flowering and 2,088 veraison observations, 1960-2007, 123 locations, mostly French"
        " research stations and collections, with each site's daily temperatures",
        "Parker et al. 2013, Agric. For. Meteorol. 180:249-264, section 2.1 (l. 156-171;"
        " literature/parker2013); observed stage dates, no model",
        "read",
    ),
    "martinezluscher2016.croatia": Dataset(
        "Budburst, flowering and fruit-maturity dates of Chasselas Doré, Riesling Italico,"
        " Istrian Malmsey and Plavac Mali in nine plantings at five Croatian stations"
        " (42.75-46.03 °N), 307 seasonal records 1961-2013 from the Croatian Meteorological and"
        " Hydrological Service via PEP725, with E-OBS gridded temperature and rain (hourly"
        " values rebuilt by chillR)",
        "Martínez-Lüscher et al. 2016, Front. Environ. Sci. 4:48, 'Materials and methods'"
        " (l. 141-190; literature/martinezluscher2016); observed dates, gridded weather",
        "read",
    ),
    "pinarey2021.ribeiro": Dataset(
        "Budburst (BBCH 09) and flowering (BBCH 61) dates of Albariño, Godello, Loureira and"
        " Treixadura, 2008-2019, in one Ribeiro DO vineyard (140 m; 20 plants a variety, a"
        " stage when half show it, visits every 6-7 days), with daily temperatures from a"
        " station in the vineyard",
        "Piña-Rey et al. 2021, Plants 10:502, section 4.1 (l. 1005-1046; literature/pinarey2021);"
        " observed, no model; the data are not shared",
        "read",
    ),
    "ruml2016.karlovci": Dataset(
        "Onset of budburst, flowering, veraison and harvest of 20 cultivars (7 red, 13 white; 20"
        " vines each) in the Novi Sad faculty's collection at Sremski Karlovci, Serbia,"
        " 1986-2011, with the national service's daily Tmax and Tmin at the site 1981-2007"
        " (the relations fitted on 1986-2007)",
        "Ruml et al. 2016, J. Agric. Sci. 154:186-206, 'Materials and methods' (l. 138-208;"
        " literature/ruml2016); observed, no model",
        "read",
    ),
    "sanchezdemiguel2011.madrid_toledo": Dataset(
        "Leaves per shoot and the largest, smallest and mean leaf area of primary and lateral"
        " shoots of Syrah, Cabernet Sauvignon, Cabernet franc, Merlot and Tempranillo at El"
        " Socorro (Madrid, 730 m) and Syrah at a Toledo vineyard (488 m), 4,856 shoots over"
        " 2003-2007 (the text says three years), late April to early October, with 25 primary"
        " and 25 lateral leaves a cultivar measured by image analysis for the main-vein lines",
        "Sanchez-de-Miguel et al. 2011, Table 1 (p. 204) and pp. 204-205; the raw values are"
        " not printed",
        "read",
    ),
    "su2022.turpan": Dataset(
        "Leaf area index of 12-year-old Thompson Seedless at Tie-Tier village, Turpan"
        " (42.87 °N, 89.20 °E, 32.8 m), under six drip quotas of 637.5-1,215 mm, three vines a"
        " treatment on 15 sampling days from 1 April to 1 October 2009, LAI from leaf counts and"
        " a vein-length allometry; degree-days above 10 °C with a 38 °C cap",
        "Su et al. 2022, Tables 1-2 (pp. 4, 7); the per-treatment LAI series are in Table 2",
        "read",
    ),
    "schumacher2024.freiburg": Dataset(
        "Downy mildew severity (percent of infected berries, 13 classes) of clusters of Pinot"
        " Noir, Souvignier Gris, Cabernet Cortis and Solaris inoculated at seven BBCH stages"
        " (53-55 to 81-83) on 42 potted vines a cultivar in an open greenhouse at Freiburg im"
        " Breisgau, 2020-2023 (1,856 clusters), rated 4 weeks after inoculation; leaf-disc"
        " sporulation of leaves at the same stages, 2021-2023, 36 discs a cultivar and stage;"
        " the 2021 untreated field trial (Pinot Noir over 90 %)",
        "Schumacher et al. 2024, Scientific Reports 14: 915, Methods and Results (pp. 2-6;"
        " literature/schumacher2024); observed, no calendar dates, means in the text only",
        "read",
    ),
    "zhu2021.marlborough": Dataset(
        "Sauvignon blanc phenology (budburst, flowering, veraison), yield, bunch number, berry"
        " weight, TSS and TA at four Marlborough long-term sites from 2004 (other regions and"
        " varieties from 2014); the retained-node-number trial at Rowley Crescent 2006-2010"
        " (leaf appearance, leaf area, biomass, NSC, yield); the post-harvest defoliation trial"
        " 2008-2012; MRL_Rapaura irrigation trial 2001-2005 (canopy, light interception, leaf"
        " and shoot biomass)",
        "Zhu et al. 2021, in silico Plants 3(2): diab021, Table 1 and 'Data sets' (l. 465-546;"
        " literature/zhu2021); observed, TSS from an empirical water-content relation",
        "read",
    ),
    "schmidt2019.geisenheim": Dataset(
        "Three Riesling vines (clone 198-30 Gm on SO4, planted 2012, 0.9 x 1.8 m) of the"
        " VineyardFACE at Geisenheim, digitised in 3D at E-L 12, 15 and 26 in"
        " May-June 2018; 50 primary shoots in the bud-position analysis; bud break 2018 at DOY"
        " 109-111; DWD station 1580 daily weather 1927-2018, about 200 m away",
        "Schmidt, Bahr, Friedel & Kahlen 2019, Agronomy 9(8): 426, 'Materials and methods'"
        " (l. 139-216, 331-349, 468-470; literature/schmidt2019); observed",
        "read",
    ),
    "vrignonbrenas2022.montpellier_pots": Dataset(
        "Leaf area per plant (5 plants a treatment, 2-7 dates an experiment), dry matter by"
        " organ, trunk and root carbohydrate and SPAD of potted Sauvignon blanc on SO4 grown"
        " outdoors at Montpellier, five experiments on three batches 2017-2019, N supply 0-8.61"
        " g per plant from budburst to veraison, SPAD 11.8-41.6; stage thermal times in Table 2",
        "Vrignon-Brenas et al. 2022, J. Exp. Bot. 73(5): 1385-1401, 'Materials and methods'"
        " (l. 129-176; literature/vrignonbrenas2022); observed; the data are available on"
        " request only",
        "read",
    ),
    "tsialtas2008.thessaly": Dataset(
        "324 leaves of Cabernet Sauvignon, 10-year-old vines on 1103 Paulsen and SO4 under"
        " three irrigation regimes (100 % ETc, 50 % ETc, none), sampled at bunch closure,"
        " veraison and ripeness in 2005 and 2006 near Thessaly (39°48' N, 22°27' E, 190 m),"
        " leaf area, length, width and perimeter by image analysis",
        "Tsialtas, Koundouras & Zioziou 2008, Photosynthetica 46(3): 452-456, 'Materials and"
        " methods' (l. 81-107; literature/tsialtas2008); observed",
        "read",
    ),
    "fernandezgomez2013.chinchon": Dataset(
        "Cabernet Sauvignon on 41 B planted 2005, 3 x 1 m VSP, Chinchon (Madrid, 550 m), 2010"
        " and 2011, four deficit regimes: stage days of the year (50 % rule, E-L 4, 23, 27, 35,"
        " 38) 111, 153, 165, 214, 280 in 2010 and 98, 143, 152, 203, 258 in 2011; Ite (base 10"
        " °C from 1 April) at flowering 328.0 and 339.8 °Cd; shoot length 110 and 103 cm at"
        " fruit set and 166 and 160 cm at growth stop (day 218 and 187); year-mean LAI 1.2,"
        " external leaf area 0.8 m²/m²; 1.9-2.0 bunches a shoot",
        "Fernandez Gomez 2013, PhD thesis, Universidad Politecnica de Madrid, Tabla 2.6"
        " (l. 3627-3630), Tabla 3.1 (l. 5879-5880), Tabla 3.2 (l. 6067-6068), Tabla 3.3"
        " (literature/fernandezgomez2013); observed, LAI computed from leaf counts",
        "read",
    ),
    "linares2009.el_socorro": Dataset(
        "Syrah 2005 and Merlot 2006-2007 at El Socorro, Comunidad de Madrid, under cover crops"
        " (Cent3, CNA), tillage and herbicide: weekly length of marked shoots (4 plants a"
        " treatment and block) and shoot velocity in cm per degree-day; leaf area from midrib"
        " lines, one leaf in three; LAI and external leaf area SA at flowering, veraison and"
        " harvest, with LAI/SA; Ite (daily mean above 10 °C, summed from 1 April) at the dated"
        " samplings of 2007 and observed budburst and veraison dates 2007-2008",
        "Linares Torres 2009, thesis, Tabla 24 (l. 9214), Tabla 48 (l. 12817-12844), Tablas"
        " 50-52 (l. 13126-13245) and Ecuaciones 11-13 (l. 6612-6677; literature/linares2009);"
        " observed, leaf area computed from midrib length",
        "read",
    ),
    "barajas2010.duero": Dataset(
        "Tempranillo on 110 R (planted 2000, Royat cordon) at four Duero vineyards, Castrillo de"
        " Duero, Pollos, Rodilana and Toro, at 1.2, 1.5 and 1.8 m spacing, 2005-2007: stage"
        " dates (50 % rule; budburst, bloom, fruit set, veraison, harvest, mean of the three"
        " spacings) in 2006 (Castrillo 14 Apr, 10 Jun, 17 Jun, 2 Aug, 26 Sep; Pollos 3 Apr,"
        " 2 Jun, 9 Jun, 25 Jul, 20 Sep; Rodilana 7 Apr, 7 Jun, 14 Jun, 30 Jul, 18 Sep; Toro"
        " 6 Apr, 5 Jun, 10 Jun, 31 Jul, 13 Sep) and veraison in 2007 (21, 16, 18 and 17 Aug);"
        " LAI (shoot leaf area by midrib length, 12, 15 and 18 shoots a vine) 1.33-3.43 and"
        " external leaf area SA 0.76-1.08 m²/m² at veraison, SA/LAI 0.28-0.61; leaf area on"
        " shoot length in 2006, y = 17.1873 x + 842.363 for all spacings (units not printed)",
        "Barajas Tola 2010, PhD thesis (Spanish; the cover names the Escuela Tecnica Superior"
        " de Ingenierias Agrarias, no university), Tabla II.20 (l. 5017-5028), Tablas"
        " III.9-III.12 (l. 7095-7147), Tabla III.15 (l. 7439-7442), Tabla II.23 (l. 5410-5433)"
        " (literature/barajas2010); observed, LAI and SA computed from shoot measurements",
        "read",
    ),
    "pallas2008.montpellier_pots": Dataset(
        "Pot experiments at Montpellier (SupAgro-INRA) with Syrah (clone 174) and Grenache N"
        " (clone 224) on Fercal, 2003, 2004 and 2006, cluster loads 0C, 1C, 2C and 6C, 12 plants"
        " a treatment: leaves unfolded on the primary axis against thermal time to 1200 °Cd"
        " above 10 °C (n 481 Syrah, 441 Grenache N), leaf length and area (n 182 and 135), leaf"
        " number and area of secondary axes (n 42 and 37), secondary-axis lag and phytomer"
        " counts, plant state at 1200 °Cd (Table 2), cluster dry weight and cluster-to-leaf"
        " ratio (1.98 to 16.7 m²/kg); water kept above 75 % of transpirable soil water",
        "Pallas et al. 2008, Physiologia Plantarum 134: 49-63, as Manuscript 1 of Pallas 2009,"
        " 'Materials and methods' and Tables 1-2 (l. 2220-2510; literature/pallas2009); observed",
        "read",
    ),
    "mcartney1998.ohio": Dataset(
        "Shoot leaf area by sampling date, 10 to 50 days after bud break, of 'DeChaunac' and"
        " 'Seyval' vines under 80 % shade cloth from flowering or unshaded (eight vines a"
        " treatment, three shoots a vine), single-leaf areas against lamina length and width,"
        " and in Chapter 9 the shoot length, diameter, leaf number and leaf area of field"
        " Seyval (n 45 shoots) and shoot elongation by period; Ohio",
        "McArtney 1998, PhD dissertation, The Ohio State University, Ch. 4 (l. 2196-2230,"
        " 2420-2480), Fig. 4.4 (p. 47), Ch. 9 (l. 6455-6490), Fig. 9.1 (p. 143);"
        " literature/mcartney1998; observed",
        "read",
    ),
    "cola2014.piacenza": Dataset(
        "Observed BBCH by shoot every 3-4 days, destructive shoot samples (five shoots on 12"
        " dates in 2011: leaf number, leaf weight, leaf area), shoot and leaf counts, canopy"
        " width and height, light interception on 8 days in 2011 (3,480 line-bar readings a"
        " date) and cluster yield of Barbera AT 84 on 420A (planted 1999) at Piacenza,"
        " 2011-2012, low density cane-pruned Guyot and high density spur cordon; validation"
        " 2003-2007 on other vines of the same vineyard for final leaf area and yield (from"
        " Bernizzoni et al. 2009), with ARPA-SIM weather at Pianello Val Tidone",
        "Cola et al. 2014, Agricultural and Forest Meteorology 184:117-136, sections 2.1-2.3"
        " (l. 111-277; literature/cola2014); observed, the raw series not printed (Table 1"
        " inputs, Tables 4-9 statistics and figures only)",
        "read",
    ),
    "lebon2004.montpellier": Dataset(
        "Four experiments with Grenache N at Montpellier, no water deficit: pots of clone 226 on"
        " Fercal (expt 1 in a glasshouse, expt 2 outside; 1999-2000 in the text, 2000-2001 in the"
        " tables) and a vineyard of clone 70 on 110 Richter planted 1987 (expts 3 and 4, 1999 and"
        " 2000): leaves initiated, unfolded and expanded on the main stem against thermal time"
        " above 10 °C (n 52, 186 and 42), leaf appearance rate against mean temperature (n 376,"
        " periods of 9-15 days at 13.0-23.8 °C), leaf length and area (93 leaves), internode"
        " length, branch leaves, harvest totals",
        "Lebon et al. 2004, Annals of Botany 93(3): 263-274, 'Materials and methods', Tables 1-3,"
        " Figs 3-4 (l. 92-470; literature/lebon2004); observed",
        "read",
    ),
    "louarn2007.montpellier_pots": Dataset(
        "Four pot experiments at Montpellier 2002-2005 with Grenache N and Syrah on Fercal (0.050"
        " m3 pots outdoors, one branch a plant, water above 70 % of pot capacity): phytomer-type"
        " sequences of 60 shoots a genotype, unfolded leaf counts on the main stem and branches,"
        " lamina length and leaf area (n 135-515 a fit), internode length and volume, branch"
        " durations, and plant state at 1200 °Cd (primary phytomers, axis lengths, leaf area)",
        "Louarn et al. 2007, Annals of Botany 99(3): 425-437, 'Materials and methods', Tables 1,"
        " 2 and 5 (l. 138-440, 826-835; literature/louarn2007); observed",
        "read",
    ),
    "forster2016.five_sites": Dataset(
        "Hourly and daily station series at five sites, each split into a calibration and a"
        " validation period: De Bilt, Netherlands (2 m; 1961-1990, 1991-2014), Ny-Alesund,"
        " Svalbard (11 m; 1993-2004, 2006-2011), Obergurgl, Austria (1938 m; 2000-2007,"
        " 2008-2014; project data, not free), Rio de Janeiro (5 m; 2003-2008, 2009-2014) and"
        " Tucson airport (779 m; 1973-1993, 1994-2014); temperature, wind, humidity and, by"
        " site, precipitation and radiation; observed",
        "Forster et al. 2016, Geosci. Model Dev. 9:2315-2333, Sect. 2 and Table 1 (l. 208-260;"
        " literature/forster2016); humidity methods H2 and H3 and the radiation constants are"
        " fitted on the calibration period, H1 and H4 need no fit",
        "read",
    ),
    "pidoto2023.germany": Dataset(
        "Germany: DWD sub-daily rainfall at 699 stations for 400 catchments (30 to over 20,000"
        " km2), common period January 2006 to December 2020; HYRAS v4.0 gridded daily mean,"
        " minimum and maximum temperature, relative humidity and global radiation, 1976-2015,"
        " for the k-NN resampling; 40 DWD sub-daily reference climate stations (20 with global"
        " radiation) for validation, 100 realisations of 15 years; observed",
        "Pidoto & Haberlandt 2023, Hydrol. Earth Syst. Sci. 27:3957-3975, Sect. 3 and 4"
        " (l. 519-587; literature/pidoto2023); the hourly step uses MELODIST's forms that need"
        " no hourly observations, set from the catchment midpoint only",
        "read",
    ),
    "gorner2021.saxony_debilt": Dataset(
        "Hourly and daily DWD data for six Saxon stations including Dresden-Klotzsche (222 m)"
        " and Fichtelberg (1213 m), September 1995 to August 2014, and KNMI De Bilt (2 m),"
        " January 1981 to December 2014 (validation against MELODIST on 1991-2014): mean"
        " temperature, precipitation, sunshine duration, relative humidity and wind speed;"
        " DWD objective weather patterns from 1979 as a filter; observed",
        "Gorner et al. 2021, Theor. Appl. Climatol. 143:241-265, Sect. 2 and Table 1 (l. 145-207,"
        " 1440; literature/gorner2021); a resampling method with no fitted parameter, the"
        " observed days are its pool",
        "read",
    ),
    "brunetto2018.santana": Dataset(
        "Dry mass of Cabernet Sauvignon leaves (and pruned stems) in 20 x 20 cm litter bags of"
        " 1 mm mesh, 30 g each, on the soil surface in the row and between rows of a vineyard at"
        " Santana do Livramento (Rio Grande do Sul, Brazil), bags laid 16 April 2009 and five per"
        " material and position collected at 0, 30, 60, 90, 120, 150, 180 and 210 days; monthly"
        " 2009 rain and air temperature from an unnamed station; observed",
        "Brunetto et al. 2018, Rev. Cienc. Agrar. 61:1-10, Sect. 2 and Table 4 (l. 75-141,"
        " 368-398; literature/brunetto2018); the exponential decay is fitted per position to the"
        " percent of mass remaining; Table 5 (stems) not used",
        "read",
    ),
    "penaquinones2020.prosser": Dataset(
        "Daily maximum and minimum air temperature from 4 thermistors at 0.5 m and 3 at 1.2 m in a"
        " Chardonnay canopy (rows north-south, 2,035 vines/ha) at Roza Farm, Prosser, Washington,"
        " against a standard station at 1.7 m about 410-415 m away, 10 December 2015 to 30 June"
        " 2017 (n 478 days compared; 437 maxima and 436 minima in the regressions); berry-cluster"
        " thermocouples on the east and west sides in 2016 and 2017; observed",
        "Pena Quinones et al. 2020, PLOS ONE 15(6):e0234436, Methods and Fig. 5 (l. 136-258;"
        " literature/penaquinones2020); the four daily regressions are fitted on this series;"
        " the S1 data file was not checked",
        "read",
    ),
    "paulescu2023.payerne": Dataset(
        "BSRN 1-minute global, diffuse and direct irradiance at Payerne, Switzerland (46.815 N,"
        " 6.944 E), the year 2020, 193,294 records with solar elevation above 5 degrees (D_FIT),"
        " on which M1 and M2 are fitted; observed. The test set (D_TEST) is 36 BSRN stations,"
        " one year each from 2002 to 2021, nearly 7 million records, with no overlap in time"
        " with the fit",
        "Paulescu & Paulescu 2023, Appl. Sci. 13:6558, Sect. 2 (l. 186-259; literature/"
        "paulescu2023); the fit statistics (R2 0.917 for M2, 0.929 for M1) do not name their"
        " dataset; BSRN access date 15 May 2023, licence not printed",
        "read",
    ),
    "laiti2018.bolzano": Dataset(
        "Hourly global, diffuse and direct irradiance from 1-minute data averaged to 15 minutes at"
        " Bolzano city airport (46.458 N, 11.329 E, 265 m), Adige Valley, 2011-2014; 10,310 valid"
        " hours (solar elevation 7 degrees or more) of which 2,098 orographically shadowed; sky"
        " view factor 0.788; observed",
        "Laiti et al. 2018, Atmosphere 9:117, Sect. 2 and Table 5 (l. 152-193, 292-293, 498-508;"
        " literature/laiti2018); the local coefficients are fitted on the same hours that"
        " validate them, no split stated",
        "read",
    ),
    "lecap2022.quincy": Dataset(
        "Hourly temperature from 37 Weenat anti-frost sensors across the Quincy vineyard (about"
        " 700 ha, flat, mean altitude 122 m), installed December 2019, daily minimum from 18:00 to"
        " 18:00, 34 frost nights in 2020-2022; Bourges synoptic data 22 km away, AROME night"
        " cloud forecast, 5 m DEM; observed. Data available from the corresponding author on"
        " request; no repository, no licence",
        "Le Cap et al. 2022, Research Square preprint rs-1932104/v1, Sect. 2 (l. 178-200,"
        " 790-796; literature/lecap2022); a preprint, the published version was not read; no"
        " formulation is fitted to it",
        "read",
    ),
    "pipan2021.victoria": Dataset(
        "Daily minimum and maximum temperature from one Tinytag TGP-4500 logger in a Stevenson"
        " screen at each of four Victorian vineyards (Yarra Burn, Whitlands, Coldstream and"
        " Rutherglen), 30-minute records, four seasons from 2015-16 to 2018-19, against SILO's 0.05"
        " degree (about 5 km) interpolated grid of about 4,600 Bureau of Meteorology stations;"
        " observed and interpolated. Logger data from the authors on request; the SILO licence is"
        " not printed",
        "Pipan et al. 2021, Front. Plant Sci. 12:635299, Sect. 2 and Table 2 (l. 160-191;"
        " literature/pipan2021); no formulation is fitted to it; Table 2 read by eye",
        "read",
    ),
    "sanderson2022.stations": Dataset(
        "Nine Sogrape Vinhos weather stations in vineyards of the upper Douro Valley, Portugal"
        " (80 to 624 m), 15-min temperature, humidity, leaf wetting, wind and rain at 2 m,"
        " January 2011 to December 2017 (Pinhao-Porto 2014-2017 only); the Leda pair (Leda 2,"
        " 318 m, and Leda 3, 163 m) gave 834 cold-pool nights; observed; not open",
        "Sanderson et al. 2022, J. Appl. Meteorol. Climatol. 61:1893-1904, Sect. 2 and Table 1"
        " (l. 107-190, 301-368; literature/sanderson2022); not fitted to TAF, which uses the SRTM"
        " 90 m DEM; daily values of the same stations are in ECA&D",
        "read",
    ),
    "kuwagata2024.kumamoto": Dataset(
        "Rice-canopy dew and micrometeorology at the NARO Kyushu Okinawa center, Kumamoto,"
        " Japan (32.87°N, 130.74°E, 76 m; rice 'Hinohikari' transplanted 11 June 2003): leaf dew"
        " by layer on four nights (three at booting, one at grain filling), with solar and"
        " downward longwave radiation, 2 m air temperature and humidity and wind;"
        " 18-27 August and 24 September-3 October 2003; observed; DOI 10.17632/fmvr43csy3.3",
        "Kuwagata et al. 2024, Agric. For. Meteorol. 354:109911, Sect. 2.3 and 3 (l. 643-723;"
        " literature/kuwagata2024); the same observations as Maruyama et al. 2023"
        " (literature/maruyama2023); the multilayer reference was checked against them",
        "read",
    ),
    "flerchinger2009.sites": Dataset(
        "Measured downward longwave, solar radiation, air temperature and humidity, mostly two"
        " years of 30-min data, at the 14 sites of Flerchinger et al. 2009's initial evaluation"
        " (Table 4): nine AmeriFlux sites (Santa Rita AZ, Campbell River BC, Niwot Ridge CO,"
        " Morgan Monroe IN, Goodwin Creek MS, Duke Forest NC, Black Hills SD, Wind River WA,"
        " Willow Creek WI), Reynolds Mountain ID, Brooks field IA, Yucheng, Ganzi and Nagqu"
        " (China), 1982-2006; observed",
        "Flerchinger et al. 2009, Water Resour. Res. 45:W03423, Sect. 3 and 4.3, Tables 4, 8"
        " and 9 (page images, 2026-10-19; literature/flerchinger2009): the clearness-index"
        " limits for complete cloud and clear sky were optimised on these sites; seven more"
        " AmeriFlux sites tested them independently",
        "read",
    ),
    "quenol2004.vinho_verde": Dataset(
        "Tiny Talk logger series in two Vinho Verde vineyards about 30 km apart, Arcos de"
        " Valdevez (Lima valley) and Moncao/Troviscoso (Minho valley), Portugal: 16 + 8 open-air"
        " thermometers at 1.50 m and 12 sheltered temperature and humidity loggers (10 + 2), every"
        " 15 min, February to October 2003; three nights analysed (15-16 and 16-17 February,"
        " 3-4 May); humidity recorded but no result printed; observed; data not offered",
        "Quenol et al. 2004, Norois 193:117-132, Sect. 2 and Tables 1-3 (l. 251-331;"
        " literature/quenol2004); not fitted by a formulation here",
        "read",
    ),
    "nakamura2005.corvallis": Dataset(
        "Air temperature at 1 m from an Onset HOBO Pro thermistor in a naturally ventilated Davis"
        " 7714 multiplate shield and from an aspirated platinum RTD (RM Young 43408), with wind and"
        " four-component radiation at 1 m and 1.5 m, over flat grassland at the Hyslop"
        " Experimental Station, Corvallis, Oregon (44°38' N, 123°12' W); dataset A 14 March to"
        " 30 August 2002 (fits the correction), dataset B 15 July to 30 August 2003 (tests it);"
        " 30-min means of 300-s HOBO samples; observed; not offered",
        "Nakamura & Mahrt 2005, J. Atmos. Oceanic Technol. 22:1046-1058, Sect. 2 and Table 2"
        " (l. 222-224, 293-298; literature/nakamura2005); not a model's output, the aspirated"
        " sensor's own radiative error being assumed small (l. 470-472)",
        "read",
    ),
    "magarey2006.geneva_adelaide": Dataset(
        "Visual and sensor leaf wetness in three grape canopies, canopy about 1.8 m: Chardonnay"
        " at Geneva, New York, 1997 (LAI 1.0; 15 unpainted and 3 painted Campbell 237"
        " sensors), Concord at Geneva, 1998 (LAI 2.0; 15 painted sensors) and Cabernet Franc"
        " in the Adelaide Hills, South Australia, 1998 (LAI 1.0; 15 painted sensors); water"
        " seen on 15 tagged leaves of each of 3 vines at 5 canopy positions, with canopy"
        " temperature and humidity, rain, wind and net radiation logged on site every 60 s;"
        " counts of dew and rain periods differ between its text, Table 1 and Tables 4-5;"
        " observed; not offered",
        "Magarey, Seem & Russo 2006, Agric. For. Meteorol. 139:361-372, Sect. 2 and Table 1"
        " (literature/magarey2006b); SWEB (magarey2006.sweb) was validated on them, not"
        " fitted; the lab Cl values came from Concord and Chancellor leaves",
        "read",
    ),
    "reuveni1998.golan": Dataset(
        "Leaf discs (12 mm) of field Cabernet Sauvignon cut from three shoot positions"
        " counted from the tip (top 3 + 4, middle 15 + 16, bottom 29 + 30), drop-inoculated"
        " with Plasmopara viticola (5 ul of 2e4 sporangia per ml), severity 0-4 at 4, 5 and 7"
        " days and sporangia per cm2 of disc; field ratings by leaf number in 1993 and 1995"
        " and a greenhouse spray test by leaf number; Golan Research Institute, Israel;"
        " observed; the raw counts are not given",
        "Reuveni 1998, J. Phytopathol. 146:525-530, Methods and Table 1 (pp. 526, 528;"
        " literature/reuveni1998)",
        "read",
    ),
    "dhakar2025.awn": Dataset(
        "Leaf wetness from PHYTOS 31 sensors at 45° (normalised 0-1, wet at 0.4) and air"
        " temperature, humidity, wind and rain at 1.5-2 m (ATMOS 41), 15-min means, from ten"
        " AgWeatherNet stations in Washington State, January 2019 to February 2023; the"
        " station Havillah alone fitted the model's parameters; observed; on request",
        "Dhakar et al. 2025, Agric. For. Meteorol. 363:110399, Sects 2.1, 2.3.6 and Table 2"
        " (literature/dhakar2025); the same station is in the validation",
        "read",
    ),
    "tarara2009.prosser": Dataset(
        "Fresh mass of clusters, leaves and stem, shoot length and leaves per shoot of"
        " own-rooted Concord (Vitis labruscana) near Prosser, Washington, 10 shoots from each"
        " of four vines every 14-21 days from before bloom to 3-4 weeks before maturity,"
        " 2002-2006 (n 1,360 shoots), shoot length on 54 vines, under deficit irrigation to"
        " 2004 and full irrigation in 2005; degree-days above 10 °C from 1 January by"
        " trapezoidal integration of 15-minute air temperature",
        "Tarara, Blom, Shafii, Price & Olmstead 2009, HortScience 44(2):334-340, 'Materials"
        " and methods' (l. 86-151; literature/tarara2009); observed, the degree-days computed",
        "read",
    ),
    "schrader2020.iowa": Dataset(
        "Budbreak, bloom, veraison (50 % of buds, flowers, berries) and harvest maturity (by"
        " soluble solids, pH and acidity) of Frontenac, La Crescent, Marquette, Petit Ami and"
        " St. Croix (18 vines each) at Iowa State's research station near Gilbert, 2011, 2013"
        " and 2014, with hourly air and soil temperature and solar radiation; 144 Marquette"
        " vines 400 m away in 2019 for validation",
        "Schrader et al. 2020, HortScience 55(12):1912-1925, 'Materials and methods'"
        " (l. 125-216; literature/schrader2020); observed, the response (days remaining) is"
        " the stage date minus the day",
        "read",
    ),
    "ramos2022.rioja": Dataset(
        "Flowers-separated, veraison and harvest dates (50 % of surveyed plants) of"
        " non-irrigated Carignan in two Rioja DOCa plots (428 and 460 m), 2008-2020, with the"
        " La Rioja government's Logroño stations (408 and 456 m) and grape composition at"
        " harvest; soil water from the VSIM model",
        "Ramos & Martínez de Toda 2022, Int. J. Biometeorol. 66:1067-1078, 'Materials and"
        " methods' (l. 115-128, 176-180; literature/ramos2022); the dates observed, the soil"
        " water a model's",
        "read",
    ),
    "ramos2023.rueda": Dataset(
        "Budbreak, flowering, veraison and ripening dates of Verdejo (nine plots), Viura and"
        " Sauvignon Blanc (two each) in Rueda DO (700-930 m), 2008-2021, from the Consejo"
        " Regulador, with the Rueda (709 m) and Medina del Campo (726 m) stations; four"
        " non-irrigated Verdejo plots used, two to calibrate and two to validate",
        "Ramos & Yuste 2023, Agronomy 13:146, section 2 (l. 142-146, 266, 306-308;"
        " literature/ramos2023); observed; not public (l. 775)",
        "read",
    ),
    "pouget1988.bordeaux": Dataset(
        "Budburst dates of 22 cultivars at INRA's Bordeaux station (Pont-de-la-Maye), 18 years"
        " within 1970-1988, and of the four reference cultivars (Perle de Csaba, Traminer,"
        " Merlot, Ugni blanc) over 1961-1987 (printed as 17 years), with the station's daily"
        " maxima and minima; the rate law behind them from growth-chamber tests at 5, 10, 15,"
        " 20 and 25 °C whose years and bud counts are not printed",
        "Pouget 1988, Conn. Vigne Vin 22:105-123, pp. 107-111 and Table VII (p. 116, read"
        " 2026-10-13 in the page image; literature/pouget1988); the dates observed, the S sums"
        " a model's",
        "read",
    ),
    "rossi2008pp.discs": Dataset(
        "Oospore germination, 1999-2003, as infection of grape leaf discs (280 a sample) by"
        " oospores from 10 g leaf-fragment samples taken weekly, late March to early July, in"
        " a 500 m2 Barbera plot at Asti, Piedmont, with hourly weather from a station in the"
        " vineyard; 124 fitted cases",
        "Rossi et al. 2008, Plant Pathol. 57:216-226, Methods and Results (read 2026-10-12,"
        " literature/rossi2008pp); the assays are observed, and the paper's field infection"
        " dates, used only as a check, were placed by Rossi et al. 2002's method",
        "read",
    ),
    "douillet2023.grandeferrade": Dataset(
        "Airborne Plasmopara viticola sporangia per m3 from six rotating-arm samplers read by"
        " LAMP three times a week, 1 April to 30 September 2019-2021, at INRAE's Grande"
        " Ferrade vineyard (Villenave-d'Ornon), three sprayed and three minimally sprayed"
        " plots, with weekly leaf and cluster ratings and the station's hourly weather",
        "Douillet 2023, thesis, chapter 3 (l. 3606-3607, 3838-3851, 3872 of the text;"
        " literature/douillet2023); the counts are observed, daily values are split evenly"
        " across 48-72 h samples, and the 'total' series adds survivors computed with"
        " Brischetto 2020's mortality",
        "read",
    ),
    "fraga2016.portugal": Dataset(
        "Field-observed day of year of budburst, flowering and veraison for 16 varieties: 14"
        " at the Dois Portos experimental vineyard, Lisbon (series of 11 to 22 years within"
        " 1990-2011, Table 1), Loureiro at Arcos de Valdevez, Vinhos Verdes (2003-2012), and"
        " Touriga-Franca at Ervedosa do Douro (2001-2011, from the Estação de Avisos do"
        " Douro), with monthly means of daily Tmin, Tmax and Tmean from each site's station"
        " (the Douro station about 20 km away)",
        "Fraga et al. 2016, J. Agric. Sci. 154:795-811, Table 1 (p. 798, read 2026-10-13 in"
        " the page image) and sections 'Phenological data' and 'Climate data'"
        " (literature/fraga2016); stages scored by eye with OIV descriptors, no model",
        "read",
    ),
    "didevarasl2026.sardinia": Dataset(
        "Budburst (47), full bloom (42) and veraison (29) dates of Cannonau at 17 Sardinian"
        " sites within 1991-2020 (University of Sassari records; mean day of year 95, 144 and"
        " 205), with daily weather from a 2.2 km COSMO-CLM downscaling of ERA5 (a model"
        " product, not station records)",
        "Didevarasl et al. 2026, Int. J. Biometeorol. 70:273, 'Data collection and"
        " preparation' (read 2026-10-13 in the publisher's HTML; literature/didevarasl2026);"
        " the site list and the dates themselves are in the supplement, on request",
        "read",
    ),
    "garciatejera2022.plots": Dataset(
        "Weekly Baggiolini-scale phenology (bud break, bloom, fruit set, veraison) of"
        " Tempranillo and Chardonnay at Raïmat (Lleida), Tempranillo at La Orden (Badajoz,"
        " 2005-2017), Touriga Nacional at Vilariça (Douro) and Aglianico at Mirabella Eclano"
        " (Campania), 2017-2020 at the three, with nearby station weather (Raïmat 1997-2017,"
        " La Orden 1998-2005, Vilariça 1985-2017, Mirabella Eclano 1978-2017 as the historical"
        " records)",
        "García-Tejera et al. 2022, OENO One 56(4):173-183, section 3 and Table 1 (l. 317-407;"
        " literature/garciatejera2022); observed, no model",
        "read",
    ),
    "ferguson2014.prosser": Dataset(
        "Cold hardiness (differential thermal analysis) of primary buds of 23 Vitis genotypes"
        " at Prosser and Paterson, Washington, since 1988, with budbreak dates since 1988",
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
    "savary2009.bordeaux": Dataset(
        "Downy and powdery mildew severity on leaves and clusters of Cabernet franc at seven"
        " crop stages (53-89), unprotected, limited and continuous protection, six replicates,"
        " at Couhins and Latresne (Bordeaux), 2006 and 2007, with on-site weather",
        "Savary et al. 2009, Phytopathology 99:930-942 (read 2026-10-13; Tables 4-5 in the page"
        " images 2026-10-20): its logistic leaf curves and cluster-transfer coefficients are"
        " fitted to them",
        "read",
    ),
    "moyer2014.cleistothecia": Dataset(
        "Season-total ascospore release from Erysiphe necator cleistothecia collected in New"
        " York and stored outdoors at Geneva NY, Chatsworth NJ, Prosser WA and North Carolina,"
        " assayed through winter and spring, 2005-2009, with site weather; and Chardonnay fruit"
        " severity against cleistothecia per vine at Geneva, 2002-2003",
        "Moyer et al. 2014, Am. J. Enol. Vitic. 65:315-324 (read 2026-10-20): its release model"
        " (Eq. 2) is fitted to the New York populations overwintered in New York",
        "read",
    ),
    "oriolani2015.mendoza": Dataset(
        "Weekly powdery mildew incidence on Chenin clusters from flowering to veraison in one"
        " untreated plot at EEA INTA Mendoza, six seasons (2001/02-2009/10), with hourly canopy"
        " weather; 40 daily increment rates classed nil, moderate or severe",
        "Oriolani et al. 2015, Rev. FCA UNCuyo 47(2):197-211 (read 2026-10-20): its ordinal"
        " logistic models are fitted to them",
        "read",
    ),
    "lewis2017.ppdb_dissipation": Dataset(
        "Measured dissipation half-lives (DT50, min, max and mean, days) of pesticides in and on"
        " plant matrices, 2,782 rows from 1,390 studies (1980-2017), with plant, matrix, in or on,"
        " field or covered, place and reference; 165 grape rows (139 fruit, 24 leaves)",
        "Lewis & Tzilivakis 2017, Data 2:28, supplementary file (CC-BY), from a Wayback capture of"
        " MDPI's file (read 2026-10-20); values from the cited studies, first-order where computed",
        "read",
    ),
    "erincik2003.ohio": Dataset(
        "Phomopsis viticola lesions per leaf and internode severity on potted Catawba and Seyval"
        " after inoculation at 5-35 °C and 5-20 h of wetness, three replicate runs, 1998-1999;"
        " and natural-rain field inoculations in two Ohio vineyards, 2000-2001",
        "Erincik et al. 2003, Plant Dis. 87:832-840 (read 2026-10-08; Tables 1-2 in the page"
        " images 2026-10-20), and Erincik's 2002 thesis: the generalized Beta model is fitted to"
        " the chamber data and tested on the field inoculations",
        "read",
    ),
    "franceschi2020.soybean_raters": Dataset(
        "Visual severity estimates by 37 inexperienced raters (unaided, then aided by an old or"
        " a new standard area diagram set) on 50 soybean rust leaflet images of 0.25-84 %"
        " severity, against image-analysis severity",
        "Franceschi et al. 2020, Plant Pathol. 69:495-505 (read 2026-10-20): the rater-error"
        " models of its Table 1 are fitted to them; files on OSF (3zmv8), licence not printed",
        "read",
    ),
    "fantke2013.halflives": Dataset(
        "4,442 measured pesticide dissipation half-lives in plants (333 substances, 183 plants),"
        " 1,030 of them with the study's mean air temperature, collated from the literature",
        "Fantke & Juraske 2013, Environ. Sci. Technol. 47 (not held), as used by Fantke et al. 2014"
        " (read 2026-10-20), whose temperature and half-life regressions are fitted to them",
        "trail",
    ),
    "schultz1993.geisenheim": Dataset(
        "Plastochron index and leaf plastochron index of 5-10 sun and shade White Riesling"
        " shoots recorded every 1-3 d from bud break to harvest at Geisenheim, 1988, with daily"
        " maximum and minimum air temperature",
        "Schultz 1993, Vitis 32:197-205 (read 2026-10-26): Eq. 3 is fitted to them by PROC"
        " NLIN in three periods of thermal time, and again on mean daily temperature",
        "read",
    ),
    "lopes2005.estremoz": Dataset(
        "Primary and lateral leaf areas, leaf counts and the areas of the largest and smallest"
        " leaf of 180 Aragonez shoots (107 with laterals) on six dates from April to August at"
        " Estremoz, Alentejo, 1997",
        "Lopes & Pinto 2005, Vitis 44:55-61 (read 2026-10-26): Eqs 8-11 are fitted to them;"
        " validated on four independent sets (Aragonez at Évora 1997, Cabernet-Sauvignon 2002,"
        " Touriga Nacional 1994 and Jaen 2001)",
        "read",
    ),
    "wermelinger1990.waedenswil": Dataset(
        "Leaf area, dry mass, water and nitrogen of primary leaves, laterals, shoots and grapes"
        " from six Pinot noir shoots sampled weekly to mid June and then every 3-5 weeks at"
        " Wädenswil, 1988, against degree-days above 10 °C",
        "Wermelinger & Koblet 1990, Vitis 29:15-26 (read 2026-10-26): its polynomials for water"
        " and nitrogen on leaf age and its shoot-against-leaf line are fitted to them; the data"
        " behind the closed Wermelinger et al. 1991 demographic model",
        "read",
    ),
    "weyand2006.geisenheim": Dataset(
        "Leaf area per vine and canopy segment, light interception grids, leaf gas exchange,"
        " night respiration, pre-dawn water potential, yield and sugar of minimal and"
        " cane-pruned Riesling at Geisenheim, 2002 and 2003",
        "Weyand & Schultz 2006, Vitis 45:105-114 (read 2026-10-26): a measurement paper; its"
        " per-zone polynomials and leaf-weight regressions are fitted to them, coefficients not"
        " printed",
        "read",
    ),
    "kovaleski2018.geneva": Dataset(
        "Low-temperature exotherms of dormant buds of eleven Vitis genotypes sampled through"
        " the 2014/15-2016/17 winters at Geneva NY and held at 2-30 °C, and budbreak stage of"
        " fully chilled buds at 2-22 °C; the chill axis is the North Carolina chill model's"
        " output on NEWA hourly weather, not an observation",
        "Kovaleski, Reisch & Londo 2018, AoB PLANTS 10:ply066 (read 2026-10-26 from the JATS"
        " text): the deacclimation rate, potential and budbreak relations are fitted to them",
        "read",
    ),
    "coertze2002.wound_infection": Dataset(
        "Wounds infected out of 120 on Dauphine berry cheeks at bunch closure, harvest and after"
        " cold storage, by freshly or previously deposited dry airborne Botrytis conidia under"
        " dry, moist and wet regimes for 24 h at 22 °C, two runs, Stellenbosch",
        "Coertze & Holz 2002, S. Afr. J. Enol. Vitic. 23:72-77 (read 2026-10-26): analysed by"
        " ANOVA only; no formulation is fitted to them",
        "read",
    ),
    "cheraiet2021.herault": Dataset(
        "Tracer spray deposits on PVC collectors through nine vineyard plots at Grabels (2016)"
        " and Villeneuve-lès-Maguelone (2017), Hérault, four stages a year from BBCH 14 to 85,"
        " with 2D LiDAR canopy height, width and beam interception",
        "Cheraïet et al. 2021, Comput. Electron. Agric. 189:106402 (read 2026-10-26): the decile"
        " models are calibrated on 2017 (n 40) and validated on 2016 (n 16)",
        "read",
    ),
    "castex2020.traps": Dataset(
        "Weekly male Lobesia botrana pheromone-trap catches at 12 sites from Andalusia to"
        " Alsace, 1997-2016 (51 of 90 site-years kept), their 10 % and 50 % flight dates by"
        " cumulative sum, and daily temperatures from stations within 10-15 km",
        "Castex et al. 2020, Ecol. Model. 420:108946 (read 2026-10-26): the Lobesia Generic"
        " Model is calibrated on a random 75 % and validated on 25 %, then refitted on all",
        "read",
    ),
    "mariani2007.alghero": Dataset(
        "BBCH stage dates of Cabernet Sauvignon and Chardonnay at Olmedo (Alghero), 2006, with"
        " hourly temperatures made from Alghero's daily maxima and minima; stages 71 and 77 of"
        " 2000-2004 for validation",
        "Mariani, Failla & Capece 2007, Ital. J. Agrometeorol. 2007(3):39-44 (read 2026-10-26):"
        " the four BBCH-on-NHH regressions are fitted to the 2006 data",
        "read",
    ),
    "phinopoulos2015.lisbon": Dataset(
        "Areas of every leaf, vein lengths and leaf counts of 210 fruiting Syrah shoots (laterals"
        " from the fourth date, n 120) sampled on seven dates from April to July 2013 at the ISA"
        " vineyard, Tapada da Ajuda, Lisbon",
        "Phinopoulos, Cadima & Lopes 2015, GiESCO proceedings pp. 385-388 (read 2026-10-26):"
        " Eqs 3-5 are fitted to them by least squares",
        "read",
    ),
    "pieri2003.bordeaux_diffuse": Dataset(
        "Daily diffuse and global radiation measured at Bordeaux over two years, 121 days, source"
        " not named",
        "Pieri & Gaudillère 2003, Vitis 42:77-82 (read 2026-10-26): Eq. 3, the diffuse fraction"
        " on the clearness index, is fitted to them (r² 0.93)",
        "read",
    ),
    "rossouw2016.stellenbosch": Dataset(
        "Manganese residue and fluorescent-pigment coverage on apple seedling leaves sprayed with"
        " mancozeb and rained on at 5 mm/h for 0, 1, 5, 10 and 15 mm, five trees and four"
        " repeats, Stellenbosch; and coverage against spray volume and concentration",
        "Rossouw 2016, MSc thesis, Stellenbosch University (read 2026-10-26): the exponential"
        " wash-off curves and the Hoerl deposition curves are fitted to them",
        "read",
    ),
    "delbac2026.grades": Dataset(
        "Yearly grades 0-6 (0 none; 1-3 local epidemics; 4-6 general) of downy and powdery"
        " mildew, black rot, grey mould, rotbrenner and two grape moths, read from the French"
        " agricultural warning service's bulletins and yearly summaries: Bordeaux 1941-2023,"
        " Champagne and Vaucluse; Recherche Data Gouv 10.57745/HM3HBE, Etalab 2.0",
        "Delbac et al. 2026, Data in Brief 64:112397 (read 2026-10-22, Europe PMC full text;"
        " the grade table and scale opened). No formulation is recorded as fitted to them;"
        " Agrarium could history-match season-level severity against them (its TRUTH-METHOD"
        " part 2)",
        "read",
    ),
    "bregaglio2022.bulletins": Dataset(
        "8,816 weekly downy mildew infection-risk classes (1-5) read by six evaluators from the"
        " bulletins of eight Italian regional plant protection services, 31 provinces,"
        " 2012-2017, and 1,689 BBCH observations; Mendeley Data 10.17632/3jsh4y2bw4.1, CC BY"
        " 4.0. The classes were set partly from the bulletins' own model-based indications",
        "Bregaglio et al. 2022, Data in Brief 43:108409 (read 2026-10-22, Europe PMC full"
        " text, l. 78): 'This dataset has been used to calibrate and evaluate the MISFITS-DSS'"
        " (Bregaglio et al. 2022, J. Environ. Manage. 317:115365, note `bregaglio2022`), whose"
        " infection parameters were chosen by accuracy against these classes. MISFITS has no"
        " record here",
        "read",
    ),
    "sanitatvegetal.penedes_avisos": Dataset(
        "The weekly plant-health warning bulletins for the Penedès (Servei de Sanitat Vegetal,"
        " Generalitat de Catalunya, relayed by the ADV of Cellers Domenys), February 2015 to"
        " September 2026: where and when the first downy mildew oil spots were found each season"
        " (first reports 29 April to 4 June; none in 2019), with spray advice, model notes and"
        " other pests. Posted at www.cellersdomenys.com/uploads/advs/penedes/; no licence stated",
        "Read 2026-10-22 by the main session in all 139 files (ten 2018 scans OCR'd), the"
        " first-spot sentences checked at their lines; the season table is in Agrarium's"
        " research note gaps-and-datasets (retry section). No formulation is recorded as fitted"
        " to them. The spots are found in treated vineyards under a first-spot prize, so the"
        " dates are of detection",
        "read",
    ),
    "kennelly2007.geneva": Dataset(
        (
            "Date of first symptoms of downy mildew in unsprayed Chancellor vines (240-300 "
            "flower clusters examined every 1-5 days from three weeks before bloom), with the "
            "rain and temperature of the infection event judged responsible (Table 1); USA, "
            "New York: Geneva (NYSAES) 1981, 1983, 1985-1997, 2001-2004; also Watkins Glen, "
            "Wayne, Ovid, Dundee in 2001-2003; 1981-2004 (29 dated site-years in Table 1; one "
            "'No disease', Dundee 2003); plots: unsprayed vines, 12-15 vines (Geneva) or 9-11 "
            "contiguous vines (commercial sites); weather: Rainfall and temperature from the "
            "nearest available station, 2 to 20 km away; Table 1 prints only the rain (mm) "
            "and temperature during the attributed infection event, incubation days and "
            "degree-days; access: Table 1 printed in the paper; station records not given; "
            "licence: not stated (Phytopathology, APS); downloadable now: no"
        ),
        (
            "Kennelly, Gadoury, Wilcox, Magarey, Seem 2007. Phytopathology 97:512-522.. Found "
            "for Agrarium D58 (literature/requests/datasets-d58.md), 2026-10-27; how checked: "
            "read"
        ),
        "read",
    ),
    "caffi2009.italy100": Dataset(
        (
            "Date of first downy mildew oil spots (window between last negative and first "
            "positive visit) in unsprayed plots; Italy: Piedmont, Lombardy (Oltrepo Pavese), "
            "Emilia-Romagna, Marche, Basilicata, Sardinia (100 vineyards); 1995-2007 (1-6 "
            "vineyards a year); plots: unsprayed plot of at least 500 m2 inspected at least "
            "weekly from budburst; 9 vineyards had no disease; weather: hourly T, RH, rain, "
            "wetness: stations in the vineyards in Piedmont and Lombardy; otherwise the "
            "nearest regional station within 15 km; interpolated 5x5 km grids in Emilia- "
            "Romagna from 2001; access: Table 1 of the paper (vineyards by region/year, "
            "onsets); not deposited; Rossi group (Univ. Cattolica Piacenza); licence: not "
            "stated (J. Plant Pathol.); downloadable now: no"
        ),
        (
            "Caffi, Rossi, Bugiani, Spanna, Flamini, Cossu, Nigro 2009. J. Plant Pathol. "
            "91:535-548.. Found for Agrarium D58 (literature/requests/datasets-d58.md), "
            "2026-10-27; how checked: read"
        ),
        "read",
    ),
    "fedele2025.piacenza_litters": Dataset(
        (
            "Primary lesions per plant (weekly or twice weekly counts from 1 April) on potted "
            "Merlot over five experimental leaf litters; oospores per g litter; Italy, "
            "Piacenza, Univ. Cattolica campus; 2021, 2022, 2023; plots: potted/experimental "
            "plants over litter of five infestation levels; this is a controlled inoculum- "
            "dose experiment, not a natural epidemic; weather: iMetos station in the "
            "experimental vineyard: hourly T, RH, rain, leaf wetness, wind (Table of seasonal "
            "values, figures); access: 'raw data ... made available by the authors, without "
            "undue reservation'; no repository; licence: article CC BY; data on request; "
            "downloadable now: no"
        ),
        (
            "Fedele, Maddalena, Furiosi, Rossi, Toffolatti, Caffi 2025. Front. Plant Sci. "
            "16:1524959.. Found for Agrarium D58 (literature/requests/datasets-d58.md), "
            "2026-10-27; how checked: read"
        ),
        "read",
    ),
    "taibi2023.castellarquato": Dataset(
        (
            "Disease incidence and severity (%) of downy and powdery mildew on leaves and "
            "bunches in untreated and treated plots at four stages per year (BBCH 69, 75, 83, "
            "89); AUDPC; Italy, Emilia-Romagna, Castell'Arquato vineyard (44.857 N, 9.856 E); "
            "2020, 2021, 2022; plots: untreated control plus 6 resistance inducers and a "
            "copper+sulfur reference; 48 untreated records (disease x portion x stage x year) "
            "and 32 treatment means; weather: Daily weather per season (Apr-Sep, 184 days a "
            "year): leaf wetness (hours), rain (mm), temperature, relative humidity; station "
            "location presumably the vineyard (README does not say); access: Zenodo "
            "10.5281/zenodo.15077508, six small CSVs "
            "(NT_UCSC_RIs_DiseaseIncidenceSeverity.csv untreated, ...Treatment.csv, "
            "...AUDPC.csv, ...WeatherdataYear1-3.csv) plus a Readme with a data dictionary; "
            "files about 1-7 KB each; licence: CC BY 4.0 (README 2.1 and Zenodo record); "
            "downloadable now: yes"
        ),
        (
            "Fedele & Rossi 2025, Zenodo; for Taibi, Fedele, Salotti, Rossi 2023, Agronomy "
            "13(12):2959.. Found for Agrarium D58 (literature/requests/datasets-d58.md), "
            "2026-10-27; how checked: read"
        ),
        "read",
    ),
    "dina2023.murfatlar": Dataset(
        (
            "Downy mildew frequency, intensity and degree of attack (G.A. %, Buffara/Caffi "
            "scales) on leaves and bunches, twice-weekly, untreated vs treated Sauvignon "
            "blanc; first-spot dates 17.05.2021 (BBCH 15) and 14.06.2022; stomatal "
            "conductance after first spots; Romania, Murfatlar (Black Sea coast), one "
            "vineyard (ERA-Net MERIAVINO project); 2021, 2022 (one wet, one dry); plots: "
            "untreated vs treated variant, n=1 plantation; caveat: leaves in the untreated "
            "variant were moistened artificially and the ground flooded to stimulate "
            "infection; weather: iMetos 3.3 station in the vineyard centre; leaf-wetness "
            "sensor (minutes of wetness, humidity); only in figures (Fig 1) and text means, "
            "no table; access: table/figures in the paper (Figs 1-4); raw numbers on request "
            "to authors; no repository seen; licence: not stated (Univ. Agron. Sci. Bucharest "
            "Scientific Papers Series B 67(2):231-?, open PDF); downloadable now: no"
        ),
        (
            "Dina, Ene, Artem, Ranca & Hnatiuc 2023, The influence of the climate on the "
            "evolution of diseases in the Sauvignon Blanc variety in the conditions of the "
            "years 2021-2022 in Murfatlar, Sci. Pap. Ser. B Hort. 67(2). Found for Agrarium "
            "D58 (literature/requests/datasets-d58.md), 2026-10-27; how checked: read "
            "(abstract, methods, results text; figures not digitised)"
        ),
        "read",
    ),
    "reis2013.bentogoncalves": Dataset(
        (
            "Weekly (2000/01) or per-visit leaf severity, incidence on 100 leaves and bunch "
            "severity (0-5), untreated control vs conventional vs warning-timed; first- "
            "symptom dates 19 Oct 2000, 14 Oct 2002, 10 Oct 2003; Brazil, Bento Gonçalves RS, "
            "Embrapa Uva e Vinho, cv. Isabel (V. labrusca); seasons 2000/01, 2002/03, "
            "2003/04; plots: control without fungicide, 4 replicates, 3 rows x 3 vines per "
            "plot; weather: Colpam-40 logger with leaf wetness and mean air temperature in a "
            "control plot, daily DDSV; values mostly in figures/tables of critical periods, "
            "not a raw series; access: table/figures in the paper; held as PDF in the library "
            "(reis2013); raw series would be on request; licence: not stated (Summa "
            "Phytopathologica; check SciELO page); downloadable now: no"
        ),
        (
            "Reis, Sônego & Mendes 2013, Summa Phytopathol. 39:10-15. Found for Agrarium D58 "
            "(literature/requests/datasets-d58.md), 2026-10-27; how checked: read (this "
            "session's fetch of the open PDF); a note reis2013.md also exists in literature/"
        ),
        "read",
    ),
    "sendhilvel2020.coimbatore": Dataset(
        (
            "Disease incidence (PDI) in an unsprayed plot against weather, Muscat; logistic "
            "fit; India, Mathampatti, Coimbatore, Tamil Nadu; 2014-2017; plots: unsprayed "
            "control plus spray treatments, 3-4 replicates; weather: automatic station on "
            "site, RH, temperatures, rain, leaf wetness, dew, radiation every 10 min; access: "
            "paper tables only (PDI 78.83 control); raw station files not offered; licence: "
            "not stated; downloadable now: no"
        ),
        (
            "Sendhilvel, Marimuthu & Geethalakshmi 2020, Madras Agric. J. 107(10-12):422-428. "
            "Found for Agrarium D58 (literature/requests/datasets-d58.md), 2026-10-27; how "
            "checked: trail (note sendhilvel2020.md, read in full 2026-10-09) plus the "
            "abstract in the library text"
        ),
        "trail",
    ),
    "agoston2020.bacskiskun": Dataset(
        (
            "Fruit-bunch downy mildew occurrence (%) by severity class, two dated counts a "
            "year; Hungary, Bács-Kiskun County; 2009 (average), 2010 (epidemic); plots: "
            "commercial; inspectors' reports via the NIR system; weather: none printed (a "
            "cited 10:10 rain rule only); access: table/figures in the paper; NIR records not "
            "open; licence: not stated; downloadable now: no"
        ),
        (
            "Ágoston 2020, Gradus 7(1):12-15. Found for Agrarium D58 "
            "(literature/requests/datasets-d58.md), 2026-10-27; how checked: trail (note "
            "agoston2020.md) and library text"
        ),
        "trail",
    ),
    "fournier2025.epicure_ifv": Dataset(
        (
            "IFV EPIcure network: about 1200 untreated controls (2x5 vines), weekly visual "
            "incidence and severity of downy mildew on leaves and bunches since 2002; France "
            "(the paper uses Nouvelle-Aquitaine / Bordeaux; the network is national); "
            "2002-2022 and later; plots: untreated controls, about 1200; weather: none in "
            "EPIcure's observations (the web page links Météo-France forecasts); weather "
            "would be added from a station or reanalysis; access: vignevin-epicure.com (login "
            "form; the paper says its records were 'downloaded from' it); not open; licence: "
            "not stated; 'Tous droits réservés'; downloadable now: no"
        ),
        (
            "Fournier et al. 2025, Environ. Microbiome 20 (doi 10.1186/s40793-025-00691-9); "
            "EPIcure web page. Found for Agrarium D58 (literature/requests/datasets-d58.md), "
            "2026-10-27; how checked: read (paper full text via Europe PMC, saved; web page "
            "saved as text)"
        ),
        "read",
    ),
    "margaritis2019.spata": Dataset(
        (
            "Downy mildew (and powdery mildew, grey mould) at the end of the 2018 season in "
            "copper-sprayed Malagouzia and Savvatiano at Spata, Attica, Greece: 'actual "
            "presence' 0-5 % and 0-3 % (printed pp. 120, 139), no unit, no dates, no "
            "interval; one passage (p. 101) calls the vines unprotected, against the copper "
            "record. Weather: a gaiasense station in the vineyard (T, RH, rain, leaf wetness "
            "at canopy height) and a vite.net station, March-September 2018, in graphs only; "
            "step not printed. No weather or disease numbers in the appendix; no licence or "
            "data offer printed. Not usable for scoring."
        ),
        (
            "Margaritis, E. 2019, MSc thesis, Agricultural University of Athens "
            "(kalligeneia.aua.gr handle 10329/6933), in Greek. Read 2026-10-27 for Agrarium "
            "and Cooptera D58 (literature/requests/theses-d58.md) from an OCR of the PDF (its "
            "text layer is garbled), pp. 77-79, 85, 101, 117-120, 131-132, 139; the 0-5/0-3 % "
            "and the step read in the page images"
        ),
        "read",
    ),
    "leoni2026.geneva_thesis": Dataset(
        (
            "Leoni, S. 2026, PhD thesis, Université de Genève (Sc. 5993, 315 pp., directors "
            "Kasparian and Dubuis): spore trapping, multiplex qPCR, real-time holographic "
            "detection and modelling of downy mildew, powdery mildew and grey mould; oospore "
            "maturation modelled 'from more than twenty years of climatic observations' "
            "(abstract). What disease and weather records it holds, and on what terms, not "
            "read: the PDF did not come through a script."
        ),
        (
            "Archive ouverte UNIGE, unige:193385, doi 10.13097/archive-ouverte/unige:193385; "
            "the landing page read 2026-10-27 (rendered: authors, pages, abstract, a "
            "downloadable main file; no licence shown) for D58. Not fetched: for Chris to "
            "download from the page"
        ),
        "snippet",
    ),
    "kleb2026.hohenheim_thesis": Dataset(
        (
            "Kleb's thesis combines Kleb et al. 2022 (ch. 4) and the 2026 preprint (ch. 5) "
            "word for word, with a 2020 plot (ch. 6, record kleb2026.hohenheim2020) and an "
            "inoculation method (ch. 7). 2021, Hohenheim, Pinot Meunier: infected leaf area "
            "by eye every 3 days in three canopy zones of three plots, each unsprayed for "
            "downy mildew only in its own three-week period (BBCH 75-79, 79-83, 83-87). "
            "Weather: T, RH (Testo 174H) and leaf wetness (PHYTOS 31, counts) every 10 min at "
            "100, 130, 160 cm, against a station 75 m away (180 cm; ch. 5: a border station "
            "at 200 cm, wetness at 160 cm) and one 23 km away. Data in figures only; the data "
            "statements say 'Not applicable'; no repository. Thesis CC BY-NC-SA 4.0 (landing "
            "page; not printed in the PDF)."
        ),
        (
            "Kleb, M. 2026, PhD thesis, Universität Hohenheim (hohPublica handle "
            "123456789/19105), 'Site-specific forecasting and early detection of Plasmopara "
            "viticola in Vitis vinifera'. Read 2026-10-27 for D58 "
            "(literature/requests/theses-d58.md): chapters 1-3 and 8 in the text layer, "
            "chapters 4-7 (page images) by OCR of PDF pp. 26-78, Tables 2-4 in the page "
            "images; 23 quotes checked at their lines"
        ),
        "read",
    ),
    "kleb2026.hohenheim2020": Dataset(
        (
            "Downy mildew in an unsprayed 250 m2 plot of 33-year-old Pinot Meunier at "
            "Hohenheim, Stuttgart, 2020: visible damage every 3rd day, first symptoms at the "
            "end of July, 30-40 % incidence a month later; T and RH (Testo 174H) and leaf "
            "wetness (PHYTOS 31; wet above 435 counts, a period wet if mean RH above 85 % "
            "when they conflicted, not validated) every 10 min at 1.3 m, a station 75 m away; "
            "thermal images 22 July to 8 September 2020. Figures only (Figs 5-8); not "
            "obtainable."
        ),
        (
            "Kleb 2026, PhD thesis, Universität Hohenheim, chapter 6 (pp. 55-60), read "
            "2026-10-27 by OCR of the page images for D58; not in the held notes kleb2022 and "
            "kleb2026"
        ),
        "read",
    ),
}

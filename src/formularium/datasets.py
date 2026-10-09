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
        " the paper itself not read)",
        "Rossi et al. 2005 (Riv. Ital. Agrometeorol. 3:7-13; read 2026-10-08 by the paper"
        " search session): incubation is 'a function of temperature and relative humidity"
        " (Goidanich et al., 1957)', and the model 'uses two regression equations relating"
        " temperature to the length of incubation, at two extreme levels of relative"
        " humidity'. That those regressions, Rossi 2008's eqs 8-9, were fitted to Goidanich's"
        " data is inferred, not stated; Rossi et al. 2002, where the fit is described, is not"
        " held. The engine's Goidanich table is these data, as Porras Soriano 2006 prints them."
        " Zachos 1959 (read 2026-10-08, p. 250) describes Casarini 1957's own curves for"
        " Emilia, at high and at low humidity, from artificial and natural inoculations;"
        " Casarini co-wrote the table, so its data are probably his (inferred, not stated)",
        "trail",
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
    "rafaila1968": Dataset(
        "Detached leaves in a polythermostat at 5-30 °C and 100% humidity, Bucharest"
        " 1963-1965; and incubation by leaf age in the Minis and Blaj vineyards",
        "Rafaila, Sevcenco & David 1968, Phytopathol. Z. 63:328-336, Tables 3 and 4 (read"
        " 2026-10-08 in the copy Chris supplied). They cite neither Müller nor Goidanich",
        "read",
    ),
    "blaeser1979": Dataset(
        "Blaeser & Weltzien 1979 (P. viticola infection data)",
        "Brischetto et al. 2021, Figure 2 caption (D): the Magarey response's parameters were"
        " estimated from Blaeser & Weltzien 1979 and Caffi et al. 2016",
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
}

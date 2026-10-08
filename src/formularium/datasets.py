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
        " held. The engine's Goidanich table is these data, as Porras Soriano 2006 prints them",
        "trail",
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
}

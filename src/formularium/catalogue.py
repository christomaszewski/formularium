"""Every formulation either tool uses, with its record (records.py), in one namespace.

The first entries came from Agrarium's `world/formulations.py` on 2026-10-07, which listed
the Cooptera engine's models as read in Cooptera's code (`cooptera@9310b91`, relisted at
`4818d26`) and the formulations Agrarium's truth uses. What changed in the move:
- the engine's relation to each formulation stayed in Agrarium: which formulations a tool
  runs is the tool's to say;
- `in_house` became `made_by`, so Agrarium's own formulations say so too;
- Brischetto et al. 2021 was read (Front. Plant Sci., open access, fetched 2026-10-07):
  its full author list and the Magarey parameters of its Figure 2 are now `read`;
- NOAA's solar position joined, with the equations both tools already computed.

How each author list was obtained is in `authors_from` (records.AUTHOR_SOURCES). A search
summary is never `read`.
"""

from __future__ import annotations

from .records import Formulation, Published

ROSSI_2008 = ("Rossi", "Caffi", "Giosuè", "Bugiani")
ROSSI_2008_HYDROTHERMAL = ("Rossi", "Caffi", "Bugiani", "Spanna", "Della Valle")

FORMULATIONS: dict[str, Formulation] = {
    # -- Downy mildew: Rossi's group (Piacenza) ---------------------------------------------------
    "rossi2008.oospores": Formulation(
        "oospore dormancy and germination",
        "Rossi, Caffi, Giosuè & Bugiani 2008, Ecol. Model. 212:480-491, with the hydro-thermal"
        " time of Rossi, Caffi, Bugiani, Spanna & Della Valle 2008, Plant Pathol. 57:216-226",
        year=2008,
        authors=tuple(dict.fromkeys(ROSSI_2008 + ROSSI_2008_HYDROTHERMAL)),
        authors_complete=True,
        authors_from="trail",
        structure="hydro-thermal-oospore-cohorts",
    ),
    "rossi2008.primary": Formulation(
        "primary infection (release, splash, 60 wet degree-hours)",
        "Rossi et al. 2008",
        year=2008,
        authors=ROSSI_2008,
        authors_complete=True,
        authors_from="trail",
        structure="wet-degree-hours-infection",
    ),
    "rossi2008.incubation": Formulation(
        "incubation window",
        "Rossi et al. 2008, eqs 8-9",
        year=2008,
        authors=ROSSI_2008,
        authors_complete=True,
        authors_from="trail",
        structure="incubation-window",
    ),
    "fedele2025.dose": Formulation(
        "primary lesions from oospore dose",
        "Fedele, Maddalena, Furiosi, Rossi, Toffolatti & Caffi 2025, Front. Plant Sci. 16:1524959",
        year=2025,
        authors=(
            "Fedele, Giorgia",
            "Maddalena, Giuliana",
            "Furiosi, Margherita",
            "Rossi, Vittorio",
            "Toffolatti, Silvia Laura",
            "Caffi, Tito",
        ),
        authors_complete=True,
        authors_from="snippet",
        structure="oospore-dose-response",
    ),
    "caffi2013.sporulation": Formulation(
        "sporulation nights",
        "Caffi, Gilardi, Monchiero & Rossi 2013, Phytopathology 103:64-73, as Brischetto 2021"
        " applies it",
        year=2013,
        authors=("Caffi", "Gilardi", "Monchiero", "Rossi"),
        authors_complete=True,
        authors_from="trail",
        structure="dark-moist-hours-sporulation",
    ),
    "brischetto2020.survival": Formulation(
        "survival of detached sporangia",
        "Brischetto, Bove, Languasco & Rossi 2020, Front. Plant Sci. 11:1187",
        year=2020,
        authors=("Brischetto", "Bove", "Languasco", "Rossi"),
        authors_complete=True,
        authors_from="trail",
        structure="vpd-survival",
    ),
    "brischetto2021.secondary": Formulation(
        "secondary infection (Magarey response, 4/21/30.2 °C, 2 h)",
        "Brischetto, Bove, Fedele & Rossi 2021, A weather-driven model for predicting"
        " infections of grapevines by sporangia of Plasmopara viticola, Front. Plant Sci."
        " 12:636607",
        year=2021,
        authors=("Brischetto, Chiara", "Bove, Federica", "Fedele, Giorgia", "Rossi, Vittorio"),
        authors_complete=True,
        authors_from="read",
        doi="10.3389/fpls.2021.636607",
        borrows=("magarey2005.generic",),
        structure="magarey-wetness-response",
        # Figure 2's caption, (D): Magarey et al. 2005's model, its parameters estimated from
        # Blaeser & Weltzien 1979 and Caffi et al. 2016, R² = 0.87.
        parameters=(
            Published("w_min_h", 2.0, "h", "Figure 2 caption (D)", "read"),
            Published("t_min_c", 4.0, "°C", "Figure 2 caption (D)", "read"),
            Published("t_opt_c", 21.0, "°C", "Figure 2 caption (D)", "read"),
            Published("t_max_c", 30.2, "°C", "Figure 2 caption (D)", "read"),
        ),
        flags=(
            "Figure 2's caption says its sporulation step is Lalancette et al. 1988a's model,"
            " and its infection rate Caffi et al. 2016's (read). Neither is in `borrows`: no"
            " tool computes those steps yet (Cooptera's port leaves severity out). Once one"
            " does, add them, and the Ohio lineage becomes kin.",
        ),
    ),
    # -- Downy mildew: rules and triggers ----------------------------------------------------------
    "goidanich.incubation": Formulation(
        "incubation table",
        "Goidanich, as Porras Soriano 2006 (Table 4.3) prints it",
        authors=("Goidanich", "Porras Soriano"),
        authors_from="trail",
        structure="daily-incubation-table",
    ),
    "kennelly2007.trigger": Formulation(
        "primary trigger: 2.5 mm, mean 11 °C",
        "Kennelly, Gadoury, Wilcox, Magarey & Seem 2007, Phytopathology 97:512-522",
        year=2007,
        authors=("Kennelly", "Gadoury", "Wilcox", "Magarey", "Seem"),
        authors_complete=True,
        authors_from="trail",
        structure="rain-temperature-trigger",
    ),
    "rule-3-10": Formulation(
        "primary trigger: 10 °C, 10 cm shoots, 10 mm",
        "the 3-10 rule, Baldacci 1947 (cooptera SOURCES.md:634)",
        year=1947,
        authors=("Baldacci, E.",),
        authors_complete=True,
        authors_from="trail",
        structure="rain-temperature-trigger",
    ),
    "magarey2010.rules": Formulation(
        "10:10:24, sporulation, 45 degree-hours",
        "P. A. Magarey 2010, GWRDC fact sheet INO904",
        year=2010,
        authors=("Magarey, P. A.",),
        authors_complete=True,
        authors_from="trail",
        structure="rain-temperature-trigger",
    ),
    "magarey2005.generic": Formulation(
        "generic infection response to temperature and wetness",
        "Magarey, Sutton & Thayer 2005, A simple generic infection model for foliar fungal plant"
        " pathogens, Phytopathology 95:92-100, as Brischetto 2021 uses it. Authors and DOI read"
        " in Brischetto 2021's references; the paper itself not read (APS refused, 2026-10-07)",
        year=2005,
        authors=("Magarey, R. D.", "Sutton, T. B.", "Thayer, C. L."),
        authors_complete=True,
        authors_from="read",
        doi="10.1094/PHYTO-95-0092",
        structure="magarey-wetness-response",
        equations="magarey2005",
    ),
    "puelles2024.ur": Formulation(
        "UR mildiu rules (Rioja)",
        "Puelles et al. 2024, Crop Protection, doi:10.1016/j.cropro.2023.106450",
        year=2024,
        authors=("Puelles",),
        authors_from="trail",
        doi="10.1016/j.cropro.2023.106450",
        structure="wet-degree-hours-infection",
    ),
    # -- Downy mildew: oospore maturity ------------------------------------------------------------
    "vitimeteo.oospores": Formulation(
        "oospore maturity, 140 °C·days",
        "VitiMeteo Plasmopara (Siegfried et al. 2004, as Leoni et al. 2026 describe it);"
        " project members as a search summary lists them",
        year=2004,
        authors=(
            "Siegfried, W.",
            "Bleyer, G.",
            "Kassemeyer, H.-H.",
            "Breuer, M.",
            "Krause, R.",
            "Viret, O.",
            "Dubuis, P.-H.",
            "Fabre, A.-L.",
            "Bloesch, B.",
            "Naef, A.",
            "Huber, M.",
            "Huber, B.",
            "Steinmetz, V.",
        ),
        authors_from="snippet",
        structure="thermal-time-oospore-threshold",
    ),
    "leoni2026.oospores": Formulation(
        "oospore maturity GLM",
        "Leoni et al. 2026, OENO One 60(3) (read by Cooptera; co-authors not recorded)",
        year=2026,
        authors=("Leoni",),
        authors_from="trail",
        structure="oospore-glm",
    ),
    # -- Leaf wetness ------------------------------------------------------------------------------
    "sentelhas2008.wetness": Formulation(
        "leaf wetness from RH and dew-point-depression thresholds",
        "Sentelhas, Dalla Marta, Orlandini, Santos, Gillespie & Gleason 2008, Agric. For."
        " Meteorol. 148:392-400",
        year=2008,
        authors=(
            "Sentelhas, P. C.",
            "Dalla Marta, A.",
            "Orlandini, S.",
            "Santos, E. A.",
            "Gillespie, T. J.",
            "Gleason, M. L.",
        ),
        authors_complete=True,
        authors_from="snippet",
        structure="rh-threshold-wetness",
    ),
    "rh90.wetness": Formulation(
        "leaf wetness from RH >= 90% or rain",
        "Cooptera's stand-in",
        made_by="cooptera",
        structure="rh-threshold-wetness",
    ),
    "cooptera.logistic-wetness": Formulation(
        "leaf wetness from a logistic model fitted on station sensors",
        "Cooptera's own, scored against stations left out",
        made_by="cooptera",
        structure="fitted-logistic-wetness",
    ),
    # -- Phenology and climate ---------------------------------------------------------------------
    "gdd5.budburst": Formulation(
        "budburst from degree-days",
        "García de Cortázar-Atauri 2006 (thesis), as García de Cortázar-Atauri, Brisson &"
        " Gaudillère 2009, Int. J. Biometeorol. 53:317-326",
        year=2009,
        authors=("García de Cortázar-Atauri, I.", "Brisson, N.", "Gaudillère, J.-P."),
        authors_complete=True,
        authors_from="snippet",
        structure="degree-day-phenology",
    ),
    "ramos2017.budburst": Formulation(
        "budburst",
        "Ramos 2017, Agric. For. Meteorol. 247:104-115",
        year=2017,
        authors=("Ramos, M. C.",),
        authors_from="snippet",
        structure="degree-day-phenology",
    ),
    "molitor2014.shoots": Formulation(
        "shoots at 10 cm",
        "Molitor, Junk, Evers, Hoffmann & Beyer 2014, Am. J. Enol. Vitic. 65:72-80",
        year=2014,
        authors=("Molitor", "Junk", "Evers", "Hoffmann", "Beyer"),
        authors_complete=True,
        authors_from="trail",
        structure="degree-day-phenology",
    ),
    "winkler.index": Formulation(
        "the Winkler index of a season's heat",
        "Amerine & Winkler 1944",
        year=1944,
        authors=("Amerine", "Winkler"),
        authors_complete=True,
        authors_from="trail",
        structure="degree-day-climate-index",
    ),
    "ferguson.cold-hardiness": Formulation(
        "bud cold hardiness",
        "Ferguson, Tarara, Mills, Grove & Keller 2011, Ann. Bot. 107:389-396; Ferguson, Moyer,"
        " Mills, Hoogenboom & Keller 2014, Am. J. Enol. Vitic. 65:59-71",
        year=2011,
        authors=("Ferguson", "Tarara", "Mills", "Grove", "Keller", "Moyer", "Hoogenboom"),
        authors_complete=True,
        authors_from="trail",
        structure="cold-hardiness",
    ),
    # -- Powdery mildew and Botrytis ---------------------------------------------------------------
    "gubler1999.powdery-index": Formulation(
        "powdery mildew risk index (UC Davis)",
        "Gubler, Rademacher, Vasquez & Thomas 1999, APSnet Feature; after Thomas, Gubler &"
        " Leavitt 1994, Phytopathology 84:1070",
        year=1999,
        authors=(
            "Gubler, W. D.",
            "Rademacher, M. R.",
            "Vasquez, S. J.",
            "Thomas, C. S.",
            "Leavitt",
        ),
        authors_from="snippet",
        structure="temperature-hours-mildew-index",
    ),
    "thiessen2018.ascospores": Formulation(
        "powdery mildew ascospore release",
        "Thiessen, Neill & Mahaffee 2018, Plant Dis. 102:1500-1508",
        year=2018,
        authors=("Thiessen", "Neill", "Mahaffee"),
        authors_complete=True,
        authors_from="trail",
        structure="ascospore-release-rule",
    ),
    "broome1995.botrytis": Formulation(
        "Botrytis infection index per wet period",
        "Broome, English, Marois, Latorre & Aviles 1995, Phytopathology 85:97-102",
        year=1995,
        authors=("Broome", "English", "Marois", "Latorre", "Aviles"),
        authors_complete=True,
        authors_from="trail",
        structure="wetness-temperature-infection-index",
    ),
    # -- Light, wind and the sun -------------------------------------------------------------------
    "erbs1982.partition": Formulation(
        "direct and diffuse light from the clearness index",
        "Erbs, Klein & Duffie 1982, Solar Energy 28(4):293-302, eq. 1, as pvlib writes it",
        year=1982,
        authors=("Erbs, D. G.", "Klein, S. A.", "Duffie, J. A."),
        authors_complete=True,
        authors_from="read",
        structure="clearness-index-partition",
    ),
    "winstral.shelter": Formulation(
        "wind shelter from the maximum upwind slope Sx",
        "Winstral & Marks 2002; Winstral et al. 2009, as SMRF implements it",
        year=2002,
        authors=("Winstral", "Marks"),
        authors_from="read",
        structure="upwind-slope-shelter",
    ),
    "winstral.shelter.decoupled": Formulation(
        "wind shelter, except on calm, clear nights, when valley air decouples",
        "Winstral's shelter by day and on windy or cloudy nights; on calm, clear nights the"
        " regional wind, unsheltered, as decoupled air drains (Daly, Conklin & Unsworth 2010,"
        " Int. J. Climatol. 30:1857-1864, search summary); its thresholds are assumed",
        year=2010,
        authors=("Winstral", "Marks", "Daly", "Conklin", "Unsworth"),
        authors_from="snippet",
        made_by="agrarium",
        borrows=("winstral.shelter",),
        structure="upwind-slope-shelter",
    ),
    "noaa.solar-position": Formulation(
        "the sun's elevation and azimuth",
        "NOAA Global Monitoring Division, General Solar Position Calculations"
        " (gml.noaa.gov/grad/solcalc/solareqns.PDF, read 2026-10-07); the azimuth in pvlib's"
        " analytical form (solar_azimuth_analytical, source read)",
        equations="solar",
        flags=(
            "NOAA's document says to use 366 days in a leap year. This module, and both tools'"
            " copies before it, use 365; kept, so no tool's numbers change. A test bounds the"
            " difference.",
            "NOAA's azimuth formula as printed, cos(180 - θ) = -(sin lat cos φ - sin decl) /"
            " (cos lat sin φ), puts the noon sun in the north if taken literally. The module"
            " uses pvlib's form, tested against the sun's direction as a vector.",
        ),
    ),
    # -- Made by Agrarium, unpublished -------------------------------------------------------------
    "kernel.mixture": Formulation(
        "dispersal: splash plus an anisotropic exponential-power wind kernel",
        "assumed; scale bounded by Gobbin et al. 2005 (abstract only)",
        made_by="agrarium",
        structure="dispersal-kernel",
    ),
    "bucket.canopy-water": Formulation(
        "leaf wetness as water on the canopy (rain, dew, evaporation)",
        "assumed (SWEB, the energy balance it once pointed to, is kin through Magarey)",
        made_by="agrarium",
        structure="canopy-water-balance",
    ),
    "drawn.stage-dates": Formulation(
        "phenology: stage dates drawn around an average, later in hollows",
        "assumed",
        made_by="agrarium",
        structure="drawn-stage-dates",
    ),
}

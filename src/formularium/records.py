"""What a formulation's record holds: what was published, and how each fact was checked.

A *formulation* is one published way of computing one process: an infection rule, an
incubation table, a phenology sum, the sun's position. Its record holds facts about the
publication, never a tool's choices:
- **the source** and, where known, its DOI;
- **the authors**, with whether the list is complete and how it was obtained
  (`AUTHOR_SOURCES`);
- **what it is part of:** the published models this formulation is, or is a piece of
  (`part_of`; empty when it is a whole model of its own);
- **borrowed equations:** formulations whose equations this one computes;
- **calibration data:** the datasets its parameters were fitted to (`calibrated_on`, ids
  of datasets.DATASETS), only where a source says so; empty means not recorded;
- **models used in its calibration** (`calibrated_with`): formulations whose output shaped
  the data it was fitted to, such as a model that decided when observations stopped;
- **how the calibration links were found** (`calibration_note`), with their status;
- **its structure,** one tag or more for its form (`STRUCTURES`), whoever wrote it. The
  tags are Agrarium's judgement, assumed from each model's title and module unless
  `structures_note` says more;
- **added authors:** names a tool recorded that the source's own list lacks, kept because
  kinship leans to linking, each group with how it was found;
- **its role** (`ROLES`): process, observation or reference, which decides how kinship
  treats it (Agrarium decision D26). `process` is the default, and the strictest;
- **published parameter values,** each with its unit, where in the source it is printed,
  and how it was checked;
- **flags:** what a person should weigh, never blocking;
- **the equations module** that computes it, if this package has one.

Which formulations a tool runs, and the ranges a tool draws a parameter from, belong to
the tool (decision D24 in Agrarium's PLAN section 15).

A formulation nobody published, made by one of the tools, says so in `made_by`. It may
still list the authors whose ideas it uses: kinship goes through them.

**Ids never change once used.** They are Cooptera's where Cooptera runs the formulation
(`xema engine models --json`): `<first author's surname><year>.<what, in snake_case>`, ASCII
and lower case, such as `lalancette1988.sporulation_bounds`; one made by a tool is
`<tool>.<what>`. Ids that predate the scheme (`rule_3_10`, `goidanich.incubation`, and
Agrarium's `bucket.canopy-water`) stay as they are, because reports and run records cite
them. The catalogue's first ids (2026-10-07, a copy of Agrarium's old hand list) were used
nowhere and gave way to Cooptera's the same day.
"""

from __future__ import annotations

from dataclasses import dataclass

AUTHOR_SOURCES = ("read", "trail", "snippet", "memory")
# How an author list or a value was obtained: read in the paper or its code; from another
# project's records, which say how they were read (Cooptera's survey, its SOURCES.md); from
# a search engine's summary; from memory. Only the first two settle anything.
SETTLED = ("read", "trail")

MAKERS = ("", "cooptera", "agrarium")
# Who made an unpublished formulation; "" for a published one.

# What a formulation models, which decides how kinship treats it (Agrarium decision D26).
# Agrarium's judgement, assumed from each model's title and module, like its structure tags.
ROLES = {
    "process": "an uncertain model of what the truth simulates and the engine predicts: the"
    " disease, the host, and the weather at the leaf",
    "observation": "how the outbreak becomes data: detection, sampling, a sensor's error",
    "reference": "known far better than anything scored (astronomy, psychrometrics, a"
    " definition), or the yardstick itself",
}

# The tags for a formulation's form. Agrarium's vocabulary (decision D19), extended as it
# classified Cooptera's list (decision D21).
STRUCTURES = {
    "rain-temperature-trigger": "infection declared when rain and temperature pass thresholds",
    "daily-incubation-table": "incubation as daily fractions from a temperature table",
    "thermal-time-oospore-threshold": "oospores mature when a heat sum passes a threshold",
    "oospore-glm": "oospore maturity from a fitted statistical model of weather",
    "hydro-thermal-oospore-cohorts": "oospore cohorts ripening on hydro-thermal time",
    "wet-degree-hours-infection": "infection when wet degree-hours pass a threshold",
    "incubation-window": "incubation as a window of temperature sums",
    "dark-moist-hours-sporulation": "sporulation on enough dark, moist hours",
    "vpd-survival": "sporangia survival as a function of vapour pressure deficit",
    "survival-days-table": "sporangia viable for days set by temperature and humidity, and"
    " killed within the hour by direct sun",
    "magarey-wetness-response": "infection from Magarey's temperature-wetness response",
    "richards-wetness-infection": "infection efficiency as a Richards curve in wetness duration,"
    " its asymptote and rate quadratic in temperature",
    "rh-threshold-wetness": "leaf wetness from humidity or dew-point thresholds",
    "fitted-logistic-wetness": "leaf wetness from a logistic model fitted on station sensors",
    "degree-day-phenology": "growth stages from degree-day sums",
    "degree-day-climate-index": "a season's heat as a degree-day index",
    "temperature-hours-mildew-index": "a daily risk score from hours in a temperature band",
    "ascospore-release-rule": "ascospore release from rain and temperature rules",
    "wetness-temperature-infection-index": "an infection index from wetness and temperature",
    "cold-hardiness": "bud hardiness acclimating and deacclimating with temperature",
    "oospore-dose-response": "primary lesions from the oospore dose",
    "dispersal-kernel": "spores spread by a distance kernel",
    "canopy-water-balance": "leaf wetness as a water budget on the canopy",
    "drawn-stage-dates": "stage dates drawn around an average",
    "clearness-index-partition": "direct and diffuse light from the clearness index",
    "upwind-slope-shelter": "wind slowed by terrain rising upwind",
    "sporulation-temperature-bounds": "sporulation only within a band of temperature",
    "bunch-susceptibility-window": "bunches susceptible for a set time after flowering",
    "sampling-detection-bound": "what a clean sample rules out, from a sampling model",
    "detection-sensitivity": "a scout's imperfect detection",
    "warning-scores": "scores of probabilistic warnings against outcomes",
    "magnus-humidity": "dew point and humidity by the Magnus formula",
    "solar-position": "the sun's position from date, time and place",
    "log-wind-profile": "wind speed at another height from a logarithmic profile",
    "chilling-dormancy": "dormancy broken by accumulated chilling",
    "cold-day-oospore-start": "oospore maturation started by a count of cold days",
    "survival-hours-temperature-humidity": "sporangia survival in hours from temperature and"
    " relative humidity, not a vapour pressure deficit",
}


@dataclass(frozen=True)
class Published:
    """One parameter value as its source prints it."""

    name: str
    value: float
    unit: str
    where: str  # where in the source: a table, an equation, a figure caption
    checked: str  # one of AUTHOR_SOURCES


@dataclass(frozen=True)
class Added:
    """Authors a tool recorded that the source's own list lacks, and how they were found."""

    names: tuple[str, ...]
    found: str  # one of AUTHOR_SOURCES
    why: str


@dataclass(frozen=True)
class Formulation:
    computes: str  # what it computes, in a few words
    source: str  # the citation, as read
    year: int | None = None
    # "Surname, Given" as the source gives them; the given name may be missing.
    authors: tuple[str, ...] = ()
    authors_complete: bool = False  # True when `authors` is the source's full list
    authors_from: str = ""  # one of AUTHOR_SOURCES; empty when there are no authors
    checked: str = ""  # where the author list was read or traced: a held PDF, a reference list
    made_by: str = ""  # one of MAKERS
    doi: str = ""
    part_of: tuple[str, ...] = ()  # the published models this one is, or is a piece of
    borrows: tuple[str, ...] = ()  # formulations whose equations this one computes
    calibrated_on: tuple[str, ...] = ()  # datasets.DATASETS ids; empty: not recorded
    calibrated_with: tuple[str, ...] = ()  # formulations used in fitting it
    calibration_note: str = ""  # where the calibration links were read, and their status
    structures: tuple[str, ...] = ()  # keys of STRUCTURES
    structures_note: str = ""  # more on how the tags were judged
    role: str = "process"  # a key of ROLES; the strictest is the default
    added_authors: tuple[Added, ...] = ()
    parameters: tuple[Published, ...] = ()
    flags: tuple[str, ...] = ()  # what a person should weigh; never blocking
    equations: str = ""  # the module of formularium.equations that computes it

    def everyone(self) -> tuple[str, ...]:
        """The authors kinship compares: the source's, then any a tool added."""
        return self.authors + tuple(n for a in self.added_authors for n in a.names)

    def published(self, name: str) -> float:
        """A published parameter's value, by name."""
        for p in self.parameters:
            if p.name == name:
                return p.value
        raise KeyError(f"no published parameter {name!r}")

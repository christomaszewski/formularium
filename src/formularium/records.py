"""What a formulation's record holds: what was published, and how each fact was checked.

A *formulation* is one published way of computing one process: an infection rule, an
incubation table, a phenology sum, the sun's position. Its record holds facts about the
publication, never a tool's choices:
- **the source** and, where known, its DOI;
- **the authors**, with whether the list is complete and how it was obtained
  (`AUTHOR_SOURCES`);
- **borrowed equations:** formulations whose equations this one computes;
- **its structure,** a tag for its form (`STRUCTURES`), whoever wrote it;
- **published parameter values,** each with its unit, where in the source it is printed,
  and how it was checked;
- **flags:** what a person should weigh, never blocking;
- **the equations module** that computes it, if this package has one.

Which formulations a tool runs, and the ranges a tool draws a parameter from, belong to
the tool (decision D22 in Agrarium's PLAN section 15).

A formulation nobody published, made by one of the tools, says so in `made_by`. It may
still list the authors whose ideas it uses: kinship goes through them.

**Ids never change once used.** A new published formulation takes the id
`<first author's surname><year>.<what it computes>`, folded to ASCII and lower case,
such as `lalancette1988.infection`. One made by a tool takes `<tool>.<what>`. Older ids
that predate the scheme (`rule-3-10`, `goidanich.incubation`) are kept as they are,
because reports and run records cite them.
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
    "magarey-wetness-response": "infection from Magarey's temperature-wetness response",
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
class Formulation:
    computes: str  # what it computes, in a few words
    source: str  # the citation, as read
    year: int | None = None
    # "Surname, Given" as the source gives them; the given name may be missing.
    authors: tuple[str, ...] = ()
    authors_complete: bool = False  # True when `authors` is the source's full list
    authors_from: str = ""  # one of AUTHOR_SOURCES; empty when there are no authors
    made_by: str = ""  # one of MAKERS
    doi: str = ""
    borrows: tuple[str, ...] = ()  # formulations whose equations this one computes
    structure: str = ""  # a key of STRUCTURES
    parameters: tuple[Published, ...] = ()
    flags: tuple[str, ...] = ()  # what a person should weigh; never blocking
    equations: str = ""  # the module of formularium.equations that computes it

    def published(self, name: str) -> float:
        """A published parameter's value, by name."""
        for p in self.parameters:
            if p.name == name:
                return p.value
        raise KeyError(f"no published parameter {name!r}")

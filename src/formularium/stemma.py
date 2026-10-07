"""The kinship graph: which formulations share a lineage, and what to hold out for a truth.

A stemma, in textual criticism, is the family tree of a text's manuscripts, drawn to tell
which copies are independent witnesses. Here the copies are formulations, and the question
is the same: may one be scored against another as if they were independent?

Two formulations are **kin** when any of these holds (Agrarium decision D19):
- **a borrowed equation:** one computes the other's equation, or both compute a third's
  (`borrows`). A name test cannot see this;
- **a shared person** (people.py): two authors are taken to be one person unless the
  evidence separates them.

**Shared structure** is a separate test (records.STRUCTURES): two formulations of the same
form are alike whoever wrote them.

**The hold-out** (Agrarium decision D22): when a run's truth uses some formulations, the
engine runs without every one of its formulations that is kin to one of them or shares its
structure. The tools ask this module, so both get the same answer from the same records.

The rule leans to linking. Wrongly linking two formulations only holds out one too many;
wrongly separating them would let a lineage be scored against itself.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass

from .catalogue import FORMULATIONS
from .people import Person, same_person
from .records import Formulation


@dataclass(frozen=True)
class Link:
    """Why a formulation is kin to another."""

    other: str
    reason: str


def shared_author(a: Formulation, b: Formulation) -> str | None:
    """The first pair of authors taken as one person, as a reason; None if there is none."""
    for x in a.authors:
        for y in b.authors:
            same, why = same_person(Person.parse(x), Person.parse(y), a.year, b.year)
            if same:
                return f"{x} and {y} taken as one person ({why})"
    return None


def link(a: str, b: str, catalogue: Mapping[str, Formulation] = FORMULATIONS) -> str | None:
    """Why formulations a and b are kin, or None. A formulation is its own kin."""
    if a == b:
        return "the same formulation"
    fa, fb = catalogue[a], catalogue[b]
    if b in fa.borrows or a in fb.borrows or set(fa.borrows) & set(fb.borrows):
        return "a borrowed equation"
    return shared_author(fa, fb)


def links(
    name: str, among: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> list[Link]:
    """Each formulation in `among` that `name` is kin to, with the reason, in `among`'s order."""
    found = []
    for other in among:
        why = link(name, other, catalogue)
        if why is not None:
            found.append(Link(other, why))
    return found


def kin(
    name: str, among: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> list[str]:
    """The formulations in `among` that `name` is kin to."""
    return [found.other for found in links(name, among, catalogue)]


def structures(
    names: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> set[str]:
    """The structure tags of these formulations."""
    return {catalogue[n].structure for n in names if catalogue[n].structure}


def hold_out(
    truth: Iterable[str],
    engine: Iterable[str],
    catalogue: Mapping[str, Formulation] = FORMULATIONS,
) -> dict[str, list[str]]:
    """The engine's formulations to hold out for a truth, each with every reason.

    `truth` is what the run's truth uses; `engine` is what the engine would run. An engine
    formulation is held out when it is kin to a truth formulation or shares the structure
    of one. Those left out of the result may run.
    """
    truth = list(dict.fromkeys(truth))
    out: dict[str, list[str]] = {}
    for e in dict.fromkeys(engine):
        reasons = [f"{t}: {why}" for t in truth if (why := link(e, t, catalogue)) is not None]
        form = catalogue[e].structure
        reasons += [
            f"{t}: the same structure, {form}"
            for t in truth
            if form and t != e and catalogue[t].structure == form
        ]
        if reasons:
            out[e] = reasons
    return out

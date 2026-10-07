"""The kinship graph: which formulations share a lineage, and what to hold out for a truth.

A stemma, in textual criticism, is the family tree of a text's manuscripts, drawn to tell
which copies are independent witnesses. Here the copies are formulations, and the question
is the same: may one be scored against another as if they were independent?

Two formulations are **kin** when they are **one model,** or pieces of one (`part_of`).
Two **process** formulations (records.ROLES) are kin, too, when they share a lineage
(Agrarium decision D19):
- **a borrowed equation:** one computes the other's equation, or both compute a third's
  (`borrows`). A piece of a model counts its model's borrowings too: running the model
  means computing them. A name test cannot see this;
- **a shared person** (people.py): two authors are taken to be one person unless the
  evidence separates them. Added authors (records.Added) count.

**Lineage counts only between process models** (Agrarium decision D26). Kinship stands for
correlated error, and errors correlate only between models of the same thing: a
sampling statistic and an infection curve by one author do not err together. So an
observation or reference piece is kin only to itself, and borrowing a piece that is not a
process (the sun's position, the Magnus formula) makes nobody kin.

**Shared structure** is a separate test (records.STRUCTURES): two formulations of the same
form are alike whoever wrote them.

**The hold-out** (Agrarium decisions D22 and D26): when a run's truth uses some
formulations, the engine runs without
- every **process** model kin to a truth formulation, or sharing a structure with one;
- every **observation** piece the truth's own observation uses, or shares a structure
  with: a matched observation model is the inverse crime's second half;
- never a **reference** piece.

The tools ask this module, so both get the same answer from the same records.

The rule leans to linking. Wrongly linking two formulations only holds out one too many;
wrongly separating them would let a lineage be scored against itself.

This is Agrarium's rule as it stood at `agrarium@44a4842` (`world/formulations.py`), moved
here on 2026-10-07 with the records it reads.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass

from .catalogue import FORMULATIONS
from .people import Person, same_person
from .records import Formulation

SAME = "the same formulation"


@dataclass(frozen=True)
class Link:
    """Why a formulation is kin to another."""

    other: str
    reason: str


@dataclass(frozen=True)
class _Entry:
    """What kinship compares about a formulation."""

    authors: tuple[str, ...]
    year: int | None
    borrows: frozenset[str]
    models: frozenset[str]  # the models it is, or is a piece of


def _entry(name: str, catalogue: Mapping[str, Formulation]) -> _Entry:
    f = catalogue[name]
    models = frozenset(f.part_of) or frozenset({name})
    borrows = set(f.borrows)
    for m in f.part_of:
        if m != name and m in catalogue:
            borrows |= set(catalogue[m].borrows)
    # Borrowing a piece that is not a process makes nobody kin (D26).
    borrows = {b for b in borrows if b not in catalogue or catalogue[b].role == "process"}
    return _Entry(f.everyone(), f.year, frozenset(borrows), models)


def _shared_author(a: _Entry, b: _Entry) -> str | None:
    for x in a.authors:
        for y in b.authors:
            same, why = same_person(Person.parse(x), Person.parse(y), a.year, b.year)
            if same:
                return f"{x} and {y} taken as one person ({why})"
    return None


def link(a: str, b: str, catalogue: Mapping[str, Formulation] = FORMULATIONS) -> str | None:
    """Why formulations a and b are kin, or None. A formulation is its own kin."""
    ea, eb = _entry(a, catalogue), _entry(b, catalogue)
    if a == b or ea.models & eb.models:
        return SAME
    if catalogue[a].role != "process" or catalogue[b].role != "process":
        return None  # lineage counts only between process models (D26)
    if (
        b in ea.borrows
        or a in eb.borrows
        or ea.models & eb.borrows
        or eb.models & ea.borrows
        or ea.borrows & eb.borrows
    ):
        return "a borrowed equation"
    return _shared_author(ea, eb)


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
    return {tag for n in names for tag in catalogue[n].structures}


def hold_out(
    truth: Iterable[str],
    engine: Iterable[str],
    catalogue: Mapping[str, Formulation] = FORMULATIONS,
) -> dict[str, list[str]]:
    """The engine's formulations to hold out for a truth, each with every reason.

    `truth` is what the run's truth uses, its observation included; `engine` is what the
    engine would run. A process model is held out when it is kin to a truth formulation or
    shares a structure with one; an observation piece when the truth's observation uses it
    or shares its structure; a reference piece never (D26). Those left out may run.
    """
    truth = list(dict.fromkeys(truth))
    out: dict[str, list[str]] = {}
    for e in dict.fromkeys(engine):
        if catalogue[e].role == "reference":
            continue
        reasons = [f"{t}: {why}" for t in truth if (why := link(e, t, catalogue)) is not None]
        tags = set(catalogue[e].structures)
        reasons += [
            f"{t}: the same structure, {tag}"
            for t in truth
            if t != e
            for tag in sorted(tags & set(catalogue[t].structures))
        ]
        if reasons:
            out[e] = reasons
    return out

"""The kinship graph: which formulations depend on each other, and what to hold out.

A stemma, in textual criticism, is the family tree of a text's manuscripts, drawn to tell
which copies are independent witnesses. Here the copies are formulations, and the question
is the same: may one be scored against another as if they were independent?

Two formulations **depend** on each other when they are **one model,** or pieces of one
(`part_of`). Two **process** formulations (records.ROLES) depend on each other, too, when
the records show a substantive dependency (Agrarium decision D27):
- **a borrowed equation:** one computes the other's equation, or both compute a third's
  (`borrows`). Borrowings are followed to the end: borrowing Brischetto 2021's model
  computes the Caffi and Lalancette equations it borrows. A piece of a model counts its
  model's borrowings too: running the model means computing them. A borrower carries what
  it borrows: its implementation and the data it was fitted to (below);
- **a shared implementation:** both are computed by the same code (`equations`, directly
  or through what they borrow);
- **shared calibration data:** both were fitted to the same observations
  (`calibrated_on`, datasets.py);
- **calibrated with the other:** one was fitted to data a model of the other shaped, such
  as a model that decided when observations stopped (`calibrated_with`), or both were
  fitted with the same model's help.

**Shared assumptions of form** are the structure tags (records.STRUCTURES): two
formulations of one form are alike whoever wrote them. The hold-out counts them too.

**Shared authorship alone is a flag, not a dependency** (D27, revising D19). People who
write together often share data, code and habits, so a shared author says to look for
those, and the records should name what is found. But it does not by itself make two
mechanically different predictors one. Masson & Knutti 2011 (read 2026-10-07) measured
dependence by the similarity of models' output: models from one institution, or sharing a
component, behaved alike; they drew no author rule, and asked that conclusions be tested
for their sensitivity to which models are included. So `hold_out(..., by_authors=True)`
adds author-only links, as a sensitivity experiment reported beside the main one.

**Lineage counts only between process models** (D26), with one exception (D29): a process
model and an observation piece fitted to the same data depend on each other, since the
observation would then read the truth's evidence too well (the engine's sampling bound and
an Ohio-matched truth share Madden, Hughes & Ellis 1995). A reference piece depends only on
itself, and borrowing a piece that is not a process (the sun's position, the Magnus
formula) creates no dependence.

**The hold-out** (D22, D26, D27): when a run's truth uses some formulations, the engine
runs without
- every **process** model that depends on a truth formulation, or shares a structure with
  one;
- every **observation** piece the truth's own observation uses, or shares a structure
  with, or shares calibration data with a truth formulation (D29): a matched observation
  model is the inverse crime's second half;
- never a **reference** piece.

The tools ask this module, so both get the same answer from the same records.

This began as Agrarium's rule at `agrarium@44a4842` (`world/formulations.py`), moved here
on 2026-10-07 with the records it reads, and was revised by D26 and D27 the same day.
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
    """What dependence compares about a formulation."""

    authors: tuple[str, ...]
    year: int | None
    borrows: frozenset[str]
    models: frozenset[str]  # the models it is, or is a piece of
    code: frozenset[str]  # the equations modules that compute it or what it borrows
    data: frozenset[str]  # the datasets it, or the model it is a piece of, was fitted to
    shaped_by: frozenset[str]  # models used in fitting it, or the model it is a piece of


def _borrowed(start: Iterable[str], catalogue: Mapping[str, Formulation]) -> set[str]:
    """Everything computed by computing `start`: borrowings followed to the end.

    A model that borrows Brischetto 2021's computes the Caffi and Lalancette equations
    Brischetto's borrows, so it depends on them too. Only process models are followed and
    kept: borrowing a piece that is not a process creates no dependence (D26). Cycles end."""
    found: set[str] = set()
    todo = list(start)
    while todo:
        b = todo.pop()
        if b in found or (b in catalogue and catalogue[b].role != "process"):
            continue
        found.add(b)
        if b in catalogue:
            todo.extend(catalogue[b].borrows)
    return found


def _entry(name: str, catalogue: Mapping[str, Formulation]) -> _Entry:
    f = catalogue[name]
    models = frozenset(f.part_of) or frozenset({name})
    wholes = [catalogue[m] for m in f.part_of if m != name and m in catalogue]
    direct = set(f.borrows).union(*(set(w.borrows) for w in wholes))
    borrows = _borrowed(direct, catalogue) - models - {name}
    # Computing a borrowed equation computes its implementation and its fitted values, so
    # the borrower carries the lender's code and calibration (and its model's, for a piece).
    lent = [catalogue[b] for b in borrows if b in catalogue]
    lent += [catalogue[m] for g in lent for m in g.part_of if m in catalogue]
    code = {f.equations, *(w.equations for w in wholes), *(g.equations for g in lent)}
    data = set(f.calibrated_on).union(*(set(w.calibrated_on) for w in [*wholes, *lent]))
    shaped_by = set(f.calibrated_with).union(*(set(w.calibrated_with) for w in [*wholes, *lent]))
    # Fitting with a piece of a model is fitting with that model.
    shaped_by |= {m for s in shaped_by if s in catalogue for m in catalogue[s].part_of}
    return _Entry(
        f.everyone(),
        f.year,
        frozenset(borrows),
        models,
        frozenset(code - {""}),
        frozenset(data),
        frozenset(shaped_by),
    )


def _shared_author(a: _Entry, b: _Entry) -> str | None:
    for x in a.authors:
        for y in b.authors:
            same, why = same_person(Person.parse(x), Person.parse(y), a.year, b.year)
            if same:
                return f"{x} and {y} taken as one person ({why})"
    return None


def link(a: str, b: str, catalogue: Mapping[str, Formulation] = FORMULATIONS) -> str | None:
    """Why formulations a and b depend on each other, or None. A formulation is its own.

    Only substantive dependencies count (D27): one model, a borrowed equation, a shared
    implementation, shared calibration data, calibration with the other's model. Structure
    is `hold_out`'s separate test, and a shared author is `possible_dependence`'s flag."""
    ea, eb = _entry(a, catalogue), _entry(b, catalogue)
    if a == b or ea.models & eb.models:
        return SAME
    roles = {catalogue[a].role, catalogue[b].role}
    if "reference" in roles:
        return None  # a reference piece depends only on itself (D26)
    if roles != {"process"}:
        # A process model and an observation piece fitted to the same data depend on each
        # other (D29): the observation would read the truth's evidence too well.
        if shared := sorted(ea.data & eb.data):
            return f"shared calibration data, {', '.join(shared)}"
        return None  # other lineage counts only between process models (D26)
    if (
        b in ea.borrows
        or a in eb.borrows
        or ea.models & eb.borrows
        or eb.models & ea.borrows
        or ea.borrows & eb.borrows
    ):
        return "a borrowed equation"
    if shared := sorted(ea.code & eb.code):
        return f"a shared implementation, formularium.equations.{', '.join(shared)}"
    if shared := sorted(ea.data & eb.data):
        return f"shared calibration data, {', '.join(shared)}"
    if used := sorted(ea.shaped_by & eb.models) or sorted(eb.shaped_by & ea.models):
        return f"calibrated with {', '.join(used)}"
    if used := sorted(ea.shaped_by & eb.shaped_by):
        return f"calibrated with a shared model, {', '.join(used)}"
    return None


def possible_dependence(
    a: str, b: str, catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> str | None:
    """A shared author between a and b, as a flag to look into; None if there is none.

    Never a reference piece's, which no one depends on through its authors."""
    if "reference" in (catalogue[a].role, catalogue[b].role):
        return None
    return _shared_author(_entry(a, catalogue), _entry(b, catalogue))


def links(
    name: str, among: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> list[Link]:
    """Each formulation in `among` that `name` depends on, with the reason, in order."""
    found = []
    for other in among:
        why = link(name, other, catalogue)
        if why is not None:
            found.append(Link(other, why))
    return found


def kin(
    name: str, among: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> list[str]:
    """The formulations in `among` that `name` depends on."""
    return [found.other for found in links(name, among, catalogue)]


def flags(
    name: str, among: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> list[Link]:
    """Formulations in `among` that share only an author with `name`: possible dependence."""
    found = []
    for other in among:
        if link(name, other, catalogue) is None:
            why = possible_dependence(name, other, catalogue)
            if why is not None:
                found.append(Link(other, why))
    return found


def structures(
    names: Iterable[str], catalogue: Mapping[str, Formulation] = FORMULATIONS
) -> set[str]:
    """The structure tags of these formulations."""
    return {tag for n in names for tag in catalogue[n].structures}


def hold_out(
    truth: Iterable[str],
    engine: Iterable[str],
    catalogue: Mapping[str, Formulation] = FORMULATIONS,
    *,
    by_authors: bool = False,
) -> dict[str, list[str]]:
    """The engine's formulations to hold out for a truth, each with every reason.

    `truth` is what the run's truth uses, its observation included; `engine` is what the
    engine would run. A process model is held out when it depends on a truth formulation
    or shares a structure with one; an observation piece when the truth's observation uses
    it or shares its structure; a reference piece never (D26). Those left out may run.

    `by_authors=True` also holds out process models that share only an author with a truth
    process formulation: the author-only sensitivity experiment (D27), reported apart.
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
        if by_authors and catalogue[e].role == "process":
            reasons += [
                f"{t}: possible dependence, {why}"
                for t in truth
                if catalogue[t].role == "process"
                and link(e, t, catalogue) is None
                and (why := possible_dependence(e, t, catalogue)) is not None
            ]
        if reasons:
            out[e] = reasons
    return out

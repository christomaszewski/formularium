"""Whether two authors are the same person, for the kinship graph (Agrarium decision D19).

An author is written "Surname, Given" as the trail gives it: the given name may be a full
first name, initials, or missing. Two authors are taken to be **the same person unless
there is evidence they are not**. Kinship excludes formulations, so wrongly merging two
people only excludes too much, and wrongly splitting one person lets a model's own
lineage pass as unrelated. The second is the error to avoid.

The decision, in order:
1. **ORCID.** If both have one, they decide.
2. **Surnames.** Compared part by part, accents folded and particles (de, della, van…)
   dropped, so "Verdugo-Vásquez" meets "Vasquez" and "Dalla Marta" meets "Marta". No
   shared part: different people.
3. **Given names.** Two full first names that differ, or first initials that differ:
   different people ("Rossi, J.-P." is not "Rossi, V."). Names that agree, or a name
   missing on either side: the same person. Chris's rule (2026-10-07): matching first
   names and a partly matching surname mean one author.
4. **Years.** Papers more than `CAREER_YEARS` apart cannot share an author.

Affiliations do not decide, since people move. When both are recorded and differ for a
pair judged the same, the reason says so, for a person to review.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

# Two papers further apart than this cannot share an author: a career is shorter.
CAREER_YEARS = 60
PARTICLES = frozenset(
    {"de", "del", "della", "dalla", "delle", "degli", "di", "da", "dos", "das", "do", "du"}
    | {"la", "le", "van", "von", "der", "den", "ter", "zu", "y", "e", "mac", "st"}
)


@dataclass(frozen=True)
class Person:
    surname: str
    given: str = ""
    orcid: str = ""
    affiliation: str = ""

    @classmethod
    def parse(cls, text: str, orcid: str = "", affiliation: str = "") -> Person:
        surname, _, given = text.partition(",")
        return cls(surname.strip(), given.strip(), orcid, affiliation)

    def __str__(self) -> str:
        return f"{self.surname}, {self.given}" if self.given else self.surname


def _fold(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).lower()


def surname_parts(surname: str) -> frozenset[str]:
    parts = {p for p in re.split(r"[\s\-']+", _fold(surname)) if p}
    kept = parts - PARTICLES
    return frozenset(kept or parts)


def _first_given(given: str) -> str:
    """The first given name, folded: a full name, or one letter for an initial."""
    token = re.split(r"[\s\-.]+", _fold(given).strip(" ."))[0] if given.strip() else ""
    return token


def same_person(
    a: Person, b: Person, year_a: int | None = None, year_b: int | None = None
) -> tuple[bool, str]:
    """Whether a and b are taken to be one person, and why."""
    if a.orcid and b.orcid:
        same = a.orcid == b.orcid
        return same, "same ORCID" if same else "different ORCIDs"
    shared = surname_parts(a.surname) & surname_parts(b.surname)
    if not shared:
        return False, "surnames differ"
    ga, gb = _first_given(a.given), _first_given(b.given)
    if ga and gb:
        if len(ga) > 1 and len(gb) > 1 and ga != gb:
            return False, f"first names differ ({a.given} / {b.given})"
        if ga[0] != gb[0]:
            return False, f"initials differ ({a.given} / {b.given})"
    if year_a is not None and year_b is not None and abs(year_a - year_b) > CAREER_YEARS:
        return False, f"papers {abs(year_a - year_b)} years apart"
    names = "first names agree" if ga and gb else "a first name is not recorded"
    reason = f"surname {'/'.join(sorted(shared))}; {names}"
    if a.affiliation and b.affiliation and _fold(a.affiliation) != _fold(b.affiliation):
        reason += f"; affiliations differ ({a.affiliation} / {b.affiliation}): review"
    return True, reason

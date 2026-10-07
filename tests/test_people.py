"""Who counts as the same person (Agrarium decision D19, moved here 2026-10-07)."""

from __future__ import annotations

from formularium.people import Person, same_person, surname_parts


def _same(a: str, b: str, ya: int | None = None, yb: int | None = None) -> bool:
    return same_person(Person.parse(a), Person.parse(b), ya, yb)[0]


# -- The same person ----------------------------------------------------------------------------


def test_surnames_match_part_by_part_with_accents_and_particles_folded() -> None:
    assert surname_parts("Verdugo-Vásquez") == {"verdugo", "vasquez"}
    assert surname_parts("Dalla Marta") == {"marta"}
    assert surname_parts("García de Cortázar-Atauri") == {"garcia", "cortazar", "atauri"}
    # Chris's rule: matching first names and a partly matching surname are one author.
    assert _same("Verdugo-Vásquez, Sergio", "Vasquez, Sergio")
    assert _same("Dalla Marta, A.", "Marta, A. D.")
    assert not _same("Rossi, V.", "Caffi, T.")


def test_different_first_names_or_initials_separate_people() -> None:
    assert not _same("Rossi, Jean-Pierre", "Rossi, Vittorio")
    assert not _same("Rossi, J.-P.", "Rossi, V.")
    assert not _same("Hill, Gareth", "Hill, Georg")  # one initial, two people
    assert _same("Rossi, Vittorio", "Rossi, V.")


def test_without_evidence_the_rule_links_people() -> None:
    # A first name missing on either side: the same person, the safe way round.
    assert _same("Rossi", "Rossi, J.-P.")
    assert _same("Magarey", "Magarey, P. A.")
    why = same_person(Person.parse("Rossi"), Person.parse("Rossi, V."))[1]
    assert "not recorded" in why


def test_orcid_decides_and_careers_end() -> None:
    a = Person("Rossi", "V.", orcid="0000-0001")
    assert same_person(a, Person("Rossi", "J.", orcid="0000-0001"))[0]
    assert not same_person(a, Person("Rossi", "V.", orcid="0000-0002"))[0]
    assert not _same("Müller", "Müller", 1923, 2020)
    assert _same("Müller", "Müller", 1990, 2020)


def test_differing_affiliations_ask_for_review_but_do_not_separate() -> None:
    same, why = same_person(
        Person("Keller", affiliation="Washington State"), Person("Keller", affiliation="Agroscope")
    )
    assert same and "review" in why

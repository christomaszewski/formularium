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
}

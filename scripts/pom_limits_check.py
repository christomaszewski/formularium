"""Which reading of POM's daily rain limits reproduces the printed indices (tranmanhsung1990.pom).

    uv run python scripts/pom_limits_check.py MERIGNAC.csv

MERIGNAC.csv is Bordeaux-Merignac's daily rain (Meteo-France station 33281001) as
`AAAAMMJJ;RR` lines, 1946-01-01 to 1988-03-31, cut from Meteo-France's "donnees climatologiques
de base quotidiennes" for the Gironde (Licence Ouverte 2.0; files Q_33_avant-1949_RR-T-Vent and
Q_33_previous-1950-2024_RR-T-Vent on data.gouv.fr). It is kept outside the repository.

It scores each reading against the paper's Table 1 (1977-1988, normals 1946-1987) and Ronzon
1987's Tableau 25 (1977-1986, normals 1951-1985), both transcribed in literature/, with the
module's own rules (equations/tranmanhsung1990.py). Numbers quoted in the record's flag and in
literature/requests/pom-limits-answer.md come from this script.
"""

from __future__ import annotations

import argparse
import calendar
import csv
import statistics as st
from pathlib import Path

import numpy as np

from formularium.equations import tranmanhsung1990 as pom

ROOT = Path(__file__).resolve().parents[1]
MONTHS = (9, 10, 11, 12, 1, 2, 3)


def table(name: str) -> dict[int, list[int]]:
    with (ROOT / "literature" / name).open() as f:
        rows = [r for r in csv.reader(f)]
    years = [int(y) for y in rows[0][1:]]
    return {y: [int(r[i + 1]) for r in rows[1:8]] for i, y in enumerate(years)}


def season(rr: dict[str, float], year: int) -> list[np.ndarray]:
    out = []
    for m in MONTHS:
        y = year - 1 if m >= 9 else year
        first = 21 if m == 9 else 1
        last = calendar.monthrange(y, m)[1]
        out.append(np.array([rr[f"{y}{m:02d}{d:02d}"] for d in range(first, last + 1)]))
    return out


def normals(rr: dict[str, float], y0: int, y1: int, wet: float) -> dict[int, tuple]:
    out = {}
    for m in MONTHS:
        tot, n, days = [], [], []
        for y in range(y0, y1 + 1):
            v = [rr[f"{y}{m:02d}{d:02d}"] for d in range(1, calendar.monthrange(y, m)[1] + 1)]
            tot.append(sum(v))
            n.append(sum(x >= wet for x in v))
            days.append(len(v))
        out[m] = (st.mean(tot), st.pstdev(tot), st.mean(n), st.mean(days))
    return out


def score(rr, printed, limits) -> dict:
    errs, jan = [], []
    for y, row in printed.items():
        got = [round(x) for x in pom.maturation_indices(season(rr, y), limits)]
        errs += [g - p for g, p in zip(got, row, strict=True)]
        jan.append((got[4], row[4]))
    return {
        "mae": sum(map(abs, errs)) / len(errs),
        "bias": sum(errs) / len(errs),
        "jan_r": st.correlation([a for a, _ in jan], [b for _, b in jan]),
        "jan_range": (min(a for a, _ in jan), max(a for a, _ in jan)),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("station", type=Path)
    a = ap.parse_args()
    rr = {}
    for line in a.station.read_text().split():
        k, v = line.split(";")
        rr[k] = float(v) if v else 0.0
    for name, printed, (y0, y1) in (
        ("Table 1 (paper p. 123)", table("tranmanhsung1990_table1.csv"), (1946, 1987)),
        ("Tableau 25 (Ronzon p. 150)", table("ronzon1987_tableau25.csv"), (1951, 1985)),
    ):
        print(f"\n== {name}, normals {y0}-{y1}")
        n01, n1 = normals(rr, y0, y1, 0.1), normals(rr, y0, y1, 1.0)
        readings = {
            "Hm = RM/rainy days (>=0.1), HM = (RM+SD)/n": [
                (n01[m][0] / n01[m][2], (n01[m][0] + n01[m][1]) / n01[m][2]) for m in MONTHS
            ],
            "Hm = RM/rainy days (>=1), HM = (RM+SD)/n": [
                (n1[m][0] / n1[m][2], (n1[m][0] + n1[m][1]) / n1[m][2]) for m in MONTHS
            ],
            "Hm = RM/rainy days (>=0.1), HM = 9 mm": [(n01[m][0] / n01[m][2], 9.0) for m in MONTHS],
            "Hm = RM/days in month, HM = 9 mm": [(n01[m][0] / n01[m][3], 9.0) for m in MONTHS],
            "Hm = RM/days in month, HM = (RM+SD)/n (>=0.1)": [
                (n01[m][0] / n01[m][3], (n01[m][0] + n01[m][1]) / n01[m][2]) for m in MONTHS
            ],
        }
        for h in (7.0, 8.0, 8.5, 10.0):
            readings[f"Hm = RM/days in month, HM = {h:g} mm"] = [
                (n01[m][0] / n01[m][3], h) for m in MONTHS
            ]
        for label, limits in readings.items():
            s = score(rr, printed, limits)
            print(
                f"  {label:48} MAE {s['mae']:6.1f}  bias {s['bias']:+6.1f}  January r"
                f" {s['jan_r']:.2f}, range {s['jan_range'][0]} to {s['jan_range'][1]}"
            )
        hm = n01[9][0] / n01[9][3]
        dry = [(y, printed[y][0]) for y in printed if sum(season(rr, y)[0]) == 0.0]
        print(f"  wholly dry 21-30 September: {dry}; ten days at Hm {hm:.2f} give {-10 * hm:.1f}")


if __name__ == "__main__":
    main()

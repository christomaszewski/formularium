"""What new records link to among a tool's models, to check against what you predicted.

    uv run python scripts/kin_report.py ID [ID ...] --engine PATH

PATH lists the tool's formulation ids. It is either Agrarium's world/engine_models.json
(its `formulations`, as ids or as objects with an `id`) or a text file with one id a line.
For each ID it prints:
- every dependency, with stemma.link's reason;
- every structure tag it shares;
- every shared-author flag.

Write down the verdicts you expect before running it. One you did not expect is a mistake
in the record or in the rule. On 2026-10-09 a record calibrated with a piece of Rossi
2008's model did not link to the model the engine runs: a gap in the rule, since fixed.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterable, Mapping
from pathlib import Path

from formularium import stemma
from formularium.catalogue import FORMULATIONS
from formularium.records import Formulation


def load_engine(path: Path) -> list[str]:
    """The formulation ids a tool runs, from its list in JSON or one id a line."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        data = json.loads(text)
        items = data["formulations"] if isinstance(data, dict) else data
        return [item["id"] if isinstance(item, dict) else item for item in items]
    return [line.strip() for line in text.splitlines() if line.strip()]


def report(
    names: Iterable[str],
    engine: Iterable[str],
    catalogue: Mapping[str, Formulation] = FORMULATIONS,
) -> list[str]:
    engine = [e for e in dict.fromkeys(engine) if e in catalogue]
    lines = []
    for name in names:
        lines.append(name)
        found = [f"  linked: {k.other}: {k.reason}" for k in stemma.links(name, engine, catalogue)]
        tags = set(catalogue[name].structures)
        found += [
            f"  same form: {e}: {tag}"
            for e in engine
            if e != name
            for tag in sorted(tags & set(catalogue[e].structures))
        ]
        found += [f"  flag: {k.other}: {k.reason}" for k in stemma.flags(name, engine, catalogue)]
        lines += found or ["  nothing: independent of every model listed"]
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("ids", nargs="+")
    parser.add_argument("--engine", type=Path, required=True)
    args = parser.parse_args()
    unknown = [i for i in args.ids if i not in FORMULATIONS]
    if unknown:
        print(f"not in the catalogue: {', '.join(unknown)}", file=sys.stderr)
        return 2
    engine = load_engine(args.engine)
    missing = [e for e in engine if e not in FORMULATIONS]
    if missing:
        print(f"engine ids not in the catalogue, skipped: {', '.join(missing)}", file=sys.stderr)
    print("\n".join(report(args.ids, engine)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

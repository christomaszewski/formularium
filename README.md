# Formularium

Published crop and disease model formulations, shared by
[Agrarium](https://github.com/christomaszewski/agrarium) (the farm disease simulator) and
[Cooptera](https://github.com/christomaszewski/cooptera) (the engine it tests). Decided by
Chris on 2026-10-07: Agrarium's PLAN section 15, decisions D20 to D22.

## What is here

| Module | What it holds |
|---|---|
| `records` | What a formulation's record holds, and how each fact was checked |
| `catalogue` | Every formulation either tool uses, in one namespace of ids |
| `people` | Whether two authors are the same person |
| `stemma` | The kinship graph, and what to hold out of the engine for a given truth |
| `equations` | The formulations' equations as pure numpy functions |

**The line through it:** the package records what was published and how it was checked.
Each tool keeps what it chooses:
- which formulations it runs;
- the ranges it draws parameters from;
- how it uses the equations (Agrarium per vine, Cooptera per station).

## Using it

Both tools pin a commit:

```toml
[project]
dependencies = ["formularium"]

[tool.uv.sources]
formularium = { git = "https://github.com/christomaszewski/formularium", rev = "<commit>" }
```

The repository is public (decision D23, 2026-10-07), so any machine can install it.

```python
from formularium import stemma
from formularium.equations.magarey2005 import required_wet_hours

stemma.kin("fedele2025.dose", among=["rossi2008.primary", "rule-3-10"])
stemma.hold_out(truth=["rossi2008.primary"], engine=["caffi2013.sporulation", "rule-3-10"])
required_wet_hours(temperatures, cardinal=(4.0, 21.0, 30.2), w_min=2.0)
```

## Licence

MIT ([LICENSE](LICENSE)). The equations and parameter values are published science; each
record cites its source.

## Commands

```sh
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
```

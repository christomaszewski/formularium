"""Formularium: published crop and disease model formulations, shared by Agrarium and Cooptera.

- `records`: what a formulation's record holds, and how each fact was checked.
- `catalogue`: every formulation either tool uses, in one namespace.
- `people`: whether two authors are the same person.
- `stemma`: the kinship graph, and what to hold out of the engine for a truth.
- `equations`: the formulations' equations as pure functions.

What was published lives here; what each tool chooses (which formulations it runs, the
ranges it draws parameters from) stays in the tool. Agrarium's PLAN, decisions D22 to D24.
"""

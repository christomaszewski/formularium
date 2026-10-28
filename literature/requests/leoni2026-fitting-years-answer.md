# Answer to leoni2026-fitting-years.md

2026-10-27, by an `ingest` session, from the paper's text (OENO One 60(3)) and Leoni's thesis
(Geneva 2026), both held in the library.

1. **The 96 observations are from 2004-2024.**
   - The paper (p. 8): "recent observations (n = 24) revealed strong correlations. Although the
     sampling was less systematic, the complete dataset (n = 96) exhibited the same trends."
     The thesis says the same (p. 166).
   - Table 1 (p. 11) and Table 3.1 (p. 170) give n = 96 before BBCH 13.
   - The complete dataset is 175 observations: 120 historical, 2004-2021, and 55 systematic,
     2022-2024 (paper p. 5; thesis p. 162). Of these, 96 are before BBCH 13 and 79 from it;
     the 2022-2024 split is 24 and 31.
   - The year of each of the 96 is not printed.
   - So the flag of #60 (2004-2024) stands. Cooptera's `engine/origins.py` (2022-2024) is
     wrong. Formularium's dataset record `leoni2026.changins`, written from the abstract on
     2026-10-08, also said 2022-2024; it is corrected here.
2. **2004-2025 is the comparison, not the fit.**
   - The GLM was applied over 2004-2025 and its dates set beside VitiMeteo's and the observed
     primary infections (paper p. 11, Figure 8, Tables S1-S2; thesis Tables 3.2-3.3).
   - But the maturity threshold, MTG < 1.5 d, was chosen on that comparison: it "aligns most
     closely with the observed maturity date" (paper p. 13; thesis p. 172). So 2025 is
     outside the coefficients' data but not outside the threshold's choice.
3. **Table 3.3's observed maturity** is "the laboratory-observed maturity date" (thesis p. 172).
   - It comes from the same germination tests, by the same method, in the years they share
     with the fit.
   - How a year's tests become one date is not stated in the passages read.

**Delivered:**
- `leoni2026.oospores`' first flag, rewritten.
- `leoni2026.changins`' description and check.
- A line in `literature/leoni2026.md` and in `literature/leoni2026thesis.md`.

`calibrated_on` already named `leoni2026.changins`, now with its years. For Cooptera: scoring
the GLM's coefficients out of sample leaves 2025 alone; seasons 2004-2024 are in-sample.

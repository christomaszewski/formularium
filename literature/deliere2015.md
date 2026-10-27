---
id: deliere2015
citation: Delière, L., Cartolaro, P., Léger, B. & Naud, O. 2015. Field evaluation of an expertise-based formal decision system for fungicide management of grapevine downy and powdery mildews (Mildium). Pest Management Science 71 (abstract record only; issue and pages not printed in what was read)
doi: 10.1002/ps.3917
read: 2026-10-25, abstract only (two HAL record abstracts, the 2015 paper's and the 2009 GrapeMilDeWS paper's, as copied from the records' meta tags), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [France]
processes: [decision support, spray count, fungicide reduction, Mildium, GrapeMilDeWS, field trial]
records: []
datasets: []
files: [dr1025_deliere2015abs.pdf (the 2026-10-25 drop)]
---

# Delière et al. 2015: Mildium, an expert-rule decision system, cut mildew sprays by 30 to 50 % in an 83-plot French trial (abstract only)

The abstract of the 2015 field evaluation of Mildium, with the abstract of the earlier French paper (Delière, Cartolaro, Léger, Naud and Alonso Ugaglia, 2009) on the same decision process, then called GrapeMilDeWS.

**Read this first.** Abstract only: the full 2015 paper is closed and no copy was available, so no spray counts, plot lists or failure details are read. Three caveats. (1) The 30 to 50 % cut is for downy and powdery mildew treatments together, at plot scale, against grower practice (l. 2). (2) The 35 % and 85 % figures are from the 2009 paper's abstract on the earlier workflow, not from the 2015 paper (l. 5). (3) Both are field trials in which researchers ran the rule; they are results for advice followed, not for growers' compliance. The doi is the 2015 paper's; the HAL record numbers are hal-02601019 (2015) and hal-02757168 (2009).

## What it holds

- **Trial:** a 4-year assessment of Mildium, a decision support system for grapevine downy and powdery mildew, in a network of 83 plots across French vineyards (l. 2).
- **Result:** in most vineyards Mildium protected the crop while cutting the number of treatments by 30 to 50 % against grower practices (l. 2). The abstract states this for plot scale and for both mildews together.
- **Context:** viticulture accounts for 20 % of the phytochemicals sprayed in French agriculture and 80 % of grapevine pesticides target powdery and downy mildews (l. 2).
- **Earlier workflow (2009 abstract):** four years of field trials of the fungicide decision process cut the number of treatments by 35 % on average, with no loss of harvest potential on 85 % of the plots tested (l. 5). So harvest potential was altered on 15 % of plots (arithmetic, not printed); the abstract says the failures showed weak points that were then adjusted.

## Dependence

- Expertise-based decision rules by IFV and INRAE. The held note `naud2010` describes GrapeMilDeWS as the same workflow, called Mildium in French; four authors are shared with it (Delière, Cartolaro, Léger, Naud), a flag only. No equations or data are borrowed that the abstract names.

## Bearing (2026-10-25)

- **Savings when a rule is followed (grower.dss_saving):** 30 to 50 % fewer treatments (both mildews, 83 plots, 4 years, France) and 35 % fewer with the earlier workflow, harvest potential unaltered on 85 % of plots. Kind: field trials run by the rule's designers; an upper bound on what growers would save. The 15 % of plots that lost harvest potential (arithmetic, not printed) is the price of the saving and belongs with it.
- **Not shown:** downy mildew alone, spray counts, intervals, delay from warning to spray, any Catalan site, how many growers follow such a rule.

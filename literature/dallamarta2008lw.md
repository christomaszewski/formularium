---
id: dallamarta2008lw
citation: Dalla Marta, A., Martinelli, L. & Orlandini, S. 2008. Leaf wetness spatial variability within grapevine canopy. American Journal of Enology and Viticulture 59(1):78-82 (read only as the UC Davis Wine Server research summary no. 188 by B. Guerra, not the paper)
doi: 10.5344/ajev.2008.59.1.78
read: "2026-10-25, a summary page, not the paper (the 2-page UC Davis research summary, whole), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [Italy, Tuscany]
processes: [leaf wetness, dew, canopy position, wetness sensor placement, leaf temperature, drying]
records: []
datasets: []
files: []
---

# Dalla Marta et al. 2008 (UC Davis summary): where in a Sangiovese canopy the leaves wet first, and a canopy of LAI 2.7 dry within an hour of sunrise

A third party's two-page summary of a 2005 Tuscany study of leaf wetness at the bottom, middle and top of a vertical vine canopy.

**Read this first.** The paper was not obtained. This note rests on a summary page written by someone else (UC Davis Wine Server, Summary 188), which prints no wetness hours, no temperatures and no table. The summary spells the second author "Martinelly"; the paper's citation, as given by the reading agent, has Martinelli. The reading JSON and the strand's LEADS.md say the dew checks were on "ten nights"; the summary does not say this (it says the inspections started at 10 pm, l. 43-45), so the number of nights is not known. Treat all of it as secondary.

## What it holds

- **Site and canopy:** Sangiovese in Tuscany, 2005; single cordon, spur pruned, a wall 80 cm high (l. 19); spacing 1 m by 3 m, north-south rows, a 16 % slope facing south, **leaf area index 2.7** (l. 20-21). A canopy with a measured LAI and a wetness record.
- **Sensors and checks:** 6 wetness sensors per vine, 2 in each of the bottom, middle and top portions, moved as the vines grew (l. 21, 25); 4 leaf temperature sensors in the outer canopy and 4 air temperature sensors just outside it (l. 22-23). Visual checks at night with a flashlight, starting at 10 pm, noting the percentage of wet leaf area (l. 43-45). A portion counted as "wet" when at least 10 % of its leaf area was wet (l. 47), a share of area, not a film depth.
- **Drying:** "At sunrise, evaporation starts taking place and all leaves dried in less than one hour" (l. 46). This is a dew case in a canopy of LAI 2.7, at every position; no rain wetting is described.
- **Position and temperature:** the top of the canopy always began to wet earlier than the middle or the bottom (l. 49). Wetting was gradual on all leaves at the top, mostly on the outside leaves at the bottom (l. 49-51). Top leaves were cooler than bottom leaves: at the top the leaf was below air temperature (condensation), at the bottom the air was below the leaf (l. 51-54), which the authors attribute to radiative cooling of exposed leaves.
- **Summary's own advice:** more than one sensor per vine, depending on canopy size and density (l. 63). The horizontal direction was not compared, since all sensors were external (l. 61).

## Dependence

- Own measurements of the 2008 paper, as relayed by a third party. The authors' leaf wetness durations in hours are not in the summary.

## Bearing (2026-10-25)

- **micro.wet_threshold_mm (0.02 mm):** no film depth. The only definition is a share of area (10 % of a portion's leaf area wet), which cannot be turned into millimetres.
- **micro.density_drying_slowdown (0.4 per unit LAI above 1) and micro.evap_mm_h_per_hpa:** one data point of a kind: dew gone in under an hour after sunrise at LAI 2.7 (l. 46). It says the canopy dried fast on that kind of night; it does not give a rate against VPD or radiation, and it is not a rain case. It says nothing about drying at other LAI.
- **micro.interception, micro.storage_mm_per_lai:** not addressed.
- **Kind of result:** measurement as relayed in a summary (one vineyard, one season). Not to be quoted as the paper; the paper (hours of wetness by layer, drying times) would add the numbers the summary lacks.

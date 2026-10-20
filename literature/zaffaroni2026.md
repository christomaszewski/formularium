---
id: zaffaroni2026
citation: "Zaffaroni, M., Alonso Ugaglia, A., Miclot, A.-S., Rimbaud, L., Papaïx, J., Rey, J.-F. & Fabre, F. 2026. Co-designing deployment strategies for disease-resistant cultivars: Insights from a participatory landscape-scale modeling study with a wine cooperative. PLOS Sustainability and Transformation 5(10): e0000286"
doi: 10.1371/journal.pstr.0000286
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Buzet, south-western France]
processes: [resistance deployment, resistance breakdown, fungicide use, landscape spread, net returns]
records: []
datasets: []
files: [zaffaroni_2026.pdf (the 2026-10-20 drop)]
---

# Zaffaroni et al. 2026: resistant vines planned with a wine cooperative

A simulation study, with the landsepi model, of downy-mildew-resistant cultivar deployment in the Buzet area. Six strategies were co-designed in workshops with the cooperative. The authors then test fungicide use and rapid or gradual deployment.

## What it holds

- Four action-research workshops with the cooperative, January to June 2023 (l. 181–182). Six strategies, among them resistant cultivars on plots over 30 years old, or on 3.3% of the oldest plots each year (l. 21–26, 581–582).
- Disease severity fell by 81–89% under S1 and by 51–56% under S2. The other scenarios (S3 to S6) gave 5–22% (l. 674–676).
- Fungicide applications fell by 83% under S1 and 50% under S2, from a baseline of 10.1 a year in the Central vineyard (l. 706–710).
- Median net benefit rose by 36% under S1 (447 € per ha a year) and by 10% under S2 (118 € per ha a year) in the Central vineyard (l. 716–718).
- Fungicide use lowered the mean risk of pathogen establishment by 27–38%. Gradual deployment lowered it by 19–31% (l. 776–781).

## Dependence

- The landsepi model, as described in the paper's refs 15 and 17 (earlier studies of the same group). The R package landsepi v1.3.0 is used (l. 358–359).
- The fungicide sub-model adapts a contact-fungicide model from Caffi and Rossi, ref 30 (l. 363–364).

## Bearing (2026-10-20)

- Serves t4 (downy mildew) and t1 (fungicide use). The batch listed t5, but the economic outputs are a smaller part of it. A vineyard simulator could take the trade-off between disease control, resistance durability and fungicide use.
- Not read in full.

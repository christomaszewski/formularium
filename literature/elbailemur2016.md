---
id: elbailemur2016
citation: Elbaile Mur, Andrea. 2016. Comportamiento de variedades de vid resistentes a enfermedades fúngicas en la comarca del Somontano [Behaviour of resistant grapevine varieties against fungal diseases in the Somontano region]. Trabajo Fin de Grado, Escuela Politécnica Superior de Huesca, Universidad de Zaragoza, Huesca
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew, grey mould]
crops: [grapevine]
regions: [Somontano Huesca Spain, Aragón]
processes: [infection, incubation, sporulation, leaf wetness, spray timing, season severity, resistant varieties, piwi, fungicide efficacy, weather data]
records: [goidanich.incubation, gubler1999.powdery_index]
datasets: []
files: [unizar_tfg_2016_5012.pdf]
---

# Elbaile Mur 2016: resistant grapevine varieties in Somontano, fungal disease

A light read (the deep-research B list).

## What it holds

- Two plots, three PIWI varieties and a Sauvignon Blanc control, weekly from 23 March to 6 September 2016 (l. 1264-1269).
- Goidanich: start 10 May, 100% development on 22 May (Table 28); observed first downy mildew symptoms 26 June (l. 2597-2618).
- Gubler: start 5 May; index 0 on 17 May, 40 on 19 May, interval cut to five days from 24 May (l. 2949-2976).
- Leaf downy mildew: no significant difference between samples; date effect significant at p = 0.001 (K = 20.98) (l. 2287-2300).
- Conclusion: resistant varieties showed leaf attack but no later cluster damage; the Goidanich and Gubler models were useful (l. 3236-3240).

## Dependence

- COMPUTES the Goidanich incubation table. The thesis applies Goidanich's daily development table (Table 1, as tabulated by G. Barrios et al. 2004; l. 436-483) with its start conditions (mature oospores, shoots about 10 cm, rain above 10 mm, mean temperature above 12 °C; l. 429-431, 2577-2584). It starts the cycle on 10 May 2016 and reaches 100% on 22 May (Table 28, l. 2596-2616). This is the engine's Goidanich incubation table, which the truth may not use. COMPUTES the Gubler index for powdery mildew (l. 611-620, 2943-2976): 20 points for six hours at 20-30 °C, minus 10 for fewer hours or 33 °C or more, cited to Thomas et al. 1994 and Naqvi 2004. That is the form of the UC Davis powdery mildew risk index (Gubler et al. 1999) on the engine list; Thomas, Gubler and Leavitt 1994 (l. 3428) is its field test. Named but not computed: the EPI model (Caffi et al. 2007, l. 418-427) and Blaeser (l. 414). Shared authors (flags only): Caffi, Rossi and Salinari have co-authored the mildew model papers in the bibliography (l. 3300, 3415).

## Bearing (2026-10-10)

- For a downy mildew truth, it is a 2016 Somontano weekly dataset with weather, and its Goidanich run (Table 28) is a worked example, which the truth may not use; for the Cooptera engine, its Goidanich and Gubler arithmetic is the dependence to avoid.

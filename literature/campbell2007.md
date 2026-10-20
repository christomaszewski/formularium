---
id: campbell2007
citation: Campbell, P., Bendek, C. & Latorre, B. A. 2007. Riesgo de oídio (Erysiphe necator) de la vid en relación con el desarrollo de los racimos (Risk of powdery mildew (Erysiphe necator) outbreaks on grapevines in relation to cluster development). Ciencia e Investigación Agraria 34(1):5-11
doi: 10.4067/S0718-16202007000100001
read: 2026-10-20, LIGHT (Spanish), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Chile, Santiago, Calera de Tango, Ovalle]
processes: [cluster susceptibility, spray timing, risk index]
records: []
datasets: []
files: [latorre_2007.pdf (the 2026-10-20 drop)]
---

# Campbell et al. 2007: the Chilean cluster stages when powdery mildew sprays count

Single fungicide sprays on clusters at different stages in Chilean vineyards (2001-2002) to
find when clusters are most at risk from powdery mildew, alongside the UC Davis risk index
computed on site.

## What it holds

- Campbell, Bendek and Latorre (Chile, PUC) sprayed kresoxim-methyl or myclobutanil on
  clusters at 2-6 stages in 2001 (Santiago, cv Criolla) and 2002 (Santiago, Calera de Tango,
  Ovalle) (l. 77-90, 113-119).
- Santiago 2001 untreated: 58% incidence, 53% severity (Table 1, l. 165-167).
- Best single spray: full flowering (stage 23): Santiago 2002 incidence 15.2% and severity
  3.8%; Calera 2002 incidence 1.9% (Table 2, l. 205-210, 255-257).
- Single spray at 7 mm berries (stage 31): 29.5% and 15.7% at Santiago; 12.8% and 4.8% at
  Ovalle (l. 206, 221).
- Critical window: stages 19 to 29, from start of flowering to small berries (l. 33-35).
- IRI (0-100) from max temperature, per Gubler et al. 1999 and Jarvis et al. 2002 (l.
  94-111). IRI 100 at full flowering in November (Table 3).
- No numeric date or stage for when berries become resistant (l. 23-25, 331-333).
- Not printed: the year of Table 3, the daily-maximum definition, replicate counts beyond
  'four', and data licence.

## Dependence

- Its risk index is computed 'according to Gubler et al. (1999)' and Jarvis et al. (2002)
  (l. 110-111, 317-318): the engine's `gubler1999.powdery_index`, run, not refitted. The
  spray trials are the authors' own. No engine author.

## Bearing (2026-10-20)

- For a powdery mildew truth or Cooptera's spray timing: the critical cluster window runs
  from the start of flowering to small berries (stages 19-29 of their scale), with a single
  full-flowering spray the most effective; no stage is given for when berries become
  resistant. Its index values are the engine's index, so they are not independent evidence
  of risk.

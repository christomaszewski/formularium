---
id: kennelly2005
citation: Kennelly, Megan M., Gadoury, David M., Wilcox, Wayne F., Magarey, Peter A. & Seem, Robert C. 2005. Seasonal development of ontogenic resistance to downy mildew in grape berries and rachises. Phytopathology 95(12):1445-1452
doi: 10.1094/PHYTO-95-1445
read: 2026-10-08, in full by a reading agent (claude-sonnet-5-5); 67 quotes checked by scripts/verify_quotes.py, the window and dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [New York, South Australia]
processes: [host susceptibility, ontogenic resistance]
records: [kennelly2005.bunch_window]
datasets: []
files: [PHYTO-95-1445.pdf]
---

# Kennelly et al. 2005: ontogenic resistance of berries and rachises

From Cornell (NYSAES Geneva) and SARDI (Loxton, South Australia). The source of the engine's
`kennelly2005.bunch_window`, "bunches past downy mildew four weeks after flowering".

## What it holds

- **Data:** clusters inoculated at Geneva (Chardonnay, Riesling, Concord, Niagara;
  2001-2003) and Loxton (Chardonnay, Riesling; 2001-2002) (l. 85, 91), from 7-16 days
  before bloom to 35 days after bloom at Geneva and 41 at Loxton (l. 101, 107, 111);
  disease scored 2 weeks later (l. 142). Bloom is observed 50% capfall (l. 120).
- **Berries:** at Geneva they stopped sporulating when inoculated later than 1 to 2 weeks
  after bloom (l. 294) and had little disease after 200 degree-days above 10 °C (l. 248).
  **Pedicels** stayed susceptible to 28 days (l. 186; the abstract's 4 weeks, l. 31); the
  **rachis** stopped sporulating after 12 days (l. 245).
- **Model:** relative severity on degree-days after bloom, pooled over cultivars,
  Y = 1.008 - 0.379·log(X + 1), r² = 0.996 (l. 243; the log's base is not printed).
  Cultivar coefficients did not differ (l. 241).
- **Loxton did not fit:** relative severity stayed above 50% at 200 degree-days (l. 260),
  and berries discoloured until at least 41 days (l. 255). Bloom lasted 8.8 days there
  against 4.5 at Geneva (l. 297-298). The authors warn that climate shifts the onset of
  resistance (l. 28).

## Dependence

- Its own inoculations; no model dated the data. DMCast is used after the fit, only to
  illustrate an application (l. 335-345).
- Authors: Kennelly, Gadoury, Wilcox, Magarey and Seem are the engine's authors for this
  model and for `kennelly2007.trigger`; that is one research group, not a dependency.

## Bearing (2026-10-08)

- **The engine's window is not what the paper found for berries.** The paper gives a
  degree-day decline, not a fixed window: berries resist from 1 to 2 weeks after bloom
  in New York, pedicels at 4 weeks, and South Australia's berries stayed susceptible much
  longer. "Four weeks after flowering" matches the pedicels only. Told to Cooptera; a flag
  on the record in Formularium.
- For Agrarium's truth: this paper's curve is a piece of the engine's model (one source),
  so a truth that used it would hold out the bunch window. The Loxton contrast is the
  better lesson: the period of susceptibility varies with climate.

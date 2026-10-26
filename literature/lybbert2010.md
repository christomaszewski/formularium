---
id: lybbert2010
citation: "Lybbert, T.J., Magnan, N. & Gubler, W.D. 2010. Powdery mildew risk & forecasting in wine grapes: do growers change risk management strategies in response to disease forecasts? Working paper, preliminary draft of March 2010 marked 'do not cite', UC Davis; AgEcon Search 61745"
doi: 10.22004/ag.econ.61745
read: 2026-10-25, lightly (abstract, introduction, data and results, about lines 1-830 of 1432; tables and figures not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [United States, California]
processes: [risk index, forecast use, spray interval, product choice, pesticide use reports, decision support]
records: []
datasets: []
files: [dr1025_lybbert2010.pdf (the 2026-10-25 drop)]
---

# Lybbert et al. 2010: California wine-grape growers use a powdery mildew risk index to choose products, not spray dates

A preliminary working paper that links 1996 to 2007 plot-level spray records to a daily powdery mildew risk index (PMI) and asks whether forecast use changes spray timing.

**Read this first.** An analogue, not a downy mildew result: the disease is powdery mildew, the crop California wine grapes and the index (PMI) a Gubler-Thomas powdery mildew model. The paper is a preliminary draft marked "do not cite" (March 2010); its revised form, an American Journal of Agricultural Economics paper of 2016, was not obtained, so the numbers may have changed. Only the abstract, introduction, data and results were read; tables and figures were not.

## What it holds

- **Main result:** most growers who use the daily risk index do not shorten or stretch their spray intervals with it; they use it to decide what to spray rather than when (l. 126). Growers using the index primarily adjust their choice of product, switching to higher-potency synthetic fungicides when risk is high.
- **Mechanism:** index users are less likely to spray on a given day as risk rises, because they shift to more potent synthetic fungicides with longer protected intervals (l. 725).
- **Use of the index:** only about half of California wine-grape growers actively use it, as high as 75 % in Napa and Sonoma (high-value, susceptible varieties) (l. 352). In the authors' online survey of 108 growers (January and February 2008), nearly two-thirds had used it to some degree; the sample is self-selected association members (l. 547).
- **Data:** California pesticide use reports, a legal daily record of every application; one data point per plot-day, March to October 1996 to 2007, 940,065 observations (l. 564). The present analysis includes 67 growers from seven major wine grape counties with adequate PMI data (l. 550).
- **Intervals:** regulated minimum intervals between sprays of the same product are commonly 7 to 14 days on California powdery mildew labels; this is the authors' stylised assumption, not a measurement (l. 476).

## Dependence

- Uses the Gubler-Thomas powdery mildew index and California pesticide use reports (public, not fetched); no downy mildew model. The paper's survey and spray data are the authors' own.

## Bearing (2026-10-25)

- **Compliance and what a forecast changes (grower.dss_compliance):** an analogue for how growers use a daily risk index: half use it, and its main effect is on the product chosen, not the interval or date (l. 126, 352, 725). Cautions against assuming a grower model's spray date moves with an alert. Kind: panel regression and survey, powdery mildew, California, preliminary; not transferable in value to Catalan downy mildew.
- **Interval (spray.interval_days):** label minimum intervals of 7 to 14 days are an assumption of the stylised model (l. 476), not a measured spray interval.
- **Data route:** the pesticide use reports are the model of what a Spanish or Catalan digital register could give (see the register dates in `sagarna2025`).
- **Not shown:** downy mildew, any delay from warning to spray, Spain.

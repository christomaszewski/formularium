---
id: leroy2013
citation: Leroy, P., Smits, N., Cartolaro, P., Delière, L., Goutouly, J.-P., Raynal, M. & Alonso Ugaglia, A. 2013. A bioeconomic model of downy mildew damage on grapevine for evaluation of control strategies. Crop Protection 53:58-71
doi: 10.1016/j.cropro.2013.05.024
read: 2026-10-22, in full (14 pages, two columns interleaved; Eq. 6, Eq. 9 and Table 1 also checked in the page image), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 44 of 44 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [France, Bordeaux]
processes: [downy mildew, bioeconomic model, yield loss, spray strategy, fungicide protection, economics, primary infection, STICS]
records: []
datasets: []
files: [gd1021_leroy2013.pdf (the 2026-10-22 drop)]
---

# Leroy et al. 2013: a daily bioeconomic model of downy mildew damage on Bordeaux Merlot, with prices and costs

The full paper behind the 2010 workshop abstract: it prints the equations, the fitted values, the economics and a 23-year comparison of spray strategies.

**Read this first.** How it differs from the held note `leroy2010`: that is the 3-page workshop abstract of the same model (GDPM, Bordeaux 2010, pp. 141-143), with no parameter values printed and 1988 to 2008 simulated. This 2013 paper prints equations (1) to (13), the fitted values (Table 1), the economics (8 t ha-1 cap, 600 euro per t, 70 euro per spray, 80 euro per observation) and runs 23 years (1988 to 2010). It adds an author (Smits). It is downy mildew only; powdery mildew is named as the next extension. Two details need care. Eq. 9 as printed (page image checked) gives P = p when Y/Ypot < rD, which contradicts the prose (the price is cut when the crop is worse than the threshold); and no numeric value of rD or rP is printed anywhere (l. 410-417). The euro sign extracts as "V", minus signs are lost in several equations, and PIarea prints "4*10" with a control character for "-7" (l. 429; the page image and Table 1 give 4e-7).

## What it holds

- **Structure:** a daily plot model; vine growth, leaf area index, phenology and potential yield come from STICS and run independently of the disease, so there is no feedback or compensation (l. 217). Potential yield is cut by 20 % to cover random effects (Ypot = 0.8 x Ypot_STICS; l. 386).
- **Infection:** Eq. 3 (PDF p. 4, l. 305): new infected leaf area per day = K_L x sporulating area x susceptible area / total leaf area, only when daily rain is at or above SImin_rain and mean temperature at or above SImin_temp. K_L = 3.6, SImin_rain 1.5 mm, SImin_temp 10.7 degC (l. 465-466). Primary infection: PImin_rain 7 mm per day and PImin_temp 10.7 degC (l. 518); window from two emerged leaves to 50 % bloom, number of primary infections unlimited (l. 511). PIarea 4e-7 ha of leaf per ha of vineyard in the 23-year run, the mean of Table 1's 4.5, 3.5 and 4.0e-7 (Salleboeuf 2006, Pompignac 2007 and 2008; first infection 2 days after "2 leaves", 4 days after "6 leaves" and at "2 leaves"; 4, 2 and 8 primary infections; l. 429, 453-457). The latent period is temperature-controlled after Blaise and Gessler (1992) and Calonnec et al. (2008), not fitted, no value printed (l. 237).
- **Lesions:** sporulation lasts 22 days a lesion, sptriang 0.5 (sporulation constant, then decreasing linearly; l. 281, 462-463); ontogenic resistance of uninfected leaves from 50 days (l. 526).
- **Damage rules, no severity curve** (l. 331, 374): before flowering, daily loss of young clusters and berries = g(t-1) x K_early x LAspor x Susc_early x [1 - Prot_early] (Eq. 4, PDF p. 5), K_early 7.2, Susc_early 1 until flowering and 0 after. After flowering (Eq. 6, PDF p. 5): daily yield loss = y(t-1) x K_late x LAspor x Susc_late x [1 - Prot_late], K_late 3.6 (l. 468). Berry susceptibility Susc_late is 1 for 25 days after bloom, then falls linearly to 0 over 40 days (l. 470-471). Severity on berries is 1 - y/ypot, the yield lost (Eq. 13, l. 416). The only severity-to-loss pairing printed is simulated: untreated, over 60 % of leaf area infected in 14 of 23 years (l. 522) and a loss then total, over 85 % (l. 525).
- **Fungicide:** protective only, efficacy 0.90 on healthy susceptible tissue (l. 444); protection lasts 16 days, 12 at full efficacy and "a decrease during the next 4 days" (l. 462-463; the decrease's shape is not printed). Parameters were estimated on untreated vineyards only, so the protection functions were not compared with measured data (l. 752).
- **Economics:** marketable yield = min(Ymax, simulated yield) (Eq. 8, l. 396), Ymax 8 t ha-1 (60 hL of wine) for the Bordeaux appellation (l. 476); price 600 euro per t, so 4,800 euro per ha potential gross product (l. 478); one spraying 70 euro per ha, of which 32 euro is fungicide, plus equipment and labour (l. 479); one observation 80 euro per ha, labour only (l. 483). Cost = sprays x cost per spray + observations x cost per observation (Eq. 11, l. 438); margin = gross product minus cost (Eq. 12). A quality cut rP x p applies when the sanitary state, taken as percentage yield loss, passes rD (l. 410-417).
- **Fitting:** three untreated Merlot data sets of the Institut Français de la Vigne et du Vin at Salleboeuf and Pompignac, 2006 (low pressure), 2007 and 2008 (high) (l. 393, 457); a low RMSE of leaf damage and of yield loss with realistic values, priority to the yield loss; no RMSE printed (l. 403, 506).
- **Strategies, 1988 to 2010 at La Ferrade:** 14-day spraying: average potential yield loss 0.8 %, worst 1999 (7 % infected leaf area, 3 % yield loss), 7.3 sprays a year (l. 543, 628). 21-day 5.0 sprays, 28-day 4.0. Mildium: 5.0 on average (2 to 6), yield loss 2.7 % on average and 14.5 % at most (1997, 2002) (l. 616, 628). Mean partial margin against 14-day: Mildium 2.7 %, 21-day 12.8 %, 28-day 20 % and untreated 57.2 % lower (l. 702).
- **Validity:** Merlot in the Bordeaux region under the last 20 years' climate; other cultivars and regions need new parameter values (l. 840).

## Dependence

- **Borrows** the disease structure from Blaise and Gessler (1992) and Gessler and Blaise (1992) (latent period, secondary infection) and the latency method of `calonnec2008`; vine growth, leaf area, phenology and potential yield from the STICS grapevine module (Garcia de Cortazar-Atauri 2006; Valdes-Gomez et al. 2009; its author is shared with the engine's budburst models: a flag); linear efficacy decline after Latin (2006); berry susceptibility after Gadoury et al. (2003) and Ficke et al. (2004); Mildium rules from Delière et al. (2009) and Léger (2008).
- **Fitted to** IFV untreated Merlot data (Salleboeuf 2006; Pompignac 2007 and 2008). The earlier `leroy2010` is the same model; the two are not independent.

## Bearing (2026-10-22)

- **What it answers:** the damage and loss equations, prices and costs asked for. Loss accumulates daily from sporulating leaf area (K_early 7.2, K_late 3.6, berry window 25 plus 40 days); there is no fitted curve of yield loss against severity. For Agrarium economics (D8) and Cooptera E6 and E7 value it offers a Bordeaux appellation set: 600 euro per t, 8 t ha-1 cap, 70 euro per spray, 80 euro per observation, in 2013 terms.
- **Takeable:** the structure (cap, price, per-spray and per-observation cost, margin) and the observation cost as a price of an observation; the 16-day protection and 90 % efficacy as one assumption. Not takeable: rD and rP (not printed), the Eq. 9 direction without the page image, any value for Catalonia or for powdery mildew, and the cap, which hides small losses when potential yield exceeds it.
- **Not shown:** validation on treated plots, RMSE values, other cultivars. Kind of result: a simulation with parameters fitted on three untreated site-years and economics assumed, not measured.

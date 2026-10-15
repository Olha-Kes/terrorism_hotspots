# Global Terrorism Hotspots (GTD, 1970–2017)

Exploratory analysis of the Global Terrorism Database: how the volume, geography, severity and methods of recorded terrorist attacks changed over time.

The project is based on a data project from [StrataScratch](https://platform.stratascratch.com/data-projects/terrorism-hotspots). The questions come from that task; the analysis, code and conclusions are my own.

## Key findings
- **Regional shift in 2004.** Middle East & North Africa and South Asia together held 32.5–53.3% of incidents in 1995–2003 and 66–77% from 2004 to 2017. The surge after 2011 increased volume within an already concentrated geography.
- **Attack types.** Bombing/Explosion is the most common type (48.6% of records), followed by Armed Assault (23.5%). Assassination fell from 20.2% (1970–79) to 6.2% (2004–17), while Bombing/Explosion rose from 39.9% (1994–2003) to 52.9% (2004–17).
- **Fatalities.** Yearly incidents explain most of the variation in yearly fatalities (`R² = 0.958` typical, `0.945` high-impact), but this is largely expected, since total fatalities equal incidents × average fatalities per incident. Average lethality per incident is essentially independent of the number of incidents.

## Data
National Consortium for the Study of Terrorism and Responses to Terrorism (START). (2017). *Global Terrorism Database* [Data file]. Retrieved from https://www.start.umd.edu/gtd

The dataset is not included in this repository (the GTD terms of use do not allow redistribution). Download it from the link above and place the archive in `data/raw/` (the notebook reads `data/raw/globalterrorismdb_0718dist.tar.bz2`).

World map for the geographic chart: [Natural Earth](https://www.naturalearthdata.com/) (1:110m, public-domain data), downloaded at run time.

## What the notebook covers
1. **Global trend**: yearly number of recorded incidents; sharp rise after 2011.
2. **Regional concentration**: shares of regions by year.
3. **Severity**: OLS models of yearly incidents vs. fatalities for typical and high-impact incidents (`nkill` > 31), with diagnostics (Durbin–Watson, heavy-tailed residuals, selection effect).
4. **Attack types**: shares by type over time, by region, and across two epochs (1970–2003, 2004–2017).
5. **Geography**: world map of recorded attacks per country.

## Notes and limitations
- GTD records are not always independent events (e.g. 9/11 is split into several records).
- 1993 is missing from the source and is kept as a gap, not filled with zeros.
- Years before 1977 have fewer than 1,000 records, so shares there are noisy.
- On the map, 1,320 of 177,134 records with coordinates (0.7%) are not shown: historical states and small territories absent from the 1:110m map.

## Repository structure
```
├── notebooks/eda_terrorism_hotspots.ipynb
├── src/helpers.py
├── outputs/figures/
├── requirements.txt
└── README.md
```

## Quick start
```bash
pip install -r requirements.txt
# place the GTD archive in data/raw/ (see Data)
jupyter notebook notebooks/eda_terrorism_hotspots.ipynb
```

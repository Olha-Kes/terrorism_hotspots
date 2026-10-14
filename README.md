# Global Terrorism Hotspots (GTD, 1970–2017)

EDA of the Global Terrorism Database: how the volume, geography, severity and methods of recorded terrorist attacks changed over time.

## Data
National Consortium for the Study of Terrorism and Responses to Terrorism (START). (2017). *Global Terrorism Database* [Data file]. Retrieved from https://www.start.umd.edu/gtd

The dataset is not included in this repository (GTD terms of use do not allow redistribution). Download it from the link above and place it in `data/`.

## What the notebook covers
1. **Global trend**: yearly number of recorded incidents; sharp rise after 2011.
2. **Regional concentration**: Middle East & North Africa and South Asia combined held 32.5–53.3% of incidents in 1995–2003 and 66–77% from 2004 to 2017.
3. **Severity**: OLS models of yearly incidents vs. casualties for typical and high-impact incidents (nkill > 31), with diagnostics (Durbin–Watson, heavy-tailed residuals, selection effect).
4. **Attack types**: shares by type over time, by region, and across two epochs (1970–2003, 2004–2017).
5. **Geography**: world map of incident density.

## Notes and limitations
- GTD records are not always independent events (e.g. 9/11 is split into several records).
- 1993 is missing from the source and is kept as a gap, not filled with zeros.
- Years before 1977 have fewer than 1,000 records, so shares there are noisy.

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
jupyter notebook notebooks/eda_terrorism_hotspots.ipynb
```
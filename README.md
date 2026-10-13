# 🌍 Global Terrorism Hotspots Analysis (1970–2017)

An exploratory data analysis (EDA) and geospatial visualization project investigating global terrorism patterns, regional trends, casualty dynamics, and attack methodologies using the **Global Terrorism Database (GTD)**.

---

## 📌 Project Overview & Scope
This project analyzes over **181,000 incident records** spanning 47 years to identify spatial and temporal hotspots, measure casualty correlations, and track shifts in tactical methods across different regions.

* **Dataset:** Global Terrorism Database (GTD) — 181,691 rows × 135 columns (1970–2017)
* **Core Focus:** Geospatial hotspot identifying, casualty impact distribution, time-series forecasting trends, and attack type classification.
* **Tools & Environment:** Python 3.x, PyCharm, Pandas, GeoPandas, Seaborn, Matplotlib, Git (`venv`).

---

## 📊 Visualizations & Key Highlights

![Global Distribution of Terrorism Hotspots (1970–2017).png](outputs/figures/Global%20Distribution%20of%20Terrorism%20Hotspots%20%281970%E2%80%932017%29.png)
| ![Linear model typical vs high impact.png](outputs/figures/Linear%20model%20typical%20vs%20high%20impact.png)![Trends Chart](output/figures/casualty_trends.png) |

---

## 🎯 Key Findings & Insights

* **Geospatial Concentration:** Over 60% of recorded incidents between 2000 and 2017 are concentrated in three primary sub-regions: South Asia, the Middle East, and North Africa.
* **Casualty vs. Incident Rate:** While total incidents peaked around 2014, the average severity (casualties per attack) varied significantly based on target type and weapon selection.
* **Shift in Tactics:** Bombing/Explosion remains the predominant attack type globally (>50%), but armed assaults show higher casualty rates per incident in private civilian targets.
* **Data Completeness:** Handled significant missing values across historical records (pre-1998 reporting vs. modern post-2000 digital reporting standards).

---

## 📂 Repository Structure

```text
terrorism_hotspots/
├── data/                  # Raw and cleaned GTD datasets (git-ignored)
│   └── raw/
├── docs/                  # Project documentation & exported visual plots
│   └── images/
├── notebooks/             # Jupyter Notebooks for EDA workflow
│   ├── [eda_terrorism_hotspots.ipynb](notebooks/eda_terrorism_hotspots.ipynb)
├── src/                   # Helper functions, custom plotting themes, data loaders
│   ├── [helpers.py](src/helpers.py)
├── .gitignore             # Git ignore file for environment & heavy data
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
⚙️ Quick Start & Installation
Prerequisites
Make sure you have Python 3.9+ installed on your system.

1. Clone the repository
Bash
git clone [https://github.com/Olha-Kes/terrorism_hotspots.git](https://github.com/Olha-Kes/terrorism_hotspots.git)
cd terrorism_hotspots
2. Set up Virtual Environment
Bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
3. Install Dependencies
Bash
pip install --upgrade pip
pip install -r requirements.txt
4. Download Data & Run Notebooks
Download the Global Terrorism Database (GTD) from START Consortium.

Place globalterrorismdb_0718dist.csv inside the data/raw/ directory.

Launch Jupyter Notebook / JupyterLab:

Bash
jupyter notebook
🛠️ Code Features & Engineering Highlights
High-Resolution Visualizations: Custom Seaborn dark/light themes configured with high DPI (dpi=300) and custom formatting (matplotlib.ticker).

Geospatial Processing: Spatial coordinate conversion via GeoPandas and Shapely geometry generation.

Efficient Memory Usage: Optimizing data types (category encoding, datetime parsing) for high-dimensional Pandas DataFrames.

📄 License & Attribution
Data sourced from the Global Terrorism Database (GTD) managed by the National Consortium for the Study of Terrorism and Responses to Terrorism (START), University of Maryland.

Created by Olha Kes
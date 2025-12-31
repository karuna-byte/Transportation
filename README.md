# Traffic Violations Data Analysis Dashboard

A Streamlit-based web application for exploring, analyzing, and visualizing traffic violations data.  
The app provides interactive dashboards, heatmaps, analytics, and summary statistics.

---

## 📁 Project Structure

```
Transportation/
├── app/
│   ├── __init__.py
│   ├── app.py                       # Main Streamlit app with sidebar navigation
│   └── pages/
│       ├── __init__.py
│       ├── HomePage.py              # Home dashboard page
│       ├── IncidentHotspots.py      # Geographical heatmap of incident hotspots
│       ├── AnalyticsExplorer.py     # Trend charts, bar plots, multi-filter insights
│       ├── ViewSummaryStatistics.py # Summary statistics page
│       └── TrafficViolationAnalytics.py # Structured analytics answering key questions
├── data/
│   └── cleaned/
│       └── Traffic_Violations_Cleaned.csv # Cleaned dataset
├── src/
│   └── data_cleaning/
│       ├── __init__.py
│       ├── load_data.py
│       ├── CleanSeqID.py
│       ├── CleanDateOfStop.py
│       ├── CleanTimeOfStop.py
│       ├── CleanAgency.py
│       ├── ClanSubAgency.py
│       ├── CleanDescription.py
│       ├── CleanLocation.py
│       ├── CleanLatitude.py
│       ├── CleanLongitude.py
│       ├── CleanBooleanColumns.py
│       ├── CleanSearchDisposition.py
│       ├── CleanSearchOutcome.py
│       ├── CleanSearchReason.py
│       ├── CleanSearchReasonForStop.py
│       ├── CleanSearchType.py
│       ├── CleanSearchArrestReason.py
│       ├── CleanState.py
│       ├── CleanVehicleType.py
│       ├── CleanYear.py
│       ├── CleanMake.py
│       ├── CleanModel.py
│       ├── CleanColor.py
│       ├── CleanViolationType.py
│       ├── CleanCharge.py
│       ├── CleanArticle.py
│       └── CleanContributedToAccident.py
├── utils/
│   ├── __init__.py
│   └── data_loader.py               # Data loading and caching utilities
└── README.md                        # Project documentation
```

---

## 🚀 Getting Started

1. **Install dependencies:**
    ```bash
    pip install streamlit pandas plotly pydeck
    ```

2. **Run the app:**
    ```bash
    cd Transportation
    streamlit run app/app.py
    ```

3. **Navigate** using the sidebar to explore dashboards, analytics, heatmaps, and statistics.

---

## 📊 Features

- **Home Dashboard:** Overview and quick filters for traffic violations data.
- **Incident Hotspots:** Interactive geographical heatmap of violation locations.
- **Analytics Explorer:** Trend charts, bar plots, and multi-filter insights.
- **Summary Statistics:** Key metrics and top categories.
- **Structured Analytics:** Answers to key analytical questions about violations.

---

## 📝 Data

- The cleaned dataset should be placed at:  
  `data/cleaned/Traffic_Violations_Cleaned.csv`

---

## 🛠️ Customization

- Add or modify pages in `app/pages/`.
- Update data cleaning scripts in `src/data_cleaning/`.
- Adjust data loading logic in `utils/data_loader.py`.

---

## 📄 License

MIT License

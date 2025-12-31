import streamlit as st
from pages.HomePage import home_page
from pages.IncidentHotspots import incident_hotspots_page
from pages.AnalyticsExplorer import analytics_explorer_page
from pages.ViewSummaryStatistics import view_summary_statistics_page
from pages.TrafficViolationAnalytics import traffic_violation_analytics_page

st.markdown(
    """
<style>
/* Hide Streamlit multipage navigation */
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""",
    unsafe_allow_html=True,
)

st.set_page_config(
    page_title="Traffic Violation Analytics",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Traffic Violations")
menu = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Analytics Explorer",
        "View Summary Statistics",
        "Traffic Violation Analytics",
    ],
)

if menu == "Home":
    home_page()
elif menu == "Analytics Explorer":
    analytics_explorer_page()
elif menu == "View Summary Statistics":
    view_summary_statistics_page()
elif menu == "Traffic Violation Analytics":
    traffic_violation_analytics_page()

import streamlit as st
import pandas as pd
from utils.data_loader import load_violations_data


def view_summary_statistics_page():
    st.title("📈 Summary Statistics")

    df = load_violations_data()

    # Total violations
    total_violations = len(df)

    # Violations involving accidents
    accident_violations = df["Accident"].sum() if "Accident" in df.columns else 0

    # High-risk zones (top 5 locations with most violations)
    high_risk_zones = (
        df["Location"].value_counts().nlargest(5)
        if "Location" in df.columns
        else pd.Series()
    )

    # Most frequently cited vehicle makes/models
    top_makes = (
        df["Make"].value_counts().nlargest(5) if "Make" in df.columns else pd.Series()
    )
    top_models = (
        df["Model"].value_counts().nlargest(5) if "Model" in df.columns else pd.Series()
    )

    st.subheader("Total Violations")
    st.metric("Total Violations", total_violations)

    st.subheader("Violations Involving Accidents")
    st.metric("Accident-Related Violations", accident_violations)

    st.subheader("High-Risk Zones (Top 5 Locations)")
    if not high_risk_zones.empty:
        st.table(high_risk_zones.rename("Violations"))
    else:
        st.write("No location data available.")

    st.subheader("Most Frequently Cited Vehicle Makes")
    if not top_makes.empty:
        st.table(top_makes.rename("Violations"))
    else:
        st.write("No vehicle make data available.")

    st.subheader("Most Frequently Cited Vehicle Models")
    if not top_models.empty:
        st.table(top_models.rename("Violations"))
    else:
        st.write("No vehicle model data available.")

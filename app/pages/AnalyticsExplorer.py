import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_violations_data


def analytics_explorer_page():
    st.title("📊 Analytics Explorer")

    df = load_violations_data()
    df["Date Of Stop"] = pd.to_datetime(df["Date Of Stop"], errors="coerce")

    # --- Multi-filter sidebar ---
    st.sidebar.header("Filter Data")
    min_date = df["Date Of Stop"].min()
    max_date = df["Date Of Stop"].max()
    date_range = st.sidebar.date_input(
        "Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date
    )
    location = st.sidebar.selectbox(
        "Location", ["All"] + sorted(df["Location"].dropna().unique().tolist())
    )
    vehicle_type = st.sidebar.selectbox(
        "Vehicle Type", ["All"] + sorted(df["VehicleType"].dropna().unique().tolist())
    )
    gender = st.sidebar.selectbox(
        "Gender", ["All"] + sorted(df["Gender"].dropna().unique().tolist())
    )
    race = st.sidebar.selectbox(
        "Race", ["All"] + sorted(df["Race"].dropna().unique().tolist())
    )
    violation_type = st.sidebar.selectbox(
        "Violation Type",
        ["All"] + sorted(df["Violation Type"].dropna().unique().tolist()),
    )

    # --- Apply filters ---
    df = df[
        (df["Date Of Stop"] >= pd.to_datetime(date_range[0]))
        & (df["Date Of Stop"] <= pd.to_datetime(date_range[1]))
    ]
    if location != "All":
        df = df[df["Location"] == location]
    if vehicle_type != "All":
        df = df[df["VehicleType"] == vehicle_type]
    if gender != "All":
        df = df[df["Gender"] == gender]
    if race != "All":
        df = df[df["Race"] == race]
    if violation_type != "All":
        df = df[df["Violation Type"] == violation_type]

    st.markdown("### Trend Chart: Violations Over Time")
    trend = df.groupby(df["Date Of Stop"].dt.date).size().reset_index(name="Count")
    fig_trend = px.line(
        trend, x="Date Of Stop", y="Count", title="Violations Over Time"
    )
    st.plotly_chart(fig_trend, use_container_width=True)

    st.markdown("### Bar Plot: Violations by Location")
    bar_loc = df["Location"].value_counts().nlargest(10).reset_index()
    bar_loc.columns = ["Location", "Count"]
    fig_bar = px.bar(bar_loc, x="Location", y="Count", title="Top 10 Locations")
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("### Distribution: Vehicle Type")
    fig_dist = px.histogram(df, x="VehicleType", title="Distribution of Vehicle Types")
    st.plotly_chart(fig_dist, use_container_width=True)

    st.markdown("### Multi-Filter Insights")
    st.dataframe(df.head(100))

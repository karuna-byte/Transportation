import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_violations_data


def traffic_violation_analytics_page():
    st.title("🚦 Traffic Violation Analytics")

    df = load_violations_data()
    df["Date Of Stop"] = pd.to_datetime(df["Date Of Stop"], errors="coerce")

    st.header("1. Most Common Violations")
    if "Violation Type" in df.columns:
        common_violations = df["Violation Type"].value_counts().nlargest(10)
        st.table(common_violations.rename("Count"))
        fig1 = px.bar(
            common_violations,
            x=common_violations.index,
            y=common_violations.values,
            labels={"x": "Violation Type", "y": "Count"},
            title="Top 10 Violation Types",
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("Violation Type data not available.")

    st.header("2. Areas/Coordinates with Highest Traffic Incidents")
    if "Location" in df.columns:
        top_locations = df["Location"].value_counts().nlargest(10)
        st.table(top_locations.rename("Incidents"))
    if "Latitude" in df.columns and "Longitude" in df.columns:
        map_df = (
            df[["Latitude", "Longitude"]]
            .dropna()
            .rename(columns={"Latitude": "latitude", "Longitude": "longitude"})
        )
        st.map(map_df)
    else:
        st.info("Location or coordinate data not available.")

    st.header("3. Demographics Correlation with Violation Types")
    if (
        "Violation Type" in df.columns
        and "Gender" in df.columns
        and "Race" in df.columns
    ):
        demo_group = (
            df.groupby(["Violation Type", "Gender", "Race"])
            .size()
            .reset_index(name="Count")
        )
        fig2 = px.sunburst(
            demo_group,
            path=["Violation Type", "Gender", "Race"],
            values="Count",
            title="Demographics and Violation Types",
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Demographic or violation type data not available.")

    st.header("4. Violation Frequency by Time of Day, Weekday, Month")
    if "Date Of Stop" in df.columns and "Time Of Stop" in df.columns:
        df["Hour"] = pd.to_datetime(df["Time Of Stop"], errors="coerce").dt.hour
        df["Weekday"] = df["Date Of Stop"].dt.day_name()
        df["Month"] = df["Date Of Stop"].dt.month_name()
        # By hour
        hour_counts = df["Hour"].value_counts().sort_index()
        fig3 = px.bar(
            x=hour_counts.index,
            y=hour_counts.values,
            labels={"x": "Hour", "y": "Violations"},
            title="Violations by Hour of Day",
        )
        st.plotly_chart(fig3, use_container_width=True)
        # By weekday
        weekday_counts = (
            df["Weekday"]
            .value_counts()
            .reindex(
                [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]
            )
        )
        fig4 = px.bar(
            x=weekday_counts.index,
            y=weekday_counts.values,
            labels={"x": "Weekday", "y": "Violations"},
            title="Violations by Weekday",
        )
        st.plotly_chart(fig4, use_container_width=True)
        # By month
        month_order = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        month_counts = df["Month"].value_counts().reindex(month_order)
        fig5 = px.bar(
            x=month_counts.index,
            y=month_counts.values,
            labels={"x": "Month", "y": "Violations"},
            title="Violations by Month",
        )
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("Date or time data not available.")

    st.header("5. Vehicle Types Most Often Involved in Violations")
    if "VehicleType" in df.columns:
        vehicle_counts = df["VehicleType"].value_counts().nlargest(10)
        st.table(vehicle_counts.rename("Violations"))
        fig6 = px.bar(
            vehicle_counts,
            x=vehicle_counts.index,
            y=vehicle_counts.values,
            labels={"x": "Vehicle Type", "y": "Violations"},
            title="Top 10 Vehicle Types",
        )
        st.plotly_chart(fig6, use_container_width=True)
    else:
        st.info("Vehicle type data not available.")

    st.header("6. Violations Involving Accidents, Injuries, or Vehicle Damage")
    accident_count = df["Accident"].sum() if "Accident" in df.columns else 0
    injury_count = df["Personal Injury"].sum() if "Personal Injury" in df.columns else 0
    damage_count = df["Property Damage"].sum() if "Property Damage" in df.columns else 0
    st.metric("Violations Involving Accidents", accident_count)
    st.metric("Violations Involving Injuries", injury_count)
    st.metric("Violations Involving Vehicle Damage", damage_count)

import streamlit as st
import pandas as pd
import pydeck as pdk
from utils.data_loader import load_violations_data


def incident_hotspots_page():
    st.title("📍 Incident Hotspots Heatmap")

    df = load_violations_data()

    # Ensure latitude and longitude columns exist and are numeric
    if "Latitude" in df.columns and "Longitude" in df.columns:
        map_df = df[["Latitude", "Longitude"]].dropna()
        map_df = map_df.astype({"Latitude": float, "Longitude": float})

        st.subheader("Heatmap of Traffic Violation Incidents")
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=pdk.ViewState(
                    latitude=map_df["Latitude"].mean(),
                    longitude=map_df["Longitude"].mean(),
                    zoom=10,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "HeatmapLayer",
                        data=map_df,
                        get_position="[Longitude, Latitude]",
                        radius=200,
                    ),
                ],
            )
        )
    else:
        st.warning("Latitude and Longitude data not available for heatmap.")


# To use this page, call incident_hotspots_page() from your main app or sidebar menu.

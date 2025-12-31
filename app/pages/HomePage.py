import streamlit as st
import pandas as pd
import math
from utils.data_loader import load_violations_data


def home_page():
    st.title("🚦 Traffic Violations Dashboard")
    st.write("Welcome to Trafic Violations Data Cleaning and Analysis App!")

    st.markdown("<br>", unsafe_allow_html=True)

    df = load_violations_data()

    # ---------------- DATE FILTER ---------------- #
    df["Date Of Stop"] = pd.to_datetime(df["Date Of Stop"], errors="coerce")
    min_date = df["Date Of Stop"].min()
    max_date = df["Date Of Stop"].max()
    start_date, end_date = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    # Filter DataFrame by selected date range
    df = df[
        (df["Date Of Stop"] >= pd.to_datetime(start_date))
        & (df["Date Of Stop"] <= pd.to_datetime(end_date))
    ]

    # ---------------- ADDITIONAL FILTERS ---------------- #
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        location = st.selectbox(
            "Location",
            options=["All"] + sorted(df["Location"].dropna().unique().tolist()),
            index=0,
        )
    with col2:
        vehicle_type = st.selectbox(
            "Vehicle Type",
            options=["All"] + sorted(df["VehicleType"].dropna().unique().tolist()),
            index=0,
        )
    with col3:
        gender = st.selectbox(
            "Gender",
            options=["All"] + sorted(df["Gender"].dropna().unique().tolist()),
            index=0,
        )
    with col4:
        race = st.selectbox(
            "Race",
            options=["All"] + sorted(df["Race"].dropna().unique().tolist()),
            index=0,
        )
    with col5:
        violation_type = st.selectbox(
            "Violation Type",
            options=["All"] + sorted(df["Violation Type"].dropna().unique().tolist()),
            index=0,
        )

    # Apply filters
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

    # ---------------- DISPLAY COLUMNS ---------------- #
    DISPLAY_COLUMNS = [
        "Date Of Stop",
        "Time Of Stop",
        "Agency",
        "SubAgency",
        "Description",
        "Location",
        "Accident",
        "Belts",
        "Personal Injury",
        "Property Damage",
        "Fatal",
        "Commercial License",
        "Commercial Vehicle",
        "Alcohol",
        "Work Zone",
        "Search Conducted",
        "Search Disposition",
        "Search Outcome",
        "Search Reason",
        "Search Reason For Stop",
        "Search Type",
        "Search Arrest Reason",
        "State",
        "VehicleType",
        "Year",
        "Make",
        "Model",
        "Color",
        "Violation Type",
        "Charge",
        "Article",
        "Contributed To Accident",
        "Race",
        "Gender",
        "Driver City",
        "Driver State",
        "DL State",
        "Arrest Type",
    ]

    # ---------------- PAGINATION SETTINGS ---------------- #
    PAGE_SIZE = st.selectbox("Rows per page", [1000, 5000, 10000], index=1)

    total_rows = len(df)
    total_pages = max(1, math.ceil(total_rows / PAGE_SIZE))

    # Session state for page
    if "page" not in st.session_state:
        st.session_state.page = 1

    # ---------------- PAGINATION CONTROLS ---------------- #
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅ Previous") and st.session_state.page > 1:
            st.session_state.page -= 1

    with col3:
        if st.button("Next ➡") and st.session_state.page < total_pages:
            st.session_state.page += 1

    with col2:
        selected_page = st.selectbox(
            "Jump to Page",
            options=list(range(1, total_pages + 1)),
            index=st.session_state.page - 1,
        )
        st.session_state.page = selected_page

    # ---------------- PAGE SLICE ---------------- #
    page = st.session_state.page
    start = (page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE

    page_df = df.iloc[start:end][DISPLAY_COLUMNS].copy()

    # Reset index to start from 1
    page_df.reset_index(drop=True, inplace=True)
    page_df.index += 1

    YES_NO_COLUMNS = [
        "Accident",
        "Belts",
        "Personal Injury",
        "Property Damage",
        "Fatal",
        "Commercial License",
        "Commercial Vehicle",
        "Alcohol",
        "Work Zone",
        "Search Conducted",
        "Contributed To Accident",
    ]

    page_df[YES_NO_COLUMNS] = (
        page_df[YES_NO_COLUMNS]
        .fillna("NO")
        .replace(
            {
                True: "YES",
                False: "NO",
                "TRUE": "YES",
                "FALSE": "NO",
                "True": "YES",
                "False": "NO",
                "Yes": "YES",
                "No": "NO",
                "Y": "YES",
                "N": "NO",
                1: "YES",
                0: "NO",
            }
        )
    )

    st.dataframe(page_df, use_container_width=True)

    # ---------------- DOWNLOAD ---------------- #
    # st.divider()
    # st.download_button(
    #     "⬇ Download Full Dataset",
    #     df.to_csv(index=False),
    #     "violations_full.csv",
    #     "text/csv",
    # )

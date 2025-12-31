import pandas as pd
import streamlit as st


@st.cache_data(show_spinner="Loading trafic violations data...")
def load_violations_data() -> pd.DataFrame:
    """
    Load and cache trafic violations data.

    Returns:
        pd.DataFrame: Cached trafic violations dataframe
    """
    df = pd.read_csv("data/cleaned/Traffic_Violations_Cleaned.csv", low_memory=False)
    return df

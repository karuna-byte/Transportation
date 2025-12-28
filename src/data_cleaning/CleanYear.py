import pandas as pd


class Year:
    def clean_Year(df):
        df["Year"] = pd.to_numeric(
            df["Year"], errors="coerce"
        )  # Convert to numeric, setting errors to NaN
        df = df[
            (df["Year"] >= 1960) & (df["Year"] <= 2025)
        ]  # Assuming valid years are between 1960 and 2025
        return df

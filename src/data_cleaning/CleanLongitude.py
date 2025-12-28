import pandas as pd
import numpy as np


class Longitude:
    @staticmethod
    def clean_longitude(df, column_name="Longitude"):
        df["Longitude"] = pd.to_numeric(
            df["Longitude"], errors="coerce"
        )  # Convert to numeric, set errors to NaN
        df["Longitude"] = df["Longitude"].replace(0, np.nan)  # Replace 0 with NaN
        df.loc[(df["Longitude"] > -65) | (df["Longitude"] < -125), "Longitude"] = (
            pd.NA
        )  # Set out-of-bounds values to NaN
        return df

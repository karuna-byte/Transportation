import pandas as pd
import numpy as np


class Latitude:
    @staticmethod
    def clean_latitude(df):
        df["Latitude"] = pd.to_numeric(
            df["Latitude"], errors="coerce"
        )  # Convert to numeric, set errors to NaN
        df["Latitude"] = df["Latitude"].replace(0, np.nan)  # Replace 0 with NaN
        df.loc[(df["Latitude"] < 24) | (df["Latitude"] > 49), "Latitude"] = (
            pd.NA
        )  # Set out-of-bounds values to NaN
        return df

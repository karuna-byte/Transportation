import pandas as pd


class Charge:
    @staticmethod
    def clean_charge(df):
        df["Charge"] = df["Charge"].astype(str)

        df["Charge"] = (
            df["Charge"]
            .astype(str)
            .str.upper()
            .str.strip()
            .str.replace(r"\s+", "", regex=True)
        )

        # Handle missing / invalid values
        df.loc[df["Charge"].isin(["", "NA", "NONE"]), "Charge"] = pd.NA
        return df

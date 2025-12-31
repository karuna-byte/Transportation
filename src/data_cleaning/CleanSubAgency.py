import pandas as pd


class SubAgency:
    @staticmethod
    def clean_sub_agency(df):
        df["SubAgency"] = (
            df["SubAgency"]
            .astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)  # fix extra spaces
            .str.replace(r"\s*,\s*", ", ", regex=True)  # normalize commas
            .str.title()
        )

        # Optional
        df["District_Number"] = df["SubAgency"].str.extract(
            r"(\d+)(?:st|nd|rd|th)?", expand=False
        )
        df["District_Number"] = (
            pd.to_numeric(df["District_Number"], errors="coerce").fillna(0).astype(int)
        )
        return df

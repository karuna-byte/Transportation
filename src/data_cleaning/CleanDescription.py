class Description:
    @staticmethod
    def clean_description(df):
        df["Description"] = df["Description"].fillna("UNKNOWN")  # Handle missing values
        df["Description"] = (
            df["Description"].astype(str).str.strip().str.upper()
        )  # Standardize case
        df["Description"] = df["Description"].str.replace(
            r"\s+", " ", regex=True
        )  # fix extra spaces
        return df

class Model:
    def clean_Model(df):
        df["Model"] = df["Model"].str.upper()
        df["Model"] = (
            df["Model"].str.replace(r"\bLX\b|\bSE\b|\bEX\b", "", regex=True).str.strip()
        )  # Remove common trim levels
        df["Model"] = df["Model"].str.strip()
        df["Model"] = df["Model"].fillna("UNKNOWN")
        return df

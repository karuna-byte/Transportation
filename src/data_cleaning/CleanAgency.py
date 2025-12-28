class Agency:
    @staticmethod
    def clean_agency(df):
        df["Agency"] = (
            df["Agency"].astype(str).str.strip().str.upper()
        )  # Standardize to uppercase and remove leading/trailing spaces
        return df

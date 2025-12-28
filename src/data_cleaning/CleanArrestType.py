class ArrestType:
    @staticmethod
    def clean_arrest_type(df):
        df["Arrest Type"] = (
            df["Arrest Type"]
            .astype("string")
            .str.upper()
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )

        # Split into code + description
        df[["ArrestCode", "ArrestDescription"]] = df["Arrest Type"].str.split(
            " - ", n=1, expand=True
        )

        # Fill missing / unknown values
        df["Arrest Type"] = df["Arrest Type"].fillna("UNKNOWN")
        df["ArrestCode"] = df["ArrestCode"].fillna("UNKNOWN")
        df["ArrestDescription"] = df["ArrestDescription"].fillna("UNKNOWN")
        return df

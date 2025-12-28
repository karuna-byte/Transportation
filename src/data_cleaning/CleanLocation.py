class Location:
    @staticmethod
    def clean_location(df):
        # Handle missing values based on known coordinates
        df.loc[
            (
                (df["Latitude"] == 39.006675)
                & (df["Longitude"] == -77.075320)
                & (df["Location"].isna())
            ),
            "Location",
        ] = "CONNECTICUT AVE / I-495"

        # Handle missing values based on known coordinates
        df.loc[
            ((df["Longitude"] == -77.2557435) & (df["Location"].isna())), "Location"
        ] = "UNKNOWN LOCATION"

        # Standardize separators (@ and /)
        df["Location"] = (
            df["Location"]
            .astype(str)
            .str.upper()
            .str.strip()
            .str.replace(r"\s*/\s*", " @ ", regex=True)
            .str.replace(r"\s*@\s*", " @ ", regex=True)
        )

        # Normalize spacing
        df["Location"] = df["Location"].str.replace(r"\s+", " ", regex=True)

        return df

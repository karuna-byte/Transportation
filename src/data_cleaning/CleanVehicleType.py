class VehicleType:
    def clean_VehicleType(df):
        df["VehicleType"] = (
            df["VehicleType"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .str.replace(r"\s*-\s*", " - ", regex=True)
        )
        # Split into Code & Category
        df[["Vehicle_Code", "Vehicle_Category"]] = df["VehicleType"].str.split(
            " - ", n=1, expand=True
        )
        return df

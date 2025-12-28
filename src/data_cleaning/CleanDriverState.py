class DriverState:
    @staticmethod
    def clean_driver_state(df):
        df["Driver State"] = (
            df["Driver State"].fillna("UNKNOWN").astype(str).str.upper().str.strip()
        )
        return df

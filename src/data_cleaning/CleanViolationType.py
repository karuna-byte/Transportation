class ViolationType:
    @staticmethod
    def clean_violation_type(df):
        df["Violation Type"] = (
            df["Violation Type"]
            .str.upper()
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )
        return df

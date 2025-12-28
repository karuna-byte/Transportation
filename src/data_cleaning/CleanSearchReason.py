class SearchReason:
    @staticmethod
    def clean_search_reason(df):
        df["Search Reason"] = (
            df["Search Reason"]
            .fillna("UNKNOWN")
            .astype(str)
            .str.strip()
            .str.title()  # Added default value 'UNKNOWN'
        )
        return df

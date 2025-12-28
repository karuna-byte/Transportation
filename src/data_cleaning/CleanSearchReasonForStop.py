class SearchReasonForStop:
    @staticmethod
    def clean_search_reason_for_stop(df):
        df["Search Reason For Stop"] = (
            df["Search Reason For Stop"]
            .fillna("UNKNOWN")
            .astype(str)
            .str.strip()
            .str.title()
        )  # Added default value 'UNKNOWN'
        return df

class SearchOutcome:
    @staticmethod
    def clean_search_outcome(df):
        df["Search Outcome"] = (
            df["Search Outcome"]
            .fillna("NA")
            .astype(str)
            .str.strip()
            .str.title()  # Added default value 'NA'
        )
        return df

class SearchDisposition:
    @staticmethod
    def clean_search_disposition(df):
        df["Search Disposition"] = (
            df["Search Disposition"]
            .fillna("Not Applicable")
            .astype(str)
            .str.strip()
            .str.title()
        )
        return df

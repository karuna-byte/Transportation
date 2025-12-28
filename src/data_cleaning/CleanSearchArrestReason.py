class SearchArrestReason:
    def clean_search_arrest_reason(df):
        df["Search Arrest Reason"] = (
            df["Search Arrest Reason"]
            .fillna("Not Applicable")
            .astype(str)
            .str.strip()
            .str.title()
        )  # .replace({'Nan': 'Not Applicable'})
        return df

class SearchType:
    def clean_search_type(df):
        df["Search Type"] = (
            df["Search Type"]
            .fillna("Not applicable")
            .astype(str)
            .str.strip()
            .str.title()
        )  # .replace({'Nan': 'Not applicable'})
        return df

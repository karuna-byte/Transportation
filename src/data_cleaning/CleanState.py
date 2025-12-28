class State:
    def clean_State(df):
        df["State"] = (
            df["State"].fillna("MD").astype(str).str.strip().str.upper()
        )  # .replace({'Nan': 'MD'})
        return df

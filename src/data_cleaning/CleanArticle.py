class Article:
    def clean_article(df):
        df["Article"] = (
            df["Article"]
            .astype("string")
            .str.upper()
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )

        df["Article"] = df.groupby("Charge")["Article"].transform(
            lambda x: x.ffill().bfill()
        )

        df["Article"] = df["Article"].fillna("UNKNOWN")
        return df

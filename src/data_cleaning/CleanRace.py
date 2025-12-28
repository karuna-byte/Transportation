class Race:
    @staticmethod
    def clean_race(df):
        df["Race"] = (
            df["Race"]
            .astype("string")
            .str.upper()
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )

        race_map = {
            "WHITE": "WHITE",
            "W": "WHITE",
            "BLACK": "BLACK",
            "AFRICAN AMERICAN": "BLACK",
            "B": "BLACK",
            "HISPANIC": "HISPANIC",
            "LATINO": "HISPANIC",
            "H": "HISPANIC",
            "ASIAN": "ASIAN",
            "A": "ASIAN",
            "OTHER": "OTHER",
            "O": "OTHER",
            "NATIVE AMERICAN": "NATIVE AMERICAN",
        }

        df["Race"] = df["Race"].replace(race_map)

        return df

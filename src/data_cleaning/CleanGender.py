class Gender:
    @staticmethod
    def clean_gender(df):
        df["Gender"] = df["Gender"].fillna("U").astype("str").str.strip().str.upper()

        gender_map = {
            "M": "M",
            "MALE": "M",
            "Male": "M",
            "F": "F",
            "FEMALE": "F",
            "Female": "F",
            "U": "U",
        }

        df["Gender"] = df["Gender"].map(gender_map)

        return df

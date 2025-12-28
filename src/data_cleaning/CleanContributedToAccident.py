class ContributedToAccident:
    @staticmethod
    def clean_contributed_to_accident(df):
        yes_no_map = {
            "YES": True,
            "Y": True,
            "TRUE": True,
            "T": True,
            "1": True,
            "NO": False,
            "N": False,
            "FALSE": False,
            "F": False,
            "0": False,
        }

        df["Contributed To Accident"] = df["Contributed To Accident"].map(yes_no_map)

        df["Contributed To Accident"] = df["Contributed To Accident"].astype("boolean")

        return df

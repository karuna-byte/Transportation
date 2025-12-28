class Color:
    def clean_color(df):
        color_map = {
            "BLUE, DARK": "BLUE",
            "BLUE, LIGHT": "BLUE",
            "GREEN, DK": "GREEN",
            "GREEN, LGT": "GREEN",
            "MAROON": "RED",
            "BURGUNDY": "RED",
            "BEIGE": "TAN",
            "CREAM": "WHITE",
            "BRONZE": "BROWN",
            "COPPER": "BROWN",
            "CHROME": "SILVER",
            "GOLD": "GOLD",
            "CAMOUFLAGE": "MULTICOLOR",
        }

        df["Color"] = df["Color"].replace(color_map)

        df["Color"] = df["Color"].fillna("UNKNOWN").astype(str).str.strip().str.upper()
        return df

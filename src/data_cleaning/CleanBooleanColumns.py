import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class BooleanColumns:
    @staticmethod
    def clean_boolean_columns(df):
        boolean_map = {
            "Y": True,
            "YES": True,
            "TRUE": True,
            "T": True,
            "N": False,
            "NO": False,
            "FALSE": False,
            "F": False,
        }

        """ 
        Accident, Belts, Personal Injury, Property Damage, Fatal,
        Commercial License, HAZMAT, Commercial Vehicle, Alcohol, Work Zone, Search Conducted
        Clean each boolean column 
        """
        df["Accident"] = (
            df["Accident"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Belts"] = (
            df["Belts"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Personal Injury"] = (
            df["Personal Injury"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Property Damage"] = (
            df["Property Damage"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Fatal"] = (
            df["Fatal"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Commercial License"] = (
            df["Commercial License"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["HAZMAT"] = (
            df["HAZMAT"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Commercial Vehicle"] = (
            df["Commercial Vehicle"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Alcohol"] = (
            df["Alcohol"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Work Zone"] = (
            df["Work Zone"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .astype(bool)
        )

        df["Search Conducted"] = (
            df["Search Conducted"]
            .astype(str)  # handle non-strings
            .str.strip()  # remove spaces
            .str.upper()  # normalize case
            .map(boolean_map)  # map values
            .fillna(False)  # optional default
            .infer_objects(copy=False)
            .astype(bool)
        )
        return df

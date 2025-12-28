import pandas as pd


class TimeOfStop:
    @staticmethod
    def clean_time_of_stop(df):
        """Cleans the 'Time Of Stop' column in the DataFrame.
        - Standardizes time format.
        """
        df["Time Of Stop"] = (
            df["Time Of Stop"]
            .astype(str)
            .str.replace(".", ":", regex=False)  # replace '.' with ':'
        )

        # Convert to time format
        df["Time Of Stop"] = pd.to_datetime(
            df["Time Of Stop"], format="%H:%M:%S", errors="coerce"
        ).dt.time

        # Combine Date Of Stop and Time Of Stop into stop_datetime
        df["stop_datetime"] = pd.to_datetime(
            df["Date Of Stop"].astype(str) + " " + df["Time Of Stop"].astype(str),
            errors="coerce",
        )
        return df

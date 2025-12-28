import pandas as pd


class DateOfStop:
    @staticmethod
    def clean_date_of_stop(df):
        """
        Cleans the 'Date Of Stop' column in the DataFrame.
        - Converts the column to datetime format.
        - Removes rows with future dates or year mistakes.
        """
        df = df.dropna(subset=["Date Of Stop"])  # drop rows with null Date Of Stop
        df["Date Of Stop"] = pd.to_datetime(
            df["Date Of Stop"], errors="coerce"
        )  # convert to datetime format

        # Filter future dates
        today = pd.Timestamp.today()
        future_dates = df[df["Date Of Stop"] > today]
        year_mistakes = df[df["Date Of Stop"].dt.year > today.year]
        df = df[~df.index.isin(future_dates.index)]  # remove future dates
        df = df[~df.index.isin(year_mistakes.index)]  # remove year mistakes
        return df

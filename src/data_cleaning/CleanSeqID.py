class SeqID:
    @staticmethod
    def clean_seq_id(df):
        """
        Cleans the 'SeqID' column in the DataFrame by stripping spaces and removing NaN values.
        """
        df["SeqID"] = (
            df["SeqID"].astype(str).str.strip()
        )  # Remove leading/trailing spaces
        return df.dropna(subset=["SeqID"])  # Drop rows where SeqID is NaN

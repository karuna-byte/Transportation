import pandas as pd
import numpy as np
from src.data_cleaning.CleanSeqID import SeqID
from src.data_cleaning.CleanDateOfStop import DateOfStop
from src.data_cleaning.CleanTimeOfStop import TimeOfStop
from src.data_cleaning.CleanAgency import Agency
from src.data_cleaning.CleanSubAgency import SubAgency
from src.data_cleaning.CleanDescription import Description
from src.data_cleaning.CleanLocation import Location
from src.data_cleaning.CleanLatitude import Latitude
from src.data_cleaning.CleanLongitude import Longitude
from src.data_cleaning.CleanBooleanColumns import BooleanColumns
from src.data_cleaning.CleanSearchDisposition import SearchDisposition
from src.data_cleaning.CleanSearchOutcome import SearchOutcome
from src.data_cleaning.CleanSearchReason import SearchReason
from src.data_cleaning.CleanSearchReasonForStop import SearchReasonForStop
from src.data_cleaning.CleanSearchType import SearchType
from src.data_cleaning.CleanSearchArrestReason import SearchArrestReason
from src.data_cleaning.CleanState import State
from src.data_cleaning.CleanVehicleType import VehicleType
from src.data_cleaning.CleanYear import Year
from src.data_cleaning.CleanMake import Make
from src.data_cleaning.CleanModel import Model
from src.data_cleaning.CleanColor import Color
from src.data_cleaning.CleanViolationType import ViolationType
from src.data_cleaning.CleanCharge import Charge
from src.data_cleaning.CleanArticle import Article
from src.data_cleaning.CleanContributedToAccident import ContributedToAccident
from src.data_cleaning.CleanRace import Race
from src.data_cleaning.CleanGender import Gender
from src.data_cleaning.CleanDriverCity import DriverCity
from src.data_cleaning.CleanDriverState import DriverState
from src.data_cleaning.CleanDLState import DLState
from src.data_cleaning.CleanArrestType import ArrestType

df = pd.read_csv("data/raw/Traffic_Violations.csv")

print("Initial DataFrame shape:", df.shape)
# print(df.head())

# print(df.duplicated().sum())


def drop_duplicate_rows(data_frame):
    """
    Removes duplicate rows from the given DataFrame.
    Returns a new DataFrame without duplicates.
    """
    return data_frame.drop_duplicates()


df = drop_duplicate_rows(df)
# print("DataFrame shape after dropping duplicates:", df.shape)

df = SeqID.clean_seq_id(df)
# print("DataFrame shape after cleaning SeqID:", df.shape)

df = DateOfStop.clean_date_of_stop(df)
# print("DataFrame shape after cleaning Date Of Stop:", df.shape)

df = TimeOfStop.clean_time_of_stop(df)
# print("DataFrame shape after cleaning Time Of Stop:", df.shape)

df = Agency.clean_agency(df)
# print("DataFrame shape after cleaning Agency:", df.shape)

df = SubAgency.clean_sub_agency(df)
# print("DataFrame shape after cleaning SubAgency:", df.shape)

df = Description.clean_description(df)
# print("DataFrame shape after cleaning Description:", df.shape)

df = Location.clean_location(df)
# print("DataFrame shape after cleaning Location:", df.shape)

df = Latitude.clean_latitude(df)
# print("DataFrame shape after cleaning Latitude:", df.shape)

df = Longitude.clean_longitude(df)
# print("DataFrame shape after cleaning Longitude:", df.shape)

df = BooleanColumns.clean_boolean_columns(df)
# print("DataFrame shape after cleaning Boolean Columns:", df.shape)

df = SearchDisposition.clean_search_disposition(df)
# print("DataFrame shape after cleaning Search Disposition:", df.shape)

df = SearchOutcome.clean_search_outcome(df)
# print("DataFrame shape after cleaning Search Outcome:", df.shape)

df = SearchReason.clean_search_reason(df)
# print("DataFrame shape after cleaning Search Reason:", df.shape)

df = SearchReasonForStop.clean_search_reason_for_stop(df)
# print("DataFrame shape after cleaning Search Reason For Stop:", df.shape)

df = SearchType.clean_search_type(df)
# print("DataFrame shape after cleaning Search Type:", df.shape)

df = SearchArrestReason.clean_search_arrest_reason(df)
# print("DataFrame shape after cleaning Search Arrest Reason:", df.shape)

df = State.clean_State(df)
# print("DataFrame shape after cleaning State:", df.shape)

df = VehicleType.clean_VehicleType(df)
# print("DataFrame shape after cleaning Vehicle Type:", df.shape)

df = Year.clean_Year(df)
# print("DataFrame shape after cleaning Year:", df.shape)

df = Make.clean_make(df)
# print("DataFrame shape after cleaning Make:", df.shape)

df = Model.clean_Model(df)
# print("DataFrame shape after cleaning Model:", df.shape)

df = Color.clean_color(df)
# print("DataFrame shape after cleaning Color:", df.shape)

df = ViolationType.clean_violation_type(df)
# print("DataFrame shape after cleaning Violation Type:", df.shape)

df = Charge.clean_charge(df)
# print("DataFrame shape after cleaning Charge:", df.shape)

df = Article.clean_article(df)
# print("DataFrame shape after cleaning Article:", df.shape)

df = ContributedToAccident.clean_contributed_to_accident(df)
# print("DataFrame shape after cleaning Contributed To Accident:", df.shape)

df = Race.clean_race(df)
# print("DataFrame shape after cleaning Race:", df.shape)

df = Gender.clean_gender(df)
# print("DataFrame shape after cleaning Gender:", df.shape)

df = DriverCity.clean_driver_city(df)
# print("DataFrame shape after cleaning Driver City:", df.shape)

df = DriverState.clean_driver_state(df)
# print("DataFrame shape after cleaning Driver State:", df.shape)

df = DLState.clean_dl_state(df)
# print("DataFrame shape after cleaning DL State:", df.shape)

df = ArrestType.clean_arrest_type(df)
# print("DataFrame shape after cleaning Arrest Type:", df.shape)

df.to_csv(
    "data/cleaned/Traffic_Violations_Cleaned.csv", index=False
)  ## Save cleaned data

print("Processed Successfully -----")

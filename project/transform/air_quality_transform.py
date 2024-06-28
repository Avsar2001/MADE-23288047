import pandas as pd
from colorama import init, Fore

from utils.constant import WORLD_AIR_QUALITY_DATA
from utils.utils import is_file_or_directory_exists, get_absolute_path

# Initialise colorama with reset color after every print
init(autoreset=True)


def transform_air_quality_dataframe():
    """
    create air quality dataframe and preprocess it from csv

    :args:
    :return:
    - Pandas DataFrame - cleaned and preprocessed data
    """
    try:
        data_file_path = (
            f"{get_absolute_path('data/raw/')}{WORLD_AIR_QUALITY_DATA['raw_data_file']}"
        )

        # Check if data file exists at observed location
        if not is_file_or_directory_exists(data_file_path):
            raise FileNotFoundError(
                f'{WORLD_AIR_QUALITY_DATA["raw_data_file"]} not exists'
            )

        # create forest dataframe from csv
        air_quality_df = pd.read_csv(data_file_path)

        # remove unused data columns
        air_quality_df = air_quality_df.drop(
            columns=WORLD_AIR_QUALITY_DATA["unused_db_cols"]
        )

        print(Fore.GREEN + f"Air quality data transform Successful!")
        # print(Fore.YELLOW + air_quality_df.head())

        return air_quality_df

    except Exception as e:
        print(Fore.RED + f"Error in transform data - world-air-quality-data: {e}")
        return None

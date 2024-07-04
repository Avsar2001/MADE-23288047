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

        # Group by countries
        air_quality_df = (
            air_quality_df.groupby("Country")[
                [
                    "AQI Value",
                    "CO AQI Value",
                    "Ozone AQI Value",
                    "NO2 AQI Value",
                    "PM2.5 AQI Value",
                ]
            ]
            .mean()
            .reset_index()
        )

        print(Fore.GREEN + f"Air quality data transform Successful!")

        # To save this file to pre-processed directory
        air_quality_df.to_csv(
            get_absolute_path(
                f"data/pre-processed/{WORLD_AIR_QUALITY_DATA['pre_processed_data_file']}"
            ),
            sep="\t",
            encoding="utf-8",
        )

        print(
            Fore.GREEN + f"Air quality data export to pre-process directory Successful!"
        )

        return air_quality_df

    except Exception as e:
        print(Fore.RED + f"Error in transform data - world-air-quality-data: {e}")
        return None

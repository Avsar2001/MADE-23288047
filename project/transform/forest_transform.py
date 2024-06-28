import pandas as pd
from colorama import init, Fore

from utils.constant import WORLD_FOREST_DATA
from utils.utils import is_file_or_directory_exists, get_absolute_path

# Initialise colorama with reset color after every print
init(autoreset=True)


def transform_forest_dataframe():
    """
    create forest dataframe and preprocess it from csv

    :args:
    :return:
    - Pandas DataFrame - cleaned and preprocessed data
    """
    try:
        data_file_path = (
            f"{get_absolute_path('data/raw/')}{WORLD_FOREST_DATA['raw_data_file']}"
        )

        # Check if data file exists at observed location
        if not is_file_or_directory_exists(data_file_path):
            raise FileNotFoundError(f'{WORLD_FOREST_DATA["raw_data_file"]} not exists')

        # create forest dataframe from csv
        forest_df = pd.read_csv(data_file_path)

        # remove unused data columns
        forest_df = forest_df.drop(columns=WORLD_FOREST_DATA["unused_db_cols"])

        print(Fore.GREEN + f"Forest data transform Successful!")
        # print(Fore.YELLOW + forest_df.head())

        return forest_df

    except Exception as e:
        print(
            Fore.RED + f"Error in transform data - world-forest-data: {e} - {type(e)}"
        )
        return None

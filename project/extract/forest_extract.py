import os

from colorama import init, Fore

from utils.constant import WORLD_FOREST_DATA
from utils.utils import is_file_or_directory_exists, kaggle_api_instance

# Initialise colorama with reset color after every print
init(autoreset=True)


def extract_forest_dataset(path_to_download):
    """
    Download a datasets in `path_to_download` using kaggle api

    :param:
    - kaggle_api - Instance of KaggleApi
    - path_to_download - Absolute path to download datasets
    """
    try:
        # download dataset from kaggle
        kaggle_api_instance.dataset_download_files(
            WORLD_FOREST_DATA["data_uri"], path=path_to_download, unzip=True
        )

        print(
            Fore.GREEN
            + f"World Forest dataset Downloaded Successfully to {path_to_download}"
        )

        # Remove Unused files from data bundle
        if is_file_or_directory_exists(
            f"{path_to_download}/{WORLD_FOREST_DATA['unused_data_file']}"
        ):
            os.remove(f'{path_to_download}/{WORLD_FOREST_DATA["unused_data_file"]}')

        print(
            Fore.GREEN
            + f"Unused raw data files Successfully deleted from {path_to_download}"
        )

    except Exception as e:
        print(Fore.RED + f"Error downloading dataset - world-forest-area: {e}")
        return None

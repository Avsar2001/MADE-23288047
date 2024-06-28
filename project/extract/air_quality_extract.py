from colorama import init, Fore

from utils.constant import WORLD_AIR_QUALITY_DATA
from utils.utils import kaggle_api_instance

# Initialise colorama with reset color after every print
init(autoreset=True)


def extract_air_quality_dataset(path_to_download):
    """
    Download a datasets in `path_to_download` using kaggle api

    :param:
    - kaggle_api - Instance of KaggleApi
    - path_to_download - Absolute path to download datasets
    """
    try:
        # download dataset from kaggle
        kaggle_api_instance.dataset_download_files(
            WORLD_AIR_QUALITY_DATA["data_uri"], path=path_to_download, unzip=True
        )

        print(
            Fore.GREEN
            + f"Air Quality dataset Downloaded Successfully to {path_to_download}"
        )

    except Exception as e:
        print(Fore.RED + f"Error downloading dataset - world-air-quality: {e}")
        return None

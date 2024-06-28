import os

from colorama import Fore, init

from utils.constant import kaggle_json_path, current_root_directory

# Define the path to your kaggle.json file
os.environ["KAGGLE_CONFIG_DIR"] = kaggle_json_path
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialise colorama with reset color after every print
init(autoreset=True)


def get_absolute_path(path):
    """
    Returns the absolute path of a given path.
    :Args:
    - path: The path to be absolute.
    :Returns:
    - path: The absolute path.
    """
    return os.path.join(current_root_directory, path)


def is_file_or_directory_exists(path):
    """
    Checks if the given path is a file or directory.
    :Args:
    - path: The absolute path to be checked.
    :Returns:
    - is_file: True if the given path is a file / directory, False otherwise.
    """
    return os.path.exists(path)


def authenticate() -> KaggleApi:
    """
    Authenticate with Kaggle

    :Returns:
    - KaggleApi - Instance of KaggleApi
    """
    try:
        # Ensure the file exists
        if not is_file_or_directory_exists(kaggle_json_path):
            raise FileNotFoundError(f"No kaggle.json file found at {kaggle_json_path}")

        # Set up the API
        kaggle_api = KaggleApi()
        kaggle_api.authenticate()

        print(Fore.GREEN + "Kaggle API authenticated Successfully")

        return kaggle_api

    except Exception as e:
        print(Fore.RED + f"Error authenticating kaggle api: {e}")
        return None


kaggle_api_instance = authenticate()

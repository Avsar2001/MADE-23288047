import unittest

from colorama import init, Fore

from utils.constant import WORLD_FOREST_DATA, WORLD_AIR_QUALITY_DATA
from utils.utils import (
    get_absolute_path,
    is_file_or_directory_exists,
)

# Initialise colorama with reset color after every print
init(autoreset=True)


class TestExtract(unittest.TestCase):

    def test_forest_extract(self):
        print(Fore.GREEN + "Extract Test started - WORLD FOREST DATASET")
        """
        test dataset retrival from kaggle
        """
        target_directory_path = get_absolute_path("data/raw")
        target_file_path = get_absolute_path(
            f"data/raw/{WORLD_FOREST_DATA['raw_data_file']}"
        )

        # test raw directory exists at desired path
        self.assertTrue(is_file_or_directory_exists(target_directory_path))

        # Test target file exists
        self.assertTrue(is_file_or_directory_exists(target_file_path))

        # Test unused files are removed
        self.assertFalse(
            is_file_or_directory_exists(
                get_absolute_path(
                    f"{target_directory_path}/{WORLD_FOREST_DATA['unused_data_file']}"
                )
            )
        )

    def test_air_quality_extract(self):
        print(Fore.GREEN + "Extract Test started - AIR QUALITY DATASET")
        """
        test dataset retrival from kaggle
        """
        target_directory_path = get_absolute_path("data/raw")
        target_file_path = get_absolute_path(
            f"data/raw/{WORLD_AIR_QUALITY_DATA['raw_data_file']}"
        )

        # test raw directory exists at desired path
        self.assertTrue(is_file_or_directory_exists(target_directory_path))

        # Test target file exists
        self.assertTrue(is_file_or_directory_exists(target_file_path))


if __name__ == "__main__":
    unittest.main()

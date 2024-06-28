from colorama import Fore, init
from sqlalchemy import create_engine

from utils.constant import WORLD_FOREST_DATA, WORLD_AIR_QUALITY_DATA
from utils.utils import get_absolute_path

# Initialise colorama with reset color after every print
init(autoreset=True)


def dump_dataset_to_db(dataframe, db_name, datatype):
    """
    dump data into processed data directory in sqlite database

    :args:
    - dataframe: pandas dataframe
    - db_name: str
    - datatype: str
    """
    try:
        # path to processed data directory
        path_to_database = get_absolute_path("data/processed")

        # save to db in sqlite
        db_engine = create_engine(f"sqlite:///{path_to_database}/{db_name}.sqlite")
        dataframe.to_sql(
            db_name, db_engine, index=False, if_exists="replace", dtype=datatype
        )

        print(Fore.GREEN + f"{db_name} data dump Successful at {path_to_database}")

    except Exception as e:
        print(Fore.RED + f"Error in load data - {db_name}: {e}")
        return None


def load_forest_data(dataframe):
    """
    dump data into processed data directory in sqlite database

    :args:
    - dataframe: pandas dataframe
    """
    dump_dataset_to_db(
        dataframe,
        WORLD_FOREST_DATA["db_name"],
        WORLD_FOREST_DATA["sqlalchemy_datatype"],
    )


def load_air_quality_data(dataframe):
    """
    dump data into processed data directory in sqlite database

    :args:
    - dataframe: pandas dataframe
    """
    dump_dataset_to_db(
        dataframe,
        WORLD_AIR_QUALITY_DATA["db_name"],
        WORLD_AIR_QUALITY_DATA["sqlalchemy_datatype"],
    )

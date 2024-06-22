import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from sqlalchemy import create_engine, FLOAT, TEXT

# Dataset const values to generate download & process data
DATASET = {
    "WORLD_FOREST_DATA": {
        "dataset_path": "webdevbadger/world-forest-area",
        "file_name": "forest_area_percent.csv",
        "db_name": "world_forest_data",
        "sqlalchemy_datatype": {
            "Country Name": TEXT,
            "1990": FLOAT(asdecimal=True),
            "1991": FLOAT(asdecimal=True),
            "1992": FLOAT(asdecimal=True),
            "1993": FLOAT(asdecimal=True),
            "1994": FLOAT(asdecimal=True),
            "1995": FLOAT(asdecimal=True),
            "1996": FLOAT(asdecimal=True),
            "1997": FLOAT(asdecimal=True),
            "1998": FLOAT(asdecimal=True),
            "1999": FLOAT(asdecimal=True),
            "2000": FLOAT(asdecimal=True),
            "2001": FLOAT(asdecimal=True),
            "2002": FLOAT(asdecimal=True),
            "2003": FLOAT(asdecimal=True),
            "2004": FLOAT(asdecimal=True),
            "2005": FLOAT(asdecimal=True),
            "2006": FLOAT(asdecimal=True),
            "2007": FLOAT(asdecimal=True),
            "2008": FLOAT(asdecimal=True),
            "2009": FLOAT(asdecimal=True),
            "2010": FLOAT(asdecimal=True),
            "2011": FLOAT(asdecimal=True),
            "2012": FLOAT(asdecimal=True),
            "2013": FLOAT(asdecimal=True),
            "2014": FLOAT(asdecimal=True),
            "2015": FLOAT(asdecimal=True),
            "2016": FLOAT(asdecimal=True),
            "2017": FLOAT(asdecimal=True),
            "2018": FLOAT(asdecimal=True),
            "2019": FLOAT(asdecimal=True),
            "2020": FLOAT(asdecimal=True),
            "2021": FLOAT(asdecimal=True)
        }
    },
    "WORLD_AIR_QUALITY_DATA": {
        "dataset_path": "adityaramachandran27/world-air-quality-index-by-city-and-coordinates",
        "file_name": "AQI and Lat Long of Countries.csv",
        "db_name": "world_air_quality_data",
        "sqlalchemy_datatype": {
            "Country": TEXT,
            "AQI Value": FLOAT(asdecimal=True),
            "CO AQI Value": FLOAT(asdecimal=True),
            "Ozone AQI Value": FLOAT(asdecimal=True),
            "NO2 AQI Value": FLOAT(asdecimal=True),
            "PM2.5 AQI Value": FLOAT(asdecimal=True)
        }
    },
}


def authenticate():
    """
    authenticate into kaggle using kaggle.json
    api credentials stored in OS env
    :return:
    """
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()

    return kaggle_api


def download_dataset(kaggle_api):
    """
    Download a datasets in Project directory and unzip it
    :param kaggle_api:
    :return:
    """
    for key, val in DATASET.items():
        kaggle_api.dataset_download_files(val['dataset_path'], path='./project', unzip=True)
        print(f"Downloaded {key} dataset")

    return


def get_and_preprocess_forest_dataframe():
    """
    create forest dataframe and preprocess it from csv
    :param:
    :return:
    """
    # create forest dataframe from csv
    forest_df = pd.read_csv(f"./project/{DATASET["WORLD_FOREST_DATA"]["file_name"]}")

    # preprocess steps for forest dataframe
    forest_df = forest_df.drop(columns=['Country Code'])

    return forest_df


def get_and_preprocess_air_quality_dataframe():
    """
    create air quality dataframe and preprocess it from csv
    :param:
    :return:
    """
    # create air quality dataframe from csv
    air_quality_df = pd.read_csv(f'./project/{DATASET["WORLD_AIR_QUALITY_DATA"]["file_name"]}')

    # preprocess steps for air quality dataframe
    air_quality_df = air_quality_df.drop(
        columns=['City', 'AQI Category', 'CO AQI Category', 'Ozone AQI Category', 'NO2 AQI Category',
                 'PM2.5 AQI Category', 'lat', 'lng'])

    return air_quality_df


def dump_dataset_to_db(dataframe, db_name, datatype):
    """
    insert data into sqlite database
    :param dataframe:
    :param db_name:
    :param datatype:
    :return:
    """

    db_engine = create_engine(f"sqlite:///./data/{db_name}.sqlite")
    dataframe.to_sql(db_name, db_engine, index=False, if_exists='replace', dtype=datatype)
    return


def data_collector():
    """
    download data from kaggle and store it into local sqlite database in '/data' directory with appropriate datatype
    :return:
    """
    kaggle_api = authenticate()

    # download dataset in local storage
    download_dataset(kaggle_api)

    # create forest dataframe from csv
    forest_df = get_and_preprocess_forest_dataframe()

    # create air quality dataframe from csv
    air_quality_df = get_and_preprocess_air_quality_dataframe()

    # insert forest data into sqlite database
    dump_dataset_to_db(dataframe=forest_df, db_name=DATASET['WORLD_FOREST_DATA']['db_name'],
                       datatype=DATASET['WORLD_FOREST_DATA']['sqlalchemy_datatype'])

    # insert air quality data into sqlite database
    dump_dataset_to_db(dataframe=air_quality_df, db_name=DATASET['WORLD_AIR_QUALITY_DATA']['db_name'],
                       datatype=DATASET['WORLD_AIR_QUALITY_DATA']['sqlalchemy_datatype'])

    return


if __name__ == "__main__":
    data_collector()
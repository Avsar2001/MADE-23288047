import os
from pathlib import Path

from sqlalchemy import FLOAT, TEXT

"""
# Get the current working directory

Ex: /Users/avsar/Desktop/FAU Sem 3/MADE-23288047
"""
current_root_directory = Path(__file__).parent.parent.parent.absolute()


"""
# Kaggle json folder path
"""
kaggle_json_path = os.path.join(current_root_directory, "project/.config")

WORLD_FOREST_DATA = dict(
    data_uri="webdevbadger/world-forest-area",
    raw_data_file="forest_area_percent.csv",
    unused_data_file="forest_area_km.csv",
    unused_db_cols=["Country Code"],
    db_name="world_forest_data",
    sqlalchemy_datatype={
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
        "2021": FLOAT(asdecimal=True),
    },
)

WORLD_AIR_QUALITY_DATA = dict(
    data_uri="adityaramachandran27/world-air-quality-index-by-city-and-coordinates",
    raw_data_file="AQI and Lat Long of Countries.csv",
    unused_db_cols=[
        "City",
        "AQI Category",
        "CO AQI Category",
        "Ozone AQI Category",
        "NO2 AQI Category",
        "PM2.5 AQI Category",
        "lat",
        "lng",
    ],
    db_name="world_air_quality_data",
    sqlalchemy_datatype={
        "Country": TEXT,
        "AQI Value": FLOAT(asdecimal=True),
        "CO AQI Value": FLOAT(asdecimal=True),
        "Ozone AQI Value": FLOAT(asdecimal=True),
        "NO2 AQI Value": FLOAT(asdecimal=True),
        "PM2.5 AQI Value": FLOAT(asdecimal=True),
    },
)

from extract.air_quality_extract import extract_air_quality_dataset
from extract.forest_extract import extract_forest_dataset
from load.data_load import load_forest_data, load_air_quality_data
from transform.air_quality_transform import transform_air_quality_dataframe
from transform.forest_transform import transform_forest_dataframe
from utils.utils import get_absolute_path

if __name__ == "__main__":
    # To extract forest data to raw data-set collection (Data lake preparation)
    extract_forest_dataset(get_absolute_path("data/raw"))

    # To extract air quality data to raw data-set collection (Data lake preparation)
    extract_air_quality_dataset(get_absolute_path("data/raw"))

    # To transform forest data and generate pandas data frame
    forest_df = transform_forest_dataframe()

    # To transform air quality data and generate pandas data frame
    air_quality_df = transform_air_quality_dataframe()

    # load forest data into sqlite database
    load_forest_data(forest_df)

    # Load air quality data into sqlite database
    load_air_quality_data(air_quality_df)

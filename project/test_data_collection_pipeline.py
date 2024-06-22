import pandas as pd
import pytest
from sqlalchemy import create_engine, inspect
import data_collection as dc


@pytest.mark.dependency()
def test_datasets_retrival():
    ds1 = dc.get_and_preprocess_forest_dataframe()
    assert isinstance(ds1, pd.DataFrame)

    ds2 = dc.get_and_preprocess_air_quality_dataframe()
    assert isinstance(ds2, pd.DataFrame)


# Execute test only if previous test passed
@pytest.mark.dependency()
def test_data_collector_pipeline():
    """
    Test: 'data_collection.py' pipeline number of created tables and names
    """
    data_dict = dc.DATASET
    dc.data_collector()

    wf_db_engine = create_engine(f"sqlite:///./data/{data_dict['WORLD_FOREST_DATA']['db_name']}.sqlite")
    wf_inspector = inspect(wf_db_engine)
    wf_tables = wf_inspector.get_table_names()

    assert len(wf_tables) == 1
    assert data_dict['WORLD_FOREST_DATA']['db_name'] in wf_tables

    waq_db_engine = create_engine(f"sqlite:///./data/{data_dict['WORLD_AIR_QUALITY_DATA']['db_name']}.sqlite")
    waq_inspector = inspect(waq_db_engine)
    waq_tables = waq_inspector.get_table_names()

    assert len(waq_tables) == 1
    assert data_dict['WORLD_AIR_QUALITY_DATA']['db_name'] in waq_tables
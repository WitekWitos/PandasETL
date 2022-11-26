import unittest
import pandas as pd
from pandasetl.entities.regions import ExtractRegions


#given
regions_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\regions.csv')
regions_row = ExtractRegions(regions_csv)

def test_get_region_id():
    # when
    result = regions_row.get_region_id()
    # then
    assert result.iloc[0] == 1
    
def test_get_region_description():
    # when
    result = regions_row.get_region_description()
    # then
    assert result.iloc[0] == 'Eastern'


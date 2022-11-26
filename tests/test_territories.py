import unittest
import pandas as pd
from pandasetl.entities.territories import ExtractTerritories


#given
territories_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\territories.csv')
territories_row = ExtractTerritories(territories_csv)

def test_get_territoryID():
    # when
    result = territories_row.get_territoryID()
    # then
    assert result.iloc[0] == 1581
    
def test_get_territory_description():
    # when
    result = territories_row.get_territory_description()
    # then
    assert result.iloc[0] == 'Westboro'

def test_get_region_id():
    # when
    result = territories_row.get_region_id()
    # then
    assert result.iloc[0] == 1

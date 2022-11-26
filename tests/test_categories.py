import unittest
import pandas as pd
from pandasetl.entities.categories import ExtractCategories


#given
categories_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\categories.csv')
categories_row = ExtractCategories(categories_csv)

def test_get_category_name():
    # when
    result = categories_row.get_category_name()
    # then
    assert result.iloc[0] == 'Beverages'
    
def test_get_category_id():
    # when
    result = categories_row.get_category_id()
    # then
    assert result.iloc[0] == 1

def test_get_description():
    # when
    result = categories_row.get_description()
    # then
    assert result.iloc[0] == 'Soft drinks coffees teas beers and ales'

def test_get_picture():
    # when
    result = categories_row.get_picture()
    # then
    assert result.iloc[0] == '0x151C2F00020000000D000E0014002100FFFFFFFF4269746D617020496D616765005061696E742E5069637475726500010500000200000007000000504272757368000000000000000000A0290000424D98290000000000005600000028000000AC00000078000000010004000000000000000000880B0000880B0000080000'
    

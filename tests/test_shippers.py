import unittest
import pandas as pd
from pandasetl.entities.shippers import ExtractShippers


#given
shippers_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\shippers.csv')
shippers_row = ExtractShippers(shippers_csv)

def test_get_shipper_id():
    # when
    result = shippers_row.get_shipper_id()
    # then
    assert result.iloc[0] == 1
    
def test_get_company_name():
    # when
    result = shippers_row.get_company_name()
    # then
    assert result.iloc[0] == 'Speedy Express'

def test_get_phone():
    # when
    result = shippers_row.get_phone()
    # then
    assert result.iloc[0] == '(503) 555-9831'

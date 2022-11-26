import unittest
import pandas as pd
from pandasetl.entities.order_details import ExtractOrder_details


#given
order_details_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\order_details.csv')
order_details_row = ExtractOrder_details(order_details_csv)

def test_get_order_id():
    # when
    result = order_details_row.get_order_id()
    # then
    assert result.iloc[0] == 10248

def test_get_product_id():
    # when
    result = order_details_row.get_product_id()
    # then
    assert result.iloc[0] == 11
 
def test_get_unit_price():
    # when
    result = order_details_row.get_unit_price()
    # then
    assert result.iloc[0] == 14.00

def test_get_quantity():
    # when
    result = order_details_row.get_quantity()
    # then
    assert result.iloc[0] == 12

def test_get_discount():
    # when
    result = order_details_row.get_discount()
    # then
    assert result.iloc[0] == 0

    

    
    

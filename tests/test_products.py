import unittest
import pandas as pd
from pandasetl.entities.products import ExtractProducts
import math

#given
products_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\products.csv')
products_row = ExtractProducts(products_csv)

def test_get_product_id():
    # when
    result = products_row.get_product_id()
    # then
    assert result.iloc[0] == 1

def test_get_product_name():
    # when
    result = products_row.get_product_name()
    # then
    assert result.iloc[0] == 'Chai'

def test_get_supplier_id():
    # when
    result = products_row.get_supplier_id()
    # then
    assert result.iloc[0] == 1  

def test_get_category_id():
    # when
    result = products_row.get_category_id()
    # then
    assert result.iloc[0] == 1  

def test_get_quantityPerUnit():
    # when
    result = products_row.get_quantityPerUnit()
    # then
    assert result.iloc[0] == '10 boxes x 20 bags'    

def test_get_unit_price():
    # when
    result = products_row.get_unit_price()
    # then
    assert result.iloc[0] == 18.00 
    
def test_get_units_in_stock():
    # when
    result = products_row.get_units_in_stock()
    # then
    assert result.iloc[0] == 39   
    
def test_get_units_on_order():
    # when
    result = products_row.get_units_on_order()
    # then
    assert result.iloc[0] == 0    

def test_get_reorder_level():
    # when
    result = products_row.get_reorder_level()
    # then
    assert result.iloc[0] == 10  
    
def test_get_discontinued():
    # when
    result = products_row.get_discontinued()
    # then
    assert result.iloc[0] == 0 
    
    
    
import unittest
import pandas as pd
from pandasetl.entities.orders import ExtractOrders
import math

#given
orders_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\orders.csv')
orders_row = ExtractOrders(orders_csv)

def test_get_order_id():
    # when
    result = orders_row.get_order_id()
    # then
    assert result.iloc[0] == 10248
    
def test_get_customer_id():
    # when
    result = orders_row.get_customer_id()
    # then
    assert result.iloc[0] == 'VINET'
 
def test_get_employee_id():
    # when
    result = orders_row.get_employee_id()
    # then
    assert result.iloc[0] == 5
    
def test_get_order_date():
    # when
    result = orders_row.get_order_date()
    # then
    assert result.iloc[0] == '1996-07-04 00:00:00.000'   

def test_get_required_date():
    # when
    result = orders_row.get_required_date()
    # then
    assert result.iloc[0] == '1996-08-01 00:00:00.000'   
    
def test_get_shipped_date():
    # when
    result = orders_row.get_shipped_date()
    # then
    assert result.iloc[0] == '1996-07-16 00:00:00.000'    
    
def test_get_ship_Via():
    # when
    result = orders_row.get_ship_Via()
    # then
    assert result.iloc[0] == 3

def test_get_freight():
    # when
    result = orders_row.get_freight()
    # then
    assert result.iloc[0] == 32.38 
   
def test_get_ship_name():
    # when
    result = orders_row.get_ship_name()
    # then
    assert result.iloc[0] == 'Vins et alcools Chevalier' 

def test_get_ship_address():
    # when
    result = orders_row.get_ship_address()
    # then
    assert result.iloc[0] == '59 rue de l\'Abbaye'   
 
def test_get_ship_city():
    # when
    result = orders_row.get_ship_city()
    # then
    assert result.iloc[0] == 'Reims'
    
def test_get_ship_region():
    # when
    result = orders_row.get_ship_region()
    # then
    assert math.isnan(result.iloc[0]) == True

def test_get_ship_postal_code():
    # when
    result = orders_row.get_ship_postal_code()
    # then
    assert result.iloc[0] == 51100 
       
def test_get_ship_country():
    # when
    result = orders_row.get_ship_country()
    # then
    assert result.iloc[0] == 'France'   
    
    
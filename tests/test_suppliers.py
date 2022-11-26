import unittest
import pandas as pd
from pandasetl.entities.suppliers import ExtractSuppliers
import math


#given
suppliers_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\suppliers.csv')
suppliers_row = ExtractSuppliers(suppliers_csv)

def test_get_supplier_id():
    # when
    result = suppliers_row.get_supplier_id()
    # then
    assert result.iloc[0] == 1
    
def test_get_company_name():
    # when
    result = suppliers_row.get_company_name()
    # then
    assert result.iloc[0] == 'Exotic Liquids'  
     
def test_get_contact_name():
    # when
    result = suppliers_row.get_contact_name()
    # then
    assert result.iloc[0] == 'Charlotte Cooper' 

def test_get_contact_title():
    # when
    result = suppliers_row.get_contact_title()
    # then
    assert result.iloc[0] == 'Purchasing Manager'
    
def test_get_address():
    # when
    result = suppliers_row.get_address()
    # then
    assert result.iloc[0] == '49 Gilbert St.'    

def test_get_city():
    # when
    result = suppliers_row.get_city()
    # then
    assert result.iloc[0] == 'London'   

def test_get_region():
    # when
    result = suppliers_row.get_region()
    # then
    assert math.isnan(result.iloc[0]) == True    
    
def test_get_postal_code():
    # when
    result = suppliers_row.get_postal_code()
    # then
    assert result.iloc[0] == 'EC1 4SD'

def test_get_country():
    # when
    result = suppliers_row.get_country()
    # then
    assert result.iloc[0] == 'UK'  

def test_get_phone():
    # when
    result = suppliers_row.get_phone()
    # then
    assert result.iloc[0] == '(171) 555-2222'

def test_get_fax():
    # when
    result = suppliers_row.get_fax()
    # then
    assert math.isnan(result.iloc[0]) == True
    
def test_get_home_page():
    # when
    result = suppliers_row.get_home_page()
    # then
    assert math.isnan(result.iloc[0]) == True   
    


    
    
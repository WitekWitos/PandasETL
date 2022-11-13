import unittest
import pandas as pd
from pandasetl.entities.customer import ExtractCustomer
import math

#given
customer_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\customer.csv')
customer_row = ExtractCustomer(customer_csv)

def test_get_customer_id():
    # when
    result = customer_row.get_customer_id()
    # then
    assert result.iloc[0] == 'ALFKI'
    
def test_get_company_name():
    # when
    result = customer_row.get_company_name()
    # then
    assert result.iloc[0] == 'Alfreds Futterkiste'

def test_get_contact_name():
    # when
    result = customer_row.get_contact_name()
    # then
    assert result.iloc[0] == 'Maria Anders'

def test_get_contact_title():
    # when
    result = customer_row.get_contact_title()
    # then
    assert result.iloc[0] == 'Sales Representative'
    
def test_get_address():
    # when
    result = customer_row.get_address()
    # then
    assert result.iloc[0] == 'Obere Str. 57'
    
def test_get_city():
    # when
    result = customer_row.get_city()
    # then
    assert result.iloc[0] == 'Berlin'

def test_get_region():
    # when
    result = customer_row.get_region()
    # then
    assert math.isnan(result.iloc[0]) == True

    
def test_get_postal_code():
    # when
    result = customer_row.get_postal_code()
    # then
    assert result.iloc[0] == 12209

def test_get_country():
    # when
    result = customer_row.get_coutry()
    # then
    assert result.iloc[0] == 'Germany'
    
def test_get_phone():
    # when
    result = customer_row.get_phone()
    # then
    assert result.iloc[0] == '030-0074321'
    
def test_get_fax():
    # when
    result = customer_row.get_fax()
    # then
    assert result.iloc[0] == '030-0076545'
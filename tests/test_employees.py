import unittest
import pandas as pd
from pandasetl.entities.employees import ExtractEmployees


#given
employees_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\employees.csv')
employees_row = ExtractEmployees(employees_csv)

def test_get_employee_ID():
    # when
    result = employees_row.get_employee_ID()
    # then
    assert result.iloc[0] == 1
    
def test_get_last_name():
    # when
    result = employees_row.get_last_name()
    # then
    assert result.iloc[0] == 'Davolio'

def test_get_first_name():
    # when
    result = employees_row.get_first_name()
    # then
    assert result.iloc[0] == 'Nancy'
    
def test_get_title():
    # when
    result = employees_row.get_title()
    # then
    assert result.iloc[0] == 'Sales Representative'
    
def test_get_title_of_courtesy():
    # when
    result = employees_row.get_title_of_courtesy()
    # then
    assert result.iloc[0] == 'Ms.'
    
def test_get_birth_date():
    # when
    result = employees_row.get_birth_date()
    # then
    assert result.iloc[0] == '1948-12-08 00:00:00.000'

def test_get_hire_date():
    # when
    result = employees_row.get_hire_date()
    # then
    assert result.iloc[0] == '1992-05-01 00:00:00.000' 
    
def test_get_address():
    # when
    result = employees_row.get_address()
    # then
    assert result.iloc[0] == '507 20th Ave. E. Apt. 2A'
    
def test_get_city():
    # when
    result = employees_row.get_city()
    # then
    assert result.iloc[0] == 'Seattle'
    
def test_get_region():
    # when
    result = employees_row.get_region()
    # then
    assert result.iloc[0] == 'WA'
    
def test_get_postal_code():
    # when
    result = employees_row.get_postal_code()
    # then
    assert result.iloc[0] == 98122
    
def test_get_country():
    # when
    result = employees_row.get_country()
    # then
    assert result.iloc[0] == 'USA'

def test_get_home_phone():
    # when
    result = employees_row.get_home_phone()
    # then
    assert result.iloc[0] ==  '(206) 555-9857'
    
def test_get_extension():
    # when
    result = employees_row.get_extension()
    # then
    assert result.iloc[0] == 5467

def test_get_photo():
    # when
    result = employees_row.get_photo()
    # then
    assert result.iloc[0] == '0x151C2F00020000000D000E0014002100FFFFFFFF4269746D617020496D616765005061696E742E506963747572650001050000020000000700000050427275736800000000000000000020540000424D20540000000000007600000028000000C0000000DF0000000100040000000000A0530000CE0E0000D80E0000000000'

def test_get_notes():
    # when
    result = employees_row.get_notes()
    # then
    assert result.iloc[0] == 'Education includes a BA in psychology from Colorado State University in 1970.  She also completed The Art of the Cold Call.  Nancy is a member of Toastmasters International.'

def test_reports_To():
    # when
    result = employees_row.get_reports_To()
    # then
    assert result.iloc[0] == 2

def test_photo_path():
    # when
    result = employees_row.get_photo_path()
    # then
    assert result.iloc[0] == 'http://accweb/emmployees/davolio.bmp'
    
    
    

    

 
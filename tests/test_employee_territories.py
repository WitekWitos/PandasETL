import unittest
import pandas as pd
from pandasetl.entities.employee_territories import ExtractEmployee_territories


#given
employee_territories_csv = pd.read_csv(r'C:\Users\1\VSC\PandasETL\tests\test_data\employee_territories.csv')
employee_territories_row = ExtractEmployee_territories(employee_territories_csv)

def test_get_employee_ID():
    # when
    result = employee_territories_row.get_employee_ID()
    # then
    assert result.iloc[0] == 1
    
def test_get_territory_ID():
    # when
    result = employee_territories_row.get_territory_ID()
    # then
    assert result.iloc[0] == 6897


import unittest
from pandasetl.customer import Customer


def test_is_not_over_18():
    # given
    customer = Customer('Witek',17,'Male','pricate client')
    # when
    result = customer.IsOver18()
    # then
    assert result == 'No, I am under 18.'

 
def test_is_over_18():
    # given
    customer = Customer('Oti',18,'female','bussiness client')
    # when
    result = customer.IsOver18()
    # then
    assert result == 'Yes I am over 18.'

def test_is_male():
    # given
    customer = Customer('Witek',17,'Male','pricate client')
    # when
    result = customer.IsMale()
    # then
    assert result == True
    
def test_is_not_male():
    # given
    customer2 = Customer('Oti',25,'female','pricate client')
    # when
    result = customer2.IsMale()
    # then
    assert result == False
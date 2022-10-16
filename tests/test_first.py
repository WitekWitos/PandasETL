
import unittest


def IsOver18(age):
    return age >= 18
    


def test_isOver18():
    # given
    age = 25
    # when
    result = IsOver18(age)
    # then
    assert result

def test_is_not_Over18():
    #given 
    age = 1
    #when
    result = IsOver18(age)
    # then:
    assert not result
    
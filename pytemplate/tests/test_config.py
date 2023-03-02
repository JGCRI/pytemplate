# Import libraries
import pytest
import bed

def test_fake():
    """
    test fake function
    :return:
    """
    assert bed.fake() == True

def test_fake2():
    """
    test fake2 function
    :return:
    """
    assert bed.fake2() == True

def test_class():
    """
    test class
    :return:
    """
    a1 = bed.Bed()  # Coming from Model.py
    a1.var1
    assert a1.var1 == 0.125
# Import libraries
import pytest
import pytemplate

def test_fake():
    """
    test fake function
    :return:
    """
    assert pytemplate.fake() == True

def test_fake2():
    """
    test fake2 function
    :return:
    """
    assert pytemplate.fake2() == True

def test_class():
    """
    test class
    :return:
    """
    a1 = pytemplate.Pytemplate()  # Coming from Model.py
    a1.var1
    assert a1.var1 == 0.125
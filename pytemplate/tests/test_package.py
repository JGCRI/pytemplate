# Import libraries
import pytest
import pytemplate
import os

def test_clean_up():
    """
    test clean_up function
    :return:
    """
    assert pytemplate.clean_up(2,2) == 4

def test_diagnostics():
    """
    test diagnostics function
    :return:
    """
    assert pytemplate.diagnostics(2,2) == 4

def test_method():
    """
    test method
    :return:
    """
    assert pytemplate.method(2,2) == 4

def test_read_config():
    """
    test read_config
    :return:
    """
    assert pytemplate.read_config() == os.path.abspath("example_config.yml")

def test_read_data():
    """
    test method
    :return:
    """
    assert pytemplate.read_data(2,2) == 4

def test_class():
    """
    test class
    :return:
    """
    assert pytemplate.Pytemplate().var == 5
    assert pytemplate.Pytemplate().config == os.path.abspath("example_config.yml")
    assert pytemplate.Pytemplate().method == 1
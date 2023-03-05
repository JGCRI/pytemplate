# Import libraries
import pytest
import pytemplate
import os

def test_get_data():
    """
    test clean_up function
    :return:
    """
    assert os.path.abspath(pytemplate.get_data()) == os.path.abspath(os.path.join(os.getcwd(),'downloaded_data/examples'))

def test_read_config():
    """
    test read_config
    :return:
    """
    downloaded_data_path = pytemplate.get_data()
    example_config = os.path.join(downloaded_data_path,'example_config.yml')
    assert pytemplate.read_config(example_config) == {'path_example_data_set': 'example_data.csv'}

def test_read_data():
    """
    test method
    :return:
    """
    downloaded_data_path = pytemplate.get_data()
    example_config = os.path.join(downloaded_data_path,'example_config.yml')
    config = pytemplate.read_config(example_config)
    example_key = list(config.keys())[0]
    example_value = os.path.join(downloaded_data_path,list(config.values())[0])
    updated_config = config
    updated_config[example_key] = example_value
    df = (pytemplate.Data(updated_config)).example_data_set
    assert list(df.name)==['a','b','c']
    assert list(df.value) == [1,2,3]

def test_method():
    """
    test method
    :return:
    """
    assert pytemplate.method(2,2) == 4

def test_write_outputs():
    """
    test diagnostics function
    :return:
    """
    assert pytemplate.write_outputs(2,2) == 4

def test_diagnostics():
    """
    test diagnostics function
    :return:
    """
    assert pytemplate.diagnostics(2,2) == 4

def test_clean_up():
    """
    test clean_up function
    :return:
    """
    assert pytemplate.clean_up(2,2) == 4

def test_class():
    """
    test class
    :return:
    """
    assert pytemplate.Pytemplate().var == 5
    assert pytemplate.Pytemplate().config == ''
    assert pytemplate.Pytemplate().method == 1
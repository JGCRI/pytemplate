# CTRL + ALT + L (Reformat)
# CTRL + / to comment out groups of lines
# pip install pytest # In terminal for testing
# pytest # In terminal for testing

import pytemplate
import os

# Get example data
data_folder = pytemplate.get_data()

# Test Model Modules
config_file = os.path.join(data_folder,"example_config.yml")
a1 = pytemplate.Pytemplate(config_file=config_file) # Coming from model.py
a1.var
a1.config
a1.method

"""
@Date:
@authors:
@Project: pytemplate v0.0

License:  BSD 2-Clause, see LICENSE and DISCLAIMER files
Copyright (c) 2022, Battelle Memorial Institute

"""

from pytemplate.read_config import read_config
from pytemplate.method import method


class Pytemplate:
    """ Model wrapper for pytemplate"""

    def __init__(self, config_file='config'):
        self.var1 = 0.125
        self.var = 5

        # Read in Config File
        self.config = read_config(config_file)

        # Read data
        # self.data = read_data(self.config)

        # Calculate building energy demand
        self.method = method()
        # self.demand_cool = demand(self.data, type = "cool")

        # diagnostics
        # diagnostics()

        # write outputs
        # write_outputs()

        # clean up and close
        # clean_up()
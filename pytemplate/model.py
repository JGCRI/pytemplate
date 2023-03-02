"""
@Date:
@authors:
@Project: bed v0.0

License:  BSD 2-Clause, see LICENSE and DISCLAIMER files
Copyright (c) 2022, Battelle Memorial Institute

"""

from bed.read_config import read_config
from bed.demand import demand


class Bed:
    """ Model wrapper for bed"""

    def __init__(self, config_file='config'):
        self.var1 = 0.125
        self.var = 5

        # Read in Config File
        self.config = read_config(config_file)

        # Read data
        # self.data = read_data(self.config)

        # Calculate building energy demand
        self.demand_heat = demand(calibration_coefficient=1, degree_hours=1, thermal_conductance=1,
                                  surface_to_floor_ratio=1, internal_gain=1, satiation=1,
                                  income_per_capita=1, service_price=1)
        # self.demand_cool = demand(self.data, type = "cool")

        # diagnostics
        # diagnostics()

        # write outputs
        # write_outputs()

        # clean up and close
        # clean_up()
from pytemplate.read_config import read_config
from pytemplate.method import method
import logging

class Pytemplate:
    """ Model wrapper for pytemplate"""

    def __init__(self, config_file=""):

        logging.info('Starting Pytemplate model.')

        self.var = 5        # Example constant to set within Pytemplate class

        # Read in Config File
        self.config = read_config(config_file)

        # Read data
        # self.data = read_data(self.config)

        # Run main method
        self.method = method()

        # Run diagnostics
        # diagnostics()

        # Write outputs
        # write_outputs()

        # clean up and close
        # clean_up()

        logging.info('Pytemplate model run complete.')
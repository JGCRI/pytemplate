import logging
import pandas as pd


class Data:
    """ Data class"""

    def __init__(self, config=''):
        """
        :param config:         configuration file path
        :type config:          yaml
        :return:               Data
        """

        logging.info('Starting to build Data class object from read_data.py...')

        self.config = config

        if config != '':
            self.example_data_set = pd.read_csv(config['path_example_data_set'])

        logging.info('Data class object built from read_data.py.')

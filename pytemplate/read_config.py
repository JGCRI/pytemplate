import os
import logging

def read_config(config_file="example_config.yml"):
    """
    Read configuration file.

    :param config_file:         configuration file path
    :type config_file:          string
    :return:
    """

    logging.info('Starting function read_config...')

    path_to_config = os.path.abspath(config_file)
    file_exists = os.path.exists(path_to_config)
    logging.info(f'config_file {path_to_config} exists: {file_exists}')

    logging.info('Function read_config complete.')

    return path_to_config
import os
import yaml
import logging

def read_config(config_file=""):
    """
    Read configuration file.

    :param config_file:         configuration file path
    :type config_file:          string
    :return:
    """

    logging.info('Starting function read_config...')

    path_to_config = os.path.abspath(config_file)
    file_exists = os.path.exists(path_to_config)

    if file_exists:
        is_file = os.path.isfile(path_to_config)
        if is_file:
            with open(path_to_config, "r") as stream:
                try:
                    config = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            config = config_file
            logging.error(f'Config file provided: {path_to_config} is not a valid file.')
    else:
        config = config_file
        logging.error(f'Config file provided: {path_to_config} is not a valid file.')

    logging.info('Function read_config complete.')

    return config

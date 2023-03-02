import logging


def read_data(read_data_param_1=1,read_data_param_2=1.0):
    """Example function read_data

    :param read_data_param_1:                    Description of param (Units)
    :type read_data_param_1:                     int
    :param read_data_param_2:                    Description of param (Units)
    :type read_data_param_2:                     int

    :return:                                    int output value

    """

    logging.info('Starting function read_data.')

    read_data_output = read_data_param_1 * read_data_param_2

    logging.info('Function read_data completed.')

    return read_data_output
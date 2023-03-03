import logging


def write_outputs(write_outputs_param_1=1,write_outputs_param_2=1.0):
    """Example function write_outputs

    :param write_outputs_param_1:                    Description of param (Units)
    :type write_outputs_param_1:                     int
    :param write_outputs_param_2:                    Description of param (Units)
    :type write_outputs_param_2:                     int

    :return:                                    int output value

    """

    logging.info('Starting function write_outputs.')

    write_outputs_output = write_outputs_param_1 * write_outputs_param_2

    logging.info('Function write_outputs completed.')

    return write_outputs_output
import logging


def method(method_param_1=1,method_param_2=1.0):
    """Example function method

    :param method_param_1:                    Description of param (Units)
    :type method_param_1:                     int
    :param method_param_2:                    Description of param (Units)
    :type method_param_2:                     int

    :return:                                    int output value

    """

    logging.info('Starting function method.')

    method_output = method_param_1 * method_param_2

    logging.info('Function method completed.')

    return method_output
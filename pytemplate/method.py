import logging
import numpy


# method

def method(param_1=1, param_2=1):
    """
    :param param_1:             Description of param_1 (Units)
    :param param_2:             Description of param_1 (Units)
    """

    logging.info('Starting function method.')

    method_output = param_1 * param_2

    logging.info('Function demand completed.')

    return method_output

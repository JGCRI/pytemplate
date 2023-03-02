import logging


def clean_up(clean_up_param_1=1,clean_up_param_2=1.0):
    """Example function clean_up

    :param clean_up_param_1:                    Description of param (Units)
    :type clean_up_param_1:                     int
    :param clean_up_param_2:                    Description of param (Units)
    :type clean_up_param_2:                     int

    :return:                                    int output value

    """

    logging.info('Starting function clean_up.')

    clean_up_output = clean_up_param_1 * clean_up_param_2

    logging.info('Function method completed.')

    return clean_up_output

import logging


def diagnostics(diagnostics_param_1=1,diagnostics_param_2=1.0):
    """Example function diagnostics

    :param diagnostics_param_1:                    Description of param (Units)
    :type diagnostics_param_1:                     int
    :param diagnostics_param_2:                    Description of param (Units)
    :type diagnostics_param_2:                     int

    :return:                                    int output value

    """

    logging.info('Starting function diagnostics.')

    diagnostics_output = diagnostics_param_1 * diagnostics_param_2

    logging.info('Function method completed.')

    return diagnostics_output
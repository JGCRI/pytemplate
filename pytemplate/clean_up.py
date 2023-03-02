import logging

# Inputs needed:
#   k unitless calibration coefficient
#   HDH heating degree hours
#   CDH cooling degree hours
#   n = thermal conductance (GJ/m2 hour C)
#   R = unitless average surface-to-floor area ratio
#   IG internal gain [GJ/m2]
#   uh = region and sector-specific demand satition for heating
#   uc = region and sector-specific demand satition for cooling
#   i = per-capita income
#   Ph = total price of service (weighted average of technologies used) heating
#   Pc = total price of service (weighted average of technologies used) cooling

def fake(fake_param: int = 1):
    """Fake function to remove.

    :param fake_param:                          A fake integer
    :type fake_param:                           int

    :return:                                    boolean value

    """

    return True

def fake2(fake_param: int = 1):
    """Fake function to remove.

    :param fake_param:                          A fake integer
    :type fake_param:                           int

    :return:                                    boolean value

    """

    logging.info('This is a log file for fake 2')

    return True
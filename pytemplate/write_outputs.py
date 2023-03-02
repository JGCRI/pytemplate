import logging

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
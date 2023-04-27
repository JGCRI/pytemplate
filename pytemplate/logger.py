import logging
from datetime import date

logging.basicConfig(filename='logfile.log', filemode='w', level=logging.INFO)
logging.info('logging started at: %s', date.today())
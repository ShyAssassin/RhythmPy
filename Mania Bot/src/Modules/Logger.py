import logging


# gets logger
logger = logging.getLogger(__name__)
# sets logger level
logger.setLevel(logging.DEBUG)
# define file handler and set formatter
LoggingFile = logging.FileHandler('app.log')
Formatter = logging.Formatter('%(name)s, %(lineno)d || %(asctime)s :: %(levelname)s :: %(message)s')
LoggingFile.setFormatter(Formatter)
# add file handler to logger
logger.addHandler(LoggingFile)

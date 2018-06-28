#!/usr/bin/python

import logging

# NOTSET	0
# DEBUG		10
# INFO		20
# WARNING	30
# ERROR		40
# CRITICAL	50

#Create and configure logger
LOG_PATH = 'log.txt'
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'

try:
	open(LOG_PATH, 'rb')
except (SystemExit, KeyboardInterrupt):
	raise
except Exception, e:
	logger.error('cannot open a file')

logging.basicConfig(filename = LOG_PATH,
	                level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

logger = logging.getLogger()

print(logger.level)

logger.debug('debug test')
logger.info('info test')
logger.warning('warning test')
logger.error('error test')
logger.critical('critical test')
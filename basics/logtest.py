##@package Wetter_logging
# Logging konfigurieren

import logging
import logging.handlers
import sys


#Get the root logger (muss in jedes Modul)
logger = logging.getLogger('Raspi_GH')

def init():
    #set the root logger level, it defaults to logging.WARNING
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    print(logger.getEffectiveLevel())

    #Bildschirm-Handler  (für Alles im Test-System)
    #logger.addHandler(screen_hdlr)
    #logger.handlers.setLevel(logging.DEBUG)

if __name__ == '__main__':
    init()
    #demonstrate the logging levels
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('W%sN%sNG', 'ar', 'i')
    logger.error('ERROR')
    logger.critical('CRITICAL')

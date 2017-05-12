import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log')
logger=logging.getLogger(__name__)
logger.info('starting')
records= {'ohn': 55, 'tom': 66}
logger.debug('Records : %s' , records)
logger.info('printing recoreds')



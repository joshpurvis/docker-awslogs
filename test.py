import logging
logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    for n in range(20000):
        logger.info(n)


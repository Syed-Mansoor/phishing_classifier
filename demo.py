from src.logger import logging
from src.exception import PhishingException
import sys

try:
    a = 1/0
    logging.info('got error')
    logging.info("Got an error")
except Exception as e:
    raise PhishingException(e,sys)
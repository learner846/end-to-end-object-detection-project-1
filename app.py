from signlanguage.logger import logger
from signlanguage.exception import SignException
import sys

#logging.info("Welcome to the project")

#import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# file_handler = logging.FileHandler("my_log.log")
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

#logger.info("Welcome to the project")
try:
    a = 7/'9'

except Exception as e:
    raise SignException(e, sys) from e
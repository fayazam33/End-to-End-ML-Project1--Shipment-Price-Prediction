from shipment.logger import logging
from shipment.exception import shippingException
import sys
logging.info("this is a test log message from demo.py")
try:
    a=1/0
except Exception as e:
    logging.info(e)
    raise shippingException(e,sys) from e
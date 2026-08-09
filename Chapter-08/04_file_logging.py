import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error")


"""
WARNING:root:Warning message
ERROR:root:Error message
CRITICAL:root:Critical error"""

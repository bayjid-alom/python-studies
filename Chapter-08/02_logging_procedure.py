# importing module
import logging

# create and configure logger
# logging.basicConfig(
#     filename="loggingProcedure.log",format="%(asctime)s%(message)s",filemode="w"
# )


# to show in terminal(basic)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s - %(levelname)s")



# creting an object
logger = logging.getLogger()

# setting the threshold or logger to DEBUG
logger.setLevel(logging.DEBUG)

# test messages
logger.debug("Harmless Debug Message")
logger.info("Just an Information")
logger.warning("It's a Warning!")
logger.error("Did you try to devide by zero?")
logger.critical("Internet is down")



"""
Output:
2026-08-04 13:39:50,028 - Harmless Debug Message - DEBUG
2026-08-04 13:39:50,028 - Just an Information - INFO
2026-08-04 13:39:50,029 - It's a Warning! - WARNING
2026-08-04 13:39:50,029 - Did you try to devide by zero? - ERROR
2026-08-04 13:39:50,029 - Internet is down - CRITICAL
"""
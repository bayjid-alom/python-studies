import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Division by zero occurred")



"""
2026-08-09 19:46:43,903 - ERROR - Division by zero occurred
Traceback (most recent call last):
  File "C:\Python-Programming\Chapter-08\05_exception_logging.py", line 9, in <module>
    result = 10 / 0
             ~~~^~~
ZeroDivisionError: division by zero

"""
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
logging.warning("This is a warning")
logging.error("Something went wrong")

# output
# INFO:root:Program Started
# WARNING:root:This is a warning
# ERROR:root:Something went wrong

# 1.B. Improve code readability and help detect type-related mistakes.
# 2.B. The function is expected to return an integer.
# 3.B. list[int]
# 4.A. The value must always be a string.
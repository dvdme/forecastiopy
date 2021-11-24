# Logging Example
# Demonstrates a very basic logging setup and how to
# disable logging messages from the forecastiopy module

# See here for logging details https://docs.python.org/3/library/logging.html

import logging

from forecastiopy import ForecastIO

# Basic logger setup
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Basic logging example
log.debug("A debug message")
log.info("An info message")
log.warning("A warning")

# Will print an info message
log.info("ForecastIO default")
ForecastIO.ForecastIO("0" * 32)

# Disables the forecastiopy logger
logging.getLogger("forecastiopy").disabled = True

# Will no longer print a warning message
log.info("ForecastIO logger disabled")
ForecastIO.ForecastIO("0" * 32)

logging.info("Finished")

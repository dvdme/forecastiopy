# -*- coding: utf-8 -*-
import logging
"""
__init__.py file for forecastiopy module.
Defines the __all__ modules.
"""

__all__ = ['ForecastIO', 'FIOCurrently', 'FIOMinutely', \
           'FIOHourly', 'FIODaily', 'FIOFlags', 'FIOAlerts']

logging.getLogger(__name__).addHandler(logging.NullHandler())

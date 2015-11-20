# -*- coding: utf-8 -*-
"""
This module recieves an ForecastIO object and holds the currently weather
conditions. It has one class for this purpose.
"""
import types


class FIOCurrently(object):
    """
    This class recieves an ForecastIO object and holds the currently weather
    conditions.
    """

    currently = None

    def __init__(self, forecast_io):
        """
        Recieves an ForecastIO object and gets the currently weather conditions
        if they are available in the object.
        """
        if forecast_io.has_currently():
            self.currently = forecast_io.get_currently()
            for item in self.currently.keys():
                setattr(self, item, self.currently[item])
      
    def get(self):
        """
        Returns a dictionary with current weather conditions.
        Returns None is none are available.
        """
        return self.currently

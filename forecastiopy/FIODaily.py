# -*- coding: utf-8 -*-
"""
This module recieves an ForecastIO object and holds the daily weather
conditions. It has one class for this purpose.
"""

class FIODaily(object):
    """
    This class recieves an ForecastIO object and holds the daily weather
    conditions. It has one class for this purpose.
    """

    daily = None

    def __init__(self, forecast_io):
        """
        Recieves an ForecastIO object and gets the daily weather conditions
        if they are available in the object.
        """
        if forecast_io.has_daily():
            self.daily = forecast_io.get_daily()

    def get(self, day=None):
        """
        Returns a dictionary with daily weather conditions.
        Returns None is none are available.
        A day can be passed as an argument, is so function will call get_day()
        to return that day.
        Look on function get_day()
        """
        if day is None:
            return self.daily
        else:
            return self.get_day(day)

    def get_day(self, day):
        """
        Recieves a day as an argument and returns the prediction for that day if
        is available. If not, function will return None.
        """
        if day > self.days():
            return None
        else:
            return self.get()['data'][day-1]

    def days(self):
        """
        Returns how many days of prediction are available
        """
        return len(self.get()['data'])

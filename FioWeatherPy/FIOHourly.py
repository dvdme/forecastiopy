# -*- coding: utf-8 -*-


class FIOHourly(object):

    hourly = None

    def __init__(self, forecast_io):
        if forecast_io.has_hourly():
            self.hourly = forecast_io.get_hourly()

    def get(self, hour=None):
        if hour is None:
            return self.hourly
        else:
            return self.get_hour(hour)

    def get_hour(self, hour):
        if hour > self.hours():
            return 'no data'
        else:
            return self.get()['data'][hour]

    def hours(self):
        return len(self.get()['data'])

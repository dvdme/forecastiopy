# -*- coding: utf-8 -*-


class FIOFlags():

    flags = None

    def __init__(self, forecast_io):
        if forecast_io.has_flags():
            self.flags = forecast_io.get_flags()

    def get(self):
        return self.flags

    def available_flags(self):
        return self.get().keys()

    def units(self):
        if 'units' in self.flags:
            return self.flags['units']
        else:
            return 'no data'

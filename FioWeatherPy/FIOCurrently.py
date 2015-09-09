# -*- coding: utf-8 -*-


class FIOCurrently(object):

    currently = None

    def __init__(self, forecast_io):
        if forecast_io.has_currently():
            self.currently = forecast_io.get_currently()

    def get(self):
        return self.currently

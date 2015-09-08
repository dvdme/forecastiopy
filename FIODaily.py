class FIODaily():

    daily = None

    def __init__(self, forecast_io):
        if forecast_io.has_daily():
            self.daily = forecast_io.get_daily()

    def get(self, day=None):
		if day is None:
			return self.daily
		else:
			return self.get_day(day)



    def get_day(self, day):
        if day > self.days():
            return 'no data'
        else:
            return self.get()['data'][day]


    def days(self):
        return len(self.get()['data'])

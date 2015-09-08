class FIOMinutely():

    minutely = None

    def __init__(self, forecast_io):
        if forecast_io.has_minutely():
            self.minutely = forecast_io.get_minutely()

    def get(self, minute=None):
		if minute is None:
			return self.minutely
		else:
			return self.get_minute(minute)



    def get_minute(self, minute):
        if minute > self.minutes():
            return 'no data'
        else:
            return self.get()['data'][minute]


    def minutes(self):
        return len(self.get()['data'])

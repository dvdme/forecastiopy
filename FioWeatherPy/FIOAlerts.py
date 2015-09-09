# -*- coding: utf-8 -*-


class FIOAlerts(object):

    alerts = None

    def __init__(self, forecast_io):
        if forecast_io.has_alerts():
            self.alerts = forecast_io.get_alerts()

    def get(self, alert=None):
        if alert is None:
            return self.alerts
        else:
            return self.get_alerts(alert)

    def get_alert(self, alert):
        if alert > self.alerts_count():
            return 'no data'
        else:
            return self.get()[alert]

    def alerts_count(self):
        return len(self.get())

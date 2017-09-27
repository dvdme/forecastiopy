import os
import sys
import json
import unittest
from forecastiopy import *

class TestFIOCurrently(unittest.TestCase):

    def setUp(self):
        with open('tests/resources/dummy_apikey.txt') as f:
            apikey = f.read()
            self.fio = ForecastIO.ForecastIO(apikey)
        with open('tests/resources/response.json') as f:
            rsp = f.read()
            self.fio.get_forecast_fromstr(rsp)
            self.cur = FIOCurrently.FIOCurrently(self.fio)
            self.response = json.loads(rsp)
            self.response = self.response['currently']

    def test_has_currently(self):
        self.assertTrue(self.fio.has_currently())

    def test_get_time(self):
        self.assertEqual(self.cur.time, self.response['time'])

    def test_get_summary(self):
        self.assertEqual(self.cur.summary, self.response['summary'])

    def test_get_icon(self):
        self.assertEqual(self.cur.icon, self.response['icon'])

    def test_get_precipIntensity(self):
        self.assertEqual(self.cur.precipIntensity, self.response['precipIntensity'])

    def test_get_precipProbability(self):
        self.assertEqual(self.cur.precipProbability, self.response['precipProbability'])

    def test_get_temperature(self):
        self.assertEqual(self.cur.temperature, self.response['temperature'])

    def test_get_apparentTemperature(self):
        self.assertEqual(self.cur.apparentTemperature, self.response['apparentTemperature'])

if __name__ == '__main__':
    # append module root directory to sys.path
    sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
    unittest.main()
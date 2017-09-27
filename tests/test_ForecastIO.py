import os
import sys
import json
import unittest
from forecastiopy import *

class TestForecastIO(unittest.TestCase):

    def setUp(self):
        with open('tests/resources/dummy_apikey.txt') as f:
            apikey = f.read()
            self.fio = ForecastIO.ForecastIO(apikey)
        with open('tests/resources/response.json') as f:
            rsp = f.read()
            self.fio.get_forecast_fromstr(rsp)
            self.response = json.loads(rsp)


    def test_get_url(self):
        with open('tests/resources/dummy_apikey.txt') as f:
            apikey = f.read()
            fio = ForecastIO.ForecastIO(apikey)
            with self.assertRaises(TypeError):
                fio.get_url()

    def test_invalid_apikey(self):
        with self.assertRaises(ValueError):
            self.fio = ForecastIO.ForecastIO('123')

    def test_get_latitude(self):
        self.assertEqual(self.fio.latitude, self.response['latitude'])

    def test_get_longitude(self):
        self.assertEqual(self.fio.longitude, self.response['longitude'])

    def test_get_timezone(self):
        self.assertEqual(self.fio.timezone, self.response['timezone'])

    def test_get_offset(self):
        self.assertEqual(self.fio.offset, self.response['offset'])


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
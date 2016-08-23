import unittest
import sys
sys.path.insert(0, '../forecastiopy')

import ForecastIO

class ForecastIOTest(unittest.TestCase):

    def setUp(self):
        self.fio = ForecastIO.ForecastIO('0' * 32)
        with open('lisbon_forecast.json') as f:
            json = f.read()
            self.fio.get_forecast_from_string(json)

    def test_latitude(self):
        self.assertEqual(self.fio.latitude, 38.7252993)

    def test_longitude(self):
        self.assertEqual(self.fio.longitude, -9.1500364)

    def test_timezone(self):
        self.assertEqual(self.fio.timezone, 'Europe/Lisbon')

    def test_offset(self):
        self.assertEqual(self.fio.offset, 1)

    def test_has_currently(self):
        self.assertEqual(self.fio.has_currently(), True)

    def test_currently(self):
        self.assertIsNotNone(self.fio.currently)


if __name__ == '__main__':
    unittest.main()

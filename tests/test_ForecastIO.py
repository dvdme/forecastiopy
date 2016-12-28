import env
import unittest
from forecastiopy import *

class TestForecastIO(unittest.TestCase):

    def test_get_url(self):
        with open('tests/resources/dummy_apikey.txt') as f:
            apikey = f.read()
            fio = ForecastIO.ForecastIO(apikey)
            with self.assertRaises(TypeError):
                fio.get_url()

    def test_invalid_apikey(self):
        with self.assertRaises(ValueError):
            fio = ForecastIO.ForecastIO('123')

if __name__ == '__main__':
    unittest.main()
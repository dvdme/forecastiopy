import env
import unittest
from forecastiopy import *

class TestForecastIO(unittest.TestCase):

    def test_get_url(self):
        with open('tests/resources/apikey.txt') as f:
            apikey = f.read()
            fio = ForecastIO.ForecastIO(apikey)
            self.assertRaises(TypeError, lambda: fio.get_url(), msg='Did not raised ValueError on invalid lat and/or lon')

if __name__ == '__main__':
    unittest.main()
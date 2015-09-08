# -*- coding: utf-8 -*-

import sys
import json
import requests

class ForecastIO():


    ForecastIOURL = 'https://api.forecast.io/forecast/'
    ForecastIOApiKey = '';
    units_url = ''
    time_url = ''
    exclude_url = ''
    lang_url = ''
    extend = ''

    Cache_Control = ''
    Expires = ''
    X_Forecast_API_Calls = ''
    X_Response_Time = ''

    raw_response = ''


    UNITS_US = 'us'
    UNITS_SI = 'si'
    UNITS_CA = 'ca'
    UNITS_UK = 'uk'
    UNITS_AUTO = 'auto'

    LANG_BOSNIAN = 'bs'
    LANG_GERMAN = 'de'
    LANG_ENGLISH = 'en'
    LANG_SPANISH = 'es'
    LANG_FRENCH = 'fr'
    LANG_ITALIAN = 'it'
    LANG_DUTCH = 'nl'
    LANG_POLISH = 'pl'
    LANG_PORTUGUESE = 'pt'
    LANG_TETUM = 'tet'
    LANG_PIG_LATIN = 'x-pig-latin'
    LANG_RUSSIAN = 'ru'


 #   forecast = ''

 #   currently = ''
    minutely = ''
    hourly = ''
    daily = ''
    flags = ''
    alerts = ''

    def __init__(self, api_key):
        if api_key.__len__() == 32:
            self.ForecastIOApiKey = api_key
            self.extend = False
            self.units_url = self.UNITS_AUTO
            self.lang_url = self.LANG_ENGLISH
        else:
            print 'The API Key doesn\'t seam to be valid.'

    def get_forecast(self, latitude, longitude):
        reply = self.http_get( self.url_builder(latitude, longitude) )
        self.forecast = json.loads(reply)
        if 'currently' in self.forecast:
            self.currently = self.forecast['currently']
        if 'minutely' in self.forecast:
            self.minutely = self.forecast['minutely']
        if 'hourly' in self.forecast:
            self.hourly = self.forecast['hourly']
        if 'daily' in self.forecast:
            self.daily = self.forecast['daily']
        #return json.dumps(self.daily, sort_keys=True, indent=4, separators=(',', ': ')) #Test Output

    def url_builder(self, latitude, longitude):
        try:
            float(latitude)
            float(longitude)
        except ValueError:
            raise ValueError('Latitude and Longitude must be a (float) number')
        url = self.ForecastIOURL + self.ForecastIOApiKey+"/"
        url += str(latitude).strip() + ',' + str(longitude).strip()
        if self.time_url and not self.time_url.isspace():
            url += ',' + self.time_url.strip()
        url += '?units=' + self.units_url.strip()
        url += '&lang=' + self.lang_url.strip()
        if self.exclude_url and not self.exclude_url.isspace():
            url += '&exclude=' + self.exclude_url.strip()
        if self.extend is True:
            url += 'extend=hourly'
        return url

    def http_get(self, request_url):
        try:
            headers = {'Accept-Encoding' : 'gzip, deflate'}
            response = requests.get(request_url, headers=headers)
        except requests.exceptions.Timeout:
            print 'Error: Timeout'
        except requests.exceptions.TooManyRedirects:
            print 'Error: TooManyRedirects'
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)

        try:
            self.Cache_Control = response.headers['Cache-Control']
            self.Expires = response.headers['Expires']
            self.X_Forecast_API_Calls = response.headers['X-Forecast-API-Calls']
            self._Response_Time = response.headers['X-Response-Time']
        except Exception as e:
            print 'Warning: Could not get headers. %s' % e

        if response.status_code is not 200:
            raise requests.exceptions.HTTPError('Bad response')
            sys.exit(1)

        self.raw_response = response.content
        return response.content

    def has_currently(self):
        return 'currently' in self.forecast

    def get_currently(self):
        return self.currently

    def has_daily(self):
        return 'daily' in self.forecast

    def get_daily(self):
        return self.daily

    def has_hourly(self):
        return 'hourly' in self.forecast

    def get_hourly(self):
        return self.hourly

    def has_minutely(self):
        return 'minutely' in self.forecast

    def get_minutely(self):
        return self.minutely

if __name__ == '__main__':
    fio = ForecastIO('a66c3d9fd49043109081f945a9d4abba')
    fio.get_forecast(37.8267,-122.423)
    print json.dumps(fio.currently, sort_keys=True, indent=4, separators=(',', ': ')) #Test Output
    print fio.has_currently()

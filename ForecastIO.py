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

    
    forecast = ''

    currently = ''
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
    
    
    
    def url_builder(self, latitude, longitude):
        try:
            float(latitude)
            float(longitude)
        except ValueError:
            raise ValueError('Latitude and Longitude must be a number')
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
            self.Cache_Control = response.headers['Cache_Control']
            self.Expires = response.headers['Expires']
            self.X_Forecast_API_Calls = response.headers['X_Forecast_API_Calls']
            self._Response_Time = response.headers['X_Response_Time']
        except Exception as e:
            print 'Warning: Could not get headers. %s' % e
            
        if response.status_code is not 200:
            raise requests.exceptions.HTTPError('Bad response')
            sys.exit(1)
        
        self.raw_response = response.content
        return response.content



if __name__ == '__main__':
    fio = ForecastIO('12345678901234567890123456789012')
    print fio.url_builder('124',124.98)
    print fio.http_get('http://www.google.com')
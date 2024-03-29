# Last update

[The ForecastIO / DarkSky API is no longer available.](https://darksky.net/dev)

This repository has not been updated for a long time but since it is from the times I was starting my career and more people used this, it will reamin archived here.


| Branch        | Travis CI     |
| ------------- |:-------------:|
| master        |[![Build Status](https://travis-ci.org/dvdme/forecastiopy.svg?branch=master)](https://travis-ci.org/github/dvdme/forecastiopy)|
| dev           |[![Build Status](https://travis-ci.org/dvdme/forecastiopy.svg?branch=dev)](https://travis-ci.org/github/dvdme/forecastiopy)|

ForcastIO Python
===================
A Python wrapper for the [darksky.net](https://darksky.net) API (previously forecast.io).
This started as port of my other wrapper [ForecastIO-Lib-Java](https://github.com/dvdme/forecastio-lib-java)
but as the languages are so different, this one took its own way. 
Anyway it is largely inspired by my previous Java wrapper.
The API is fully implemented except for something I missed.
Further development and improvements will continue.

Tested with the following Python version:
- 2.7
- 3.5
- 3.6
- 3.7-dev

#### What's new with 0.3

* Logging support.


#### What's new with 0.21

* Changed api url from old api.forecast.io to the new api.darksky.net

* Some docstrings typos fixed

#### What's new with 0.2

* Indexes of auto created properties now start in 0, 0 being the current day [Issue #s](https://github.com/dvdme/forecastiopy/issues/2)

* If the API key is invalid, an ValueError is raised [Issue #3](https://github.com/dvdme/forecastiopy/issues/3)

* Better Python 3 support

* Other improvements

#### Quick Start:
Install the package:
```
pip install forecastiopy
```

Get the coordinates of your location, let's say Lisbon:
```python
>>> Lisbon = [38.7252993, -9.1500364]
```

Get the current temperature and precipitation probability:
```python
>>> from forecastiopy import *
>>> fio = ForecastIO.ForecastIO(YOUR_APY_KEY, latitude=Lisbon[0], longitude=Lisbon[1])
>>> current = FIOCurrently.FIOCurrently(fio)
>>> print 'Temperature:', current.temperature
Temperature: 11.07
>>> print 'Precipitation Probability:', current.precipProbability
Precipitation Probability: 0.29
```

#### What is does:

* It can read Data Points and Data blocks from the [darksky.net](https://darksky.net) API.
  * This means it can read Currently, Minutely, Hourly, Daily, Flags and Alerts data.
* It reads all available fields.
* It reads all the available flags.
* It reads all the available alerts. 
* It reads all the available errors. 

#### What it does not:

* It does not implements the `callback` request option.

#### To Do:

* I'm not sure at this point in time but I'm sure something will appear.
* I need to improve the docstrings

#### How it works:

The `forecastiopy` package has 9 classes.
The main class is `ForecastIO`: It handles the connection, build the url and the gets the initial data from the API.
The classes `FIOCurrently`, `FIOMinutely`, `FIOHourly`, `FIODaily`, `FIOFlags` and `FIOAlerts` 
contain the currently, minutely, hourly, daily, flags and alerts reports.
Data can be accessed by the returned dictionary or directly by attributes made with reflection magic.
See "Usage Examples" below.

Please refer to the API docs [https://darksky.net/dev/](https://darksky.net/dev/) 
for better understanding of the data and for the API key. - You'll need a key to get it to work.

#### Dependencies: 

* [requests](https://pypi.python.org/pypi/requests/)


Usage Examples
--------------

**This instantiates the ForecastIO class**
```python
from forecastiopy import *

apikey = YOUR_APY_KEY

Lisbon = [38.7252993, -9.1500364]

fio = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=Lisbon[0], longitude=Lisbon[1])
                            
print 'Latitude', fio.latitude, 'Longitude', fio.longitude
print 'Timezone', fio.timezone, 'Offset', fio.offset
print fio.get_url() # You might want to see the request url
print
```

**Get Currently weather data for the requested location**
```python
if fio.has_currently() is True:
	currently = FIOCurrently.FIOCurrently(fio)
	print 'Currently'
	for item in currently.get().keys():
		print item + ' : ' + unicode(currently.get()[item])
	print
	# Or access attributes directly
	print currently.temperature
	print currently.humidity
	print
else:
	print 'No Currently data'
```

**Get Minutely weather data for the requested location**
```python
if fio.has_minutely() is True:
	minutely = FIOMinutely.FIOMinutely(fio)
	print 'Minutely'
	print 'Summary:', minutely.summary
	print 'Icon:', minutely.icon
	print
	for minute in range(0, minutely.minutes()):
		print 'Minute', minute+1
		for item in minutely.get_minute(minute).keys():
			print item + ' : ' + unicode(minutely.get_minute(minute)[item])
		print
		# Or access attributes directly for a given minute. 
		# minutely.minute_3_time would also work
		print minutely.minute_1_time
		print
	print
else:
	print 'No Minutely data'
```

**Get Hourly weather data for the requested location**
```python
if fio.has_hourly() is True:
	hourly = FIOHourly.FIOHourly(fio)
	print 'Hourly'
	print 'Summary:', hourly.summary
	print 'Icon:', hourly.icon
	print
	for hour in range(0, hourly.hours()):
		print 'Hour', hour+1
		for item in hourly.get_hour(hour).keys():
			print item + ' : ' + unicode(hourly.get_hour(hour)[item])
		print
		# Or access attributes directly for a given minute. 
		# hourly.hour_5_time would also work
		print hourly.hour_3_time
		print
	print
else:
	print 'No Hourly data'
```

**Get Daily weather data for the requested location**
```python
if fio.has_daily() is True:
	daily = FIODaily.FIODaily(fio)
	print 'Daily'
	print 'Summary:', daily.summary
	print 'Icon:', daily.icon
	print
	for day in range(0, daily.days()):
		print 'Day', day+1
		for item in daily.get_day(day).keys():
			print item + ' : ' + unicode(daily.get_day(day)[item])
		print
		# Or access attributes directly for a given minute. 
		# daily.day_7_time would also work
		print daily.day_5_time
		print
	print
else:
	print 'No Daily data'
```

**Get Flags weather data for the requested location**
```python
if fio.has_flags() is True:
	from pprint import pprint
	flags = FIOFlags.FIOFlags(fio)
	pprint(vars(flags))
	# Get units directly
	print flags.units
else:
	print 'No Flags data'
```

**Get Alerts weather data for the requested location**
It should work just like Flags and the other ones, but at the time I am writting this I could not find a location with alerts to test on.

**A note on time**
The API returns time in unix time. Although this is a good computer format,
it is not particulary _human-readable_
So, to get a more _human-sane_ format, you can do soething like this:
```python
import datetime

time = datetime.datetime.fromtimestamp(int(currently.time).strftime('%Y-%m-%d %H:%M:%S')
print 'unix time:', currently.time
print 'time:', time

```

Output should be like:
```
unix time: 1448234556
time: 2015-11-22 23:22:36
```

Issues
------
To report issues please do it in [Github](https://github.com/dvdme/forecastiopy) or
send me an <a href="mailto:david.dme@gmail.com">email</a>.<br>

Documentation
-------------
Thanks to pylint complaning, I did wrote docstring for everything!

Why I did this?
-------
For fun.
I like weather and weather data. 
And I like Python.

License
-------
The code is available under the terms of the [Eclipse Public License](http://www.eclipse.org/legal/epl-v10.html).

Contributors
------------
* Thanks to everyone that [contribuited](https://github.com/dvdme/forecastiopy/graphs/contributors) to make this software better.

Acknowledgements
---------------


[![Python Powered](https://www.python.org/static/community_logos/python-powered-w-200x80.png)](https://www.python.org/)

[![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby.png)](https://darksky.net/poweredby/)

[![Jet Brains IntelliJ IDEA](/art/jetbrains-variant-3.png)](http://www.jetbrains.com/idea/)

Thanks to [JetBrains](https://www.jetbrains.com/) for providing an open source license for.

from setuptools import setup



setup(name='forecastiopy',
      version='0.3',
      description='A wrapper to access weather data provided by darksky.net',
      url='http://github.com/dvdme/forecastiopy',
      download_url='http://github.com/dvdme/forecastiopy/archive/0.3.tar.gz',
      author='David Ervideira',
      author_email='david.dme@gmail.com',
      license='Eclipse Public License',
      packages=['forecastiopy'],
      keywords=['weather','forecastio', 'forecast.io','rest', 'darksky','darksky.net'],
      install_requires=[
          'requests',
      ],
      zip_safe=True,
      test_suite="tests")
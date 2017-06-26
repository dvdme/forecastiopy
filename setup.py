from setuptools import setup



setup(name='forecastiopy',
      version='0.22',
      description='A wrapper to access weather data provided by darksky.net',
      url='http://github.com/dvdme/forecastiopy',
      download_url='http://github.com/dvdme/forecastiopy/tarball/0.2',
      author='David Ervideira',
      author_email='david.dme@gmail.com',
      license='Eclipse Public License',
      packages=['forecastiopy'],
      keywords=['weather','forecastio', 'forecast.io','rest', 'darksky','darksky.net'],
      install_requires=[
          'requests',
      ],
      zip_safe=True)
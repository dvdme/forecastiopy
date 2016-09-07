from setuptools import setup



setup(name='forecastiopy',
      version='0.2',
      description='A wrapper to access weather data provided by forecast.io',
      url='http://github.com/dvdme/forecastiopy',
      download_url='http://github.com/dvdme/forecastiopy/tarball/0.2',
      author='David Ervideira',
      author_email='david.dme@gmail.com',
      license='Eclipse Public License',
      packages=['forecastiopy'],
      keywords=['weather','forecastio','rest'],
      install_requires=[
          'requests',
      ],
      zip_safe=True)
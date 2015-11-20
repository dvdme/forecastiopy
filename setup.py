from setuptools import setup



setup(name='forecastiopy',
      version='0.1',
      description='A wrapper to access weather data provided by forecast.io',
      url='http://github.com/dvdme/forecastiopy',
      author='David Ervideira',
      author_email='david.dme@gmail.com',
      license='Eclipse Public License',
      packages=['forecastiopy'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
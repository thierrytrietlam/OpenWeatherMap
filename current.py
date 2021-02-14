# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 13:52:19 2020

@author: lammi

Before run, you need to install this library:
$ pip install pyowm
"""

import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_id(3026391)
weather = obs.weather

# Status of current weather
weather = obs.weather
print("Status of current weather: ",weather.detailed_status)

# Current temperature
temperature = weather.temperature(unit='celsius')['temp_min']
temperature1 = weather.temperature(unit='celsius')['temp']
temperature2 = weather.temperature(unit='celsius')['temp_max']
print("min",temperature,"normal",temperature1,"max",temperature2)

## Weather Info
# Humidity
humidity = weather.humidity
print(f'The current humidity is {humidity}%')
# wind - direction (degrees), and speed  (meters/second)
wind = weather.wind()
print(f'The current wind is {wind}')
# Cloud
clouds = weather.clouds
print(f'The current cloud is {clouds}%')

# Sunrise and Sunset times
print("Sunrise: ",weather.sunrise_time(timeformat='iso'))
print(weather.sunrise_time())
# Get the sunset time in the GMT timezone in the unix time format
sunset_unix = weather.sunset_time()
print("Sunset: ", weather.sunset_time(timeformat='iso'))
print(sunset_unix)
 
# # Create `pytz` timezone objects
# eastern = pytz.timezone('US/Eastern')
# gmt = pytz.timezone('GMT') 
 
# # Create a UTC `datetime` object from the unix timestamp
# sunset = datetime.utcfromtimestamp(sunset_unix)
 
# # Make the `datetime` object timezone aware so Python will
# # know how to convert it to a different timezone
# sunset = gmt.localize(sunset) 
 
# # Convert time to Eastern time and print it
# sunset_eastern = sunset.astimezone(eastern)
# print(sunset_eastern)

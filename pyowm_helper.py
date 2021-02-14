# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 07:49:23 2020

@author: lammi

# Before run, you need to install 2 libraries
# $ pip install openweather
# $ pip install pyowm
"""

import os
import pyowm
# Use this library if you need to change timezone
from timezone_conversion import gmt_to_eastern 


API_KEY = os.environ['API_KEY']

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()

def get_temperature():
    # Create empty arrays
    days = []
    dates = []
    temp_min = []
    temp_max = []
    
    # Get the time of the weather forecast and convertingto a Datetime object
    forecaster = mgr.forecast_at_place('Chasseneuil-du-Poitou, FR', '3h')
    # forecast_at_place() returns a Forecaster object
    forecast = forecaster.forecast
    
    for weather in forecast:
        # Get time of the weather forecast, convert to a Datetime object.
        # day = datetime.utcfromtimestamp(weather.reference_time())
        
        # Only use if you need to change time zone from GMT to Eastern
        day = gmt_to_eastern(weather.reference_time())
        # store just the date in the date object, remove hour, minute... 
        date = day.date()
        
        if date not in dates:
            dates.append(date)
            # Start reading temperature for a new day
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature('kelvin')['temp']
        
        # If it is the first data or temperature is less than it:
        if not temp_min[-1] or temperature < temp_min[-1]:
            temp_min[-1] = temperature
        # If it is the first data or temperature is more than it: 
        if not temp_max[-1] or temperature > temp_max[-1]:
            temp_max[-1] = temperature
    # 'days' hold 'Datetime' object
    print(days, temp_min, temp_max)
    return(days, temp_min, temp_max)

# def get_humidity():
#     # Create empty arrays
#     days = []
#     dates = []
#     hum = []
    
#     # Get the time of the weather forecast and convertingto a Datetime object
#     forecaster = mgr.forecast_at_place('Chasseneuil-du-Poitou, FR', '3h')
#     # forecast_at_place() returns a Forecaster object
#     forecast = forecaster.forecast
    
#     for weather in forecast:
#         day = gmt_to_eastern(weather.reference_time())
#         date = day.date()
#         if date not in dates:
#             if len(days) >= 5:
#                 return(days, hum)
#             dates.append(date)
#             hum.append(weather.humidity)
#             days.append(date)
 
#         if day.hour in [11, 12, 13, 14, 15]:
#             hum[-1] = weather.humidity
#     # 'days' hold 'Datetime' object
#     print(days, hum)
#     return(days, hum)

def get_humidity():
    # Create empty arrays
    days = []
    dates = []
    hum_min = []
    hum_max = []
    
    # Get the time of the weather forecast and convertingto a Datetime object
    forecaster = mgr.forecast_at_place('Chasseneuil-du-Poitou, FR', '3h')
    # forecast_at_place() returns a Forecaster object
    forecast = forecaster.forecast
    
    for weather in forecast:
        # Get time of the weather forecast, convert to a Datetime object.
        # day = datetime.utcfromtimestamp(weather.reference_time())
        
        # Only use if you need to change time zone from GMT to Eastern
        day = gmt_to_eastern(weather.reference_time())
        # store just the date in the date object, remove hour, minute... 
        date = day.date()
        
        if date not in dates:
            dates.append(date)
            # Start reading humidity for a new day
            hum_min.append(None)
            hum_max.append(None)
            days.append(date)
        humidity = weather.humidity
        
        # If it is the first data or humidity is less than it:
        if not hum_min[-1] or humidity < hum_min[-1]:
            hum_min[-1] = humidity
        # If it is the first data or humidity is more than it: 
        if not hum_max[-1] or humidity > hum_max[-1]:
            hum_max[-1] = humidity
    # 'days' hold 'Datetime' object
    print(days, hum_min, hum_max)
    return(days, hum_min, hum_max)

def get_pressure():
    # Create empty arrays
    days = []
    dates = []
    pre_min = []
    pre_max = []
    
    # Get the time of the weather forecast and convertingto a Datetime object
    forecaster = mgr.forecast_at_place('Chasseneuil-du-Poitou, FR', '3h')
    # forecast_at_place() returns a Forecaster object
    forecast = forecaster.forecast
    
    for weather in forecast:
        # Get time of the weather forecast, convert to a Datetime object.
        # day = datetime.utcfromtimestamp(weather.reference_time())
        
        # Only use if you need to change time zone from GMT to Eastern
        day = gmt_to_eastern(weather.reference_time())
        # store just the date in the date object, remove hour, minute... 
        date = day.date()
        
        if date not in dates:
            dates.append(date)
            # Start reading pressure for a new day
            pre_min.append(None)
            pre_max.append(None)
            days.append(date)
        pressure = weather.pressure['press']

        # If it is the first data or pressure is less than it:
        if not pre_min[-1] or pressure < pre_min[-1]:
            pre_min[-1] = pressure
        # If it is the first data or pressure is more than it: 
        if not pre_max[-1] or pressure > pre_max[-1]:
            pre_max[-1] = pressure
    # 'days' hold 'Datetime' object
    print(days, pre_min, pre_max)
    return(days, pre_min, pre_max)

if __name__ == '__main__':
    get_temperature()
    get_humidity()
    get_pressure()

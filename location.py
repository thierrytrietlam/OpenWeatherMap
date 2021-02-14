"""
Created on Wed Dec 02 13:01:24 2020

@author: lammi
"""

import pyowm
from api_key import API_KEY

'''
Firstly, there are 4 ways to identify a location which are in 
city_name, city_id, zip_code, and lat_lon. 
They are edited to relocate to Chasseneuil-du-Poitou, France.
'''

# =============================================================================
# 1. By the id
# =============================================================================
owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_id(3026391) #3026391 is code of Chasseneuil-du-poitou
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']

print(f'The temperature is {temperature} degrees Celsius.')

# =============================================================================
# 2. By the name of city
# =============================================================================

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Chasseneuil-du-Poitou, FR')
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']

print(f'The temperature is {temperature} degrees Celsius.')

# =============================================================================
# 3. By the longitude and latitude
# =============================================================================
owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_coords(lat=46.650703, lon=0.374772)
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']

print(f'The temperature is {temperature} degrees Celsius.')

# =============================================================================
# 4. By the zip code
# =============================================================================

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_zip_code('86360', 'FR')
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']

print(f'The temperature is {temperature} degrees Celsius.')
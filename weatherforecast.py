# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 19:11:57 2020

@author: lammi

Before run, you need to install:
$ pip install pyowm
"""

import pyowm
import json
import requests
from pprint import pprint
from pyowm.utils import timestamps
from datetime import datetime, timedelta
from api_key import API_KEY
import os

#Define Current Path & Items in Current Working Directory
current_path = os.getcwd()
current_directory = os.listdir()

#Loop Through Items in Current Working Directory
for item in current_directory:
    
    #Find Folder for Global Weather Data
        
    #Find Folder for Output Plots
    if item.lower().find('every hour forecast data') >= 0:
        
        #Define File Path for Output Plots
        output_file = current_path + '/' + item + '/'
        output_file_exact = current_path + '/' + item + '/exact' + '/'
        
    elif item.lower().find('three-hour forecast data') >= 0:
        
        #Define File Path for Output Plots
        output_file_3 = current_path + '/' + item + '/'

#Define Range of Latitudes & Longitudes

print(output_file)
print(output_file_exact)

degree_sign= u'\N{DEGREE SIGN}'
owm = pyowm.OWM(API_KEY)
lat_data = str(46.650703);
lon_data = str(0.374772);
# Three Hours Forecast
api_key = API_KEY
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Chasseneuil-du-Poitou, FR', '3h')
forecast = forecaster.forecast
weather_list = forecast.weathers
a = datetime.now().strftime("%Y-%m-%d-%H")
# time.strftime("%Y-%m-%d-%H-%M-%S")
print(a)
# print(type(a))

def threehoursforecast(weather_list):
# Three Hours Forecast for 5 days
    list_dt_day = [] 
    print('Three hours forecast (Times are in GMT)')
    for weather in weather_list:
        dict_={}
        temp = weather.temperature(unit='celsius')['temp']
        humidity = weather.humidity
        # dict_['Time']=weather.reference_time('iso')
        dict_['dt']=weather.reference_time('unix')
        dict_['temp']=temp
        dict_['humidity']=humidity
        list_dt_day.append(dict_)
        # print with iso time and unix time
        # print(weather.reference_time('unix'),weather.reference_time('iso'), f'Temperature: {temp}{degree_sign}C')
    pprint(list_dt_day, indent = 4)
    return list_dt_day

def write_data_json(list_dt_day):
    # Save in Json file
    with open(output_file_3+"threehoursforecast" + a+".json", 'w') as outfile:
        json.dump(list_dt_day, outfile)   

def everyhourhorecast():
# Every Hour Forecast for 48 hours
    Final_url = base_url + "lat=" + lat_data + "&lon=" + lon_data + "&exclude=current,minutely,daily,alerts" + "&appid=" + api_key
    weather_data = requests.get(Final_url).json() # Type Dict
    # pprint (weather_data['hourly'], indent = 4)
    # Check keys in weather_data dictionary 
    # print ("The dictionary contains the following keys: ", weather_data.keys())
    # Check keys in keys
    # print('Check', weather_data['hourly'].keys())
    return weather_data

def write_data_everyhour_json(weather_data):
    # Save in Json file
    with open(output_file+"everyhourforecast" + a+".json", 'w') as outfile:
        json.dump(weather_data, outfile) 
        
def select_data_json(weather_data):
    # Extract Json data includes dt, temperature and humidity
    # Exclude the other keys
    list_hour = [] 
    for a in weather_data['hourly']:
        # print ('Get value', dt['dt']) 
        dict_={}
        dict_['dt'] = a['dt']
        dict_['temp'] = a['temp']
        dict_['humidity'] = a['humidity']
        list_hour.append(dict_)
    # pprint(list_hour) # Type list
    print(list_hour)
    return list_hour

def write_data_everyhour_exact_json(list_hour):
    # Save in Json file
    with open(output_file_exact+"exact_everyhourforecast" + a+".json", 'w') as outfile:
        json.dump(list_hour, outfile) 


def weather_at_time():
# Get Weather At a Specific Time
    da = int(input('Enter the future day:'))
    ho = int(input('Enter the future hour:'))
    if da >= 1 or ho >= 3 and da <5:
        # Input only allows to get data at least 3 hours to 5 days.
        time = datetime.now() + timedelta(days= da , hours= ho)
        weather = forecaster.get_weather_at(time)
        temperature = weather.temperature(unit='celsius')['temp']
        print(f'The temperature at {time.strftime("%Y-%m-%d %H:%M:%S")} is {temperature}{degree_sign}C')
        
def weather_tomorrow():
    # Get Weather at a Specific Time of tomorrow
    tmr = int(input('Enter the desired hour tomorrow:'))
    time = timestamps.tomorrow(tmr,0)
    weather = forecaster.get_weather_at(time)
    temperature = weather.temperature(unit='celsius')['temp']
    print(f'The temperature at {time} is {temperature}{degree_sign}C')

def will_have():
# Check for certain weather conditions in a forecast
    print("Rain: ", forecaster.will_have_rain())
    print("Clear: ", forecaster.will_have_clear())
    print("Fog: ", forecaster.will_have_fog())
    print("Cloud: ",forecaster.will_have_clouds())
    print("Snow: ", forecaster.will_have_snow())
    print("Storm: ", forecaster.will_have_storm())
    print("Tornado: ", forecaster.will_have_tornado())
    print("Hurricane: ", forecaster.will_have_hurricane())

def will_be():
# Check if a particular weather condition exists at a specified time for 5 days
    yyyy = int(input('Enter the year:'))
    mm = int(input('Enter the month:'))
    dd = int(input('Enter the day:'))
    hh = int(input('Enter the hour:'))
    print("Rainy: ", forecaster.will_be_rainy_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Clear: ", forecaster.will_be_clear_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Foggy: ", forecaster.will_be_foggy_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Cloudy: ", forecaster.will_be_cloudy_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Snowy: ", forecaster.will_be_snowy_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Stormy: ", forecaster.will_be_stormy_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Tornado: ", forecaster.will_be_tornado_at(datetime(yyyy, mm, dd, hh, 0)))
    print("Hurricane: ", forecaster.will_be_hurricane_at(datetime(yyyy, mm, dd, hh, 0)))

def main():
    # # weather_at_time()
    # # weather_tomorrow()
    # # will_have()
    # # will_be()     
    # list_dt_day = threehoursforecast(weather_list)
    # write_data_json(list_dt_day)
    # weather_data = everyhourhorecast()
    # write_data_everyhour_json(weather_data)
    # list_hour = select_data_json(weather_data)
    # write_data_everyhour_exact_json(list_hour)
    
if __name__ == "__main__":
    main()



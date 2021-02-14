# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:13:58 2021
 
@author: lammi
"""
# WeatherPy
 
#Import Modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from citipy import citipy # pip install citipy
import os
import json
from pprint import pprint 
 
'Import API Key'
from api_key import API_KEY
 
#Define Current Path & Items in Current Working Directory
current_path = os.getcwd()
current_directory = os.listdir()

#Loop Through Items in Current Working Directory
for item in current_directory:
    
    #Find Folder for Global Weather Data
    if item.lower().find('global weather data') >= 0:
        
        #Define Output File Name & Path
        output_file = current_path + '/' + item + '/Global_Weather_Data.csv'
        
    #Find Folder for Output Plots
    elif item.lower().find('images') >= 0:
        
        #Define File Path for Output Plots
        output_plot = current_path + '/' + item + '/'

#Define Range of Latitudes & Longitudes
lat_range = (60, 61)
long_range = (-161, -160)
# print(output_file)
 
'List for holding lat_lngs and cities'
lat_lngs = []
cities = []
 
#Create Set of Random Latitude & Longitude Combinations
lats = np.random.uniform(low = lat_range[0], high = lat_range[1], size = 2000)
lngs = np.random.uniform(low = long_range[0], high = long_range[1], size = 2000)
lat_lngs = zip(lats, lngs)
 
#Loop Through Latitude & Longitude Combinations
for lat_lng in lat_lngs:
    
    #Collect Name of Nearest City for Each Latitude & Longitude Combination
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    #Check if City Name Has Already Been Found
    if city not in cities:
        
        #Append New City Names to Final List of Cities
        cities.append(city)
 
#Print Length of City Name List
len(cities)
 
'Set Open Weather Map API Base URL'
base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
 
#Define Python Lists for Individual Weather Parameters
city = []
cloud = []
country = []
date = []
humidity = []
latitude = []
longitude = []
temp = []
wind = []
 
#Set Counter Variable for API Status Messages
count_1 = 1
 
#Print API Start Status Message
print('Starting Weather Data Collection from API.')
print('----------------------------------')
 
#Loop Through List of City Names
for name in cities:
    
    #Set Full API URL for Individual City
    full_url = base_url + name + '&APPID=' + API_KEY + '&units=imperial'
    
    #Collect Individual City Data from API
    raw_data = requests.get(full_url).json()
    print("Check", type(raw_data))
    
    #Print API Status Message for Individual City
    print('Processing City ' + str(count_1) + ': ' + name.title())
    
    #Set Condition for City Found In API Database
    if raw_data['cod'] == 200:
        
        #Write Individual City Data to Individual Weather Parameter Lists
        city.append(raw_data.get('name'))
        cloud.append(raw_data['clouds']['all'])
        country.append(raw_data['sys']['country'])
        date.append(raw_data['dt'])
        humidity.append(raw_data['main']['humidity'])
        latitude.append(raw_data['coord']['lat'])
        longitude.append(raw_data['coord']['lon'])
        temp.append(raw_data['main']['temp_max'])
        wind.append(raw_data['wind']['speed'])
    else:
        
        #Print API Status Message For Individual City No Found in API Databse
        print(name.title() + ' Not Found! Skipping!')
    
    #Pause Code to Prevent Exceeding API Call Limit
    time.sleep(1.5)
    
    #Increment Counter Variable for API Status Messages
    count_1 = count_1 + 1
 
#Print API End Status Message
print('----------------------------------')
print('Weather Data Collection Completed')
 
#Create Data Frame of Combined City Weather
city_data = pd.DataFrame({'City': city, 'Cloudiness (%)': cloud, 'Country': country, 'Date': date, 'Humidity (%)': humidity,
                          'Latitude': latitude, 'Longitude': longitude, 'Max Temp (F)': temp, 'Wind Speed (mph)': wind})
print(type(city_data)) 
#Display Combined City Weather Data Frame
city_data
print(city_data)
 
#Export Combined City Weather Data Frame to CSV File
city_data.to_csv(output_file, index = False)
     
 

#Plot Latitude Data Versus Maximum Temperature Data
F1, AX1 = plt.subplots()
AX1.scatter(city_data['Latitude'], city_data['Max Temp (F)'], facecolor = 'blue', edgecolor = 'black')
AX1.grid()
AX1.set_title('Maximum Temperature vs City Latitude')
AX1.set_xlabel('City Latitude')
AX1.set_ylabel('Max Temp (F)')
plt.savefig(output_plot + 'Maximum_Temperature_vs_City_Latitude.png')
plt.show()


def open_json():
    # Open a JSON file
    with open('ChasseneuilWeather_Final.json') as json_file:
        data = json.load(json_file)
    pprint(data[0]['dt']) # Type list
    
    
    return data   

    
def main():   
    data = open_json()   
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:47:23 2021

@author: lammi
"""


import requests
import datetime
import time
from pprint import pprint #Uncomment line 63
import json
import os
{} type dict
[] type list


#Define Current Path & Items in Current Working Directory
current_path = os.getcwd()
current_directory = os.listdir()

#Loop Through Items in Current Working Directory
for item in current_directory:
    
    #Find Folder for Global Weather Data
        
    #Find Folder for Output Plots
    if item.lower().find('historical weather data') >= 0:
        
        #Define File Path for Output Plots
        output_file = current_path + '/' + item + '/'
        output_file_exact = current_path + '/' + item + '/selected' + '/'
        output_file_final = current_path + '/' + item + '/final' + '/'

#Define Range of Latitudes & Longitudes

# print(output_file)
    
def init_():
    yyyy = int(input('Enter the year:'))
    mm = int(input('Enter the month:'))
    dd = int(input('Enter the day:'))
    API_key = 'db8b55378d950841ba215808e438c082'
    base_url = "http://api.openweathermap.org/data/2.5/onecall/timemachine?"
    #lat, lon is Chasseneuil-du-Poitou, FR
    lat_data = str(46.650703);
    lon_data = str(0.374772);
    #city ID of Chasseneuil-du-Poitou, FR
    city_id = str(3026391);
    return API_key,base_url,lat_data,lon_data,city_id,yyyy,mm,dd

def date_to_unix_timestamp(yyyy,mm,dd):
# =============================================================================
# Convert date to unix timestamp string
# =============================================================================
    # yyyy = 2020; mm = 12; dd = 29;
    dt = datetime.datetime(yyyy, mm, dd, 19, 00, 00)
    dt_unix = int((time.mktime(dt.timetuple())))
    print("Unix Timestamp: ",dt_unix)
    # print(type(dt_unix))
    # print(str(dt_unix))
    return dt_unix

def unix_timestamp_to_date():
# =============================================================================
# Convert unix timestamp string to readable date
# =============================================================================
    dt_unix1= int(1284105682);
    print(datetime.datetime.fromtimestamp(dt_unix1).strftime('%Y-%m-%d %H:%M:%S'))
    return (dt_unix1);

def url_(base_url,lat_data,lon_data,dt_unix,API_key):
# This is final url. This is concatenation of base_url, API_key and city_id
    Final_url = base_url + "lat=" + lat_data + "&lon=" + lon_data + "&dt=" + str(dt_unix) + "&appid=" + API_key
    print(Final_url)
    return Final_url

def create_json(Final_url):
    # Print data in Json object
    weather_data = requests.get(Final_url).json() # Type Dict
    # Convert Python object into a json string
    weather_data_str = json.dumps(weather_data) # Type String

    if "future" in weather_data_str: #Check in type String
        print("You're in future, please get data of 5 previous days")
    elif "5 days back" in weather_data_str:
        print("You're too late, please get data of 5 previous days")
    else:
        return weather_data, weather_data_str

def print_json(weather_data):
    #Show JSON data
    pprint(weather_data,indent=4) 
    
def write_Json(yyyy,mm,dd,weather_data,weather_data_str): 
    #Define Current Path & Items in Current Working Directory

    # Save in Json file with all keys
    with open(output_file+str(yyyy)+"-"+str(mm)+"-"+str(dd)+".json", 'w') as outfile:
        json.dump(weather_data, outfile)
    # Check keys in weather_data dictionary 
    print ("The dictionary contains the following keys: ", weather_data.keys())    
    
    # Check keys in keys
    # print('Check', weather_data['current'].keys())
    return weather_data

def select_data_json(weather_data):
    # Extract Json data includes dt, temperature and humidity
    # Exclude the other keys

    list_dt_day = [] 

    for a in weather_data['hourly']:
        # print ('Get value', dt['dt']) 
        dict_={}
        dict_['dt'] = a['dt']
        dict_['temp'] = a['temp']
        dict_['humidity'] = a['humidity']
        dict_['pressure'] = a['pressure']
        dict_['clouds'] = a['clouds']
        dict_['wind_speed'] = a['wind_speed']
        dict_['wind_deg'] = a['wind_deg']
        dict_['description'] = a['weather'][0]['description']
        
        # for b in weather_data['hourly']['description']:
        #     dict_['description'] = b['description']
        list_dt_day.append(dict_)
 
    # pprint(list_dt_day) # Type list
    print ('Sunrise', weather_data['current']['sunrise'])  
    print(list_dt_day)
    return list_dt_day

def write_exact_data_json(yyyy,mm,dd,list_dt_day):
    # Save in Json file
    with open(output_file_exact+"exact_historical_"+str(yyyy)+"-"+str(mm)+"-"+str(dd)+".json", 'w') as outfile:
        json.dump(list_dt_day, outfile)
     
def create_1_data_json(weather_data):
    # Create 3 separated lists of dictionaries dt, temp, humidity 
    # like {'temp': 279.71}
   
    list_dt_day = [] 
    list_temp_day = []
    list_humidity_day = []
    list_dt_day_dt = []
    list_temp_day_temp = []
    list_humidity_day_humidity = []
    
    for a in weather_data['hourly']:
        # print ('Get value', dt['dt']) 
        list_dt_day.append(a['dt'])
        list_temp_day.append(a['temp'])
        list_humidity_day.append(a['humidity'])
        # print(a['dt'])
        # json.dumps(dt['dt']) 
    # print('List dt value in a day', list_dt_day) # Type list
    
    # Add key to the values
    
    for i in range(len(list_dt_day)): 
        a = ['dt']
        b = dict.fromkeys(a,list_dt_day[i])
        list_dt_day_dt.append(b)
    # print('List of dictionary with dt key', list_dt_day_dt)
    # print(type(list_dt_day_dt))
    
    for i in range(len(list_temp_day)): 
        a = ['temp']
        b = dict.fromkeys(a,list_temp_day[i])
        list_temp_day_temp.append(b)
    # print('List of dictionary with temp key', list_temp_day_temp)
    
    for i in range(len(list_humidity_day)): 
        a = ['humidity']
        b = dict.fromkeys(a,list_humidity_day[i])
        list_humidity_day_humidity.append(b)
    # print('List of dictionary with humidity key', list_humidity_day_humidity)

    return list_dt_day, list_dt_day_dt, list_temp_day_temp, list_humidity_day_humidity

def open_json():
    # Open a JSON file
    with open('ChasseneuilWeather_Final.json') as json_file:
        data = json.load(json_file)
    pprint(data, indent = 4) # Type list
    
    return data   

def check_json(list_dt_day,data):
    # Check the duplicated data before adding to the json file
    # Pre-check manually
    dt_value = data[0]['dt']
    print ('Get value', dt_value)
    print(type(dt_value))

    print('Check', list_dt_day[0]['dt']) 
    print(type(list_dt_day[0]['dt']))

    # New data
    for sublist1 in list_dt_day:
        flag = 0
        # print (sublist1['dt'])
        # Old data
        for sublist2 in data:
            # print ('a', sublist2['dt'])
            # Check old data and new data
            if sublist2['dt'] == sublist1['dt']:
                print('Duplicated data')
                flag = 1
                return False
        data.append(sublist1)
        
    # pprint(data)
    print(len(data))

    # with open("data.json", 'w') as outfile:
    #     json.dump(data, outfile)
    return data

def add_json(yyyy,mm,dd,data):
    # Add the current data to the previous json file 
    pprint(data)  

    # save all data to a JSON file
    with open(output_file_final+"Final_"+str(yyyy)+"-"+str(mm)+"-"+str(dd)+".json", 'w') as outfile:
        json.dump(data, outfile)
    
def main():
    # unix_timestamp_to_date()
    API_key,base_url,lat_data,lon_data,city_id,yyyy,mm,dd = init_()
    dt_unix = date_to_unix_timestamp(yyyy,mm,dd)
    Final_url = url_(base_url,lat_data,lon_data,dt_unix,API_key)
    weather_data, weather_data_str = create_json(Final_url)
    print_json(weather_data) #Only show data
    write_Json(yyyy,mm,dd,weather_data,weather_data_str)
    
    list_dt_day = select_data_json(weather_data)
    write_exact_data_json(yyyy,mm,dd,list_dt_day)
    
    # create_1_data_json(weather_data)
    
    # data = open_json()
    # data = check_json(list_dt_day,data)
    # add_json(yyyy,mm,dd,data)
    
    
if __name__ == "__main__":
    main()
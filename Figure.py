# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:47:23 2021

@author: lammi
"""


import datetime
from pprint import pprint #Uncomment line 63
import json
import os
import matplotlib.pyplot as plt
import numpy as np

# {} type dict
# [] type list


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
        
        #Find Folder for Output Plots
    elif item.lower().find('images') >= 0:
        
        #Define File Path for Output Plots
        output_plot = current_path + '/' + item + '/'


def ChasseneuilWeather_Final():
    # Open a JSON file
    with open('ChasseneuilWeather_Final.json') as json_file:
    # with open ('ChasseneuilWeather_Final_Update_Need.json') as json_file:
        data = json.load(json_file)
    # pprint(data[0]['dt']) # Type list 1609945200
    # print(datetime.datetime.fromtimestamp(data[0]['dt']).strftime(%h-%d'))
    # 16-06   
    list_dt = []
    list_temp = []
    list_hum = []
    for i in range(len(data)):
        # Days
        # list_dt.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Hh-%d/%m'))
        # Years
        list_dt.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Hh-%d/%m/%y'))
        list_temp.append(data[i]['temp'])
        list_hum.append(data[i]['humidity'])
    print(list_dt)
    # print(list_temp)
    return data, list_dt, list_temp, list_hum

def forecast():
    # Open a JSON file
    # with open('ChasseneuilWeather_Final.json') as json_file:
    with open ('ChasseneuilWeather_Final_Update_Need.json') as json_file:
        data = json.load(json_file)
    pprint(data[0]['dt']) # Type list 1609945200
    # print(datetime.datetime.fromtimestamp(data[0]['dt']).strftime(%h-%d'))
    # 16-06   
    list_dt = []
    list_temp = []
    list_hum = []
    for i in range(len(data)):
        list_dt.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Hh-%d/%m'))
        list_temp.append(data[i]['temp'])
        list_hum.append(data[i]['humidity'])
    # print(list_dt)
    # print(list_temp)
    return data, list_dt, list_temp, list_hum
    
def hour_scatter_interval_temp_time(list_dt, list_temp):
    #Plot Latitude Data Versus Maximum Temperature Data
    F1, AX1 = plt.subplots()
    AX1.scatter(list_dt, list_temp, facecolor = 'blue', edgecolor = 'black')
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/6), rotation='vertical')
    AX1.set_title('Temperature vs Time')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature_vs_Time.png')
    
    plt.show()
    
def hour_scatter_interval_temp_humd(list_hum, list_temp):
    #Plot Latitude Data Versus Maximum Temperature Data
    F1, AX1 = plt.subplots()
    AX1.scatter(list_hum, list_temp, facecolor = 'blue', edgecolor = 'black')
    AX1.grid()
    AX1.set_title('Humidity vs Temperature 01/02/2021-06/02/2021')
    AX1.set_xlabel('Humidity')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Humidity_vs_Time.png')
    
    plt.show()

def hour_line_interval_temp_time(list_dt, list_temp):
    F1, AX1 = plt.subplots()
    AX1.plot(list_dt, list_temp)
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/5), rotation='vertical')
    AX1.set_title('Temperature vs Time from 1979-2021')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature vs Time_Line Chart.png')
    plt.show()
    
def hour_bar_interval(list_dt, list_temp):
    F1, AX1 = plt.subplots()
    AX1.bar(list_dt, list_temp, width=0.4)
    # AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/6), rotation='vertical')
    AX1.set_title('Test_bar')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Test_bar.png')
    plt.show()
    
def compare_forecast(list_dt, list_temp):
    F1, AX1 = plt.subplots()
    AX1.plot(list_dt, list_temp)
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/5), rotation='vertical')
    AX1.set_title('Test_Line')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Test_Line.png')
    plt.show()
    
    
def main():   
    data, list_dt, list_temp, list_hum  = ChasseneuilWeather_Final()
    # hour_scatter_interval_temp_time(list_dt, list_temp)
    hour_line_interval_temp_time(list_dt, list_temp)
    # hour_bar_interval(list_dt, list_temp)
    hour_scatter_interval_temp_humd(list_hum, list_temp)

    
if __name__ == "__main__":
    main()
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

def hour_scatter_interval():
    # Open a JSON file
    # with open('ChasseneuilWeather_Final.json') as json_file:
    with open ('ChasseneuilWeather_Final.json') as json_file:
        data = json.load(json_file)
    pprint(data[0]['dt']) # Type list 1609945200
    # print(datetime.datetime.fromtimestamp(data[0]['dt']).strftime(%h-%d'))
    # 16-06

   
    list_dt = []
    list_temp = []
    for i in range(len(data)):
        list_dt.append(datetime.datetime.fromtimestamp(data[i]['dt']).strftime('%Hh-%d/%m'))
        list_temp.append(data[i]['temp'])
    print(list_dt)
    print(list_temp)

    #Plot Latitude Data Versus Maximum Temperature Data
    F1, AX1 = plt.subplots()
    AX1.scatter(list_dt, list_temp, facecolor = 'blue', edgecolor = 'black')
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/6), rotation='vertical')
    AX1.set_title('Temperature vs Time')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature_vs_Time.png')

    
    # fig, ax = plt.subplots(figsize=(12, 6))

    # x = list_dt()
    # y = list_temp
    # ax.plot(x, y, color='blue', label='Temperature_vs_Time')
    
    plt.show()
    return data, list_dt, list_temp   

def hour_line_interval(list_dt, list_temp):
    F1, AX1 = plt.subplots()
    AX1.plot(list_dt, list_temp)
    AX1.grid()
    plt.xticks(np.arange(0,len(list_dt),len(list_dt)/5), rotation='vertical')
    AX1.set_title('Test')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Test.png')
    plt.show()
    
def main():   
    data, list_dt, list_temp  = hour_scatter_interval() 
    hour_line_interval(list_dt, list_temp)

    
if __name__ == "__main__":
    main()
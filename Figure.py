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

def open_json():
    # Open a JSON file
    # with open('ChasseneuilWeather_Final.json') as json_file:
    with open ('exact_everyhourforecast2021-01-06-16.json') as json_file:
        data = json.load(json_file)
    pprint(data[0]['dt']) # Type list
    list_dt = []
    list_temp = []
    for i in range(len(data)):
        list_dt.append(data[i]['dt'])
        list_temp.append(data[i]['temp'])
    print(list_dt)
    print(list_temp)
    
    #Plot Latitude Data Versus Maximum Temperature Data
    F1, AX1 = plt.subplots()
    AX1.scatter(list_dt, list_temp, facecolor = 'blue', edgecolor = 'black')
    AX1.grid()
    AX1.set_title('Temperature vs Time')
    AX1.set_xlabel('Time')
    AX1.set_ylabel('Temperature (K)')
    plt.savefig(output_plot + 'Temperature_vs_Time.png')
    plt.show()

    return data   

    
def main():   
    data = open_json()   
    
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:11:57 2020

@author: lammi

Before run, you need to install 2 libraries
$ pip install openweather
$ pip install pyowm
You need to run timezone_conversion -> pyowm_helper -> weatherGUI
"""

from matplotlib import pyplot as plt
from matplotlib import dates
from datetime import datetime
from pyowm_helper import get_temperature
from pyowm_helper import get_humidity
from pyowm_helper import get_pressure
import os


a = datetime.now().strftime("%Y-%m-%d")
degree_sign= u'\N{DEGREE SIGN}' # Symbol of temperature
#Define Current Path & Items in Current Working Directory
current_path = os.getcwd()
current_directory = os.listdir()

#Loop Through Items in Current Working Directory
for item in current_directory:
    
    #Find Folder for Global Weather Data
        
    #Find Folder for Output Plots
    if item.lower().find('images') >= 0:
        
        #Define File Path for Output Plots
        output_file = current_path + '/' + item + '/'


def init_plot_t():
    # Create a window has a titlebar, width and height in inches
    plt.figure('PyOWM Weather', figsize=(10,8))
    # Create labels and titles to the plot
    plt.xlabel('Day')
    plt.ylabel(f'Temperature ({degree_sign}C)' )
    plt.title('Temperature Forecast at Chasseneuil-du-Poitou')
    
def plot_temperatures(days, temp_min, temp_max):
    # Convert list of "datetime" obj to "matplotlib" dates
    # Offset the two plots so that the bars don't cover each other
    days = dates.date2num(days)
    bar_min = plt.bar(days-.25, temp_min, width=0.5, color='#4286f4') #blue
    bar_max = plt.bar(days+.25, temp_max, width=0.5, color='#e58510') #orange
    return (bar_min, bar_max)

def label_xaxis(days):
    # Use the days as the x-axis labels 
    plt.xticks(days)
    # Get the axes of the plot
    axes = plt.gca()
    # Specify a format of the month and day separated by a slash
    xaxis_format = dates.DateFormatter('%m/%d')
    # Set date format as the format for x-axis
    axes.xaxis.set_major_formatter(xaxis_format)

def write_temperatures_on_bar_chart(bar_min, bar_max):
    # Display the temperature at the top of each bar in the chart
    axes = plt.gca()
    # Get the maximum value of the y-axis and multiple it by .03
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .03
    # Loop through each bar chart
    for bar_chart in [bar_min, bar_max]:
        # Loop through each bar of each bar chart
        for index, bar in enumerate(bar_chart):
            # Get the bar height for each bar
            height = bar.get_height()
            # Calculate the horizontal center of the bar
            xpos = bar.get_x() + bar.get_width()/2.0
            # Calculate the y-coordinate of the label
            ypos = height - label_offset
            # Set the label text equal to the height of the bar
            label_text = str(float(height)) + degree_sign
            plt.text(xpos, ypos, label_text,
                  horizontalalignment='center',
                  verticalalignment='center',
                  color='black')

def init_plot_h():
    plt.figure('PyOWM Weather', figsize=(10,8))
    plt.xlabel('Day')
    plt.ylabel('Humidity (%)' )
    plt.title('Humidity Forecast at Chasseneuil-du-Poitou') 


def plot_humidity(days, hum_min, hum_max):
    # Convert list of "datetime" obj to "matplotlib" dates
    # Offset the two plots so that the bars don't cover each other
    days = dates.date2num(days)
    bar_h_min = plt.bar(days-.25, hum_min, width=0.5, color='#4286f4') #blue
    bar_h_max = plt.bar(days+.25, hum_max, width=0.5, color='#e58510') #orange
    return (bar_h_min, bar_h_max)

def write_humidity_on_bar_chart(bar_h_min, bar_h_max):
    # Display the humidity at the top of each bar in the chart
    axes = plt.gca()
    # Get the maximum value of the y-axis and multiple it by .03
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .03
    # Loop through each bar chart
    for bar_chart in [bar_h_min, bar_h_max]:
        # Loop through each bar of each bar chart
        for index, bar in enumerate(bar_chart):
            # Get the bar height for each bar
            height = bar.get_height()
            # Calculate the horizontal center of the bar
            xpos = bar.get_x() + bar.get_width()/2.0
            # Calculate the y-coordinate of the label
            ypos = height - label_offset
            # Set the label text equal to the height of the bar
            label_text = str(float(height)) + degree_sign
            plt.text(xpos, ypos, label_text,
                  horizontalalignment='center',
                  verticalalignment='center',
                  color='black')
            
    
            
def init_plot_p():
    plt.figure('PyOWM Weather', figsize=(10,8))
    plt.xlabel('Day')
    plt.ylabel('Pressure (%)' )
    plt.title('Pressure Forecast at Chasseneuil-du-Poitou') 

def plot_pressure(days, pre_min, pre_max):
    # Convert list of "datetime" obj to "matplotlib" dates
    # Offset the two plots so that the bars don't cover each other
    days = dates.date2num(days)
    bar_p_min = plt.bar(days-.25, pre_min, width=0.5, color='#4286f4') #blue
    bar_p_max = plt.bar(days+.25, pre_max, width=0.5, color='#e58510') #orange
    return (bar_p_min, bar_p_max)

def write_pressure_on_bar_chart(bar_p_min, bar_p_max):
    # Display the pressure at the top of each bar in the chart
    axes = plt.gca()
    # Get the maximum value of the y-axis and multiple it by .03
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .03
    # Loop through each bar chart
    for bar_chart in [bar_p_min, bar_p_max]:
        # Loop through each bar of each bar chart
        for index, bar in enumerate(bar_chart):
            # Get the bar height for each bar
            height = bar.get_height()
            # Calculate the horizontal center of the bar
            xpos = bar.get_x() + bar.get_width()/2.0
            # Calculate the y-coordinate of the label
            ypos = height - label_offset
            # Set the label text equal to the height of the bar
            label_text = str(float(height)) + degree_sign
            plt.text(xpos, ypos, label_text,
                  horizontalalignment='center',
                  verticalalignment='center',
                  color='black')
            
if __name__ == '__main__':
    # Show temperature
    days, temp_min, temp_max = get_temperature()
    init_plot_t()
    bar_min, bar_max = plot_temperatures(days, temp_min, temp_max)
    label_xaxis(days)
    # Add the Temperatures as Labels on the Bar Chart
    write_temperatures_on_bar_chart(bar_min, bar_max)
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig(output_file + "forecast_temp_" +a+".png")


    
    # Show humidity
    days, hum_min, hum_max = get_humidity()
    init_plot_h()
    bar_h_min, bar_h_max = plot_humidity(days, hum_min, hum_max)
    label_xaxis(days)
    write_humidity_on_bar_chart(bar_h_min, bar_h_max)
    fig2 = plt.gcf()
    plt.show()
    fig2.savefig(output_file + "forecast_humi_" +a+".png")

    # Show pressure
    days, pre_min, pre_max = get_pressure()
    init_plot_p()
    bar_p_min, bar_p_max = plot_pressure(days, pre_min, pre_max)
    label_xaxis(days)
    write_humidity_on_bar_chart(bar_p_min, bar_p_max)
    fig3 = plt.gcf()
    plt.show()
    fig3.savefig(output_file + "forecast_pres_" +a+".png")
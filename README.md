# BE_OpenWeatherMap

# Introduction
Hello to the OpenWeatherMap Program,
These programs are used to load the online data of OpenWeatherMap, create the JSON file, and analyze the data.
They have already supported a library in Python named "pyowm". You can find more detailed information at this link [here](https://pypi.org/project/pyowm/).
![alt text](https://upload.wikimedia.org/wikipedia/commons/f/f6/OpenWeather-Logo.jpg)

# Purpose
This project aims to get the historical data, current data, forecast data from OpenWeatherMap platform. Then, we use this data to compare with the experimental data. For this reason, we created these following steps to visualize the progress:
1. Understand the OpenWeatherMap syntax to get the data
2. Store the readable useful data.
3. Analyze this data.
4. Compare between the OpenWeatherMap data and the experimental data and fiving conclusion.

## API key
### api_key.py
First, we need to have an API key of OpenWeatherMap to use their services. In my part, we have the api "db8b55378d950841ba215808e438c082".
We add this api key to the OS environment. This program is to call this key.

### location.py
There are 4 ways to identify a location following the OpenWeatherMap library. There are:
1. name
2. id
3. latitude - longitude
4. zipcode

## Current data
### current.py
This program allows you to get all the current weather data. We can use it when we need data at the current time of the experiment.

## Historical data
This part is aimed to create a historical database from 01/01/1979 to the present focused on the temperature and humidity factors. 
It is required to update everyday from the website because of the limitation of the free account. So we created a program to store and analyze the data in the JSON type.
There are 2 programs:
### learningjson.py
A draft illustrates many functions and examples of JSON files and a 'list of dictionaries' analysis. 

### historicaldata.py
This program is one of the most important parts in order to store and analyze the historical data.
1. Change the Unix timestamp to normal time and vice versa.
2. Get the online data in the previous 5 days.
3. Store it as a JSON file.
4. Extract wanted data from the new JSON file.
5. Change the data to the same type as the old data.
6. Check if existing any duplicated data.
7. Append the wanted data to the old data.
8. Create the updated JSON file.

## Forecast data

### weatherforecast.py: 
1. Get the forecast weather in the next 5 days, 3-hour interval.
2. Get the forecast weather in the next 48 hours, 1-hour interval.
3. Write all data as the JSON type including:

| Name                                     |Type  | Description                                | Exemple                                                                          |
|------------------------------------------|------|--------------------------------------------|----------------------------------------------------------------------------------|
| **threehoursforecast** *yyyy-mm-dd-hh*      | Json | Needed data 3-hour interval for 5 days     | [threehoursforecast2021-01-06-16.json](https://cloud.ensma.fr/s/cJ5R6YqSnAYepZQ)      |
| **everyhourforecast** *yyyy-mm-dd-hh*       | Json | Detailed data 1-hour interval for 48 hours | [everyhourforecast2021-01-06-16.json](https://cloud.ensma.fr/s/FyB6TptLXtZjjwq)       |
| **exact_everyhourforecast** *yyyy-mm-dd-hh* | Json | Needed data 1-hour interval for 48 hours   | [exact_everyhourforecast2021-01-06-16.json](https://cloud.ensma.fr/s/CQr5Sg3D7D2jtcJ) |


4. Get Weather At a Specific Time.
5. Get Weather at a Specific Time of tomorrow.
6. Check for certain weather conditions in a forecast.
7. Check if a particular weather condition exists at a specified time for 5 days.

# Continue

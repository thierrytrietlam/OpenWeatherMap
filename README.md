# BE_OpenWeatherMap

# Introduction
Hello to the OpenWeatherMap Program,

OpenWeather is a team of IT experts and data scientists that has been practicing deep weather data science since 2014. For each point on the globe, OpenWeather provides historical, current, and forecasted weather data via light-speed APIs.

They provide data for any coordinates by utilizing our proprietary convolutional neural network/machine learning model that they use for weather forecasting and historical data calculation. On different levels, different data sources are used (such as radars and a vast network of weather stations, along with data from global/local providers such as NOAA, Environment Canada, and the Met Office). 

They provide weather data through our API, they use their own numerical weather prediction (NWP) model, which uses several data sources:

* Global NWP models:
  - NOAA GFS 0.25 and 0.5 grid sizes
  - NOAA CFS
  - ECMWF ERA
* Weather stations:
  - METAR stations
  - Users’ stations
  - Companies’ stations
* Weather radar data
* Satellite data

They download and save data from these sources. Then it is processed by their in-house set of algorithms, to improve its quality and accuracy. This data processing is being done in real-time, to provide the latest nowcasts and forecasts.
These programs are used to load the online data of OpenWeatherMap, create the JSON file, and analyze the data.
They have already supported a library in Python named "pyowm". You can find more detailed information at this link [here](https://pypi.org/project/pyowm/).

In order to use this data, we must create an account and get the personal API key. For more details, you can access this link [here](https://openweathermap.org/api).

![alt text](https://upload.wikimedia.org/wikipedia/commons/f/f6/OpenWeather-Logo.jpg)

# Purpose
This project aims to get the historical data, current data, forecast data from OpenWeatherMap platform. Then, we use this data to compare with the experimental data. For this reason, we created these following steps to visualize the progress:
1. Understand the OpenWeatherMap syntax to get the data.
2. Store the readable useful data.
3. Analyze this data.
4. Compare between the OpenWeatherMap data and the experimental data and fiving conclusion.

# Data

## Historical data

I had bought the package historical data of Chasseneuil-du-Poitou, France from 1979 until December 2020. 
The name of this file: 
[ChasseneuilWeather2021.csv](https://cloud.ensma.fr/s/gpzP3KHi8SK2SQq)

However, the data was too much. For this reason, I selected the needed data and changed it to JSON type including *time, temperature, pressure, humidity, wind speed, wind degree, and weather description*.

[ChasseneuilWeather_Final_Update_Need.json](https://cloud.ensma.fr/s/xb6jTAiL8XFsNKA)

After that, I need to update my data every day by the personal API key. I save the name following some rules:

| Name                                     |Type  | Description                                | Exemple                                                                          |
|------------------------------------------|------|--------------------------------------------|----------------------------------------------------------------------------------|
| *yyyy-mm-dd*      | Json | Historical every-hour data on 10th March, 2021     | [2021-3-10.json](https://cloud.ensma.fr/s/D7R4XqgTXeKa9P5)      |
| **exact_historical_** *yyyy-mm-dd*       | Json | The needed data extracted from *yyyy-mm-dd* file | [exact_historical_2021-3-10.json](https://cloud.ensma.fr/s/fxXnmzXz3Apm9sf)       |
| **Final_** *yyyy-mm-dd* | Json | The final file after appended the last data extend until the newest data   | [Final_2021-2-2.json](https://cloud.ensma.fr/s/MpSotFNgJjmBXbf) |

Here is the link to my data warehouse:
[Historical Data](https://cloud.ensma.fr/s/XqQHNfq3T4XJWpK)

## Forecast data
For the Forecast data, the OpenWeatherMap provides many ways to get data. There are some options for you:

* Data 3-hour interval for 5 days
* Data 1-hour interval for 48 hours

As the same as the historical data, here is how I named my files:

| Name                                     |Type  | Description                                | Exemple                                                                          |
|------------------------------------------|------|--------------------------------------------|----------------------------------------------------------------------------------|
| **threehoursforecast** *yyyy-mm-dd-hh*      | Json | Needed data 3-hour interval for 5 days     | [threehoursforecast2021-01-06-16.json](https://cloud.ensma.fr/s/cJ5R6YqSnAYepZQ)      |
| **everyhourforecast** *yyyy-mm-dd-hh*       | Json | Detailed data 1-hour interval for 48 hours | [everyhourforecast2021-01-06-16.json](https://cloud.ensma.fr/s/FyB6TptLXtZjjwq)       |
| **exact_everyhourforecast** *yyyy-mm-dd-hh* | Json | Needed data 1-hour interval for 48 hours   | [exact_everyhourforecast2021-01-06-16.json](https://cloud.ensma.fr/s/CQr5Sg3D7D2jtcJ) |

Here is the link to my forecast data warehouse:
[Forecast5days](https://cloud.ensma.fr/s/bX4ad4dY84P4yEo)
[Forecast](https://cloud.ensma.fr/s/W8edexLBfS8SmiQ)

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

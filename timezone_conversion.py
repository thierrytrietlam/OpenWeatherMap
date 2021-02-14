# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:45:23 2020

@author: lammi

# Before run, you need to install 2 libraries
# $ pip install openweather
# $ pip install pyowm
Learn more here http://pytz.sourceforge.net/
"""

import pytz
from datetime import datetime

# Convert time from GMT to Eastern time
def gmt_to_eastern(unix_gmt):
    eastern = pytz.timezone('Europe/Paris')
    # Create a GMT timezone object
    gmt = pytz.timezone('GMT')
    # Create a datetime object from the unix time 
    date = datetime.utcfromtimestamp(unix_gmt)
    # Associate the day with the GMT timezone
    date = gmt.localize(date)
    # Convert the day to our chosen timezone
    eastern_time = date.astimezone(eastern)
    # Return that day
    return eastern_time

if __name__ == '__main__':
    for timezone in pytz.all_timezones:
        print(timezone)

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:32:36 2020

@author: lammi
"""

# =============================================================================
# Learning JSON and Dictionary Manipulation
# =============================================================================

from pprint import pprint #Uncomment line 63
import json

def basic_json():
    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["name"])

    # a Python object (dict):
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
        } # different from ''

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

# Convert Python objects into JSON strings, and print the values:
    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

# Convert a Python object containing all the legal data types:
    x1 = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann","Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
            ]
        }

    print(json.dumps(x1))

# use . and a space to separate objects, and a space, 
# a = and a space to separate keys from their values:
    print(json.dumps(x1, indent=4))
    print(json.dumps(x1, indent=4, separators=(". ", " = ")))

# sort the result alphabetically by keys:
    print(json.dumps(x1, indent=4, sort_keys=True))
    return x,y,x1

def definition():
    # Opening JSON file 
    f = open('data.json',) 
  
# returns JSON object as a dictionary 
    data = json.load(f) 
  
# Iterating through the json list 
    for i in data['emp_details']: 
        print(i) 
  
# Closing file 
    f.close() 

def json_to_file():
# Writing JSON to a File
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
        })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
        })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
        })

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    print (data)    
    return data

def dict_manipulation():
    """
You are here: Home / Dictionary / Dictionary Manipulation in Python
Dictionary Manipulation in Python
Last Updated: August 26, 2020

Overview
A dictionary is a collection of key-value pairs.

A dictionary is a set of key:value pairs.

All keys in a dictionary must be unique.

In a dictionary, a key and its value are separated by a colon.

The key, value pairs are separated with commas.

The key & value pairs are listed between curly brackets ” { } ”

We query the dictionary using square brackets ” [ ] ”
    """
    # Create an empty dictionary
    months = {}
    months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" } 
    print(months)
    print(type(months)) 
    # Print all keys
    print ("The dictionary contains the following keys: ", months.keys())    
    # Get a value out of a dictionary
    whichMonth = months[1]
    print ('Get value', whichMonth)
    # Delete an element from a dictionary
    del(months[5])
    print ('Delete', months.keys())
    # Update an element of a dictionary
    months[1] = "Jan"
    print (months)
    # Sort 
    sortedkeys = months.keys()
    print ('Sorting', sortedkeys)
    # Iterate over keys
    for key in months:
        print ('Loops over keys', key, months[key])
        
    # Iterate over (key, value) pairs
    for key, value in months.items():
        print ('Pair', key, value)
    print ("The entries in the dictionary are:")
    for item in months.keys():
        print ("months[ ", item, " ] = ", months[ item ])
    return months

def combine_list_dict():
    "Combining List and Dictionary"
    #  List of dictionaries
    customers = [{"uid":1,"name":"John"},
    {"uid":2,"name":"Smith"},
           {"uid":3,"name":"Andersson"},
            ]
    print ('origin', customers)
    print ('Type', type(customers))
    # Print the uid and name of each customer
    for x in customers:
        print (x["uid"], x["name"])
    # Modify an entry
    customers[2]["name"]="charlie"
    print ('Modify', customers[2])
    # Add a new field to each entry
    for x in customers:
        x["password"]="123456" # any initial value
    print ('Add for all', customers)
    # Delete a field
    del customers[1]
    print ('Delete a field', customers)
    # This will delete id field of each entry.
    for x in customers:
        del (x["uid"], x["password"])
    print ('Delete 2 keys', customers)
    
    return customers

def listToDict(lstA, lstB):
    zippedLst = zip(lstA, lstB)
    op = dict(zippedLst)
    return op

    
def main():
    # basic_json()
    # json_to_file()
    # dict_manipulation()
    # combine_list_dict()
    
    # lstStr = ['millie', 'caleb', 'finn', 'sadie', 'noah']
    # lstInt = [11, 21, 19, 29, 46]
    # print(listToDict(lstStr, lstInt))
    # listToDict(lstStr, lstInt)
    

    
if __name__ == "__main__":
    main()
#!/usr/bin/python
# ISTE 432
# Eyob Abegaz, 
# Exercise - 2
# Converting CSV file to JESON file

# Import csv module to read and write tabular data in CSV format
# Import json module to convert the python dictionary into a json string 
# that can be written into a file
# Import time module to get today's date in YYYYMMDD format
import csv
import json
import time

# Assign today's date in YYYYMMDD format to a variable 
my_date = time.strftime('%Y%m%d')

# Read and fix the original csv file and
# write the fixed data on another csv file
with open('mockData.csv', 'r') as inpu, open('fixed_mocked.csv', 'w') as out:
    for line in inpu:
        l=line.replace(', Jr,', ',').replace(', III,', ',').replace(', ', ',').lower()
        out.write(l)

# Create a dictionary 
data = {} 
      
# Open a csv reader called DictReader 
with open('fixed_mocked.csv', 'r') as f: 
     csvReader = csv.DictReader(f) 
          
     # Convert each row into a dictionary  
     # and add it to data 
     for rows in csvReader: 
              
         # Assuming a column named 'id' to 
         # be the primary key 
         key = rows['id'] 
         data[key] = rows 
  
# Open a json writer, and use the json.dumps()  
# function to dump data 
with open(str(my_date) +'.json', 'w') as jf:
    
    # Make it more readable and pretty while writing
    jf.write(json.dumps(data, indent=4))

#!/usr/bin/python
# ISTE 432
# 09/04/2020
# Eyob Abegaz 
# Exercise - 2
# Converting CSV file to JESON file

# Import re module to get full support for the regular expressions 
# Import time module to get today's date in YYYYMMDD format
import csv
import json
import re
import time

# Function to fix the original csv file and 
# write the first name, last name, and gender in json file
def changeToJson():

    # Assign today's date in YYYYMMDD format to a variable 
    my_date = time.strftime('%Y%m%d')

    # Read and fix the original csv file and
    # open a json file in write mode
    with open('mockData.csv', 'r') as inpu, open(str(my_date) +'.json', 'w') as outpu:
        
        # Read line by line
        lines = inpu.readlines()
        
        # Remove the first line(the header)
        lines = lines[1:]

        # regex for email matching  
        email = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')  
        outpu.write("[\n")
        for line in lines:
            lineList = line.lower().strip().split(',')
    
            # Assign list items based on the index
            # to work with the desired fields
            fName = lineList[1]
            lName = lineList[2]
            gender = lineList[4] if email.match(lineList[3]) else lineList[5]
            desResult = ('{"First Name":"' + fName.title() + '","Last Name":"' + lName.title() + '","Gender":"' + gender.title() + '"},\n')
            if lines.index(line) == len(lines) - 1:  
                
                # Remove comma and new line from last lines
                desResult = desResult[:-2]  
            
            # Write into the json file               
            outpu.write(desResult)
          
        outpu.write("\n]")

        # Close both files
        outpu.close()
        inpu.close()

# main
if __name__ == '__main__':

    # Call the function changeToJson
    changeToJson()


import csv
import json

with open('mockData.csv', 'r') as inp, open('my.csv', 'w') as out:
    for line in inp:
        l=line.replace(', Jr,', ',').replace(', III,', ',').replace(', ', ',').lower()
        out.write(l)
# create a dictionary 
data = {} 
      
# Open a csv reader called DictReader 
with open('my.csv', 'r') as csvf: 
     csvReader = csv.DictReader(csvf) 
          
     # Convert each row into a dictionary  
     # and add it to data 
     for rows in csvReader: 
              
         # Assuming a column named 'No' to 
         # be the primary key 
         key = rows['id'] 
         data[key] = rows 
  
# Open a json writer, and use the json.dumps()  
# function to dump data 
with open('my.json', 'w') as jsonf: 
    jsonf.write(json.dumps(data, indent=4))

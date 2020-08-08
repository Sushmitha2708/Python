#this progam deals with how to load JSON files into python objects and then write those
# objects back to JSON files

import json

# to load a JSON file into a python object we use JSON 'load' method

#load method--> loads a file into python object
#loads method --> loads a string into a python object

# to load a file,it must be opened first
with open('countries.json') as f:
 	data=json.load(f)#after opening it is now loaded into a python obj

for country in data['countries']:
	print(country['name'],country['pm'])

for country in data['countries']:
	del country['capital']

#after deleting, the file is dumped back to a new json file usinng 'dump' method

#dump method--> dumps a file into python object
#dumps method --> dumps a string into a python object

#before dumping the data to a new json file, it must be created
with open('new_countries.json','w') as f:
	json.dump(data,f,indent=2)
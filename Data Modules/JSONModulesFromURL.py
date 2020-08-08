# in this a public API is used to pull the data into a python object and then parse out the information

import json
from urllib.request import urlopen

#To make a request to the web API, built-in 'urllib' module is used and specifically import urlopen to open the file

with urlopen("https://jsonplaceholder.typicode.com/users") as response:
	source= response.read()

#print(source)

#this response is loaded into a python object using JSON module

data= json.loads(source)# python obj->'data'

#this loaded data is dumped back to JSON string

print(json.dumps(data,indent=2,sort_keys=True))
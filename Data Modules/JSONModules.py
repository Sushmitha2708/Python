# JSON- Javascript Object Notation
# this program deals with conversion of strings to python objects and vice versa

import json

people_str= '''
{ 
	"people": [  
		{
		    "name":"Sherlock Holmes",
		    "profession": "Detective",
		    "address":"221B Bakers street",
		    "has_gun":false

		},
		{
			"name":"James Watson",
		    "profession":"Doctor",
		    "address":"221B Bakers street",
		    "has_gun":true


		}
	]
}
'''

#to load this data into python object from a string json.loads method is used

data=json.loads(people_str)
#print(data)
print(type(data)) # declares the type of data as 'dict'
print(type(data['people'])) # declares the 'people' JSONstring as a 'list' in python

for person in data['people']:
	print(person['name'])

for person in data['people']:
	del person['profession']

new_str= json.dumps(data, indent=2, sort_keys=True) # 'dumps' is used to dump back the remaining keys into JSON string
#from python objects
print(new_str)
print('-------------------------------------------------')
print(data)
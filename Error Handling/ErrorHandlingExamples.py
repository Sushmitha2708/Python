
person={'name':'Jessica Jones','age': 26}
person={'name':'Jessica Jones','age': 26,'job':'Detective'}

# Non-pythonic way
if 'name' in person and 'age' in person and 'job' in person:
	print("I am {name}.I am {age} yrs old and I am a {job}".format(**person))
else:
	print("missing some keys")
#pythonic way
try:
	print("I am {name}.I am {age} yrs old and I am a {job}".format(**person))
except KeyError as e:
	print("missing {} key".format(e))
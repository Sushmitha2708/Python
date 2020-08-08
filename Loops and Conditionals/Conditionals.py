#IF CONDITIONAL

language="Python"
if language=="Python":
	print("It is true")
elif language=="Java" :
	print("It is not true")
else:
	print("No match")

user='Admin'
logged_in= True
if user=='Admin' and logged_in:
	print('Adimn page')
else:
	print("Incorrect creds")

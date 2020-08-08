#EXAMPLE1
try:
	f=open('sample.txt')
	#var= blah
	#print(f.read())

except FileNotFoundError as e:
	print(e) #reason gets printed
except Exception as e:
	print(e)
	#print("Something went wrong")
else: # else runs when the try block doesn't catch an error
	print(f.read())
	f.close()

finally: #'finally' executes regardless of whats happens in the try block
	print("Executing finally")

#EXAMPLE2-generating an exception manually

try:
	f=open('sample.txt')
	if f.name=='sample.txt':
		raise Exception

except Exception as e:
	print("ERROR!!")

#reading files

with open('sample.txt','r') as f : 
	
	size_to_read=15
	f_contents=f.read(size_to_read)
	print(f_contents, end='///')
	f.seek(0) # to start reading from a certain point

	f_contents=f.read(size_to_read)
	print(f_contents)

	
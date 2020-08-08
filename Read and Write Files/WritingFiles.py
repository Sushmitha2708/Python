# To create and write in a file

with open('sample2.txt','w') as f: # it creates a new file if it doesn't exist
	f.write('Test')
	f.seek(0)   # starts from a certain point and replaces the existing text
	f.write('Testing..')

#to read from an existing file and write in it
with open('sample.txt','r') as rf:
	with open('sample_copy.txt','w') as wf: # sample_copy doesn't exist, It is being created ippo
		for line in rf: #for every line present in rf file
			wf.write(line) # copy that in wf file 



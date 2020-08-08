import csv

with open('names.csv','r') as csv_file:
	#csv_reader=csv.reader(csv_file) to read
	csv_reader=csv.DictReader(csv_file)
	for line in csv_reader:
		print(line['Computer Science and Engineering'])

	with open('new_names.csv','w') as new_file:
		csv_writer=csv.writer(new_file,delimiter='\t')

	for line in csv_reader:
		print(line[2])
		for line in csv_reader:
			csv_writer.writerow(line)

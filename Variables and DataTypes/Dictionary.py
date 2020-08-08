#Dictionary

student= { 'name':'Frank Castle', 'age':30,'courses':['History','Economics']}

print(student['name']) #or

print(student.get('name','not found')) #get is to give default value
print(student.get('phone','not found')) 

student.update({'name':'Karen page','phone': '555-5555' })
print(student)
del student['phone']
print(student)

for key,value in student.items():
	print(key,value)
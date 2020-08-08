language="Pytho"
if language=="Python":
	print("it is true")
elif language=="Java" :
	print("it is also true")
else:
	print("no match")

user='Admn'
logged_in= True

if user=='Admin' and logged_in:
	print('Adimn page')
else:
	print("incorrect creds")

#FOR LOOP

nums=[1,2,3,4]
for num in nums:
	print(num)

for num in nums:
	if num==3:
		print('FOUND!')
		continue
	print(num)

#LOOP IN A LOOP
for num in nums:
	for letter in 'abc':
	   print(num, letter)

#WHILE LOOP
x=0
while x<10:
	if x==5:
		break
	print(x)
	x+=1

#CLASS EXAMPLE 1

class Temperature:
	def __init__(self,cel,fah):
		self.cel=cel
		self.fah=fah
	def to_celsius(self):
		r=((self.fah-32)*0.55)
		print(r)
	def to_fahrenheit(self):
		cels=(self.cel*0.55+32)
		print(cels)
t1=Temperature(1,32)

t1.to_celsius()
t1.to_fahrenheit()


#CLASS EXAMPLE 2

class Student:
	def __init__(self):
		self.fname="John"
		self.lname="Doe"
		self.email="johndoe@gmail.com"
		

	def setAge(self,age):
		self.age=age
		print("age is {}".format(self.age))

	def setMarks(self):
		self.marks=97
		print("marks are {}".format(self.marks))

s1=Student()
s1.setMarks()
s1.setAge(20)


#CLASS EXAMPLE 3

class StudentMarks:
	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2

	def __add__(self,other):
		m1=self.m1+other.m1
		m2=self.m2+other.m2
		s3=StudentMarks(m1,m2)
		return s3

s1=StudentMarks(55,66)
s2=StudentMarks(77,88)

s3=s1+s2
print(s3.m1)

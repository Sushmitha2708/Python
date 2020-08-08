#Dunder methods-Dunder method is a method which has two prefix and suffix underscores in the method name. Dunder here means Double Under(Underscores). These are commonly used for operator overloading
class Employee:

	num_of_emps=0
	raise_amt=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email= first+'.'+last+'@company.com'
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay=int(self.pay* self.raise_amt)

	def __repr__(self): #it is used for an object and can be used for debugging
		return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

	def __str__(self): # str is a readable representation of an obj and also as a display to the end user
		return "{}-{}".format(self.fullname(),self.email)


	

emp_1=Employee('Dmitri','Petrov',5000)
emp_2=Employee('Talia','Petrov',6000)

print(1+2)
print('a'+'b')

print(emp_1)
print(emp_1.__repr__())
print(emp_1.__str__())
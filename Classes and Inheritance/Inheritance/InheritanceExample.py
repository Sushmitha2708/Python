class Employee:

	raise_amt=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email= first+'.'+last+'@company.com'
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay=int(self.pay*self.raise_amt)

class Developer(Employee): 
	raise_amt=1.90 #To change the value declared in the parent class
	def __init__(self,first,last,pay,pgm_lang):
		super().__init__(first,last,pay) #'super' allows to access methods of the base class
		self.pgm_lang=pgm_lang

class Manager(Employee):# manages few employees
	def __init__(self,first,last,pay,list_of_employees=None):
		super().__init__(first,last,pay) #'super' allows to access methods of the base class
		if list_of_employees is None:
			self.list_of_employees=[]
		else:
			self.list_of_employees=list_of_employees

	def to_add(emp):
		if emp not in list_of_employees:
			self.list_of_employees.append(emp)

	def to_remove(emp):
		if emp  in list_of_employees:
			self.list_of_employees.remove(emp)

	def print_emps(self):

		for emp in self.list_of_employees:
			print('-->',emp.fullname())



emp_1=Developer('Dmitri','Petrov',5000,'JAVA')
emp_2=Developer('Talia','Petrov',6000,"Python")

print(help(Developer))#displays all the inherited items from the employee class
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.pgm_lang)

mgr_1=Manager('Sandor','Clegane',9000,[emp_1])

print(mgr_1.email)

mgr_1.print_emps()

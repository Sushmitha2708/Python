class A:#PARENT CLASS
	def function1(self):
		print("function1 is working")

	def function2(self):
		print("function2 is working")

class B(A): # child class which inherits the parent class
	def function3(self):
		print("function3 is working")

	def function4(self):
		print("function4 is working")

a1=A()

a1.function1()
a1.function2()

b1=B()

b1.function3()
b1.function4()
#inheriting
b1.function2()

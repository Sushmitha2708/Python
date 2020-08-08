class Student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
		self.laptop=self.Laptop() #INSTANCE OF INNER CLASS

	def show(self):
		print("details are",self.name,self.rollno)

	#inner class
	class Laptop:
		def __init__(self):
			self.brand="lenovo"
			self.cpu="i5"
			self.ram=8

		def showw(self):
			print("my laptop is",self.brand)

s1=Student("Karen",697)

s1.show()

#s1.lap.brand is to call the object of inner class

laptop1 = s1.laptop.showw() # an obj for inner class
laptop2= s2.laptop # TO CALL INNER CLASS DIRECTLY WITHOUT THE OBJ OF OUTER ONE

laptop1= Student.Laptop()
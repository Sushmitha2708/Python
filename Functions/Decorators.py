
def outer_fn():
	message="HEYY!"

	def inner_fn():
		print(message)
	return inner_fn
#outer_fn()
#or
my_func =outer_fn()
my_func()

#ex

def outer_function(msg):
	def inner_function():
		print(msg)
	return inner_function

hi_function=outer_function("hi")
bye_function=outer_function("bye")

hi_function()
bye_function()

#Decorators
#A decorator is a design pattern in Python that allows a user to add new
#functionality to an existing object without modifying its structure. 

def decorator_function(original_function): # function is taken as an argument
	def wrapper_function():
		print("wrapper executed this before {}".format(original_function.__name__))
		return original_function()
	return wrapper_function

def display():
	print("display function ran")

decorated_display = decorator_function(display)
decorated_display()
	


def hey_function():
	print("HEY!")
hey_function()
#OR

def heyy_function():
	return "HEY!"
print(heyy_function())

def heey_function(greeting,name):
	return '{} {}'.format(greeting,name)
print(heey_function('heyy','rheon'))

def student_info(*args,**kwargs):
	print(args)
	print(kwargs)

courses=['Math','Art']
info={'name':'Iwan','age':22}
student_info(*courses,**info)# to unpack the list and dictionary


#EXAMPLE

month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    
    return year%4==0 and (year%100!=0 or year %400==0)

def days_in_month(year,month):
	if month==2 and is_leap(year):
		return 29
	else:
		return month_days[month]

print(is_leap(2028))
print(days_in_month(2020,0))

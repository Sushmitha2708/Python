#List
#Example1
courses=['History','Math','Biology','English']

print(len(courses))
print(courses[0])
print(courses[-1]) #prints the last one
courses[2]='Science' # to replace
print(courses)
courses.append('Art') # Append is to add in the last
print(courses)
courses.insert(0,'Chemistry') # To add in a particular location
print(courses)

courses_2=['Economics','French']
courses.append(courses_2)
print(courses)

courses.remove('Art')
print(courses)
courses.pop() # Another way to delete thr last one
print(courses)

courses.reverse()
print(courses)

courses.sort() # sorts letters in alpabetical order
print(courses)

#Example2
nums=[1,2,3,4,5,6,7,8,9,10]
nums.sort()# ASC
print(nums)

nums.sort(reverse=True)#DESC
print(nums)

my_list=[]
for n in nums:
	my_list.append(n)
print (my_list)

#COMPREHENSION
my_list=[n for n in nums]
print(my_list)


#LIST FUNCTIONS

print(min(nums))
print(max(nums))
print(sum(nums))

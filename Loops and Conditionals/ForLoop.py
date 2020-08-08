#SET COMPREHENSIONS
# set is similar to list but with unique values

nums=[1,1,1,2,3,5,5,5,4,6,7,7,8,9,9] #list
my_set=set()
for n in nums:
	my_set.add(n)
print(my_set)

#comprehension

my_set={n for n in nums}
print(my_set)
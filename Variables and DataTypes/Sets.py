#SETS ARE UNORDERED AND WITHOUT DUPLICATES

set1={'Obama','Trump','Clinton','JFK'}
print(set1)

set2 = {'Michelle','Clinton','Melania'}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

#SET COMPREHENSIONS

nums=[1,1,1,2,3,5,5,5,4,6,7,7,8,9,9] #list
my_set=set()
for n in nums:
	my_set.add(n)
print(my_set)

#comprehension

my_set={n for n in nums}
print(my_set)
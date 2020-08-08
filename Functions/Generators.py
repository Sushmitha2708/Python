#Generators don't hold the entire result in the memory
#It yields one result at a time, so it waits for us to ask for the next result
#Normal
def sq_numbers(nums):
	result=[]
	for i in nums:
		result.append(i*i)
	return result

numbers= sq_numbers([1,2,3,4,5])

print(numbers)

#Generators
def square_numbers(nums):
	for i in nums:
		yield(i*i) #yield keyword gives the result and makes it a generator

number = square_numbers([1,2,3,4,5])
for num in number:
	print(num)


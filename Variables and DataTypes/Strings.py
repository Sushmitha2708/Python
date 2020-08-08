#String
a = "Hello World!"
print(a)

#Entering values in the placeholders
tag='h1'
text='This is a headline'
sentence3 ='<{0}>{1}</{0}>'.format(tag,text)
print(sentence3)


for i in range(1,11):
	sentence4='the sentence is {:04}'.format(i)
	print (sentence4)

#Decimal values
pi=3.14159265
sentence5='pi is {:.2f}'.format(pi)  # : --> to specify that formatting is needed
print(sentence5)

#SLICING STRINGS

string1= 'daenarys targaryan'

print (string1)
print(string1[::-1])
print(string1[0:-1:1])
print(string1[:8])



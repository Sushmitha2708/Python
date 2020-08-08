from collections import namedtuple

#named tuple is like a normal tuple with more readability
#normal tuple
#color=(55,100,110)
#print(color[0])

Color=namedtuple('color',['red','black','blue'])

color=Color(55,100,105)
print(color[0])
print(color.red)
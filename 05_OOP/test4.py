from pprint import pprint
from random import randrange
# pprint(tuple.__dict__)

class boy:
    age = 15
    height = 160


a = []
for i in range(5):
    a.append(boy())

index = randrange(0, 5)
a[index].height = 165
a_height = [a[index].height for index in range(5)]

index = randrange(0, 5)
a_height.pop(index)
pprint(a_height)
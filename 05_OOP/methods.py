class Person:
    age = 16
    name = 'Max'
    gender = 1

#getting objetct attribute
print(getattr(Person, 'name', 'Impossible')) 

#setting a new object attribute
setattr(Person, 'k', 'ssss')
print(Person.__dict__)

#delete object attribute
del Person.k
print(Person.__dict__)

#delete object attribute
delattr(Person, 'age')
print(Person.__dict__)

#existence verification object attribute
print(hasattr(Person, 'name'))
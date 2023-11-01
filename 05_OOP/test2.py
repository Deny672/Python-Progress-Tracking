class Person:
    age = 16
    name = 'Max'


# print(getattr(Person, 'name', 'Impossible'))
# setattr(Person, 'k', 'ssss')
# del Person.age
# delattr(Person, 'age')
print(Person.__dict__)
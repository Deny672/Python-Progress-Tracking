class Cat:
    breed: str = 'Sibiryan'
    age: int = 5

print(getattr(Cat, 'breed'), getattr(Cat, 'age'))

Tom = Cat()
setattr(Tom, 'age', 8)
print(Tom.__dict__)

class Car:
    speed: int = 80
    color: str = 'white'

print(Car.speed, Car.color, sep= '\n')
del Car.speed
print(Car.__dict__)
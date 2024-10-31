from dataclasses import dataclass, field
from pprint import pprint

# This code compares a regular Thing class with a ThingData 
# class created using the @dataclass decorator. The example 
# shows how dataclass simplifies the creation of classes with 
# auto-generated methods (e.g. __init__, __repr__, __eq__) and 
# provides convenient customizations for fields using field. The 
# code also demonstrates overriding the __eq__ method in dataclass to compare 
# objects by weight, which shows the possibilities of customizing dataclass behavior.


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing: {self.__dict__}"

@dataclass
class ThingData:
    name: str
    weight: int 
    price: float = 0
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight



t = Thing("Учебник по литературе", 100, 1000)
print(t)


td = ThingData("Учебник по литературе", 100, 1000)
td2 = ThingData("Учебник по OOP", 80, 500)
td3 = ThingData("Учебник по OOP", 80)

print(td)
print(td == td2)
print(td3 == td2)

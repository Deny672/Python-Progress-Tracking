from typing import Any


class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    #We can get the value of an attribute, and make a restriction that certain attributes cannot be obtained
    def __getattribute__(self, item):
        if item =="x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)
    
    #Sets the value of the attribute, you can make for example a restriction
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            # print(key, value)
            # print("__setattr__")
            object.__setattr__(self, key, value)
    
    #If there is no such attribute, it will return False
    def __getattr__(self, item):
        return False
    
    def __delattr__(self, item):
        print("__delattr__: "+item)
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
print(pt1.__dict__)
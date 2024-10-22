# With __slots__ we set 3 attributes that an 
# instance of a class can have. Also with @property 
# decorator we can get and change our length (__lenght).

class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x*x+y*y)**0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

pt = Point2D(1, 2)

print(pt.length)
pt.length = 10
print(pt.length)
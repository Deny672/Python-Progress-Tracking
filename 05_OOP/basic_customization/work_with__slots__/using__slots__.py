import timeit

# With __slots__ we can limit the number of created 
# local properties, reduce the memory occupied by the class 
# instance and speed up the work with local properties.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__=('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

p1 = Point(1, 2)
p2 = Point2D(10, 20)

t1 = timeit.timeit(p1.calc)
t2 = timeit.timeit(p2.calc)

print(t1, t2)
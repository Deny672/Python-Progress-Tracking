# In the parent class (Point2D), we cannot create 
# or modify attributes other than 'x' and 'y'. In 
# the child class, we use __slots__ to specify that 
# we cannot modify all attributes other than those in 
# the Point2D class.

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    # If you want to add and modify attributes in instances of the Point3D class:
    __slots__ = ()          # comment it out
    # pass          #uncomment it out

pt = Point3D(10, 20)
pt.x = 9
print(pt.x)

# pt.z = 15
# print(pt.z)
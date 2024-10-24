class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        self.verify_coord(value)
        setattr(instance, self.name, value)
    
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    

p = Point3D(1, 2, 3)

print(p.__dict__)
p.x = 2
print(p.__dict__)
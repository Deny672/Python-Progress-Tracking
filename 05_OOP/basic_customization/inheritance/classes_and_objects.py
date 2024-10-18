class Geom:
    pass

class Line(Geom):
    pass


g = Geom()
l = Line()


print(issubclass(Line, Geom))
print(issubclass(Geom, Line))

print(isinstance(l, object))
print(isinstance(Geom, object))


print(isinstance(int, object))


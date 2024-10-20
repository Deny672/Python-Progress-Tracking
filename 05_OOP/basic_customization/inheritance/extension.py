# We can see the extension of the base class Geom, by another class Line
# Расширение базового класса


class Geom:
    name = 'Geom'

class Line(Geom):
    def draw(self):
        print("Рисование линии")
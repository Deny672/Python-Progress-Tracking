# Since we create a draw function in the Line class,
# we override the draw function in the Geom class.
# We can see the overriding of the base Geom class
# by another Line class. But if we call the draw
# function with an instance of the Geom class,
# then this function will be called from the Geom class.
# Переопределение базового класса

class Geom:
    name = 'Geom'
    def draw(self):
        print("Рисование линии")

class Line(Geom):
    def draw(self):
        print("Рисование линии")
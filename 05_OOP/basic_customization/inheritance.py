# During inheritance, we can make it so that one
# class can inherit the functionality of another
# class. Also, if there is no overriding of attributes
# for example, they will be taken from the class that is inherited.

class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Установка координат")


class Line(Geom):
    name = 'Line'
    # def draw(self):
    #     print("Рисование линии")


class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")

g = Geom()

l = Line()
r = Rect()

l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)

print(l.__dict__)
print(r.__dict__)
print(l.name)
print(r.name)


print(l.draw())
print(r.draw())
print(g.draw())
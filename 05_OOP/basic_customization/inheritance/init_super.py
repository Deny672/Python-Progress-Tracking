# In the Line class, we use the __init__ method
# of the Geom class using inheritance. But in the
# situation with the Rect class we use the 'super().'
# function to take the __init__ method from the Geom
# class to initialize the part of attributes that we need.


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор класса Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):

    def draw(self):
        print("Рисование линии")

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2) #Delegation (Делегирование)
        print("Инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")

l = Line(0, 0, 10, 12)
r = Rect(1, 1, 2, 2)
print(l.__dict__)
print(r.__dict__)


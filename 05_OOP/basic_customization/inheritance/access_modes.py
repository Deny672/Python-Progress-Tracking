# Inheritance:
# Public(attribute): completely open and accessible from everywhere.
# Protected(_attribute): available inside the class and its subclasses, but it is “not recommended” to access it from outside.
# Private(__attribute): hidden from external access and even from subclasses, but can be accessed through the name mangling “mechanism”.


class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор класса Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

    
    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(0, 0, 10, 20)
print(r.__dict__)
print(r.get_coords())
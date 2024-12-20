class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.MAX_COORD)
pt1.set_bound(52)
print(pt1.MIN_COORD)
print(Point.MIN_COORD)
print(pt1.MIN_COORD)
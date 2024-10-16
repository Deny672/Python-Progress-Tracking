class Point:
    "sosav dvajdi"
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords(11, 2)
f=getattr(pt, "get_coords")
print(f())
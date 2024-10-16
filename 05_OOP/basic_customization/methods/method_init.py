class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        print("вызов __init__")
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y
    
pt = Point(1, 4)
# pt.set_coords(1, 2)
print(pt.__dict__)
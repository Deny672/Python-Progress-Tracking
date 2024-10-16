class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # The __len__ method changes the output of the called
    # function “len(our_class_instance)” and if the __bool__
    # method is not defined in the class, then the call of 
    # the function “bool(our_class_instance)” will output a 
    # boolean value that returns the __len__ method.
    
    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y
    
    # The __bool__ method is called when checking the truth
    #  (we can make any conditions, for example, the identity 
    # of coordinates). If this method is not defined, the __len__
    #  method is called (objects with non-zero length are considered true).
    
    def __bool__(self):
        print("__bool__")
        return self.x == self.y


p = Point(1, 1)
print(len(p))
print(bool(p))

if p:
    print("object p returned True")
else:
    print("object p returned False")
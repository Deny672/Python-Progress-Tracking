# Using the __mro__ function, we can see the order 
# in which classes are viewed in multiple inheritance. 
# In the NoteBook class, we inherit from Goods and MixinLog, 
# so our order will be NoteBook, Goods, MixinLog and object. 
# It is also preferable not to use attributes in the second 
# class when inheriting two classes. Otherwise we will have 
# to write super().__init__() in the __init__ method of the first 
# class we inherit from, which complicates code readability significantly.


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("Init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class MixinLog:
    ID = 0

    def __init__(self):
        print("Init MixinLog")
        MixinLog.ID +=1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в :00")


    def print_info(self):
        print(f"print_info into MixinLog")

class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)

n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)
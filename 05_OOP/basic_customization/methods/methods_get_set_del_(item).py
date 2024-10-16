# In this code we have redefined how to work with
#  student's marks (get, set, delete), not by
#  referring to the list, but to the student's instance.
#  That is, we don't call “s1.marks[0]”, we call “s1[0]”. 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    # The __getitem__ method gives access by index (or key).
    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    # The __setitem__ method assigns an element by index. 
    # Also added logic that if there is no such value, 
    # it will be preceded by empty values.
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    # __delitem__ method deletes an item by index.
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        del self.marks[key]

s1 = Student("Sergey", [5, 5, 4, 2, 3, 3])
print(s1[2])
s1[10] = 6
print(s1[2])

print(s1.marks)
del s1[2]
print(s1.marks)
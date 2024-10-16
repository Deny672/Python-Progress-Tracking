# Here we have overloaded arithmetic methods like (+; -; *; /; //; %)
# as well as added the ability to do these operations on class instance
# attributes. In our code we can subtract seconds from seconds, take 
# integer part from division and so on.


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def validate_type_int_or_clock(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или обьэктом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return sc

    # Clock + int
    def __add__(self, other):
        print("__add__")
        sc = self.validate_type_int_or_clock(other)
        return Clock(self.seconds + sc)

    # int + Clock
    def __radd__(self, other):
        print("__radd__")
        return self + other

    # Clock += int
    def __iadd__(self, other):
        print("__iadd__")
        sc = self.validate_type_int_or_clock(other)
        self.seconds += sc
        return self

    # Clock - int
    def __sub__(self, other):
        print("__sub__")
        sc = self.validate_type_int_or_clock(other)
        return Clock(self.seconds - sc)

    # int - Clock
    def __rsub__(self, other):
        print("__rsub__")
        return self - other

    # Clock -= int
    def __isub__(self, other):
        print("__isub__")
        sc = self.validate_type_int_or_clock(other)
        self.seconds -= sc
        return self

    # Clock * int
    def __mul__(self, other):
        print("__mul__")
        sc = self.validate_type_int_or_clock(other)
        return Clock(self.seconds * sc)

    # int * Clock
    def __rmul__(self, other):
        print("__rmul__")
        return self * other

    # Clock *= int
    def __imul__(self, other):
        print("__imul__")
        sc = self.validate_type_int_or_clock(other)
        self.seconds *= sc
        return self

        # Clock * int
    
    # Clock / int
    def __truediv__(self, other):
        print("__truediv__")
        sc = self.validate_type_int_or_clock(other)
        return Clock(self.seconds // sc) # In fact, we need self.seconds / sc, but we have Clock, which has integer seconds

    # int / Clock
    def __rtruediv__(self, other):
        print("__rtruediv__")
        return self / other

    # Clock /= int
    def __itruediv__(self, other):
        print("__itruediv__")
        sc = self.validate_type_int_or_clock(other)
        self.seconds //= sc # In fact, we need self.seconds /= sc, but we have Clock, which has integer seconds
        return self

        # Clock // int
    
    # Clock // int
    def __floordiv__(self, other):
        print("__floordiv__")
        sc = self.validate_type_int_or_clock(other)
        return Clock(
            self.seconds // sc)

    # int // Clock
    def __rfloordiv__(self, other):
        print("__rfloordiv__")
        return self // other

    # Clock //= int
    def __ifloordiv__(self, other):
        print("__ifloordiv__")
        sc = self.validate_type_int_or_clock(other)
        self.seconds //= sc
        return self

    # Clock % int
    def __mod__(self, other):
        print("__mod__")
        sc = self.validate_type_int_or_clock(other)
        return Clock(
            self.seconds % sc)  # In fact, we need self.seconds / sc, but we have Clock, which has integer seconds

    # int % Clock
    def __rmod__(self, other):
        print("__rmod__")
        return self % other

    # Clock %= int
    def __imod__(self, other):
        print("__imod__")
        sc = self.validate_type_int_or_clock(other)
        self.seconds %= sc  # In fact, we need self.seconds /= sc, but we have Clock, which has integer seconds
        return self

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")



c1 = Clock(1000)
c2 = 100 + c1
c2 += 100
c3 = c2 + c1
print(c3.get_time())

c1 = Clock(1000)
c2 = 100 - c1
c2 -= 100
c3 = c2 - c1
print(c3.get_time())

c1 = Clock(10)
c2 = 100 * c1
c2 *= 100
c3 = c2 * c1
print(c3.get_time())

c1 = Clock(100000000)
c2 = 100 / c1
c2 /= 100
c3 = c2 / c1
print(c3.get_time())

c1 = Clock(100000000)
c2 = 100 // c1
c2 //= 100
c3 = c2 // c1
print(c3.get_time())

c1 = Clock(100000000)
c2 = 100 % c1
c2 %= 100
c3 = c2 % c1
print(c3.get_time())











# class Clock:
#     __DAY = 86400

#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__DAY

#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

#     def __add__(self, other):
#         print("__add__")
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Правый операнд должен быть int или обьэктом Clock")

#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds

#         return Clock(self.seconds + sc)

#     def __radd__(self, other):
#         print("__radd__")
#         return self + other

#     def __iadd__(self, other):
#         print("__iadd__")
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Правый операнд должен быть int или обьэктом Clock")

#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds

#         self.seconds += sc
#         return self

#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(2, "0")

# c1 = Clock(1000)
# c2 = 100 + c1
# c2 += 100
# c3 = c2 + c1
# print(c3.get_time())
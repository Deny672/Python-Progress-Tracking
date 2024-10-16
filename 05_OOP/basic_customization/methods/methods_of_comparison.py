class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def validate_type_int_or_clock(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или обьэктом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return sc

    #Realizes the comparison (==) of two values of second instances of the Clock class, and also if we try to check the inequality, the (not (==)) will be used.
    def __eq__(self, other):
        print("__eq__")
        sc = self.validate_type_int_or_clock(other)
        return self.seconds == sc
    #Realizes inequality comparison (!=) of two values of the second instances of the Clock class
    def __ne__(self, other):
        print("__ne__")
        sc = self.validate_type_int_or_clock(other)
        return self.seconds != sc


    # It implements a check if the first value is less than the second value (c1 < c2), but if we enter (c1 > c2) and (>) is not implemented, it will check (c2 < c1)
    def __lt__(self, other):
        print("__lt__")
        sc = self.validate_type_int_or_clock(other)
        return self.seconds < sc

    # It implements a check if the first value is greater than the second value (c1 > c2), but if we enter (c1 < c2) and (<) is not implemented, it will check (c2 > c1)
    def __gt__(self, other):
        print("__gt__")
        sc = self.validate_type_int_or_clock(other)
        return self.seconds > sc
    
    # It implements a check that the first value is less than or equal to the second value (c1 <= c2), but if we enter (c1 >= c2) and (>=) is not implemented, it will check (c2 =< c1).
    def __le__(self, other):
        print("__le__")
        sc = self.validate_type_int_or_clock(other)
        return self.seconds <= sc
    
    # It implements checking if the first value is greater or equal than the second value (c1 >= c2), but if we enter (c1 <= c2) and (<=) is not implemented, it will check (c2 => c1).
    def __ge__(self, other):
        print("__ge__")
        sc = self.validate_type_int_or_clock(other)
        return self.seconds >= sc
    
# From this code we can understand that for each comparison operation 
# we only need to define one method, and the opposite 
# one will be performed by the method that is defined




c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
print(c1 >= c2)
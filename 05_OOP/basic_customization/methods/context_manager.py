# In the code below, by overriding the __enter__ and __exit__ 
# methods, we can change the behavior of the with context manager. 
# In our case we don't want our initial list to change if an error occurs, 
# so we create a temporary list 'self.__temp = self.__v[:]' to work with, and 
# assign the temporary list to the passed one when it finishes without error.

v1 = [1, 2, 3]
v2 = [2, 3]

class DefenderVector:
    def __init__(self, v):
        self.__v = v
    
    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False

try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Ошибка")
print(v1)
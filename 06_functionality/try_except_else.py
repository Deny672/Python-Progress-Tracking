# When we set the 'else' operator in error 
# handling, the code it contains will be 
# executed if no exceptions occur.

try:
    x, y = map(int, input().split())
    res = x/y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
else:
    print("Исключений не произошло, результат от деления = ", res)
# When we set the 'finally' operator in error handling, 
# the code it contains will always be executed.

try:
    x, y = map(int, input().split())
    res = x/y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
finally:
    print("Блок finally выполняется всегда")
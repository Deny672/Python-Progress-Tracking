# In the code below we can see how we 
# could do nested exception handling, we 
# could also do it as a function where x / y.

res = 0
try:
    x, y = map(int, input().split())
    try:
        res = x/y
    except ZeroDivisionError:
        print("Деление на ноль")
except ValueError as z:
    print(z)

print(res)
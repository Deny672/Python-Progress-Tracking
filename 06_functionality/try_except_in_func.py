# Using the code below, we can see that when try, 
# except, finally are written in a function that 
# returns a certain value, the part of the code 
# written in finally will be executed before the return.

def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print("finally выполняется до return")

x, y = get_values()
print(x, y)
"""
Define a function that takes an integer argument and returns a logical
value true or false depending on if the integer is a prime.
"""
def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

number = int(input('Введіть ваше число '))
print(is_prime(number))
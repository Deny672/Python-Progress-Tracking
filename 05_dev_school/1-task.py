"""
Create a code that returns the sum of all numbers that are multiples of 3
or 5 that are less than the number you entered.

Alternatively, if the number is negative, print 0.

Remarks: If the number is a multiple of both 3 and 5, count it only once.
"""

def task(num):
    sum = 0
    while num > 0:
        if num % 3 == 0 and num % 5 == 0:
            sum += num
        elif num % 3 == 0 or num % 5 == 0:
            sum += num
        num -= 1
    return sum


number = int(input('Введіть ваше число '))
print(task(number))
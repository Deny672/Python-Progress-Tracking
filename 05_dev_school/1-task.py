
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
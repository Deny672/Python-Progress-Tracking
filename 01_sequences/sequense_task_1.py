num = 1
multiplication = 1
while multiplication % 1000 != 0:
    num = int(input('Введить число: '))

    multiplication *= num
print(multiplication)
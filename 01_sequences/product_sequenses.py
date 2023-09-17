num = None
multiplication = None
while num != 0:
    num = int(input('Введить число: '))
    if multiplication == None:
        multiplication = 1
    if num != 0:
        multiplication *= num
print(multiplication)
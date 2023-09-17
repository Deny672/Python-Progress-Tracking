num = None
length = None
while num != 0:
    num = int(input('Введить число: '))
    if length == None:
        length = 0
    length += 1
print(length)
num = 10
if num <= 1:
    print("Не просте число")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Не просте число")
            break
        else:
            print("Просте число")
            break
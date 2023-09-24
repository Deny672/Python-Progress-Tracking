
def sort_num(num):
    arr = []

    for i in str(num):
        arr.append(int(i))


    for i in range(0, len(arr) - 1):
        flag = False
        for x in range(0, len(arr) - 1):
            if arr[x] < arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                flag = True
        if not flag:
            break
    return arr

number = 145263
print(sort_num(number))
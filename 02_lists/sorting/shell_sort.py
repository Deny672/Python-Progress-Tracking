list1 = [3, 2, 1, 1, 2, 3, 4, 2, 3]
n = len(list1)
gap = n // 2
while gap > 0:
    for i in range(gap, n):
        temp = list1[i]
        j = i
        while j >= gap and list1[j - gap] > temp:
            list1[j] = list1[j - gap]
            j -= gap
        list1[j] = temp
    gap //= 2
print(list1)
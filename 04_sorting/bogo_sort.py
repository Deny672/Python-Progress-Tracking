import random

list1 = [5, 2, 1, 4, 3]
value_sort = 0
while value_sort != len(list1) - 1:
    random.shuffle(list1)
    value_sort = 0
    for i in range(1, len(list1)):
        if list1[i - 1] < list1[i]:
            value_sort += 1
print(list1)
import random

list1 = [1, 2, 3, 4, 5]
for i in range(len(list1)-1, 0, -1):
        j = random.randint(0, i)
        list1[i], list1[j] = list1[j], list1[i]
print(list1)
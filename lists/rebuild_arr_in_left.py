list1 = [1, 2, 3, 4, 5]
value =  1
list1 = list1[value::]
i = 0
while i != value:
    i += 1
    list1.append(0)
print(list1)
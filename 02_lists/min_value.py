list_1 = [1, 2, 2, 3, 1, 5, 0, 6, 3]
min_value = list_1[0]
for item in list_1:
    if item < min_value:
        min_value = item
print(min_value)

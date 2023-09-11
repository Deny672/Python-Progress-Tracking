list_1 = [ -1, -1, 2, 3, 0, 4, 5, 6, 1, 2, 6]
min_value = list_1[0]
max_value = list_1[0]
quantity_zero = 0
quantity_max = 0
quantity_min = 0

for item in list_1:
    if item > max_value:
        max_value = item
    if item < min_value:
        min_value = item

for item in list_1:
    if 0 == item:
        quantity_zero += 1
    if max_value == item:
        quantity_max += 1
    if min_value == item:
        quantity_min += 1
print(quantity_zero, quantity_max, quantity_min)
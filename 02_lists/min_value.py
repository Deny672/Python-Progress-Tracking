list_1 = [0.4138, 0.5862] 
sum = 0.0
min_value = list_1[0]
for item in list_1:
    sum += item
    if item < min_value:
        min_value = item
print("Значение = ", min_value)
print(sum)

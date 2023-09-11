list_1 = [1, 1, 2, 2, 4, 4, 4, 4, 4]
data = {}
quantity = 0
for item in list_1:
  while list_1.count(item) != 0:
    list_1.remove(item)
    quantity += 1
  data[item] = quantity
  quantity = 0
print(data)
max_value = 0
value = 0
for item in data:
    if data[item] > max_value:
        max_value = data[item]
        value = item
print(value)
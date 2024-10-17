list_1 = [1, 1, 2, 2, 2, 4, 4]
value_same_num = []
same_num = []
k = 0
for item in list_1:
  while list_1.count(item) != 0:
    list_1.remove(item)
    k += 1
  value_same_num.append(k)
  same_num.append(item)
  k = 0
max_value = value_same_num[0]
k = 0
for item in range(0, len(value_same_num)):
    if value_same_num[item] > max_value:
        max_value = value_same_num[item]
        k = item

print(same_num[k])

arr = [0, 5, 4, 3, 2, 2]

count_arr = [0] * 10

for i in arr:
  count_arr[i] += 1

result = [num for num, count in enumerate(count_arr) for i in range(count)]

print(result)
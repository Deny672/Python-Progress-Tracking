arr = [1, 5, 2, 6, 4, 3, 5]
for i in range(0, len(arr) - 1):
  flag = False
  for x in range(0, len(arr) - 1):
    if arr[x] > arr[x + 1]:
      arr[x], arr[x+1] = arr[x+1], arr[x]
      flag = True
  if not flag:
    break
print(arr)
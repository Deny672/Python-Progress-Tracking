arr = [4, 15, 2, 5, 16, 3, 4]
for i in range(0, len(arr) - 1):
  flag = False
  for x in range(0, len(arr) - 1):
    if arr[x] > arr[x + 1]:
      arr[x], arr[x+1] = arr[x+1], arr[x]
      flag = True
      print(arr)
  if not flag:
    break
print(arr)
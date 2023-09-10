matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

sum_all_element = 0
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    sum_all_element += matrix[i][j]

print(sum_all_element)
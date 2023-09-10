matrix = []
value_matrix = 1
for i in range(0, 4):
  matrix.append([])
  for j in range(0, 3):
    matrix[i].append(value_matrix)
    value_matrix += 1
for i in range(len(matrix)):

  print(matrix[i])
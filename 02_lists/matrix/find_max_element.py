"""
6 29 91  9 10
 11 12 53 14 15
 16 70 18 39 20
 21 22 23 24 25

91
"""


matrix = [[6, 29, 91, 9, 10],
          [11, 12, 53, 14, 15],
          [16, 70, 18, 39, 20],
          [21, 22, 23, 24, 25]]

max_value = 0
row = 0
column = 0
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if max_value < matrix[i][j]:
      max_value = matrix[i][j]
      row = i
      column = j

print(max_value)
print(row, column)
"""
 0 29 91  9 10
 11 12 53 14 15
 16 70 18  0  0
  0 22 23 24 25

4
"""

matrix = [[0, 29, 91, 9, 10],
[11, 12, 53, 14, 15],
[16, 70, 18, 0, 0],
[0, 22, 23, 24, 25]]

count_zero = 0
for row in range(len(matrix)):
  for column in range(len(matrix[row])):
    if 0 == matrix[row][column]:
      count_zero += 1

print(count_zero)
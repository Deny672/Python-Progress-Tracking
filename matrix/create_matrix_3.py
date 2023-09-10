"""
  6  7  8  9 10
 11 12 13 14 15
 16 17 18 19 20
 21 22 23 24

"""

matrix = []

row = 0
matrix.append([])
for i in range(6, 25):
    matrix[row].append(i)
    if len(matrix[row]) == 5:
        matrix.append([])
        row += 1

for i in range(len(matrix)):
    print(matrix[i])
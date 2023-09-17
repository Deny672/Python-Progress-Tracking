"""
1 2 3    3 2 1
4 5 6 => 4 5 6
7 8 9    9 8 7

 1  2  3  4  5     5  2  3  4  1
 6  7  8  9 10     6  9  8  7 10
11 12 13 14 15 => 11 12 13 14 15
16 17 18 19 20    16 19 18 17 20
21 22 23 24 25    25 22 23 24 21
"""

matrix = [ [1, 2, 3, 4, 5],
[ 6, 7, 8,  9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]]


for i in range(len(matrix)):
  matrix[i][i] , matrix[i][-1 - i] = matrix[i][-1 - i], matrix[i][i]

for i in range(len(matrix)):
  print(matrix[i])
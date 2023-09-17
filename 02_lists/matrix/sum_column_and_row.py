"""
 6  7  8  9 10
 11 12 13 14 15
 16 17 18 19 20
 21 22 23 24

"""

matrix = [[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24]]

#Массив для сумм строк

row_sums = [0] * len(matrix)

#Его заполнение

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        row_sums[row] += matrix[row][column]

num_columns = max(len(row) for row in matrix)

#Массив для сумм столбцов

column_sums = [0] * num_columns

#Его заполнение

for row in matrix:
    for i in range(len(row)):
        column_sums[i] += row[i]

#Вывод

for i in range(len(row_sums)):
    print(f'{i + 1} row sum: ', row_sums[i])

for i in range(len(column_sums)):
    print(f'{i + 1} column sum: ', column_sums[i])
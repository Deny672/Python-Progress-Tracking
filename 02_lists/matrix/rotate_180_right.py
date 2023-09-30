"""
1 2 3    9 8 7
4 5 6 => 6 5 4
7 8 9    3 2 1
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = []

def rotate_180_right(matrix):
    for i in range(len(matrix)):
        new_matrix.append([])

    row_new_matrix = 0
    for row in range(len(matrix)-1, -1, -1):
        for column in range(len(matrix)-1, -1, -1):
            new_matrix[row_new_matrix].append(matrix[row][column])
        row_new_matrix += 1
    print(new_matrix)
    return new_matrix

matrix = rotate_180_right(matrix)

for i in range(len(matrix)):
    print(matrix[i])
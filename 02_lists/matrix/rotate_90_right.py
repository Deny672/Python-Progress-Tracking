"""
1 2 3    7 4 1
4 5 6 => 8 5 2
7 8 9    9 6 3
"""


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate_90_right(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for column in range(len(matrix) - 1, -1, -1):
            new_matrix[row].append(matrix[column][row])
    return new_matrix

matrix = rotate_90_right(matrix)

for i in range(len(matrix)):
    print(matrix[i])
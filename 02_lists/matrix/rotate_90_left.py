"""
1 2 3    3 6 9
4 5 6 => 2 5 8
7 8 9    1 4 7
"""


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate_90_left(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([])

    row_new_matrix = 0
    for row in range(len(matrix)-1, -1, -1):
        for column in range(len(matrix)):
            result[row_new_matrix].append(matrix[column][row])
        row_new_matrix += 1
    print(result)
    return result

matrix = rotate_90_left(matrix)

for i in range(len(matrix)):
    print(matrix[i])
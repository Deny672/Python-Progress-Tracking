matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = []
for row in range(len(matrix)):
    new_matrix.append([])
    for column in range(len(matrix[row]) - 1, -1, -1):
        new_matrix[row].append(matrix[row][column])

for i in range(len(new_matrix)):
    print(new_matrix[i])
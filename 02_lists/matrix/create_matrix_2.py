matrix = []

for i in range(0, 4):
    matrix.append([])
    for j in range(0, 3):
        matrix[i].append(i * j)

for i in range(len(matrix)):
    print(matrix[i])
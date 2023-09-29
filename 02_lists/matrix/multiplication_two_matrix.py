"""
# multiplication of two matrices
  [0,  1,  2]
  [1,  2,  2]

  [0,  1,  2,  3]
  [1,  1,  3,  3]
  [2,  2,  3,  5]
# result
  [5,  5,  9, 13]
  [6,  7, 14, 19]
"""

A = [ [0,  1,  2],
      [1,  2,  2] ]

B = [ [0,  1,  2,  3],
      [1,  1,  3,  3],
      [2,  2,  3,  5] ]

def matrix_multiplication(matrix_A, matrix_B):
    if len(matrix_A) != len(matrix_B[0]) and len(matrix_A[0]) != len(matrix_B):
        return None

    result = []
    add = 0
    for row_A in range(len(matrix_A)):
        result.append([])
        for row_B in range(len(matrix_B[0])):
            for column in range(len(matrix_B)):
                add += matrix_A[row_A][column] * matrix_B[column][row_B]
            result[row_A].append(add)
            add = 0

    return result

for item in matrix_multiplication(A, B):
    print(item)
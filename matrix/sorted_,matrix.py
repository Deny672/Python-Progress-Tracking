"""
3 1 5    0 1 1
2 3 0 => 2 2 3
4 1 2    3 4 5
"""

matrix = [[3, 1, 5], [2, 3, 0], [4, 1, 2]]
arr = []

#added elem matrix in arr

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        arr.append(matrix[row][column])

#sort arr

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            temp = array[j]
            array[j] = array[j-1]
            array[j - 1] = temp
            j = j -1
    return array

arr = insertion_sort(arr)
element_arr = 0

#rebuild matrix

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        matrix[row][column] = arr[element_arr]
        element_arr += 1

print(matrix)
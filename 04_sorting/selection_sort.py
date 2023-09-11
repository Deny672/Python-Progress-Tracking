def selection_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j

        arr[i], arr[min_value] = arr[min_value], arr[i]

    return arr


array = [0, 5, 4, 3, 2, 2]
print(selection_sort(array))
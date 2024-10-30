def selection_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j

        arr[i], arr[min_value] = arr[min_value], arr[i]
        print(arr)
    return arr


array = [4, 5, 2, 8, 6, 3, 1]
print(selection_sort(array))
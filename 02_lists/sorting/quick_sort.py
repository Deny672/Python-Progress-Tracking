def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left_array = [x for x in arr[:-1] if x <= pivot]
    right_array = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


arr = [5, 1, 4, 3, 2]
sorted_arr = quick_sort(arr)
print(sorted_arr)
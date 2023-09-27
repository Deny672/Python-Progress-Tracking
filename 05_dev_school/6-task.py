"""
Your task is to make a function that can take any non-negative integer
as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""

def sort_num(num):
    arr = []

    for i in str(num):
        arr.append(int(i))


    for i in range(0, len(arr) - 1):
        flag = False
        for x in range(0, len(arr) - 1):
            if arr[x] < arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                flag = True
        if not flag:
            break
    return arr

number = 145263
print(sort_num(number))
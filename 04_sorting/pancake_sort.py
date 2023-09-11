list1 = [5, 2, 1, 4, 3]
n = len(list1)-1
while n != -1:
    max_index = 0
    for i in range(0 , n+1):
        if list1[i] > list1[max_index]:
            max_index = i
    list1[0 : max_index+1] = list1[0 : max_index+1][::-1]
    list1[0 : n+1] = list1[0 : n+1][::-1]
    print(list1)
    n -= 1
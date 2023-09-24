
def find_nb(m):
    n = 0
    while m > 0:
        n += 1
        m -= n ** 3
    if m == 0:
        return n
    else:
        return -1

num = 1071225

print(find_nb(num))
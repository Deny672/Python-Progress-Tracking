"""
Your task is to build a building consisting of a pile of n cubes.
The cube at the bottom will have volume n^3, the cube at the top will have volume (n-1)^3
with volume (n-1)^3, and so on until the top, which will have volume
1^3.

You are given the total volume of the building m. Given the volume m, you can
find the number n of cubes to be built?
"""
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
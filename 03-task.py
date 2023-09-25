'''
Your task is to construct a building which will be a pile of n cubes.  
The cube at the bottom will have a volume of n^3, the cube above will  
have volume of (n−1)^3 and so on until the top which will have a volume  of 1^3. 
'''

def find_floor(num):
    floor = 0
    while num > 0:
        floor += 1
        num -= floor ** 3
    if num == 0:
        return floor
    else:
        return -1

# Driver
num = 1071225
print(find_floor(num))

# class A:
#     year: int = 2020
#     height: int = 175
#     weight: float = 65
#     count_man: int = 150
#
# A.year += 1
# A.count_man -= 2
# print(A.__dict__)

class Cat:
    color: str = 'white'


arr = []
count_black_cat = 2
for i in range(0, 14):
    arr.append(Cat)




print(arr)

# for i in range(0, 14):
#     arr.append(Cat.color)
#
# count_black_cat = 2
# for i in range(count_black_cat):
#     arr[len(arr)- 1 - i] = 'black'
#
# print(arr)
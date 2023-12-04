from pprint import pprint

# class A:
#     x = 1
# if hasattr(A, 'name'):
#     del A.name
# else:
#     print('Такого атрибута не существует')


languages = ['Russian','Ukrainian', 'English']

class Country:
    headcount: int = 5000000
    regimes = ["Демократический", "Политический","Государственный"]
    square: int = 300000


arr = [Country() for _ in range(3)]
for count, country in enumerate(arr):
    country.language = languages[count]

print([arr[index].language for index in range(3)])
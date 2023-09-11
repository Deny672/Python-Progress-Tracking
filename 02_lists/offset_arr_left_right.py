list1 = [1, 2, 3, 4, 5]
side_num = int(input('Виберіть напрямок 1 - вліво, 2 - вправо: '))
num = int(input('Виберіть на скільки змістити масив: '))
num = num % len(list1)
if side_num == 1:
    list1 = list1[num:] + list1[:num]
    print(list1)
elif side_num == 2:
    list1 = list1[-num:] + list1[:-num]
    print(list1)
else:
  print('Невірне число з напрямком')
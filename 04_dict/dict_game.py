def shop():
    money = 100
    basket = {}
    offer = {
        "apple": {
            "price": 48,
            "count": 2,
        },
        "banana": {
            "price": 7,
            "count": 3,
        },
        "pear": {
            "price": 3,
            "count": 1,
        }
    }
    flag = True
    while flag is True:
        print(f'У вас залишилось ще {money} грн')
        for item in offer:
            if offer[item]["count"] == 0:
                break
            else:
                print(f'В наявності {item}, в кількості {offer[item]["count"]}, за ціною {offer[item]["price"]}')
        product = (input('Введіть назву товару, який хочете придбати, якщо не хочете чого-небудь придбати, напишіть "end": '))
        text = ''
        if product in offer:
            if offer[product]['count'] != 0:
                offer[product]['count'] -= 1
                if (money - offer[product]['price']) >= 0:
                    money -= offer[product]['price']
                    if product in basket:
                        basket[product]['count'] += 1
                    else:
                        basket[product] = {'count': 1}
                    for item in basket:
                        text += f'{item} у кількості {basket[item]["count"]}, '
                    print('У вашому кошику зараз ' + text)
                else:
                    print('У вас недостатньо коштів')
            else:
                print('Такий товар закінчився, або його немає в нашому асортименті')
        elif product == 'end':
            for item in basket:
                print(f'Ви придбали {item} в кількості {basket[item]["count"]}')
            print(f'У вас залишилось ще {money} грн')
            flag = False
        else:
            print('Ви ввели невірну назву товару')



shop()
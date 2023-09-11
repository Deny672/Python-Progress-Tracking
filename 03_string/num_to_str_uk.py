dictionary = {
    0: "",
    1: "один",
    2: "два",
    3: "три",
    4: "чотири",
    5: "п'ять",
    6: "шість",
    7: "сім",
    8: "вісім",
    9: "дев'ять",
    10: "десять",
    11: "одинадцять",
    14: "чотирнадцять",
    20: "двадцять",
    30: "тридцять",
    40: "сорок",
    50: "п'ятдесят",
    60: "шістдесят",
    70: "сімдесят",
    80: "вісімдесят",
    90: "дев'яносто",
    100: "сто",
    200: "двісті",
    500: "п'ятсот",
    600: "шістсот",
    900: "дев'ятсот",
}


def convert_num_to_word(dekan, text):
    # 1 - 10
    if dekan < 10:
        text = dictionary[dekan]

    # 10, 11, 14
    elif (dekan == 10 or dekan == 11 or dekan == 14):
        text = dictionary[dekan]

    # 15, 16, 19
    elif (dekan == 15 or dekan == 16 or dekan == 19):
        text = dictionary[dekan - 10]
        text = text[0: -1] + "надцять"

    # 12, 13, 17, 18
    elif (20 > dekan > 11):
        text = dictionary[dekan - 10] + "надцять"

    # 20 - 99
    elif (100 > dekan >= 20):
        second_num = (dekan // 10) * 10
        first_num = dekan - second_num
        text = f"{dictionary[second_num]} {dictionary[first_num]}"


    # 100 - 1000
    elif (1000 > dekan >= 100):
        # 300, 400
        if (str(dekan)[0] == '3' or str(dekan)[0] == '4'):
            key = int(str(dekan)[0])
            text += dictionary[key] + 'ста'
        # 700, 800
        elif (str(dekan)[0] == '7' or str(dekan)[0] == '8'):
            key = int(str(dekan)[0])
            text += dictionary[key] + 'сот'
        # залишок
        else:
            second_num = (dekan // 100) * 100
            first_num = dekan - second_num
            text = f"{dictionary[second_num]}"
        second_num = (dekan // 100) * 100
        first_num = dekan - second_num
        text += f' {convert_num_to_word(first_num, text)}'

    # Відмінки декан

    first_num = dekan % 10

    dekan_list = ["декан", "декани", "деканів"]
    dekan_in_text = False
    for i in dekan_list:
        if i in text:
            dekan_in_text = True
            break

    if dekan_in_text == False:
        first_num = dekan % 10
        if first_num == 1:
            text += " декан"
        elif 1 < first_num < 5:
            text += " декани"
        else:
            text += " деканів"

    return text


for nani in range(1, 1000):
    text = ''
    uk = convert_num_to_word(nani, text)
    print(uk)
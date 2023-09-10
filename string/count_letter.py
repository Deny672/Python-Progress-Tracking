def count_every_element(text):
    dict_element_count = {}
    for item in text:
        if item in dict_element_count:
            dict_element_count[item] += 1
        else:
            dict_element_count[item] = 1

    return dict_element_count


text = "Aabacccdddd111"
result = count_every_element(text)

for item, count in result.items():
    print(f"{item}: {count}")
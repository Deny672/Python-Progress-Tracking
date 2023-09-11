def character_change(string):
    result = string.replace('.', '')
    return result


text = "I.'.m. .love. .this. .day."
print(character_change(text))
def change_text(string):
    new_string = ''
    for char in string:
        if char.isupper():
            new_string += '_' + char.lower()
        else:
            new_string += char
    return new_string


text = "someTextInSnakeNotation"
print(change_text(text))

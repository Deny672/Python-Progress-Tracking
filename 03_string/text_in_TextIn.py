def change_text(string):
    parts = string.split("_")
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


text = "some_text_in_snake_notation"
print(change_text(text))

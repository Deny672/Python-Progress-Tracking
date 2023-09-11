def character_change(string):
    while '  ' in string:
      string = string.replace('  ', ' ')
    return string


text = "     a               l      a                   n "
print(character_change(text))
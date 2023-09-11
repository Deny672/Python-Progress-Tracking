def change_text(string):
    word_list = string.split()
    i = 0
    while i != len(word_list) - 1:
      i += 1
      if word_list[i].isnumeric() is True:
        word_list.pop(i)
        i -= 1
      if len(word_list[i]) <= 3:
            word_list.pop(i)
            i -= 1
    return word_list


text = """алфАвІт 

ц

кОпчений 12

т

веснЯнИй  п

в

перенестИ в

1
"""
print(change_text(text))
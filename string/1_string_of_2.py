def take_emenets_in_str(str1, str2):
  result = str1[:2] + str2[-2:]
  return result

text1 = '12344321'
text2 = f"GOOD DAY"

text3 = (take_emenets_in_str(text1, text2))
print(text3)